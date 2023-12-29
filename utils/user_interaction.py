from src.hh import HH
from src.superjob import SuperJob
from src.json_storage import JSONStorageVacancy
from src.user_vacancies_list import Vacancy


def choose_platform():
    """Функция выбора платформы для поиска вакансий"""

    # Создаем объект Класса JSONStorageVacancy
    storage = JSONStorageVacancy("vacancies.json")

    while True:
        platform_choosing = input("\nВыберите платформу для поиска вакансий.\n"
                                  "1 - HeadHunter\n2 - SuperJob\n3 - На обеих платформах\n"
                                  "\nВведите выбранный вариант: ")

        if platform_choosing == '1':
            print("\nВы выбрали платформу HeadHunter.\n")
            keyword = input("Введите название вакансии для поиска: ")
            print(f"\nИдет сбор информации.\n")
            hh = HH()
            hh_vacancies = hh.get_vacancies(keyword)
            headhunter_vacancies = storage.add_vacancies(hh_vacancies)
            if storage.len_vacancies() == 0:
                print("К сожалению, по данному запросу вакансий не найдено.\n"
                      "Попробуйте изменить запрос!\n")
                continue
            return headhunter_vacancies
        elif platform_choosing == '2':
            print("\nВы выбрали платформу SuperJob.\n")
            keyword = input("Введите название вакансии для поиска: ")
            print(f"\nИдет сбор информации.\n")
            sj = SuperJob()
            sj_vacancies = sj.get_vacancies(keyword)
            superjob_vacancies = storage.add_vacancies(sj_vacancies)
            if storage.len_vacancies() == 0:
                print("К сожалению, по данному запросу вакансий не найдено.\n"
                      "Попробуйте изменить запрос!\n")
                continue
            return superjob_vacancies
        elif platform_choosing == '3':
            print("\nВы выбрали обе платформы.\n")
            keyword = input("Введите название вакансии для поиска: ")
            print(f"\nИдет сбор информации.\n")
            hh = HH()
            sj = SuperJob()
            hh_vacancies = hh.get_vacancies(keyword)
            sj_vacancies = sj.get_vacancies(keyword)
            all_vacancies = hh_vacancies + sj_vacancies
            json_vacancies_all = storage.add_vacancies(all_vacancies)
            if storage.len_vacancies() == 0:
                print("К сожалению, по данному запросу вакансий не найдено.\n"
                      "Попробуйте изменить запрос!\n")
                continue
            return json_vacancies_all
        else:
            print("Указано неверное значение.\n"
                  "Попробуйте изменить запрос!\n")


def sort_vacancies() -> list[dict]:
    """Функция сортировки полученных вакансий по зарплате (от большего к меньшему)"""

    storage = JSONStorageVacancy("vacancies.json")

    vacancies = storage.get_vacancies()
    sorted_vacancies = sorted(vacancies, key=lambda vacancy: vacancy["salary_from"], reverse=True)
    storage.add_vacancies(sorted_vacancies)
    return sorted_vacancies


def top_vacancies():
    """Выводит топ-вакансий по зарплате"""

    user_input = input("Вывести топ-вакансий по зарплате, нажмите:\n1 - для получения\n2 - для отмены\n")
    if user_input.title() == '1':
        storage = JSONStorageVacancy("vacancies.json")
        vacancies = storage.get_vacancies()
        sorted_vacancies = sorted(vacancies, key=lambda vacancy: vacancy["salary_from"], reverse=True)
        top_sorted_vacancies = sorted_vacancies
        for vacancy in top_sorted_vacancies:
            vac = Vacancy(vacancy['published_date'], vacancy['employer'], vacancy['title'], vacancy['location'],
                          vacancy['url'], vacancy['employment_type'], vacancy['salary_from'], vacancy['salary_to'],
                          vacancy.get('description'))
            print(repr(vac))
    elif user_input.title() == '2':
        storage = JSONStorageVacancy("vacancies.json")
        vacancies = storage.get_vacancies()
        vacancies_1 = vacancies
        for vacancy in vacancies_1:
            vac = Vacancy(vacancy['published_date'], vacancy['employer'], vacancy['title'], vacancy['location'],
                          vacancy['url'], vacancy['employment_type'], vacancy['salary_from'], vacancy['salary_to'],
                          vacancy.get('description'))
            print(repr(vac))
    else:
        print("Некорректный ввод, повторите попытку")
