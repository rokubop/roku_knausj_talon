class BaseGame:
    __app_name: str
    __icon_path: str

    def __init__(self, app_name: str, icon_path: str):
        self.__app_name = app_name
        self.__icon_path = icon_path

    def get_app_name(self):
        """should return the same value as App.name of the game so that it can be automatically detected"""
        return self.__app_name

    def get_icon_path(self):
        return self.__icon_path
