import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


@pytest.mark.true
def test_selenium_web_google(driver):
    url_google = "https://www.google.com/"

    driver.get(url_google)

    assert driver.title == "Google"
    assert driver.current_url == url_google


@pytest.mark.true
def test_selenium_web_github(driver):
    url_githab = "https://github.com/"

    driver.get(url_githab)

    assert (
        driver.title == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub"
    )
    assert driver.current_url == url_githab