from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/trial-of-the-stones")

# Locators of the elements

input1_css_locator = "input[id='r1Input']"
button1_xpath_locator = "//button[@id='r1Btn']"
password2_xpath_locator = "//div[@id='passwordBanner']/h4"
input2_css_locator = "input[id='r2Input']"
button2_xpath_locator = "//button[@id='r2Butn']"
input3_css_locator = "input[id='r3Input']"
button3_xpath_locator = "//button[@id='r3Butn']"
merch1_xpath_locator = "//b[text()='Jessica']/../../p]"
merch2_xpath_locator = "//b[text()='Bernard']/../../p]"
button_check_xpath_locator = "//button[@id='checkButn']"
complete_banner_xpath_locator = "//div[@id='trialCompleteBanner']/h4"

# Assign elements

input1_element = browser.find_element_by_css_selector(input1_css_locator)
button1_click = browser.find_element_by_xpath(button1_xpath_locator)
password_element = browser.find_element_by_xpath(password2_xpath_locator)
input2_element = browser.find_element_by_css_selector(input2_css_locator)
button2_click = browser.find_element_by_xpath(button2_xpath_locator)
input3_element = browser.find_element_by_css_selector(input3_css_locator)
button3_click = browser.find_element_by_xpath(button3_xpath_locator)
button_check_click = browser.find_element_by_xpath(button_check_xpath_locator)
complete_sign = browser.find_element_by_xpath(complete_banner_xpath_locator)

# Manipulate elements

input1_element.send_keys("rock")
button1_click.click()
input2_element.send_keys(str(password_element.text))
button2_click.click()
if merch1_xpath_locator > merch2_xpath_locator:
    jess = "Jessica"
    input3_element.send_keys(jess)
else:
    bern = "Bernard"
    input3_element.send_keys(bern)
button3_click.click()
button_check_click.click()

# Result visualisation

print(str(complete_sign.text))
