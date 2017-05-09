import easygui
import sys

import functions


def find_steam_path():
    msg = 'Выберите путь до папки Steam'
    title = 'Путь к Steam'
    steam_path = easygui.diropenbox(msg, title)
    if steam_path is not None:
        functions.set_steam_path(steam_path + '\Steam.exe')


def add_account():
    msg = 'Введите логин и пароль для аккаунта'
    title = 'Добавление аккаунта'
    fieldNames = ["Название", "Логин", "Пароль"]
    login_data = easygui.multenterbox(msg, title, fieldNames)
    if login_data is not None:
        acc = {login_data[0]: {
            'login': login_data[1],
            'password': login_data[2]
            }
        }
        functions.add_acc(acc)


def choice_account():
    accs = functions.read_accs()
    msg = 'Выберите аккаунт'
    title = 'Выбор аккаунта'
    choices = []
    for acc in accs:
        choices.append(acc)
    if choices != []:
        choice = easygui.choicebox(msg, title, choices)
        if choice == 'Add more choices':
            msg = 'Больше никогда это не выбирай'
            title = 'Аккаунты'
            easygui.msgbox(msg, title)
            choice_account()
        if choice is not None:
            functions.login(accs[choice])
    else:
        msg = 'У вас нет аккаунтов'
        title = 'Аккаунты'
        easygui.msgbox(msg, title)


def main():
    msg = "Выберите действие"
    title = "Steam Account Manager"
    choices = ["Выбрать аккаунт", "Добавить аккаунт", "Настройки", "Выйти"]
    choice = easygui.choicebox(msg, title, choices)
    if choice == 'Выбрать аккаунт':
        if choice_account() is None:
            main()
    if choice == 'Добавить аккаунт':
        if add_account() is None:
            main()
    if choice == 'Настройки':
        if find_steam_path() is None:
            main()
    if choice == 'Выйти':
        sys.exit(0)


if __name__ == '__main__':
    main()
