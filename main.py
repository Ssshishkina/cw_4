from utils.user_interaction import choose_platform, top_vacancies
from src.json_storage import JSONStorageVacancy


def main():
    """Функция для взаимодействия с пользователем"""

    storage = JSONStorageVacancy("vacancies.json")
    while True:
        print('Привет! Данная программа выполняет поиск вакансий на платформах HH.ru и SuperJob.ru')
        choose_platform()
        print(f'По вашему запросу найдено {storage.len_vacancies()} вакансий')
        top_vacancies()
        input_user = int(input("\nВы хотите продолжить поиск вакансий?\n1 - Да\n2 - Нет\n"
                               "\nВведите выбранный вариант: "))
        if input_user == 1:
            continue
        elif input_user == 2:
            print("\nБудем рады помочь в поисках работы мечты! До встречи!")
            break
        else:
            print("Некорректный ввод!\n")


if __name__ == "__main__":
    main()
