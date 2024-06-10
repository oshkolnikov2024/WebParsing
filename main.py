
#---------------------------------------request------------------------------------

# import requests
# import pprint
#
# params= {
#     'q' : 'html'
# }
#
# response = requests.get('https://api.github.com/search/repositories', params=params)
# print(response.status_code)
# response_json = response.json()
# pprint.pprint(response_json)
# print(f"кол-во HTML: {response_json ['total_count']}")

# ------------------------------------------------------------------------------------
#
# import requests
# params= {
#     'userIdq' : '1'
# }
# response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
# print(response.status_code)
# print(response.text)


# ------------------------------------------------------------------------------------

# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title" : "тест-post",
#     "foo" : "чего-то",
#     "body" : "тело",
#     "bar" : "еще чего-то",
#     "userId" : 1
# }
#
# response = requests.post(url, data=data)
# print(response.status_code)
# print (f"ответ - {response.json()}")


#-------------------  BeautifulSoup  ------------------------------------------

# from bs4 import BeautifulSoup
# import requests
# from googletrans import Translator
#
# url = "https://randomword.com/"
#
# def get_engl_words():
#     url = "https://randomword.com/"
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, "html.parser")
#         engl_words = soup.find("div", id="random_word").text.strip()
#         word_definition = soup.find("div", id="random_word_definition").text.strip()
#         # print(engl_words)
#         # print(word_definition)
#         return {
#             "engl_words": engl_words,
#             "word_definition": word_definition
#         }
#     except:
#         print("Ошибка")
#
# def word_game():
#     print(" Привет!")
#     while True:
#         word_dict = get_engl_words()
#         word = word_dict.get("engl_words")
#         word_definition = word_dict.get("word_definition")
#
#         translator = Translator()
#
#         result_word = translator.translate(word, dest="ru")
#         # print(f"Загадано слово англ.: {word}")                    #подсказка
#         print(f"Подсказка: {result_word.text}\n")      # подсказка
#
#         result_word_definition = translator.translate(word_definition, dest="ru")
#         print(f"Значение слова: {result_word_definition.text}")
#
#         user = input("Угадай что это за слово?")
#         if user==result_word.text:
#             print("Угадал!!")
#         else:
#             print(f"Не верно, было загадано: {result_word.text}")
#
#         play_again = input("Продолжим? y/n")
#         if play_again != "y":
#             print("До свиданья!")
#             break
# word_game()

#-------------------  Selenium  ------------------------------------------

# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
# browser.save_screenshot("screen.jpg")
# time.sleep(10)
# browser.quit()

#____________________________________________________________________________

# from selenium import webdriver
# from selenium.webdriver import Keys             # для ввода текста как бы с клавиатуры
# from selenium.webdriver.common.by import By     # для поиска элементов на странице через DOM
# import time
#
# browser = webdriver.Chrome()
# browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
#
# assert "Википедия" in browser.title             # проверяем есть ли слово Википедия в открытом сайте
# time.sleep(3)
# search_box = browser.find_element(By.ID, "searchInput")
# search_box.send_keys("Электромобиль")
# time.sleep(3)
# search_box.send_keys(Keys.RETURN)
#
# time.sleep(3)
# a = browser.find_element(By.LINK_TEXT, "Электрокар")
# a.click()
#
# time.sleep(15)

#____________________________________________________________________________

from selenium import webdriver
from selenium.webdriver import Keys             # для ввода текста как бы с клавиатуры
from selenium.webdriver.common.by import By     # для поиска элементов на странице через DOM
import time
import random

def main():
    browser = webdriver.Chrome()
    browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

    query = input("Введите запрос: ")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    a = browser.find_element(By.LINK_TEXT, query)
    a.click()

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Ваш выбор: ")

        if choice == '1':
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(paragraph.text)
                input()

        elif choice == '2':
           hr = browser.find_element(By.TAG_NAME, "a").get_attribute("href")
           browser.get(hr)

        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

main()

