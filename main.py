from tkinter import *
import itertools
import enchant

d_EN = enchant.Dict("en_US")
d_DK = enchant.Dict("da")
d_FR = enchant.Dict("fr_FR")
d_DE = enchant.Dict("de_DE")
d_ES = enchant.Dict("es_ES")

root = Tk()
root.title("Word Game Solver")
root.geometry("400x400")

Welcome_Label = Label(root, text="Hello! This app is a word solver.")
Welcome_Label.grid(row=0, column=0, columnspan=2)


def show():
    available_letters = letterEntry.get()
    available_letters = available_letters.lower()
    language = clicked_language.get()
    min_length = int(clicked.get())
    max_length = len(available_letters)
    if language == "English (US)":
        d = d_EN
    elif language == "Danish":
        d = d_DK
    elif language == "French":
        d = d_FR
    elif language == "German":
        d = d_DE
    elif language == "Spanish":
        d = d_ES

    all_perm_list = []
    for i in range(min_length, max_length + 1):
        temp_list = list(itertools.permutations(available_letters, i))
        all_perm_list.append(temp_list)

    perm_list = []
    for lst in all_perm_list:
        for perm in lst:
            word = "".join(perm)
            perm_list.append(word)

    available_words = []
    for word in perm_list:
        if d.check(word) == True:
            if word not in available_words:
                available_words.append(word)

    # for word in available_words:
    #    print(word)

    my_label = Label(root,
                     text="Selected language is '{}'.\nThe available letters are '{}'.\nMinimum length of words is '{}'.\nThere is a total of {} word(s) possible".format(
                         language, available_letters, min_length, str(len(available_words))))  # language, available_letters, min_length
    my_label.grid(row=5, column=0, columnspan=2)
    top = Toplevel()
    top.title("Results")
    for i in available_words:
        result_label = Label(top, text=i)
        result_label.pack()


options_min_word_len = [
    "2",
    "3",
    "4",
    "5",
    "6"
]

language_options = [
    'English (US)',
    'Danish',
    'French',
    'German',
    'Spanish'
]

clicked_language = StringVar()
clicked_language.set(language_options[0])

clicked = StringVar()
clicked.set(options_min_word_len[1])

language_option_label = Label(root, text="Select a language:", anchor=W)
language_option_label.grid(row=1, column=0, padx=10, pady=3, sticky=W + E)
language_option = OptionMenu(root, clicked_language, *language_options)
language_option.grid(row=1, column=1)

letterEntry_label = Label(root, text="Type the available letters in the box:", anchor=W)
letterEntry_label.grid(row=2, column=0, padx=10, pady=3, sticky=W + E)
letterEntry = Entry(root, width=10, bg="blue", fg="white", borderwidth=5)
letterEntry.grid(row=2, column=1, sticky=W + E)

minimumButton_label = Label(root, text="Minimum length of possible words:", anchor=W)
minimumButton_label.grid(row=3, column=0, padx=10, pady=3, sticky=W + E)
minimumButton = OptionMenu(root, clicked, *options_min_word_len)
minimumButton.grid(row=3, column=1)

showButton_label = Label(root, text="Click to show your selection:", anchor=W)
showButton_label.grid(row=4, column=0, padx=10, pady=3, sticky=W + E)
showButton = Button(root, text="Show Selection", command=show)
showButton.grid(row=4, column=1)

root.mainloop()
