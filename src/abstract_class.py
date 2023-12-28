from abc import ABC, abstractmethod


class JobBoard(ABC):
    """ Абстрактный класс для работы по API с вакансиями."""
    @abstractmethod
    def get_vacancies(self, keyword: str):
        """ Функция подключения к сайту по API и получения списка вакансий."""
        pass
