import tkinter as tk
import birthdays_functional
from PIL import ImageTk, Image
import numpy as np

# Define main window
window = tk.Tk()
window.title('Birthdays')
window.geometry('700x400+250+150')
window.resizable(False, False)

# Define icon
window.iconbitmap('person.ico')
 
# Define image
img = Image.open('birthday-cake.png').resize((100,100))
img = ImageTk.PhotoImage(img)

# Divide window in frames
frame0 = tk.Frame(master=window, height=50)
frame0.pack(fill=tk.X)

frame1 = tk.Frame(master=window, height=150)
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=150)
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=50)
frame3.pack(fill=tk.X)

# Birthday information
bd_today, contacts = birthdays_functional.Birthday_today()
has_number = lambda x : any(i.isdigit() for i in x)
no_number = '(No contact information)'
next = birthdays_functional.next_Birthday()


next_day = int(next.day)
next_month = int(next.month)

for i, contato in enumerate(contacts):
    if has_number(contato):
        pass
    else:
        contacts[i] = no_number



# Filling main window
if len(bd_today) > 0:
    
    text = 'Today is the birthday of:\n\n'

    for i in range(len(bd_today)):
        text = text + bd_today[i] + ' - ' + contacts[i] + '\n\n'

    l1 = tk.Label(frame1, text = text, justify='center')
    l1.config(font =("Courier", 14))
    l1.pack()


    l2 = tk.Label(frame2, image=img)
    l2.pack()

else:

    months = {1: "January", 2: "February", 3: "March", 4: "April", 5:"May", 6:"June", 7:"July", 8:"Agust",\
        9:"September", 10:"October", 11:"Novembero", 12:"December"}


    text = 'Today we have no birthdays\n\n'

    l1 = tk.Label(frame1, text = text, justify='center')
    l1.config(font =("Courier", 14))
    l1.pack()



    text_2 = f'Next birthday is {next_day} of {months.get(next_month)}'

    l2 = tk.Label(frame2, text = text_2)
    l2.config(font =("Courier", 14))
    l2.pack()


# Display window
window.mainloop()

