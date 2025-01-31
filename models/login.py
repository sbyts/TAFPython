import time

from env import BASE_URL

NEXT_BUTTON = "//*[contains(text(),'Next')]"
LOGIN_BUTTON = "//button[@class = 'login-with-button google-login-button']"


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        # logging.info('Go to ' + full_url)
        self.page.goto(BASE_URL + '/login')
        self.page.wait_for_selector(LOGIN_BUTTON)

    def login(self, user, password):
        self.navigate()
        self.page.locator(LOGIN_BUTTON).click(force=True, timeout=100000)
        with self.page.expect_popup() as popup_info:
            popup = popup_info.value
            popup.wait_for_selector("//input[@type='email']").fill(user)
            popup.click(NEXT_BUTTON)
            popup.wait_for_selector("//input[@type='password']").fill(password)
            popup.click(NEXT_BUTTON)
