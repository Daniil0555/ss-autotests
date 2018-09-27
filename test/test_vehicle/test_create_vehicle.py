from model.group import Group


def test_create_vehicle(app):
    app.open_home_page()
    app.seesion.login(Group(username="evgenija.bezsonova@stfalcon.com", password="qwerty"))
    app.vehicle.open_page()
    app.vehicle.open_page_create()
    #app.vehicle.create()
    app.seesion.logout()
