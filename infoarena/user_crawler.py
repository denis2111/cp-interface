"""
This file is handling of infoarena users crawling.
"""
import requests
import re
from bs4 import BeautifulSoup
import links
from structures.user import User
from structures.task import Task


def get_user_info_from_table(user, info_table):
    real_name = info_table.find_all("tr")[0].find_all("td")[1].text
    user.set_real_name(real_name)
    user_name = info_table.find_all("tr")[1].find_all("td")[0].text
    user.set_user_name(user_name)
    rating = info_table.find_all("tr")[2].find_all("td")[0].text
    user.set_rating(rating)


def get_user(link: str) -> User:
    """
    Get an user from his profile(status) page.
    :param link: A link to profile(status) page.
    :return: The user with information from the profile.
    """
    user_id = link.rsplit('?', 1)[0].split('/')[-1]
    user = User(user_id, user_link=link)

    user_page = requests.get(link)
    parsed_user_page = BeautifulSoup(user_page.text, 'html.parser')

    info_table = parsed_user_page.find_all("table", attrs={"class": "compact"})[0]
    get_user_info_from_table(user, info_table)

    solved_tasks_text = parsed_user_page.find_all("div", attrs={"class": "wiki_text_block"})[2]
    solved_tasks_text = solved_tasks_text.find_all("span")[1]
    solved_tasks_text = solved_tasks_text.find_all("a")

    solved_tasks = []
    for solved_task in solved_tasks_text:
        task_id = solved_task['href'].split('/')[-1]
        solved_tasks.append(task_id)
    user.set_solved_tasks(solved_tasks)

    return user


if __name__ == "__main__":
    get_user(links.user_page)