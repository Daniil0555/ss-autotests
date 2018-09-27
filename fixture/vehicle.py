class VehicleHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Т/с").click()

    def open_page_create(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Новое Т/С").click()

    def create(self):     #не могу подцепить 2 поля
        wd = self.app.wd
        wd.find_element_by_css_selector("input.select2-search__field").click()
        #wd.find_element_by_css_selector("input.select2-search__field").clear()
        wd.find_element_by_css_selector("input.select2-search__field").send_keys("35320")
        wd.find_element_by_xpath("//div[@class='content-box']/form/div[1]/div[1]/div[2]/div/span/span[1]/span").click()
        #wd.find_element_by_xpath("//div[@class='content-box']/form/div[1]/div[1]/div[2]/div/span/span[1]/span").send_keys("")
        wd.find_element_by_css_selector("input.select2-search__field").click()
        wd.find_element_by_css_selector("input.select2-search__field").clear()
        wd.find_element_by_css_selector("input.select2-search__field").send_keys("КаМаз")
        wd.find_element_by_xpath("//div[@class='content-box']/form/div[1]/div[1]/div[1]/div/span/span[1]/span").click()
        wd.find_element_by_xpath("//div[@class='content-box']/form/div[1]/div[1]/div[1]/div/span/span[1]/span").send_keys("")