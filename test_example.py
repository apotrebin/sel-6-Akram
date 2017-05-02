import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    # wd = webdriver.Ie(executable_path="C:/Tools/IEDriverServer.exe")
    # wd = webdriver.Firefox(firefox_profile = options, capabilities={"marionette": True}, executable_path="C:/Tools/geckodriver.exe", firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
    # wd = webdriver.Firefox(executable_path="C:/Tools/geckodriver.exe", firefox_binary="C:/Program Files/Nightly/firefox.exe")

    # ---------------- Chorme --------------------- #
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})

    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")


    wd = webdriver.Chrome(executable_path="C:/Tools/chromedriver.exe", chrome_options=options)
    # print(wd.capabilities)
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)

    return wd


def test_stickers_equal_products(driver):
    driver.get('http://localhost:8082/litecart/en/')
    all_products = driver.find_elements_by_css_selector('.col-xs-halfs.col-sm-thirds.col-md-fourths.col-lg-fifths')
    all_stickers = driver.find_elements_by_css_selector('.sticker')
    assert len(all_products) == len(all_stickers)












