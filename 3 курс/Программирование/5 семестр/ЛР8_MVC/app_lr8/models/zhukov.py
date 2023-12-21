from .user import User 


class UserZhukov(User):

    def __init__(self):
        self.__second_name = "Жуков"
        self.__first_name = "Николай"
        self.__fathers_name = "Николаевич"

    def get_first_name(self):
        return self.__first_name

    def show_name(self):
        print(
            f"{self.__second_name} {self.__first_name} {self.__fathers_name}")

    def get_fullname(self):

        fullname = {
            'first_name': self.__first_name,
            'second_name': self.__second_name,
            'fathers_name': self.__fathers_name
        }
        return fullname

    def get_personal_id(self):
        return 3869


