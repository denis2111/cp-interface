import pickle
from os import path

TASKS_CACHE_FILE_NAME = "tasks_cache.pkl"
USERS_CACHE_FILE_NAME = "users_cache.pkl"


def persist_tasks(tasks):
    try:
        with open(TASKS_CACHE_FILE_NAME, "wb") as tasks_file:
            pickle.dump(tasks, tasks_file)
    except:
        print(f"Persisting tasks in file {TASKS_CACHE_FILE_NAME} failed!")


def load_tasks():
    try:
        if not path.exists(TASKS_CACHE_FILE_NAME):
            return dict()
        with open(TASKS_CACHE_FILE_NAME, "rb") as tasks_file:
            tasks = pickle.load(tasks_file)
            if not isinstance(tasks, dict):
                return dict()
            return tasks
    except:
        return dict()


def persist_users(users):
    try:
        with open(USERS_CACHE_FILE_NAME, "rb") as users_file:
            pickle.dump(users, users_file)
    except:
        print(f"Persisting users in file {USERS_CACHE_FILE_NAME} failed!")


def load_users():
    try:
        if not path.exists(USERS_CACHE_FILE_NAME):
            return dict()
        with open(USERS_CACHE_FILE_NAME, "rb") as users_file:
            users = pickle.load(users_file)
            if not isinstance(users, dict):
                return dict()
            return users
    except:
        return dict()
