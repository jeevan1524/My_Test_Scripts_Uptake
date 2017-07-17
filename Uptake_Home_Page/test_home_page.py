#-*- coding: utf8 -*-
from selenium import webdriver
from Uptake_Home_Page.common_functions import Header, Footer
import unittest
import time
url = 'https://www.uptake.com'
url_no_www = 'https://uptake.com'

class TestHomepageHeader(Header, Footer, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)
        time.sleep(2)
        cls.home_logo = cls.driver.find_elements_by_css_selector('.mainLogo')[0]
        cls.expected_menu_items = 6
        cls.expected_menu_list_items = 'APPROACH, PRODUCTS, INDUSTRIES, NEWSROOM, BEYOND.UPTAKE, BLOG'
        cls.expected_uptake_newsroom = 'NEWSROOM'
        cls.expected_newsroom_url = url+'/newsroom'
        cls.expected_footer_text_h5 = 'Uptake Named World Economic Forum Technology Pioneer.'
        cls.expected_footer_contact_link = 'LEARN MORE'
        cls.expected_copyright_text = u'© 2017 Uptake Technologies Inc., all rights reserved. "Uptake" and related marks are trademarks of Uptake Technologies Inc.'
        cls.expected_twitter_instagram_linkedin_img_srcs = [u'https://www.uptake.com/img/twitter.svg', u'https://www.uptake.com/img/instagram.svg', u'https://www.uptake.com/img/linkedin.svg']
        cls.expected_privacy_policy_link = 'PRIVACY POLICY'
        cls.expected_privacy_policy_url = url+'/privacy-policy'
        cls.expected_careers_link = 'CAREERS'
        cls.expected_careers_url = url_no_www+'/careers'
        cls.expected_contact_link = 'CONTACT'
        cls.expected_contact_link_title = 'Get in Touch'
         
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        
if __name__ == "__main__":
    unittest.main()