from selenium import webdriver
import unittest

class Nova_Poshta (unittest.TestCase):
    def testing_received_tracking_number(self):
        # open Chrome
        chrome = webdriver.Chrome(executable_path="C:\\Users\\Mary\\Desktop\\chromedriver.exe")
        # open https://novaposhta.ua/ru
        chrome.get("https://novaposhta.ua/ru")
        # write_xpath
        cargo_number_xpath = "//*[@id='cargo_number']"
        chrome.find_element_by_xpath(cargo_number_xpath).send_keys("20400136373026\n")
        status_xpath = "//div[@class='status']"
        status = chrome.find_element_by_xpath(status_xpath).text
        self.assertTrue(status.__contains__('Получено'), 'Error. Delivery is not received')
        chrome.quit()

    def testing_not_existing_tracking_number(self):
        chrome = webdriver.Chrome(executable_path="C:\\Users\\Mary\\Desktop\\chromedriver.exe")
        # open https://novaposhta.ua/ru
        chrome.get("https://novaposhta.ua/ru")
        # write_xpath
        cargo_number_xpath = "//*[@id='cargo_number']"
        chrome.find_element_by_xpath(cargo_number_xpath).send_keys("204001363730267\n")
        status_xpath = '//div[@class="not-found"]/span'
        status = chrome.find_element_by_xpath(status_xpath).text
        self.assertEqual('Експрес-накладної з таким номером не знайдено.', status, "Error. {}".format(status))
        chrome.quit()

    def testing_invalid_trcking_number_format(self):
        chrome = webdriver.Chrome(executable_path="C:\\Users\\Mary\\Desktop\\chromedriver.exe")
        chrome.get("https://novaposhta.ua/ru")
        cargo_number_xpath = "//*[@id='cargo_number']"
        chrome.find_element_by_xpath(cargo_number_xpath).send_keys("333\n")
        status_xpath = '//div[@class="not-found"]/span'
        status = chrome.find_element_by_xpath(status_xpath).text
        self.assertEqual('Некоректний формат номера накладної. Номер повинен починатися з цифр 5, 2 або 1 -переконайтеся в правильності введення номера', status, 'Error. {}'.format(status))
        chrome.quit()

    def testing_empty_tracking_number(self):
        chrome = webdriver.Chrome(executable_path="C:\\Users\\Mary\\Desktop\\chromedriver.exe")
        # open https://novaposhta.ua/ru
        chrome.get("https://novaposhta.ua/ru")
        # write_xpath
        cargo_number_xpath = "//*[@id='cargo_number']"
        chrome.find_element_by_xpath(cargo_number_xpath).send_keys("\n")
        status_xpath = '//input[@id="cargo_number_inp"]'
        placeholder_value = chrome.find_element_by_xpath(status_xpath).get_attribute('placeholder')
        self.assertTrue(placeholder_value == "Введите номер для отслеживания", 'Error.  {}'.format(placeholder_value))
        chrome.quit()

if __name__ == '__main__':
    unittest.main()
