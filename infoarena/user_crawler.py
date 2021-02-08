"""
This file is handling of infoarena users crawling.
"""
import requests
from bs4 import BeautifulSoup
from structures.user import User
from utils import data
from crawler.users_crawler_interface import UsersCrawlerInterface
from config import *
from infoarena import links


class InfoarenaUsersCrawler(UsersCrawlerInterface):
    @staticmethod
    def _get_user_info_from_table(user, info_table):
        real_name = info_table.find_all("tr")[0].find_all("td")[1].text
        user.set_real_name(real_name)
        user_name = info_table.find_all("tr")[1].find_all("td")[0].text
        user.set_user_name(user_name)
        rating = info_table.find_all("tr")[2].find_all("td")[0].text
        user.set_rating(rating)

    @staticmethod
    def get_user(link: str, force_update=False) -> User:
        """
        Get an user from his profile(status) page.
        :param link: A link to profile(status) page.
        :param force_update: If it is False, the user will be downloaded from the site only if it doesn't exists in
        data.users. If it is True, the user will be downloaded and updated anyway.
        :return: The user with information from the profile.
        """
        user_id = INFOARENA_PREFIX + '-' + link.rsplit('?', 1)[0].split('/')[-1]
        user = User(user_id, user_link=link)

        if not force_update:
            if user.user_id in data.users:
                return data.users.get(user.user_id)

        user_page = requests.get(link)
        parsed_user_page = BeautifulSoup(user_page.text, 'html.parser')

        info_table = parsed_user_page.find_all("table", attrs={"class": "compact"})[0]
        InfoarenaUsersCrawler._get_user_info_from_table(user, info_table)

        solved_tasks_text = parsed_user_page.find_all("div", attrs={"class": "wiki_text_block"})[2]
        solved_tasks_text = solved_tasks_text.find_all("span")[1]
        solved_tasks_text = solved_tasks_text.find_all("a")

        solved_tasks = []
        for solved_task in solved_tasks_text:
            task_id = solved_task['href'].split('/')[-1]
            solved_tasks.append(task_id)
        user.set_solved_tasks(solved_tasks)

        data.users[user.user_id] = user
        return user

    @staticmethod
    def get_user_by_id(user_id: str, force_update=False) -> User:
        """
        Get an user from his profile(status) page.
        :param user_id: id of an user
        :param force_update: If it is False, the user will be downloaded from the site only if it doesn't exists in
        data.users. If it is True, the user will be downloaded and updated anyway.
        :return: The user with information from the profile.
        """
        link = links.get_user_page_from_id(user_id.split('-')[-1])
        return InfoarenaUsersCrawler.get_user(link, force_update)

    @staticmethod
    def get_prefix() -> str:
        return INFOARENA_PREFIX
