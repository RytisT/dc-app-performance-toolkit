from selenium.webdriver.common.by import By
from selenium_ui.conftest import print_timing
from util.conf import BITBUCKET_SETTINGS

from selenium_ui.base_page import BasePage


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_snippets_page")
        def sub_measure():
            page.go_to_url(f"{BITBUCKET_SETTINGS.server_url}/snippets/browse")
            page.wait_until_visible((By.CLASS_NAME, 'list-snippets')) # Wait for repo navigation panel is visible
            page.go_to_url(f"{BITBUCKET_SETTINGS.server_url}/snippets/02ced55ffa824d42b9404afb00aa5a38")
            page.wait_until_visible((By.CLASS_NAME, 'snippet-file-header')) # Wait for repo navigation panel is visible
        sub_measure()
    measure()
