class SeesionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, group):  # установил сигнатуру метода, что бы передавать параметры явно
        wd = self.app.wd
        # Если изменим домашнюю страницу, нужно добавить сюда переход на форму логина
        wd.find_element_by_id("inputEmail").click()
        wd.find_element_by_id("inputEmail").clear()
        wd.find_element_by_id("inputEmail").send_keys(group.username)
        wd.find_element_by_id("inputPassword").click()
        wd.find_element_by_id("inputPassword").clear()
        wd.find_element_by_id("inputPassword").send_keys(group.password)
        wd.find_element_by_xpath("//form[@class='has-validation-callback']//button[.='Войти']").click()

    def disabled_login(self, group):
        # Нужно добавить цикл с невалидными данными, что бы не вызывать их явно в тесте
        wd = self.app.wd
        wd.find_element_by_id("inputEmail").click()
        wd.find_element_by_id("inputEmail").clear()
        wd.find_element_by_id("inputEmail").send_keys(group.username)
        wd.find_element_by_id("inputPassword").click()
        wd.find_element_by_id("inputPassword").clear()
        wd.find_element_by_id("inputPassword").send_keys(group.password)
        wd.find_element_by_xpath("//form[@class='has-validation-callback']//button[.='Войти']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_id("profile-menu-trigger").click()
        wd.find_element_by_link_text("Выйти").click()
