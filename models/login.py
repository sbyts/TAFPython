
from env import BASE_URL

NEXT_BUTTON = "//*[contains(text(),'Next')]"


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        # logging.info('Go to ' + full_url)
        self.page.goto(BASE_URL + '/login')
        self.page.wait_for_selector('.google-auth-login')

    def login(self, user, password):
        self.navigate()
        with self.page.expect_popup() as popup_info:
            self.page.click(".google-auth-login")
        popup = popup_info.value
        popup.wait_for_selector("//input[@type='email']").fill(user)
        popup.click(NEXT_BUTTON)
        popup.wait_for_selector("//input[@type='password']").fill(password)
        popup.click(NEXT_BUTTON)
