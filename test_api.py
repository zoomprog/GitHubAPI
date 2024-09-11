import os
from github import Github
from github.GithubException import GithubException
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение токена из переменной окружения
token = os.getenv("GITHUB_TOKEN")

if not token:
    raise ValueError("Необходимо установить переменную окружения GITHUB_TOKEN")

# Аутентификация с использованием токена
g = Github(token)
user = g.get_user()

def create_repo(repo_name):
    try:
        # Проверка на существование репозитория
        user.get_repo(repo_name)
        print(f"Репозиторий с именем {repo_name} уже существует.")
    except GithubException as e:
        if e.status == 404:
            repo = user.create_repo(repo_name, private=False)
            print(f"Создан репозиторий: {repo.full_name}")
        else:
            print(f"Ошибка при создании репозитория: {e}")

def delete_repo(repo_name):
    try:
        repo_to_delete = user.get_repo(repo_name)
        repo_to_delete.delete()
        print(f"Репозиторий {repo_name} удален.")
    except GithubException as e:
        if e.status == 404:
            print(f"Репозиторий {repo_name} не найден.")
        else:
            print(f"Ошибка при удалении репозитория: {e}")

def main():
    while True:
        print("Меню:")
        print("1. Создать репозиторий")
        print("2. Удалить репозиторий")
        print("3. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            repo_name = input("Введите имя репозитория для создания: ")
            create_repo(repo_name)
        elif choice == '2':
            repo_name = input("Введите имя репозитория для удаления: ")
            delete_repo(repo_name)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
