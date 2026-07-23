import tkinter as tk
import requests
from datetime import datetime, timedelta
import random

# url = "https://labs.bible.org/api/?passage=John+3:16"
url = "https://bible-api.com/John 3:16"

book = ["Genesis ", "Exodus ", 'Leviticus ', 'Numbers ', 'Deuteronomy ',
        'Joshua ', 'Judges ', '1 Samuel ', '2 Samuel ', '1 Kings ',
        '2 Kings ', '1 Chronicles ', 'Nehemiah ', 'Isaiah ', 'Jeremiah ',
        'Ezekiel ', 'Daniel ', 'Hosea ', 'Zachariah ', 'Matthew ',
        'Mark ', 'Luke ', 'John ', 'Acts ', 'Romans ', '1 Corinthians ',
        '2 Corinthians ', 'Hebrews ', 'Revelation ']


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
    if hour == '01':
        return 'LUK '
    elif hour == '02':
        return 'Ezra '
    elif hour == '03':
        return 'LAM '
    elif hour == '04':
        return four[random.randint(0, 3)]
    elif hour == '05':
        return five[random.randint(0, 1)]
    elif hour == '06':
        return six[random.randint(0, 1)]
    elif hour == '07':
        return seven[random.randint(0, 2)]
    elif hour == '08':
        return eight[random.randint(0, 1)]
    elif hour == '09':
        return 'LUK '
    elif hour == '10':
        return 'PSA '
    elif hour == '11':
        return 'PSA '
    elif hour == '12':
        return 'LUK '


def minute_change(minute):  # minute is the next minute already prepared
    time_now = datetime.now().minute
    if str(time_now) == minute:
        datetime.now().minute
        return True
    else:
        time_now = datetime.now().minute
        return False


def bible_clock(first=False):
    now = get_time()
    now = now + timedelta(minutes=1)
    time = now.strftime('%I:%M')
    hour = now.strftime("%I")
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
    if first:
        first = False
    else:
        check = False
        while not check:  # While check is false
            check = minute_change(minute)
    label_var.set(verse)

    root.after(100, bible_clock)


try:
    root = tk.Tk()

    label_var = tk.StringVar()
    label_var.set("hello world")
    label = tk.Label(root, textvariable=label_var)
    label.pack()
    bible_clock(True)
    root.mainloop()
except Exception as e:
    print(e)
