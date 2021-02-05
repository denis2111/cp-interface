class Task:
    def __init__(self, task_id, name="", task_link="", source="", author="", time_limit="", memory_limit="", difficulty="N/A",
                 link_name="", in_file_name="", out_file_name="", examples=(), standard_io=False, statement=""):
        self._task_id = task_id
        self._task_link = task_link
        self._name = name
        self._source = source
        self._author = author
        self._time_limit = time_limit
        self._memory_limit = memory_limit
        self._difficulty = difficulty
        self._link_name = link_name
        self._in_file_name = in_file_name
        self._out_file_name = out_file_name
        self._examples = examples
        self._standard_io = standard_io
        self._statement = statement

    @property
    def task_id(self):
        return self._task_id

    def set_link(self, link):
        self._task_link = link

    @property
    def task_link(self):
        return self._task_link

    def set_name(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def set_source(self, source):
        self._source = source

    @property
    def source(self):
        return self._source

    def set_author(self, author):
        self._author = author

    @property
    def author(self):
        return self._author

    def set_time_limit(self, time_limit):
        self._time_limit = time_limit

    @property
    def time_limit(self):
        return self._time_limit

    def set_memory_limit(self, memory_limit):
        self._memory_limit = memory_limit

    @property
    def memory_limit(self):
        return self._memory_limit

    def set_difficulty(self, difficulty):
        self._difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    def set_link_name(self, link_name):
        self._link_name = link_name

    @property
    def link_name(self):
        return self._link_name

    def set_in_file_name(self, in_file_name):
        self._in_file_name = in_file_name

    @property
    def in_file_name(self):
        return self._in_file_name

    def set_out_file_name(self, out_file_name):
        self._out_file_name = out_file_name

    @property
    def out_file_name(self):
        return self._out_file_name

    def set_examples(self, examples):
        """
        Examples is a tuple of examples. Each example is a dictionary with two fields: in and out.
        :param examples:
        :return:
        """
        self._examples = examples

    @property
    def examples(self):
        """
        Examples is an array of examples. Each example is a dictionary with two fields: in and out.
        :return:
        """
        return self._examples

    def set_standard_io(self, standard_io):
        self._standard_io = standard_io

    @property
    def standard_io(self):
        return self._standard_io

    def set_statement(self, statement):
        self._statement = statement

    @property
    def statement(self):
        return self._statement
