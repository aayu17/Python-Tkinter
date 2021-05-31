import ctypes  # pip install ctypes
from tkinter import *  # pip install tkinter
from PyDictionary import PyDictionary  # pip install PyDictionary
from PIL import Image, ImageTk  # pip install pillow

dictionary = PyDictionary()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root = Tk()
root.title("Dictionary")
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry(f"{window_width}x{window_height}")
root.config(background="Black")


def click(*args):
    word_entry.delete(0, 'end')  # to delete placeholder text


def search(event=""):
    meaning = dictionary.meaning(word.get())['Noun'][0]
    label_meaning_output.config(text=meaning)

    antonym = dictionary.antonym(word.get())
    label_antonym_output.config(text=antonym)

    synonym = dictionary.synonym(word.get())[4]
    label_synonym_output.config(text=synonym)


label_heading = Label(text="DICTIONARY", font=(
    "Arial 50 underline"), bg="Black", fg="White")
label_heading.place(x=730, y=10)

label_sub_text = Label(text="What word do you want to look up?", font=(
    "Arial 15 bold"), bg="Black", fg="White")
label_sub_text.place(x=700, y=130)

word = StringVar()

word_entry = Entry(root, textvariable=word, width=70, relief=RAISED)
word_entry.insert(5, 'Search for a word')
word_entry.bind("<Button-1>", click)
word_entry.place(x=700, y=170, height=35)

label_meaning = Label(text="Meaning :", font=(
    "Arial 15"), bg="black", fg="White")
label_meaning.place(x=20, y=320)
label_antonym = Label(text="Antonym :", font=(
    "Arial 15 "), bg="black", fg="White")
label_antonym.place(x=20, y=360)

label_synonym = Label(text="Synonym :", font=(
    "Arial 15 "), bg="black", fg="White")
label_synonym.place(x=20, y=400)


image_search = Image.open("search.png")
image_search = image_search.convert("RGB")
image_search = image_search.resize((30, 30), Image.ANTIALIAS)
image_search = ImageTk. PhotoImage(image_search)
label_search_image = Button(image=image_search, command=search)
label_search_image.place(x=1250, y=170)
root.bind("<Return>", search)


label_meaning_output = Label(text="", bg="Black", fg="White", font=("10,bold"))
label_meaning_output.place(x=140, y=320)

label_antonym_output = Label(text="", bg="Black", fg="White", font=("10,bold"))
label_antonym_output.place(x=140, y=360)

label_synonym_output = Label(text="", bg="Black", fg="White", font=("10,bold"))
label_synonym_output.place(x=140, y=400)


root.mainloop()
