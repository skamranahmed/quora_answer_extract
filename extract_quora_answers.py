from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains
import csv



profile_url = str(input("Enter the profile url of the person:\n"))



driver = webdriver.Chrome('/Users/syedkamrnahmed/Desktop/Scrape/chromedriver')

driver.get(profile_url)

bottom_of_the_page_xpath = '//div[@class="spinner_display_area hidden"]'   #determing the end part of the profile webpage

print("\n")

person_name_xpath = '//span[@class="user"]'

person_name = driver.find_element_by_xpath(person_name_xpath)

person_name_text = person_name.text + ".csv"

csv_file = open(person_name_text,'w',encoding='utf-8')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Question','Link'])



while True:

    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()   #triggering the arrow down key to move down in the page

    try:
        bottom_of_the_page = driver.find_element_by_xpath(bottom_of_the_page_xpath)

        question_xpath = '//span[@class="ui_content_title ui_content_title--default ui_content_title--medium"]/span[@class="ui_qtext_rendered_qtext"]'

        questions = driver.find_elements_by_xpath(question_xpath)

        question_links = driver.find_elements_by_class_name('question_link')

        list_of_links = [ ]

        for question_link in question_links:

            link = question_link.get_attribute('href')

            list_of_links.append(link)


            i = 0

        for question in questions:

            question_text = question.text

            print(question_text)

            print(list_of_links[i] + '\n')

            csv_writer.writerow([question_text, list_of_links[i]])

            i = i + 1

        break

    except:

        continue














