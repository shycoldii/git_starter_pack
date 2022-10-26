# git_starter_pack

<h1>Начало</h1>

1. Поставь репозиторию звездочку
2. Сделай fork репозитория
3. Открой на своем компьютере папку для будущего проекта
4. Открой терминал в этой папке и склонируй удаленный репозиторий с помощью git clone
5. Открой проект с помощью Pycharm
6. Запусти основной файл

<h1> Возвращаемся в прошлое </h1>

git config —-local user.name "John Doe"

git config —-local user.email johndoe@example.com

1. Попробуй сделать изменение в файле binary_search.py
2. git add binary_search.py 
3. git commit -m "Something terribly misguided"
4. git reset HEAD~ - Undo last commit
5. Убираем свои изменения и добавляем где-то пробел, чтобы было что-то новенькое
6. git add .
7. git commit -m "Cool commit"
8. git push origin main

<h1> Откат отправленного коммита на GitHub обратно </h1>

1. git push origin +62b182ac^:main , где 62b182ac - номер коммита, который хотим откатить
2. Убеждаемся, что пуш откатился

<h1> Теги... Теги! </h1>

1. git tag
2. git tag v1.0
3. git tag
4. git push origin v1.0
5. Видим тег в репозитории
6. git push —delete origin v1.0  - откатываем тег из репозитория
