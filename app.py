from tkinter import *

# create window object
app = Tk()

# Part
part_text = StringVar()
part_label = Label(app, text='How can i help you?', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Buttons
add_btn = Button(app, text='Voice')

app.title('Bonnie')
app.geometry('700x350')

# start program
app.mainloop()
