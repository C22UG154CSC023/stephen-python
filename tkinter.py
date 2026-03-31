import tkinter as tr


main = tr.Tk()
main.geometry("1366x768")
main.config(background="#90a955")
container = tr.Frame(main,bg="#bbd0ff")
container.place(x=0, y=0, width="1366", height="768")

registration = tr.Frame(container,bg="#dee2e6")
login_Form = tr.Frame(container,bg="#6c757d")
mp = tr.Frame(container,bg="#e9d8a6")

for pages in (registration,login_Form,mp):
    pages.place(x=0, y=0, width="1366", height="768")

title = tr.Label(registration,text = "Registration Form",bg="#dee2e6", fg = "#000814", font = ("Times new roman",30))
title.place(x=500, y=100)

tr.Label(registration,text="User Name :",bg="#dee2e6",fg="#000814",font=("Times new roman",20)).place(x=400,y=200)
registration_name = tr.Entry(registration,bg="#dee2e6",fg="#000814",font=("Times new roman",20))
registration_name.place(x=580,y=200)

tr.Label(registration,text="Phone :",bg="#dee2e6",fg="#000814",font=("Times new roman",20)).place(x=450,y=250)
registration_phone = tr.Entry(registration,bg="#dee2e6",fg="#000814",font=("Times new roman",20))
registration_phone.place(x=580,y=250)

tr.Label(registration,text="Email :",bg="#dee2e6",fg="#000814",font=("Times new roman",20)).place(x=450,y=300)
registration_Email = tr.Entry(registration,bg="#dee2e6",fg="#000814",font=("Times new roman",20))
registration_Email.place(x=580,y=300)

tr.Label(registration,text="Password :",bg="#dee2e6",fg="#000814",font=("Times new roman",20)).place(x=410,y=350)
registration_Password = tr.Entry(registration,bg="#dee2e6",fg="#000814",font=("Times new roman",20))
registration_Password.place(x=580,y=350)


def register_action():
    name = registration_name.get()
    phone = registration_phone.get()
    email = registration_Email.get()
    password = registration_Password.get()

    print("Name:", name)
    print("Phone:", phone)
    print("Email:", email)
    print("Password:", password)


tr.Button(registration, text="Register",bg="#000814",fg="white",font=("Times new roman", 18)
          ,command=register_action).place(x=580, y=420)

registration.tkraise()
main.mainloop()
