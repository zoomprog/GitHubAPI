# Manage GitHub Repository

Этот проект предоставляет скрипт на Python для управления репозиториями на GitHub. Скрипт позволяет создавать и удалять репозитории, используя GitHub API.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/zoomprog/GitHubAPI.git
    cd GitHubAPI
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корне проекта и добавьте ваш GitHub токен:
    ```env
    GITHUB_TOKEN=your_github_token
    ```
5. Запустите скрипт
```commandline
python test_api.py
```

## Использование

Запустите скрипт:
```sh
python manage_repo.py
```
## Перед вами будет меню с выбором:
1. Создать репозиторий
2. Удалить репозиторий
3. Выйти

Выберите нужную опцию и следуйте инструкциям на экране.


