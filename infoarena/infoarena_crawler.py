"""
This file put together all functions for crawling infoarena.
"""

import data

from tasks_crawler import get_task
from tasks_crawler import get_tasks_from_page
from tasks_crawler import get_all_tasks

if __name__ == "__main__":
    import links
    # task = get_task(links.task_page)
    tasks = get_tasks_from_page(links.tasks_page)
    # print(tasks[1].name)
    data.persist_data()
