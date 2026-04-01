from tkinter import *
from tkinter import messagebox

root = Tk()

def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str = f'Данні: {login}, {password}'
    messagebox.showinfo(title='Назва', message=info_str )

    # messagebox.showerror(title='', message='Error')

    if not login or not password:
        messagebox.showwarning("Увага", "Заповніть всі поля")
        return

root['bg'] = '#fafafa'
root.title('Назва програми')
root.wm_attributes('-alpha', 0.7)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='gray')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текст підказка', bg='blue', font=('Arial', 14))
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()

root.mainloop()