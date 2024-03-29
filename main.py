from tkinter import *
from tkinter.ttk import *

# function to be called when the Exit button is clicked
def exit_program():
  window.destroy()

# function to display a popup window
def madlib_generator():
  madlib = red_input.get().capitalize() + " are red,\n" + \
           blue_input.get().lower() + " are blue.\n" + \
           "I like " + like_input.get().lower() + \
           ",\nbut not as much as I love\n" + \
           verb_input.get().lower() + " with you!"
  print(madlib)
  madlib_popup(madlib)

# function to display a popup window
def madlib_popup(msg):
  popup = Tk()
  popup.wm_title("Results")
  popup.configure(bg="PaleTurquoise2")

  label = Label(popup, text=msg, background="PaleTurquoise2")
  label.pack()

  button2 = Button(popup, text="OK", command = popup.destroy)
  button2.pack()

  popup.mainloop()

window = Tk()
window.title("MadLib Generator")
window.configure(background="MediumPurple1")

button_style = Style()
button_style.configure("TButton", padding=2, borderwidth=4)

label_style = Style()
label_style.configure("TLabel", foreground="white", background="MediumPurple1")

input_style = Style()
input_style.configure("TEntry", foreground="black", background="white")

top_label = Label(window, text="")
top_label.pack()

red_label = Label(window, text="Enter something red (e.g. roses):")
red_label.pack()

red_input = Entry(window, text = "")
red_input.pack()

filler_label1 = Label(window, text="")
filler_label1.pack()

blue_label = Label(window, text="Enter something blue (e.g. violets):")
blue_label.pack()

blue_input = Entry(window, text = "")
blue_input.pack()

filler_label2 = Label(window, text="")
filler_label2.pack()

like_label = Label(window, text="Enter something you like (e.g. puppies):")
like_label.pack()

like_input = Entry(window, text = "")
like_input.pack()

filler_label3 = Label(window, text="")
filler_label3.pack()

verb_label = Label(window, text="Enter a verb (e.g. dancing):")
verb_label.pack()

verb_input = Entry(window, text = "")
verb_input.pack()

bottom_label = Label(window, text="")
bottom_label.pack()

# adding a generate button
button_image = PhotoImage(file="fairyMagic2.png")
button1 = Button(window, text="Generate MadLib", image = button_image, compound = TOP, command = madlib_generator)
button1.pack()

filler_label4 = Label(window, text="")
filler_label4.pack()

# adding Exit button
qbutton = Button(window, text="Exit", command = exit_program)
qbutton.pack()

window.mainloop()  # GUI main event loop