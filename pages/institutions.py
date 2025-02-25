from selenium.webdriver.common.by import By

import settings
from base.locators import ComponentLocator, GroupLocator, Locator
from components.navbars import InstitutionsNavbar
from pages.base import OSFBasePage


class InstitutionsLandingPage(OSFBasePage):
    url = settings.OSF_HOME + '/institutions/'

    # TODO fix insitution typo
    identity = Locator(
        By.CSS_SELECTOR, 'div[data-test-insitutions-header]', settings.VERY_LONG_TIMEOUT
    )

    search_bar = Locator(By.CSS_SELECTOR, '.ember-text-field')

    # Group Locators
    institution_list = GroupLocator(By.CSS_SELECTOR, 'span[data-test-institution-name]')

    navbar = ComponentLocator(InstitutionsNavbar)


class InstitutionBrandedPage(OSFBasePage):

    identity = Locator(
        By.CSS_SELECTOR,
        '#fileBrowser > div.db-header.row > div.db-buttonRow.col-xs-12.col-sm-4.col-lg-3 > div > input',
    )
