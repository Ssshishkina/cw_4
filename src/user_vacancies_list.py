from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vacancy:
    """
    Класс для работы с вакансиями.
    employer (str): наименование работодателя
    title (str): наименование вакансии
    location (str): локация вакансии
    url (str): ссылка на вакансию
    salary_from (float): зарплата "от"
    salary_to (float): зарплата "до"
    employment_type (str): тип занятости
    published_date (datetime): дата публикации вакансии
    """
    __slots__ = ("employer", "title", "location", "url", "salary_from", "salary_to",
                 "employment_type", "published_date", "description")

    employer: str
    title: str
    location: str
    url: str
    salary_from: float
    salary_to: float
    employment_type: str
    published_date: datetime
    description: str

    def __repr__(self):
        return f"""
        Работодатель: {self.employer}
        Вакансия: {self.title}
        Город: {self.location}
        Ссылка: {self.url}
        Зарплата от {self.salary_from} до {self.salary_to}
        Тип занятости: {self.employment_type}
        Дата публикации: {self.published_date}
        Описание вакансии: {self.description}"""
