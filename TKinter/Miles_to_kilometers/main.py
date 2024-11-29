from tkinter import *

INPUT = 0

window = Tk()

window.title("Convert Miles to Kilometer")
window.minsize(height=250, width=250)
window.config(padx=100, pady=100)
# window.interpaddr(padx=100,pady=100 )

# label (Miles)

label = Label(text="Miles", font=("times new roman", 10, "bold"))
label.grid(column=2, row=0)

# label 2 (is equal to)

label1 = Label(text="is equal to ", font=("times new roman", 10, "bold"))
label1.grid(column=0, row=1)

# label 3 (output)
label2 = Label(text=0, font=("times new roman", 10, "bold"))
label2.grid(column=1, row=1)

# label 4 (KM)
label3 = Label(text="KM", font=("times new roman", 10, "bold"))
label3.grid(column=2, row=1)


# button
def clicked():
    INPUT = float(input.get())
    result = INPUT * 1.6
    label2["text"] = result


button = Button(text="Calculate", command=clicked)
button.grid(column=1, row=2)

# entry

input = Entry()
input.grid(column=1, row=0)
# INPUT = input.get()


window.mainloop()
