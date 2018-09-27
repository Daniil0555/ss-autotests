class DriverHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Водители").click()

    def open_page_create(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Новый водитель").click()

    def create(self):
        wd = self.app.wd
        wd.find_element_by_id("driver_lastName").click()
        wd.find_element_by_id("driver_lastName").clear()
        wd.find_element_by_id("driver_lastName").send_keys("Головин")
        wd.find_element_by_id("driver_firstName").click()
        wd.find_element_by_id("driver_firstName").clear()
        wd.find_element_by_id("driver_firstName").send_keys("Даниил")
        wd.find_element_by_id("driver_middleName").click()
        wd.find_element_by_id("driver_middleName").clear()
        wd.find_element_by_id("driver_middleName").send_keys("Евгеньевич")
        wd.find_element_by_id("driver_driverProfileDetails_passportNumber").click()
        wd.find_element_by_id("driver_driverProfileDetails_passportNumber").clear()
        wd.find_element_by_id("driver_driverProfileDetails_passportNumber").send_keys("1111 222222")
        wd.find_element_by_id("driver_driverProfileDetails_passportIssuedWhen").click()
        wd.find_element_by_id("driver_driverProfileDetails_passportIssuedWhen").click()
        wd.find_element_by_id("driver_driverProfileDetails_passportIssuedWhen").clear()
        wd.find_element_by_id("driver_driverProfileDetails_passportIssuedWhen").send_keys("04.04.2014")
        wd.find_element_by_id("driver_driverProfileDetails_passportIssuedBy").click()
        wd.find_element_by_id("driver_driverProfileDetails_passportIssuedBy").clear()
        wd.find_element_by_id("driver_driverProfileDetails_passportIssuedBy").send_keys("Аааааааааааааааааааааааа ааааааааааааааааааа ааааааааааааааааааа")
        wd.find_element_by_id("driver_city").click()
        wd.find_element_by_id("driver_city").clear()
        wd.find_element_by_id("driver_city").send_keys("фываыфвафыва")
        wd.find_element_by_id("driver_birthday").click()
        wd.find_element_by_id("driver_birthday").clear()
        wd.find_element_by_id("driver_birthday").send_keys("04.04.1990")
        wd.find_element_by_id("driver_address").click()
        wd.find_element_by_id("driver_address").clear()
        wd.find_element_by_id("driver_address").send_keys("фывафывафыва фывафыва фывафыва")
        wd.find_element_by_id("driver_phoneNumber").click()
        wd.find_element_by_id("driver_phoneNumber").clear()
        wd.find_element_by_id("driver_phoneNumber").send_keys("+79455554433")
        wd.find_element_by_id("driver_email").click()
        wd.find_element_by_id("driver_email").clear()
        wd.find_element_by_id("driver_email").send_keys("smalik007+4434234@mail.ru")
        wd.find_element_by_id("driver_driverLicenseNumber").click()
        wd.find_element_by_id("driver_driverLicenseNumber").clear()
        wd.find_element_by_id("driver_driverLicenseNumber").send_keys("4536436346346")
        wd.find_element_by_id("driver_driverLicenseExpire").click()
        wd.find_element_by_id("driver_driverLicenseExpire").clear()
        wd.find_element_by_id("driver_driverLicenseExpire").send_keys("04.04.2020")
        wd.find_element_by_id("form-submit-button").click()

