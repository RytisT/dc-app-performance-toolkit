from selenium.webdriver.common.by import By
from selenium_ui.conftest import print_timing
from util.conf import CONFLUENCE_SETTINGS

from selenium_ui.base_page import BasePage
from selenium_ui.confluence.pages.pages import Login, AllUpdates, PopupManager, Page, Dashboard, TopNavPanel, Editor, \
    Logout

def app_specific_action(webdriver, datasets):
    edit_page = Editor(webdriver, page_id=datasets['page_id'])

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:view_source_editor")
        def sub_measure():
            edit_page.go_to()
            edit_page.wait_for_page_loaded()
            edit_page.wait_until_visible((By.ID, "rte-source-editor-button"))  # Wait for title field visible
            button = (By.ID, 'rte-source-editor-button')
            edit_page.get_element(button).click()
            edit_page.wait_until_visible((By.CLASS_NAME, "monaco-editor"))  # Wait for title field visible
        sub_measure()


        @print_timing("selenium_app_custom_action:submit_source_editor_content")
        def sub_measure():
            button = (By.XPATH, "//button[.//span//text()='Apply']")
            edit_page.get_element(button).click()

            edit_page.wait_until_invisible((By.CLASS_NAME, "monaco-editor"))  # Wait for title field visible
        sub_measure()
    measure()
