#!/usr/bin/python

import unittest
#import tinys3
import uuid
import re
#import s3_keys
import local_help

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

UUID = str(uuid.uuid1())

#S3_ACCESS_KEY = s3_keys.access_key()
#S3_SECRET_KEY = s3_keys.secret_key()

class RobotImageTest(unittest.TestCase):
  def setUp(self):
    self.d = webdriver.Chrome()

#  def send_ss(self, name):
#    d = self.d
#    cfn = name + '.png'
#    lfn = UUID + '_' + cfn
#    rfn = UUID + '/' + cfn
#    d.get_screenshot_as_file('/tmp/' + lfn)
#    f = open('/tmp/' + lfn, 'rb')
#    s3 = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,tls=True)
#    s3.upload(rfn, f, 'net.kb3tix.selenium-test')

  def test_get_google(self):
    d = self.d
    self.get_google()
#    self.send_ss('google')
    self.assertEqual('Google', d.title)

    pass

  def test_get_google_img(self):
    d = self.d
    self.get_google_img()
#    self.send_ss('images')
    self.assertEqual('Google Images', d.title)

    pass

  def get_google(self):
    d = self.d
    d.get('http://www.google.com')

  def get_google_img(self):
    d = self.d
    self.get_google()
    WebDriverWait(d, 10).until(lambda s: s.find_element(By.LINK_TEXT, 'Images').is_displayed())
    img_link = d.find_element(By.LINK_TEXT, 'Images')
    img_link.click()

  def test_get_google_img_result(self):
    d = self.d
    self.get_google()
    self.get_google_img()
    # WebDriverWait(d, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, '#lst-ib'))
    local_help.wait_elem_css(d, '#lst-ib') 
    query = d.find_element(By.CSS_SELECTOR, '#lst-ib')
    query.send_keys('robot', Keys.ENTER)
    local_help.wait_elem_css(d, '#rg_s > div')
    pix_results = d.find_elements(By.CSS_SELECTOR, '#rg_s > div')   
    self.assertTrue(len(pix_results) > 0)
#    self.send_ss('robots')

    pass

  def tearDownModule(self):
      d = self.d
      d.quit()

if __name__ == '__main__':
   unittest.main()
