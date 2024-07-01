from playwright.sync_api import expect


class DatasetsPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator('[aria-label="Enter your search term"]')

    def check_dataset_icon(self):
        self.page.wait_for_selector('//*[@data-tooltip-content="My Datasets"]')

    def create_new_dataset(self, title):
        self.page.click('//*[@data-tooltip-content="Create a new dataset"]')
        self.page.type('//input[@placeholder="Add dataset title e.g my first dataset"]', title)
        self.page.click('//*[contains(@class, "modalInnerContainerExpanded")]//img[contains(@src,"BlackCross")]')

    def verify_header(self):
        locator = self.page.locator('//*[contains(@class, "headerContainer")]')
        expect(locator).to_contain_text("My Datasets")

    def verify_left_menu(self):
        raise NotImplementedError
