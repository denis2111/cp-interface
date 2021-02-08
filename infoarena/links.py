root = "https://www.infoarena.ro"
tasks_page = "https://infoarena.ro/arhiva?filtru=&display_entries=250&first_entry=0"
user_page = "https://www.infoarena.ro/utilizator/"
task_page = "https://infoarena.ro/problema/gard"


def get_user_page_from_id(user_id:str) -> str:
    return user_page + user_id + "?action=stats"