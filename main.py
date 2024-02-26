from tkinter import *

def calculate():
    miles = float(mile_entry.get())
    km = miles * 1.609
    val_label.config(text=km)

window = Tk()
window.title("My First GUI Program")
window.minsize()
window.config(padx=20, pady=20)

# Row 1
mile_entry = Entry()
mile_entry.insert(END, "0")
mile_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Row 2
miles_label = Label(text="is equal to")
miles_label.grid(column=0, row=1)

val_label = Label(text="0")
val_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Row 3
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)




window.mainloop()