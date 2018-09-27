from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.seesion import SeesionHelper
from fixture.driver import DriverHelper
from fixture.forgot_password import ForgotPassword
from fixture.vehicle import VehicleHelper


class Aplication:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.seesion = SeesionHelper(self)
        self.driver = DriverHelper(self)
        self.forgot = ForgotPassword(self)
        self.vehicle = VehicleHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://smartseeds.ru/login") # Это не домашняя страница :(

    def destroy(self):
        self.wd.quit()
