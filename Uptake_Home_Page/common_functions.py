import time
browser = 'Chrome'

class Header():
    #tests & verifies the header elements along with the text
    def test1_home_page_header(self):
        menu_items = self.driver.find_elements_by_css_selector('.menu__item')
        actual_menu_items = len(menu_items)
        self.assertEqual(self.expected_menu_items, actual_menu_items)
        print'Successfully verified expected & actual value match : ',actual_menu_items
        items = 0
        for headers in menu_items:
            actual_menu_list_items = self.driver.find_elements_by_css_selector('.menu__item')[items].text
            self.assertIn(actual_menu_list_items, self.expected_menu_list_items)
            print 'Successfully verified expected & actual value match :', actual_menu_list_items
            items = items+1
            
    #tests & verifies 'Newsroom' page navigation - url validation   
    def test2_home_page_header_element(self):
        uptake_newsroom = self.driver.find_elements_by_css_selector('.menu__item')[3]
        actual_uptake_newsroom = uptake_newsroom.text
        self.assertEqual(self.expected_uptake_newsroom, actual_uptake_newsroom)
        print'Successfully verified expected & actual value match : ',actual_uptake_newsroom    
        uptake_newsroom.click()
        time.sleep(2)
        
        actual_newsroom_url = self.driver.current_url
        self.assertEqual(self.expected_newsroom_url, actual_newsroom_url)
        print'Successfully verified expected & actual value match : ',actual_newsroom_url
        self.home_logo.click()
        time.sleep(2)
        
class Footer():        
    #tests & verifies the footer texts
    def test1_home_page_footer_texts(self):
        actual_footer_text_h5 = self.driver.find_element_by_css_selector('.footer-text').text
        self.assertEqual(self.expected_footer_text_h5, actual_footer_text_h5)
        print'Successfully verified expected & actual value match : ',actual_footer_text_h5
        
        actual_footer_contact_link = self.driver.find_element_by_css_selector('.contact-link').text
        self.assertEqual(self.expected_footer_contact_link, actual_footer_contact_link)
        print'Successfully verified expected & actual value match : ',actual_footer_contact_link
        
        actual_footer_copyright_text = self.driver.find_element_by_css_selector('.copyright-text').text
        self.assertEqual(self.expected_copyright_text, actual_footer_copyright_text)
        print'Successfully verified expected & actual value match : ',actual_footer_copyright_text
        
    #tests & verifies the sources of social share links
    def test2_home_page_footer_social_links(self):
        actual_twitter_instagram_linkedin_img_srcs = [x.get_attribute('src') for x in self.driver.find_elements_by_css_selector
                                                      ('.social-links .social-link img')]
        self.assertEqual(self.expected_twitter_instagram_linkedin_img_srcs, actual_twitter_instagram_linkedin_img_srcs)
        print'Successfully verified expected & actual value match : ',actual_twitter_instagram_linkedin_img_srcs
        
    #tests & verifies the privacy_policy link along with navigation - url validation
    def test3_home_page_footer_privacy_policy(self):
        privacy_policy_link = self.driver.find_elements_by_css_selector('.underline-link')[0]
        actual_privacy_policy_link = privacy_policy_link.text
        self.assertEqual(self.expected_privacy_policy_link, actual_privacy_policy_link)
        print'Successfully verified expected & actual value match : ',actual_privacy_policy_link
        privacy_policy_link.click()
        time.sleep(2)
        
        actual_privacy_policy_url = self.driver.current_url
        self.assertEqual(self.expected_privacy_policy_url, actual_privacy_policy_url)
        print'Successfully verified expected & actual value match : ',actual_privacy_policy_url
        self.home_logo.click()
        time.sleep(2)
   
    #tests & verifies the contact link along with navigation - title validation
    def test4_home_page_footer_contact(self):     
        contact_link = self.driver.find_element_by_css_selector('.real-button')
        actual_contact_link = contact_link.text
        self.assertEqual(self.expected_contact_link, actual_contact_link)
        print'Successfully verified expected & actual value match : ',actual_contact_link
        contact_link.click()
        time.sleep(2)
        
        actual_contact_link_title = self.driver.find_element_by_css_selector('.contact__form__title').text
        self.assertEqual(self.expected_contact_link_title, actual_contact_link_title)
        print'Successfully verified expected & actual value match : ',actual_contact_link_title
    
    #tests & verifies the careers link along with navigation - url validation   
    def test5_home_page_footer_careers(self):
        careers_link = self.driver.find_elements_by_css_selector('.underline-link')[1]
        actual_careers_link = careers_link.text
        self.assertEqual(self.expected_careers_link, actual_careers_link)
        print'Successfully verified expected & actual value match : ',actual_careers_link
        careers_link.click()
        time.sleep(2)
        
        actual_careers_url = self.driver.current_url
        self.assertEqual(self.expected_careers_url, actual_careers_url)
        print'Successfully verified expected & actual value match : ',actual_careers_url
        
        print '###Successfully verified the Header & Footer section on the Home Page###'
        
        
        
        
        
        
        