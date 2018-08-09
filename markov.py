# Maxwell Andrew
# Apr 14, 2015
# Markov model text generation

from random import randint
from Tkinter import *
import os

# callback function for the 'create model' button
def create_action():
    global n
    n = order_entry.get()
    f = file_entry.get()
    if n.isdigit() == False:
        display_message('Error: please enter valid decimal digit.')
        return None
    n = int(n)
    if os.path.isfile(f) == False:
        display_message('Error: please enter valid file path.')
        return None
    display_message(' ')
    text = open(f)
    global inputStr
    inputStr = text.read()
    # empty dictionary for model
    global model
    model = {}
    for i in range(len(inputStr)):
        key = inputStr[i:i+n]
        successor = inputStr[i+n:i+n+1]
        if key in model:
            model[key] += successor
        else:
            model[key] = successor
        
# generate sample
def generate_action():
    m = 1000
    output = inputStr[0:n]
    for i in range(m-n):
        key = output[i:i+n]
        if key not in model:
            break
        else:
            key = output[i:i+n]
            randLoc = randint(0,len(model[key])-1)
            output += model[key][randLoc]
    print output

def display_message(message):
    message_label.config(text=message)   

window = Tk()
window.title('Markov model text generator')

output = Text(window,wrap=WORD,bd=10,highlightcolor='#a44245',highlightbackground='#a44245',highlightthickness=10,padx=5,pady=5)
output.grid(row=0,column=0,columnspan=2)

# create the entry widgets
order_label = Label(window,text='Enter the order of the model:')
order_label.grid(row=1,column=0,sticky='E')

order_entry = Entry(window)
order_entry.grid(row=1,column=1,sticky='W')

file_label = Label(window,text='Enter the name of the sample file:')
file_label.grid(row=2,column=0,sticky='E')

file_entry = Entry(window)
file_entry.grid(row=2,column=1,sticky='W')

message_label = Label(window,fg='red')
message_label.grid(row=3,column=0,columnspan=2)

# create buttons
create_button = Button(window,text='Create model',command=create_action)
create_button.grid(row=4,column=0,)

gen_button = Button(window,text='Generate text',command=generate_action)
gen_button.grid(row=4,column=1)

window.mainloop()

