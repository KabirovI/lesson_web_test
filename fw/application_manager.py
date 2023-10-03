from fw.actions_in_main_page import ActionsInMainPage
from fw.driverinstance import DriverInstance


class ApplicationManager:

    def __init__(self):
        self.actions_in_main_page = ActionsInMainPage(self)
        self.driver_instance = DriverInstance()
