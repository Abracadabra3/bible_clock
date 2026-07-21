import tkinter as tk
import requests

# url = "https://labs.bible.org/api/?passage=John+3:16"
url = "https://bible-api.com/john 3:16"


def bible_clock():
    # url = "https://labs.bible.org/api/?passage="
    # url += ("John+")
    # url += ("3:16")
    response = requests.get(url)
    response = response.json()
    verse = response['text']
    address = response["reference"]
    verse += address
    print(verse)
    label_var.set(verse)
    root.after(1000, bible_clock)


root = tk.Tk()

label_var = tk.StringVar()
label_var.set("hello world")
label = tk.Label(root, textvariable=label_var)
label.pack()

bible_clock()
root.mainloop()
