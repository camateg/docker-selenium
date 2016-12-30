from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def wait_elem_css(driver, elem):
  WebDriverWait(driver,10).until(lambda s: s.find_element(By.CSS_SELECTOR, elem))
