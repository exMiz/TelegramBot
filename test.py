import random
import os
import time
import requests
import re
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import json

# weigth = 40
# heigth = 15

# matrix = [['|' for i in range(weigth)] for j in range(heigth)]


# def show():
#     for i in range(heigth):
#         for j in range(weigth):
#             print(matrix[i][j], end=' ')
#         print()


# def play():
#     # while 1:
#     text = []
#     for c in open('song').read():
#         for j in range(weigth):
#             max = random.randint(1, heigth)
#             for x in range(heigth):
#                 if x <= max:
#                     matrix[x][j] = ' '
#                 else:
#                     matrix[x][j] = '|'
#         os.system('clear')
#         show()
#         for i in text:
#             print(i, end="")
#         print()
#         text.append(c)
#         time.sleep(0.1)


# play()

# min_value = 1
# max_value = 10
# array = [i for i in range(min_value, max_value + 1)]

# while True:
#     if len(array) == 1:
#         print("I win! " + str(array[0]))
#         break

#     random_value = random.choice(array)
#     answer = input("This is your value " + str(random_value) + " ? ")
#     if answer == "yes":
#         print("I win! " + str(random_value))
#         break
#     else:
#         array.remove(random_value)


# length = 25
# sumbol = ">"
# array = [" "] * length
# array.append(sumbol)
# move = 1
# i = 5


# def change_sumbol(new_sumbol, sumbol):
#     array[array.index(sumbol)] = new_sumbol
#     sumbol = new_sumbol
#     return sumbol


# def show(array):
#     for x in array:
#         print(x, end="")
#     print()
#     time.sleep(0.05)


# while True:
#     if i == 0:
#         move = 1
#         sumbol = change_sumbol(">", sumbol)
#     elif i == len(array) - 1:
#         move = -1
#         sumbol = change_sumbol("<", sumbol)
#     array[array.index(sumbol)] = " "
#     array[i] = sumbol
#     i += move
#     show(array)
#     os.system('clear')
#     break

def shedule(group_id):
    text = ''
    url = "http://schedule.sumdu.edu.ua/index/htmlschedule"
    post_data = {'data[DATE_BEG]': time.strftime("%d.%m.%Y"),
                 'data[DATE_END]': time.strftime("%d.%m.%Y"),
                 'data[KOD_GROUP]': group_id,
                 'data[ID_FIO]': 0,
                 'data[ID_AUD]': 0,
                 'data[PUB_DATE]': 'false',
                 'data[PARAM]': 0}
    response = requests.post(url, post_data)
    response.encoding = "windows-1251"

    para_key = {1: "08:15-09:35",
                2: "09:50-11:10",
                3: "11:25-12:45",
                4: "13:25-14:45",
                5: "15:00-16:20",
                6: "16:35-17:55",
                7: "18:00-19:20",
                8: "19:25-20:45",
                }
    soup = BeautifulSoup(response.text, 'html.parser')
    for index, x in enumerate(soup.find_all('td'), start=1):
        info = ''
        for y in x:
            if re.search("^[^\s+]", y.get_text()):
                info += y.get_text() + "\n"
        if info:
            text += "Пара " + para_key[index] + "\n" + info + "\n"
    return text
