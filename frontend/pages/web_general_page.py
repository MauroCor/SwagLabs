from selenium.webdriver.common.by import By


class WebGeneralPage:
    elements = {
        "PRODUCT-BUTTON": "//div[div/a/div/text()='{}']//button",
        "BUTTON": "//*[local-name() = 'a' or local-name() = 'button'][text()='{}']",
    }

    ancestors = [
        "@style='display: none;'",
        "@class='modal fade'"
    ]

    @staticmethod
    def not_ancestors():
        not_ancestors = "[not("
        for a in WebGeneralPage.ancestors:
            if WebGeneralPage.ancestors.index(a) != 0:
                not_ancestors += " or "
            not_ancestors += f"ancestor::*[{a}]"
        not_ancestors += ")]"
        return not_ancestors

    @staticmethod
    def elem(element, param):
        elem = (By.XPATH, WebGeneralPage.elements.get(element).format(param) + WebGeneralPage.not_ancestors())
        return elem
