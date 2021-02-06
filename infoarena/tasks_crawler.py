"""
This file is handling of infoarena tasks crawling.
"""
import requests
import re
from bs4 import BeautifulSoup
import links
from structures.task import Task
from utils.capture_eq import CaptureEq
import data


def get_task(link: str, force_update=False) -> Task:
    """
    Get all information about a task from it's page.
    :param force_update: If it is False, the task will be downloaded from the site only if it doesn't exists in
    data.tasks. If it is True, the task will be downloaded and updated anyway.
    :param link:
    :return:
    """
    task = Task(task_id=link.rsplit('/', 1)[-1], link_name=link.rsplit('/', 1)[-1], task_link=link)

    if not force_update:
        if task.task_id in data.tasks:
            return data.tasks.get(task.task_id)
    print("Update task: ", task.task_id)

    task_page = requests.get(link)
    parsed_task_page = BeautifulSoup(task_page.text, 'html.parser')

    parsed_task_page = parsed_task_page.find_all("div", attrs={'id': 'main'})[0]
    parsed_task_page = parsed_task_page.find_all("div", attrs={'class': 'wiki_text_block'})[0]

    info_table = parsed_task_page.find_all("table")[0]
    _extract_info_from_table_task_page(task, info_table)

    info_table.decompose()
    task_name = parsed_task_page.find_all("h1")[0].text
    task.set_name(task_name)
    parsed_task_page.find_all("h1")[0].decompose()
    parsed_task_page.find_all("p")[0].decompose()
    parsed_task_page.find_all("p")[0].decompose()

    examples_table = parsed_task_page.find_all("table", attrs={'class': 'example'})[-1]
    _extract_examples_from_table(task, examples_table)

    for element in examples_table.fetchNextSiblings():
        element.decompose()
    examples_table.decompose()

    task.set_statement(parsed_task_page.text)

    data.tasks[task.task_id] = task
    return task


def get_tasks_from_page(link: str, force_update=False):
    """
    Get all tasks from a page of archive.
    :param force_update: If it is False, the task will be downloaded from the site only if it doesn't exists in
    data.tasks. If it is True, the task will be downloaded and updated anyway.
    :param link:
    :return:
    """
    tasks_page = requests.get(link)
    parsed_tasks_page = BeautifulSoup(tasks_page.text, 'html.parser')

    task_attrs = {
                    'class': 'task'
                }
    tasks_text = parsed_tasks_page.find_all('td', attrs=task_attrs)
    tasks = []
    for task in tasks_text:
        task = BeautifulSoup(str(task), 'html.parser')

        task_path = str(task.find('a').get('href'))
        task_url = links.root + task_path
        task = get_task(task_url, force_update)
        tasks.append(task)

    return tasks


def get_all_tasks(force_update=False):
    """
    Get all tasks from infoarena and return them as an array of Task.
    It get only tasks from main archive.
    :param force_update: If it is False, the task will be downloaded from the site only if it doesn't exists in
    data.tasks. If it is True, the task will be downloaded and updated anyway.
    :return:
    """
    tasks_page = requests.get(links.tasks_page)
    parsed_tasks_page = BeautifulSoup(tasks_page.text, 'html.parser')

    attrs = {
        'accesskey': re.compile(r"\d+")
    }
    tasks_pages = parsed_tasks_page.find_all('a', attrs=attrs)

    tasks = get_tasks_from_page(links.tasks_page, force_update)
    visited_links = set()
    for tasks_page in tasks_pages:
        tasks_page_link = links.root + tasks_page.get("href")
        if tasks_page_link in visited_links:
            continue
        visited_links.add(tasks_page_link)
        tasks.extend(get_tasks_from_page(tasks_page_link, force_update))

    return tasks


def _extract_info_from_table_task_page(task, table):
    """
    Extract source, author, time limit, memory limit and difficulty from the top table of a problem page.
    :param task: The task where the information will be added.
    :param table: The table with the information.
    :return:
    """
    task_source = table.find_all("tr")[0].find_all("td")[3].text
    task.set_source(task_source)
    task_author = table.find_all("tr")[1].find_all("td")[1].text
    task.set_author(task_author)
    task_time_limit = table.find_all("tr")[2].find_all("td")[1].text
    task.set_time_limit(task_time_limit)
    task_memory_limit = table.find_all("tr")[2].find_all("td")[3].text
    task.set_memory_limit(task_memory_limit)
    task_difficulty = table.find_all("tr")[3].find_all("td")[3].find_all("div", attrs={'class': 'hidden'})[0].text
    task.set_difficulty(task_difficulty)


def _extract_examples_from_table(task, table):
    """
    Get examples of the task from it's page.
    :param task: The task where the examples will be added.
    :param table: Table with the examples.
    :return:
    """
    rows = table.find_all("tr")

    in_file_name = rows[0].find_all("th")[0].text
    task.set_in_file_name(in_file_name)
    out_file_name = rows[0].find_all("th")[1].text
    task.set_out_file_name(out_file_name)

    examples = []
    for example_row in rows[1:]:
        example = {
            "in": example_row.find_all("td")[0].text,
            "out": example_row.find_all("td")[1].text,
        }
        examples.append(example)
    task.set_examples(tuple(examples))


