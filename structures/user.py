from structures.task import Task


class User:
    def __init__(self, user_id, user_name="", real_name="", rating="", solved_tasks=None, tried_tasks=None,
                 user_link=""):
        if solved_tasks is None:
            solved_tasks = dict()
        if tried_tasks is None:
            tried_tasks = dict()
        self._user_id = user_id
        self._user_name = user_name
        self._real_name = real_name
        self._rating = rating
        self._solved_tasks = solved_tasks
        self._tried_tasks = tried_tasks
        self._user_link = user_link

    @property
    def user_id(self):
        return self._user_id

    def set_user_name(self, user_name):
        self._user_name = user_name

    @property
    def user_name(self):
        return self._user_name

    def set_real_name(self, real_name):
        self._real_name = real_name

    @property
    def real_name(self):
        return self._real_name

    def set_rating(self, rating):
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    def set_solved_tasks(self, solved_tasks):
        """
        :param solved_tasks: A dictionary with task_id as key and task as value.
        :return:
        """
        self._solved_tasks = solved_tasks

    @property
    def solved_tasks(self):
        """
        Solved tasks is a dictionary with task_id as key and task as value.
        :return: A dictionary with solved tasks.
        """
        return self._solved_tasks

    def set_tried_tasks(self, tried_tasks):
        """
        :param tried_tasks: A dictionary with task_id as key and task as value.
        :return:
        """
        self._tried_tasks = tried_tasks

    @property
    def tried_tasks(self):
        """
        Tried tasks is a dictionary with task_id as key and task as value.
        :return: A dictionary with tried tasks.
        """
        return self._tried_tasks

    def set_user_link(self, user_link):
        self._user_link = user_link

    @property
    def user_link(self):
        return self._user_link
