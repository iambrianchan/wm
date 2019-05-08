import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Test the Signup page
class TestSignupPage(unittest.TestCase):
    
    # Create the webdriver, declare common page variables 
    def __init__(self, *args, **kwargs):
        super(TestSignupPage, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver') # Set the path of the chrome driver on the machine
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None
        self.checkbox = None
        self.register_button = None

    # Get to the signup page with webdriver, set values to the common page variables
    def setUp(self):
        self.driver.get('https://dev.workmarket.com/register/campaign/10081C503B209A0C8E7F05FDCC1AA98D4C904DEEF5F73265CAE38C744E7EAD3E')
        joinAsIndividual = self.driver.find_elements_by_tag_name("button")
        joinAsIndividual[1].click()
        time.sleep(2)
        self.first_name = self.driver.find_elements_by_css_selector("#firstname")[0]
        self.last_name = self.driver.find_elements_by_css_selector("#lastname")[0]
        self.email = self.driver.find_elements_by_css_selector("#email")[0]
        self.password = self.driver.find_elements_by_css_selector("#password")[0]
        self.checkbox = self.driver.find_elements_by_tag_name("input")[4]
        self.register_button = self.driver.find_elements_by_tag_name("button")[2]

    # Quit the webdriver
    def tearDown(self):
        self.driver.quit()        

    # test that an empty name is invalid and produces the expected error message
    def test_invalid_firstname(self):
        self.first_name.send_keys("a")
        time.sleep(3)
        self.first_name.send_keys(Keys.BACKSPACE)
        self.register_button.click()

        error_msg = ""
        divs = self.driver.find_elements_by_tag_name("div")
        for i in range(len(divs)):
            if divs[i].text == "Please enter a valid first name":
                error_msg = divs[i].text
                break

        self.assertEqual(error_msg, "Please enter a valid first name")

    # Test that a valid firstname does not produce the expected error message
    def test_valid_firstname(self):
        self.first_name.send_keys("a")
        time.sleep(3)
        self.register_button.click()

        error_msg = None
        divs = self.driver.find_elements_by_tag_name("div")
        for i in range(len(divs)):
            if divs[i].text == "Please enter a valid first name":
                error_msg = divs[i].text
                break

        self.assertEqual(error_msg, None)

    # Test that an empty last name is invalid and produces the expected error message
    def test_invalid_lastname(self):
        self.last_name.send_keys("b")
        time.sleep(3)
        self.last_name.send_keys(Keys.BACKSPACE)
        self.register_button.click()

        error_msg = ""
        divs = self.driver.find_elements_by_tag_name("div")
        for i in range(len(divs)):
            if divs[i].text == "Please enter a valid last name":
                error_msg = divs[i].text
                break

        self.assertEqual(error_msg, "Please enter a valid last name")

    # Test that a valid last name does not produce the expected error message
    def test_valid_lastname(self):
        self.last_name.send_keys("b")
        time.sleep(3)
        self.register_button.click()

        error_msg = None
        divs = self.driver.find_elements_by_tag_name("div")
        for i in range(len(divs)):
            if divs[i].text == "Please enter a valid last name":
                error_msg = divs[i].text
                break

        self.assertEqual(error_msg, None)

    # Test that an invalid email address produces the expected error message
    def test_invalid_email(self):
        self.email.send_keys("c")
        self.register_button.click()
        time.sleep(3)

        error_msg = None
        divs = self.driver.find_elements_by_tag_name("div")
        for i in range(len(divs)):
            if divs[i].text == "Please enter a valid email":
                error_msg = divs[i].text
                break

        time.sleep(3)
        self.assertEqual(error_msg, "Please enter a valid email")

    # Test that a valid email address does not produce the expected error message
    def test_valid_email(self):
        self.email.send_keys("c" + str(int(time.time())) + "@test.com")
        self.register_button.click()
        time.sleep(3)

        error_msg = None
        divs = self.driver.find_elements_by_tag_name("div")
        for i in range(len(divs)):
            if divs[i].text == "Please enter a valid email":
                error_msg = divs[i].text
                break

        self.assertEqual(error_msg, None)

    # Test that an empty email address produces the expected error message
    def test_empty_email(self):
        self.email.send_keys("c")
        self.register_button.click()
        self.email.send_keys(Keys.BACKSPACE)
        self.register_button.click()
        time.sleep(3)

        error_msg = None
        divs = self.driver.find_elements_by_tag_name("div")
        for i in range(len(divs)):
            if divs[i].text == "Please enter a valid email":
                error_msg = divs[i].text
                break

        self.assertEqual(error_msg, "Please enter a valid email")

    # Test that an empty password produces the expected error message
    def test_empty_password(self):
        self.password.send_keys("c")
        self.register_button.click()
        self.password.send_keys(Keys.BACKSPACE)
        self.register_button.click()
        time.sleep(3)

        error_msg = None
        divs = self.driver.find_elements_by_tag_name("div")
        for i in range(len(divs)):
            if divs[i].text == "Please enter a valid password":
                error_msg = divs[i].text
                break

        self.assertEqual(error_msg, "Please enter a valid password")

    # Test that the first name is required by checking the disabled attribute on the register button
    def test_firstname_required(self):
        self.last_name.send_keys("b")
        self.email.send_keys("c" + str(int(time.time())) + "@test.com")
        self.password.send_keys("Password1")
        self.checkbox.click()

        register_button_disabled = self.register_button.get_attribute("disabled")
        self.assertEqual(register_button_disabled, "true")

    # Test that the last name is required by checking the disabled attribute on the register button
    def test_lastname_required(self):
        self.first_name.send_keys("a")
        self.email.send_keys("c" + str(int(time.time())) + "@test.com")
        self.password.send_keys("Password1")
        self.checkbox.click()

        register_button_disabled = self.register_button.get_attribute("disabled")
        self.assertEqual(register_button_disabled, "true")

    # Test that the email is required by checking the disabled attribute on the register button
    def test_email_required(self):
        self.first_name.send_keys("a")
        self.last_name.send_keys("b")
        self.password.send_keys("Password1")
        self.checkbox.click()

        register_button_disabled = self.register_button.get_attribute("disabled")
        self.assertEqual(register_button_disabled, "true")

    # Test that the password is required by checking the disabled attribute on the register button
    def test_password_required(self):
        self.first_name.send_keys("a")
        self.last_name.send_keys("b")
        self.email.send_keys("c" + str(int(time.time())) + "@test.com")
        self.checkbox.click()

        register_button_disabled = self.register_button.get_attribute("disabled")
        self.assertEqual(register_button_disabled, "true")

    # Test that the checkbox is required by checking the disabled attribute on the register button
    def test_checkbox_required(self):
        self.first_name.send_keys("a")
        self.last_name.send_keys("b")
        self.email.send_keys("c" + str(int(time.time())) + "@test.com")
        self.password.send_keys("Password1")

        register_button_disabled = self.register_button.get_attribute("disabled")
        self.assertEqual(register_button_disabled, "true") 

    # Test that all 5 fields allow submission
    def test_submit(self):
        self.first_name.send_keys("a")
        self.last_name.send_keys("b")
        self.email.send_keys("c" + str(int(time.time())) + "@test.com")
        self.password.send_keys("WorkMarket861")
        self.checkbox.click()

        register_button_disabled = self.register_button.get_attribute("disabled")
        self.assertEqual(register_button_disabled, None)

        self.register_button.click()
        time.sleep(4)

        h3_header = ""
        h3_headers = self.driver.find_elements_by_tag_name("h3")
        for i in range(len(h3_headers)):
            if h3_headers[i].text == "Next Steps":
                h3_header = h3_headers[i].text
        self.assertEqual(h3_header, "Next Steps")

# Test the search page
class TestSearchPage(unittest.TestCase):
    
    # Create the webdriver
    def __init__(self, *args, **kwargs):
        super(TestSearchPage, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    
    # Navigate to the search page, search "test"  
    def setUp(self):
        #login to workmarket
        self.driver.get('http://dev.workmarket.com/login')
        time.sleep(4)
        user = "qa+candidatetest@workmarket.com"
        passw = "candidate123"
        login_button = self.driver.find_elements_by_tag_name("button")[0]
        userField = self.driver.find_elements_by_css_selector("#login-email")[0]
        userField.send_keys(user)
        passField = self.driver.find_elements_by_css_selector("#login-password")[0]
        passField.send_keys(passw)
        login_button.click()
        time.sleep(4)

        #get to search page
        a_tags = self.driver.find_elements_by_tag_name("a")
        find_talent = None
        for i in range(len(a_tags)):
            if a_tags[i].text == "Find Talent":
                find_talent = a_tags[i]
                break
        time.sleep(4)
        find_talent.click()

        #search "test"
        search_bar = self.driver.find_elements_by_css_selector("#input-text")[0]
        search_bar.send_keys("test")
        search_bar.send_keys(Keys.ENTER)
        time.sleep(4)

    # Quit the webdriver
    def tearDown(self):
        self.driver.quit()

    # Test the validity of the results
    def test_filtered_results(self):
        # Get all profile cards
        profile_cards = self.driver.find_elements_by_css_selector(".profile-card")

        # Loop and determine if "test" in profile card text
        for i in range(len(profile_cards)):
            inner_html = profile_cards[i].text.lower()
            self.assertIn("test", inner_html)

if __name__ == '__main__':
    unittest.main()