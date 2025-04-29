import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://docs.djangoproject.com/en/5.2/")
    page.locator("#s-first-steps").get_by_role("link", name="Overview").click()
    page.get_by_role("link", name="data-model syntax").click()
    page.locator("[id=\"s-module-django\\.db\\.models\"]").get_by_role("link", name="Making queries").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

