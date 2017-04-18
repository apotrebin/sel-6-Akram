import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    wait = WebDriverWait(driver, 10)  # seconds
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath(".//*[@id='box-login']/form/div[2]/button").click()
    driver.find_element_by_xpath(".//*[@id='shortcuts']/a[5]/i").click()
    wait.until(EC.title_is("My Store"))


