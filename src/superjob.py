from src.abstract_class import JobBoard
import os
import requests


class SuperJob(JobBoard):
    """Класс для подключения к API и получения вакансий Superjob.ru"""

    url = "https://api.superjob.ru/2.0/vacancies/"
    API_KEY: str = os.getenv('SUPERJOB_API')

    def __init__(self):
        self.url = SuperJob.url
        self.API_KEY = SuperJob.API_KEY

    def get_vacancies(self, keyword: str):
        """
        Метод, осуществляющий подключение  и запрос, по АПИ к сайту Superjob.ru
        params (dict): Параметры запроса к API HeadHunter.
                        count: количество вакансий на странице.
                        page: номер страницы результатов.
                        text: keyword - ключевое слово для поиска вакансии.
                        area: код региона
        headers (dict): Заголовки запроса к API HeadHunter.
        Итоговые значения записываются в json-файл.
        """
        params = {
            "count": 50,  # количество вакансий на странице.
            "page": None,  # номер страницы результатов.
            "keyword": keyword,  # строка поиска по названию вакансии.
            "c": 1,  # Код страны (1 - Россия)
            "t": 4, # Код города (1 - Москва)
        }
        headers = {
            "HH-User-Agent": "parser-for-searching-vacancies-on-superjob.ru",
            "X-Api-App-Id": self.API_KEY

        }
        response = requests.get(self.url, params=params, headers=headers)

        if response.ok:
            data = response.json()
            vacancies_list = []
            try:
                for vacancy in data["objects"]:
                    vacancy_info = {
                        "employer": vacancy.get("firm_name"),
                        "published_date": vacancy.get("date_published"),
                        "employment_type": vacancy.get("type_of_work"),
                        "title": vacancy.get("profession"),
                        "location": vacancy.get("client", {}).get("town", {}).get("title"),
                        "url": vacancy.get("link"),
                        "salary_from": vacancy.get("payment_from") if vacancy["payment_from"] else None,
                        "salary_to": vacancy.get("payment_to") if vacancy["payment_to"] else None
                    }
                    if vacancy_info["salary_from"] is None:
                        vacancy_info["salary_from"] = 0

                    if vacancy_info["salary_to"] is None:
                        vacancy_info["salary_to"] = 0

                    if vacancy_info["salary_to"] == 0:
                        vacancy_info["salary_to"] = vacancy_info["salary_from"]
                    vacancies_list.append(vacancy_info)
                return vacancies_list
            except (ValueError, KeyError):
                print("Ошибка запроса")
        else:
            print("Запрос не выполнен")
            quit()
