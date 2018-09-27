from model.group import Group


def test_create_drivers(app):
    app.open_home_page()
    app.seesion.login(Group(username="evgenija.bezsonova@stfalcon.com", password="qwerty"))
    app.driver.open_page()
    app.driver.open_page_create()
    app.driver.create()
    app.seesion.logout()

# Урезать логин - не вызывать параметры явно, а через ENV