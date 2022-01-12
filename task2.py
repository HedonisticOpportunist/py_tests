
import BaseTest

# !!! Do not create your own WebDriver. !!!
#
# You can copy credentials from here:
#  - login@codility.com    password
#  - unknown@codility.com  password


class LoginPageTest(BaseTest.BaseTest):
    def testLoginFormPresent(self):

        # check that page elements are present 
        email_input = self.driver.find_element_by_id("email-input")
        password_input = self.driver.find_element_by_id("password-input")
        login_button = self.driver.find_element_by_id("login-button")

    def testThatLoginWithValidCredentialsWorks(self):

        # set up page elements 
        email_input = self.driver.find_element_by_id("email-input")
        password_input = self.driver.find_element_by_id("password-input")
        login_button = self.driver.find_element_by_id("login-button")

        # login 
        email_input.send_keys("login@codility.com")
        password_input.send_keys("password")
        login_button.send_keys("")

        # verify that welcome message is present
        welcome_message = self.driver.find_element_by_xpath("//div[@class='message success']")
        assert welcome_message.text == "Welcome to Codility"

    def testThatLoginWithInvalidCredentialsDoesNotWork(self):

         # set up page elements 
        email_input = self.driver.find_element_by_id("email-input")
        password_input = self.driver.find_element_by_id("password-input")
        login_button = self.driver.find_element_by_id("login-button")

        # invalid login 
        email_input.send_keys("unknown@codility.com")
        password_input.send_keys("password")
        login_button.send_keys("")

        # verify that error message appears
        error_message = self.driver.find_element_by_css_selector("div.message.error")
        assert error.message.text == "You shall not pass! Arr!"

    def testEmailValidationIsWorking(self):

         # set up page elements 
        email_input = self.driver.find_element_by_id("email-input")
        password_input = self.driver.find_element_by_id("password-input")
        login_button = self.driver.find_element_by_id("login-button")

         # invalid email 
        email_input.send_keys("unknown.codility.com")
        password_input.send_keys("password")
        login_button.send_keys("")

        # verify that validation error is present
        email_validation = self.driver.find_element_by_xpath("//div[@class='validation error']")
        assert email_validation.text == "Enter a valid email"

    def testThatEmptyFieldValidationWorks(self):

         # set up page elements 
        email_input = self.driver.find_element_by_id("email-input")
        password_input = self.driver.find_element_by_id("password-input")
        login_button = self.driver.find_element_by_id("login-button")

         # invalid email 
        email_input.send_keys("")
        login_button.send_keys("")

         # verify that validation error is present
        empyt_field_validation = self.driver.find_element_by_xpath("//div[@class='validation error']")
        assert email_validation.text == "Email is required"


