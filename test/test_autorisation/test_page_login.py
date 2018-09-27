from model.group import Group


def test_page_login_validation(app):
    app.open_home_page()
    app.seesion.disabled_login(Group(username="", password=""))
    app.seesion.disabled_login(Group(username="111111111", password="22222222"))
    app.seesion.disabled_login(Group(username="asdfasdf@mail.ru", password="asdfasdfasdf"))
    app.seesion.disabled_login(Group(username="ывфафывафыва", password="фывафывафыва"))
    app.seesion.disabled_login(Group(username="daniil.golovin@anywayanyday.com", password="asdfasdf"))
    app.seesion.login(Group(username="evgenija.bezsonova@stfalcon.com", password="qwerty"))
    app.seesion.logout()


# Урезать дизейбл логин - не вызывать параметры явно, а через ENV