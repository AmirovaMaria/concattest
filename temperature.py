from selenium import webdriver
import datetime


date_str = input("Enter the date\n")
date = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()

if date < datetime.date.today():
    raise Exception("Error : The date was selected in the past")

if date > datetime.date.today() + datetime.timedelta(10):
    raise Exception("Error : the date was selected in the future, weathercast can not be done further than for 10 days")

driver = webdriver.Chrome(executable_path="C:\\Users\\Mary\\Desktop\\chromedriver.exe")
# sinoptic has date format like: YYYY-MM-DD
driver.get("https://sinoptik.ua/погода-одесса/" + str(date))

xpath_min = '//p[@data-link="//sinoptik.ua/погода-одесса/{}"]/following-sibling::div[2]/div[1]/span'.format(date)
xpath_max = '//p[@data-link="//sinoptik.ua/погода-одесса/{}"]/following-sibling::div[2]/div[2]/span'.format(date)

min_temp = driver.find_element_by_xpath(xpath_min).text
max_temp = driver.find_element_by_xpath(xpath_max).text

print("Weathercast for {} : \n min temperature = {} \n max temperature = {}".format(date, min_temp, max_temp))

driver.quit()