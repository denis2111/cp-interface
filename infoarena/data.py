import cacheing

tasks = dict()
users = dict()


def load_data():
    global tasks
    global users

    tasks = cacheing.load_tasks()
    users = cacheing.load_users()


def persist_data():
    cacheing.persist_tasks(tasks)
    cacheing.persist_users(users)


load_data()
