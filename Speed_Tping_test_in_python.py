#CODECLAUSE

#GOLDEN PROJECT-1

from tkinter import *
from tkinter import ttk
import time
import random
import difflib


class MainWindow:

    def __init__(self, root):
        self.text = ["He enjoys reading these articles.",
                     "My brother scared the hell out of me!",
                     "Kamal is writing a letter and listening to music.",
                     "The boy who is dark and tall and wore a red t-shirt, has gone for a long drive as he bought a new car.",
                     "Yesterday was a sunny day, so we thought we would go swimming in the pool but entry was full in Water Park then we decided to visit the zoo.",
                     "The pizza was delivered on time, but the delivery boy left before I reached.",
                     "We get it. Learning the meaning of the many words that make up the English language can seem overwhelming.",
                     "A complex sentence is made up of an independent clause and one or more dependent clauses connected to it.",
                     "While he waited at the train station, Joe realized that the train was late.",
                     "Because Mary and Samantha arrived at the bus station before noon, I did not see them at the station."]
        self.speed = 0
        self.accuracy = 0
        self.time_start = 0
        self.time_end = 0
        root.title("Speed Typing Test")
        root.minsize(500, 500)
        for row in range(5):
            root.grid_rowconfigure(row, weight=1)
        for col in range(3):
            root.grid_columnconfigure(col, weight=1)
        self.label_text = Label(
            root, text="""******Welecome to Typing Speed Test******
    Click the Start button, and NewText Button! To start typing....""", height=5,wraplength=500)
        self.label_text.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.user_text = Text(root)
        self.user_text.grid(column=0, row=1, columnspan=3, sticky="nsew")

        self.btn_start = Button(root, text="Start/Restart", command=self.start)
        self.btn_start.grid(column=0, row=2, columnspan=1, sticky="nsew")
        self.btn_stop = Button(root, text="Finish", command=self.stop)
        self.btn_stop.grid(column=1, row=2, columnspan=1, sticky="nsew")
        self.btn_newtext = Button(root, text="New Text", command=self.new_text)
        self.btn_newtext.grid(column=2, row=2, columnspan=1, sticky="nsew")

        self.label_speed = Label(
            root, text=f"Your typing speed is {self.speed} WPM")
        self.label_speed.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.label_accuracy = Label(
            root, text=f"Your typing accuracy is {self.speed} %")
        self.label_accuracy.grid(row=4, column=0, columnspan=3, sticky="nsew")

    def start(self):
        self.time_start = time.time()

    def stop(self):
        self.time_end = time.time()
        words = self.label_text.cget("text").split(' ')
        self.speed = round(len(words)/((self.time_end - self.time_start)/60))
        self.label_speed.config(
            text=f"Your typing Speed is {self.speed} WPM")
        self.accuracy = round(difflib.SequenceMatcher(None, self.label_text.cget(
            "text"), self.user_text.get("1.0", 'end-1c')).ratio()*100)
        self.label_accuracy.config(
            text=f"Your typing accuracy is {self.accuracy} %")

    def new_text(self):
        self.label_text.config(
            text=self.text[random.randint(0, len(self.text)-1)])
        self.user_text.delete('1.0', END)


def main():
    root = Tk()
    myapp = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
