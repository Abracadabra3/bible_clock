import tkinter as tk
import requests
from datetime import datetime
import random

# url = "https://labs.bible.org/api/?passage=John+3:16"
url = "https://bible-api.com/John 3:16"

book = ["Genesis ", "Exodus ", 'Leviticus ', 'Numbers ', 'Deuteronomy ',
        'Joshua ', 'Judges ', '1 Samuel ', '2 Samuel ', '1 Kings ',
        '2 Kings ', '1 Chronicles ', 'Nehemiah ', 'Isaiah ', 'Jeremiah ',
        'Ezekiel ', 'Daniel ', 'Hosea ', 'Zachariah ', 'Matthew ',
        'Mark ', 'Luke ', 'John ', 'Acts ', 'Romans ', '1 Corinthians ',
        '2 Corinthians ', 'Hebrews ', 'Revelation ']


# TODO:
# figure out how to get a real bible verse for each hour


def get_time():
    now = datetime.now()
    return now


def get_verse(time, book):

    url = "https://bible-api.com/"
    print(url)
    url += (str(book))
    print(url)
    url += (str(time))
    print(url)
    # Get the verse and format it
    response = requests.get(url)
    if response.status_code != 200:
        return "ERROR"
    response = response.json()
    verse = response['text']
    address = response["reference"]
    verse += address
    return verse


def get_book(hour):
    four = ['GEN ', 'PSA ', 'ISA ', 'EZK ']
    five = ['PSA ', 'ISA ']
    six = ['1CH ', 'JHN ']
    seven = ['NUM ', 'NEH ', 'ACT ']
    eight = ['1KI ', 'JHN ',]
    if hour == '1':
        return 'LUK '
    elif hour == '2':
        return 'Ezra '
    elif hour == '3':
        return 'LAM '
    elif hour == '4':
        return four[random.randint(0, 3)]
    elif hour == '5':
        return five[random.randint(0, 1)]
    elif hour == '6':
        return six[random.randint(0, 1)]
    elif hour == '7':
        return seven[random.randint(0, 2)]
    elif hour == '8':
        return eight[random.randint(0, 1)]
    elif hour == '9':
        return 'LUK '
    elif hour == '10':
        return 'PSA '
    elif hour == '11':
        return 'PSA '
    elif hour == '12':
        return 'LUK '


def bible_clock():
    now = get_time()
    time = now.strftime("%H:%M")
    hour = now.strftime("%H")
    minute = now.strftime('%M')
    book = "hello, world"
    book = get_book(hour)
    verse = get_verse(time, book)
    if verse == 'ERROR':
        time = hour
        time += minute[0]
        time += ":"
        time += minute[1]
        verse = get_verse(time, book)
    print(time)
    label_var.set(verse)

    root.after(60000, bible_clock)


try:
    root = tk.Tk()

    label_var = tk.StringVar()
    label_var.set("hello world")
    label = tk.Label(root, textvariable=label_var)
    label.pack()
    # time = get_time()
    # now = datetime.now()
    # current_time = now.strftime("%H:%M")
    # hour = now.strftime("%H")
    # current_book = get_book(hour)
    # get_verse(time, current_book)
    bible_clock()
    root.mainloop()
except Exception as e:
    print(e)
