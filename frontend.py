import tkinter as tk
from tkinter import *
import json
from difflib import get_close_matches
import  tkinter.messagebox
data = json.load(open('original.json'))


def search_engine():
    word = searchbox.get()
    list.delete('1.0', END)
    x=0
    y = 1
    if word in data:

        results = data[word]

        for result in results:
            list.insert(END, str(y) + ". " + result + "\n")
            x+=1
            y+=1
    elif len(get_close_matches(word, data.keys())) > 0:
        real_list = get_close_matches(word, data.keys(), cutoff=0.8)
        real_word = real_list[0]
        answer = tkinter.messagebox.askquestion("Word Suggestion", "Is your word " + real_word + "?")
        if answer == 'yes':
            results = data[real_word]
            list.insert(END, "Result for " + real_word + " instead of " + word + ".\n")
            for result in results:
                list.insert(END, str(y) + ". " + result + "\n")
                x += 1
                y += 1
        else:
            list.insert(END, "No word found")

    else:
        list.insert(END, "No word found")





def display_command(word):
    list.delete(0, END)





home = tk.Tk()
home.title('Joecode Dictionary')
home_canvas = Canvas(home, width =1000, height=500,  bg = "#C1B1D6")
home_canvas.pack()
"""
home_canvas2 = Canvas(home_canvas,bg = "#D3C9A7")
home_canvas2.place( relwidth=0.2, relheight = 0.8,  relx=0.78, rely= 0.1)
"""
#title label
heading = Label(home_canvas, text="TJ Dictionary", bg = "#C1B1D6", fg = "#1A80AC")
heading.config(font=('forte 20'))
heading.place(relx=0.425, rely = 0.02)

homeframe= Frame(home_canvas, bg='#D3C9A7', bd =5)
homeframe.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.1)
search = Label(homeframe, text = "Enter your word here", bg='#D3C9A7', fg="black")
search.config(font=('jokerman 12'))
search.place(relx=0.15, rely=0.14)
word_text = StringVar()
searchbox = Entry(homeframe, bg = "white", fg="black", textvariable=word_text)
searchbox.config(width=42)
searchbox.place(relx=0.36, rely=0.15)




searchbut = Button(homeframe, text="search", relief = FLAT, command=search_engine)
searchbut.place(relx=0.5, rely= 0.24, anchor=CENTER)



#result_label = Label(homeframe, bg = "#C1B1D6")
#result_label.place(relwidth=0.85, relheight= 0.6, relx=0.1, rely=0.3)
#lower_frame= Frame(result_label, bg ='white')
#lower_frame.place(relwidth=0.95, relheight= 0.9, relx=0.025, rely=0.05)

list = Text(homeframe, bg="white")
list.place(relwidth=0.9, relheight= 0.6, relx=0.06, rely=0.3)

footer= Label(home_canvas, text="Software Developed by Joshua Tobi Ajagbe", fg="red", bg = "#C1B1D6")
footer.config(font=('perpetua 15'))
footer.place(relx=0.35, rely=0.93)

home.mainloop()
