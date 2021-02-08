from typing import List

from structures.task import Task


class TasksCrawlerInterface:
    @staticmethod
    def get_task(link: str, force_update=False) -> Task:
        """
        Get all information about a task from it's page.
        :param force_update: If it is False, the task will be downloaded from the site only if it doesn't exists in
        data.tasks. If it is True, the task will be downloaded and updated anyway.
        :param link:
        :return:
        """
        pass

    @staticmethod
    def get_all_tasks(force_update=False) -> List[Task]:
        """
        Get all tasks from archive and return them as an array of Task.
        It get only tasks from main archive.
        :param force_update: If it is False, the task will be downloaded from the site only if it doesn't exists in
        data.tasks. If it is True, the task will be downloaded and updated anyway.
        :return:
        """
        pass

    @staticmethod
    def get_prefix() -> str:
        pass
