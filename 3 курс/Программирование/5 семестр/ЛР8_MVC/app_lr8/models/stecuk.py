from .user import User 


class UserStecuk(User):

    def __init__(self):
        self.__second_name = "Стецук"
        self.__first_name = "Максим"
        self.__fathers_name = "Николаевич"
        self.__birth_date = "03.03.2003"
        self.__fav_prog_lan = "Python"

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

    def get_b_date(self):
      return self.__birth_date

    def get_f_lan(self):
      return self.__fav_prog_lan