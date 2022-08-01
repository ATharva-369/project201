from tkinter import *
from tkinter import ttk

def calculate_si():
    p = float(principalInput.get())
    r = float(rate_of_interestInput.get())
    t = float(timeInput.get())
    i = (p*r*t)/100
    interest = round(i,2)

    resultLabel.destroy()
    output_message = Label(resultFrame,text="The simple interest is: "+str(interest), bg = "lightcyan", font=("Calibri", 200), width=55) 
    output_message.place(x=20,y=20) 
    output_message.pack()     

window = Tk()
window.title('Simple Interest Calculator')
window.geometry('400x400')
appLabel = Label(window, text='Simple Interest Calculator')
appLabel.place(x = 50, y = 10)

principalLabel = Label(window, text = 'Enter the principal amount: ', fg = 'black', bg = 'lightcyan', font = ('Calibri',12), bd = 1)
principalLabel.place(x = 20, y = 90) 
principalInput = Entry(window, text = '', bd = 2, width = 20)
principalInput.place(x = 250, y = 90)

rate_of_interestLabel = Label(window, text = 'Enter the rate of interest: ', fg = 'black', bg = 'lightcyan', font = ('Calibri',12), bd = 1)
rate_of_interestLabel.place(x = 20, y = 160) 
rate_of_interestInput = Entry(window, text = '', bd = 2, width = 20)
rate_of_interestInput.place(x = 250, y = 160)

timeLabel = Label(window, text = 'Enter the period of time: ', fg = 'black', bg = 'lightcyan', font = ('Calibri',12), bd = 1)
timeLabel.place(x = 20, y = 230) 
timeInput = Entry(window, text = '', bd = 2, width = 20)
timeInput.place(x = 250, y = 230)

calculateButton = Button(window, text = "Calculate Simple Interest", fg = 'black', bg = 'cyan', bd = 4, command=calculate_si)
calculateButton.place(x = 110, y = 300)

resultFrame = LabelFrame(window, text = 'Simple Interest: ', bg = 'lightcyan', font = ('Calibri',8), height = 70)
resultFrame.pack(padx = 20, pady = 20)
resultFrame.place(x = 20, y = 350)

resultLabel = Label(resultFrame, text = '', bg = 'lightcyan', font = ('Calibri', 8), width = 33)
resultLabel.place(x = 20, y = 20)
resultLabel.pack()

window.mainloop()