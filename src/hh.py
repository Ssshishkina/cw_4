from src.abstract_class import JobBoard
import requests

class HH(JobBoard):
    """Класс для подключения к API и получения вакансий HeadHunter.ru"""
    url = "https://api.hh.ru/vacancies"

    def __init__(self) -> None:
        self.url = HH.url

    def get_vacancies(self, keyword: str):
        """
        keyword (str): ключевое слово для поиска вакансий.
        params (dict): параметры запроса к API HeadHunter.
        headers (dict): заголовки запроса к API HeadHunter.
        Итоговые значения записываются в JSON-файл.
        """
        params = {
            "per_page": 50,  # количество вакансий на странице.
            "page": None,  # номер страницы результатов.
            "text": keyword,  # поиск по названию вакансии.
            "area": 1,  # Код региона (1 - Москва)
        }
        headers = {
            "HH-User-Agent": "PyCharm_Parsing"
        }
        response = requests.get(self.url, params=params, headers=headers)
        if response.ok:
            data = response.json()
            vacancies_list = []
            for vacancy in data["items"]:
                vacancy_info = {
                    "published_date": vacancy.get("published_at"),
                    "employer": vacancy["employer"].get("name"),
                    "title": vacancy.get("name"),
                    "location": vacancy["area"].get("name"),
                    "url": vacancy.get("apply_alternate_url"),
                    "employment_type": vacancy["schedule"].get("name"),
                    "salary_from": vacancy["salary"].get("from") if vacancy["salary"] else None,
                    "salary_to": vacancy["salary"].get("to") if vacancy["salary"] else None,
                    "description": vacancy.get("snippet", {}).get("requirement")
                }
                if vacancy_info["salary_from"] is None:
                    vacancy_info["salary_from"] = 0

                if vacancy_info["salary_to"] is None:
                    vacancy_info["salary_to"] = 0

                if vacancy_info["salary_to"] == 0:
                    vacancy_info["salary_to"] = vacancy_info["salary_from"]

                vacancies_list.append(vacancy_info)
            return vacancies_list
        quit()
