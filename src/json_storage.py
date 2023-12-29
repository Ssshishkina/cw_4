from abc import ABC, abstractmethod
import json


class JSONStorage(ABC):
    """Абстрактный класс для работы с JSON-файлом списка вакансий"""

    @abstractmethod
    def add_vacancies(self, vacancies):
        """Функция сохранения найденных вакансии в JSON-файл"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Функция вывода вакансий из JSON-файла"""
        pass

    @abstractmethod
    def selected_vacancies(self, criterion):
        """Функция сортировки вакансий в JSON-файле"""
        pass

    @abstractmethod
    def delete_vacancies(self, criterion):
        """Функция удаления вакансий из JSON-файла"""
        pass


class JSONStorageVacancy(JSONStorage):
    """Класс для работы с JSON-файлом вакансий"""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def add_vacancies(self, vacancies: list[dict]):
        """Функция сохранения найденных вакансии в JSON-файл"""

        with open(self.file_path, "w", encoding='UTF-8') as file:
            json.dump(vacancies, file, indent=2, ensure_ascii=False)

    def get_vacancies(self):
        """Функция вывода вакансий из JSON-файла"""
        with open(self.file_path, "r", encoding='UTF-8') as file:
            vacancies = json.load(file)
            return vacancies

    def selected_vacancies(self, criterion):
        """Функция сортировки вакансий в JSON-файле по заданному критерию"""

        result = []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                for value in vacancy.values():
                    if criterion in str(value):
                        result.append(vacancy)

        with open(self.file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(result, json_file, ensure_ascii=False, indent=2)
            json_file.write('\n')

        return result

    def delete_vacancies(self, criterion):
        """Функция удаления вакансий из JSON-файла по заданному критерию"""
        with open(self.file_path, "r", encoding='UTF-8') as file:
            data = json.load(file)
        for vacancy in data:
            if vacancy != criterion:
                data.remove(vacancy)

        with open(self.file_path, "w", encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def len_vacancies(self) -> int:
        """Подсчет количества вакансий в JSON-файле"""
        with open(self.file_path, "r", encoding='UTF-8') as file:
            vacancies = json.load(file)
        try:
            vacancies_count = len(vacancies)
            return vacancies_count
        except TypeError:
            print("Список вакансий пустой.\n")
