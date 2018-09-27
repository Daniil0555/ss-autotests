class ForgotPassword:

    def __init__(self, app):
        self.app = app

    def open_page_forgot_password(self):
        wd = self.app.wd
        wd.find_element_by_class_name("help-link__text").click()

    def fill_disabled_email_and_submit(self, email):
        # Нужно добавить цикл по невалидным данным, что бы не вызывать их явно
        wd = self.app.wd
        wd.find_element_by_id("request_token_email").click()
        wd.find_element_by_id("request_token_email").clear()
        wd.find_element_by_id("request_token_email").send_keys(email)
        wd.find_element_by_name("submitBtn").click()

    def fill_email_and_submit(self, email):
        wd = self.app.wd
        wd.find_element_by_id("request_token_email").click()
        wd.find_element_by_id("request_token_email").clear()
        wd.find_element_by_id("request_token_email").send_keys(email)
        wd.find_element_by_name("submitBtn").click()


    # Нужно дописать проверку отправленного письма