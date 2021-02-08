from structures.user import User


class UsersCrawlerInterface:
    @staticmethod
    def get_user(link: str, force_update=False) -> User:
        """
        Get an user from his profile(status) page.
        :param link: A link to profile(status) page.
        :param force_update: If it is False, the user will be downloaded from the site only if it doesn't exists in
        data.users. If it is True, the user will be downloaded and updated anyway.
        :return: The user with information from the profile.
        """
        pass

    @staticmethod
    def get_user_by_id(user_id: str, force_update=False) -> User:
        pass

    @staticmethod
    def get_prefix() -> str:
        pass
