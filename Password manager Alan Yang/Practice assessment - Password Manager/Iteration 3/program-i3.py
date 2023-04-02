from tkinter import*
from tkinter import ttk
window = Tk()
saved = []

def frames1():
    window.geometry("270x500")
    global frame1
    frame1 = Frame(window)
    frame1.grid(sticky="nsew")
    window.title("Login")
    
    titlef1 = Label(frame1, text="Password Manager", font = ("'' 16 underline"))
    titlef1.grid(row = 0, column = 0, pady=30,padx=5)
    heading = Label(frame1, text="Please enter login", font = ("' 10 "))
    heading.grid(row = 1, column = 0, pady=8,padx=5)

    userlabel = Label(frame1, text="Enter username")
    userlabel.grid(row = 2, column = 0, pady=8,padx=90)
    userentry = Entry(frame1)
    userentry.grid(row = 3, column = 0, padx=10)

    passwordlabel = Label(frame1, text="Enter Password")
    passwordlabel.grid(row = 4, column = 0, pady=8,padx=10)
    passwordentry = Entry(frame1, show="*")
    passwordentry.grid(row = 5, column = 0, padx=10)

    loginbtn = Button(frame1, text="Login", command=lambda: login(userentry, passwordentry, message))
    loginbtn.grid(row = 6, column = 0, pady=8,padx=10)

    message = Label(frame1)
    message.grid(row = 7, column = 0, pady=8,padx=10)

    with open("Practice assessment - Password Manager\Iteration 3\savedlogin.txt", "r") as file:
        files = file.read()
        if not files:
            heading.config(text="Enter username and password to set login")

def frames2():
    global frame2
    frame2 = Frame(window)
    frame2.grid(sticky="nsew")
    window.title("Login")
    window.geometry("530x500")
    frame1.grid_forget()

    paddings = Label(frame2)
    paddings.grid(row = 0, column = 0, pady=10,padx=10)

    greeting = Label(frame2,text=f"Hello, {username} ",font=('Sans Serif', 12), anchor=CENTER)
    greeting.place(x=260, y=25, anchor="center")

    addlogin = Label(frame2,text="New Login",font= ('Arial 10 underline'))
    addlogin.grid(row = 1, column = 0, pady=8,padx=10)

    newwebsite = Label(frame2,text="Website: ")
    newwebsite.grid(row = 2, column = 0, pady=8,padx=10)
    webentry = Entry(frame2)
    webentry.grid(row = 2, column = 1, pady=8,padx=10)

    newlogin = Label(frame2,text="Username: ")
    newlogin.grid(row = 3, column = 0, pady=8,padx=10)
    logentry = Entry(frame2)
    logentry.grid(row = 3, column = 1,pady=8,padx=10)

    newpassword = Label(frame2,text="Password: ")
    newpassword.grid(row = 4, column = 0, pady=8,padx=10)
    passentry = Entry(frame2, show="*")
    passentry.grid(row = 4, column = 1, pady=8,padx=10)

    addlogin = Button(frame2, text="Save Login", command= lambda: createlogin(webentry, logentry, passentry, completedmsg, view, list))
    addlogin.grid(row = 5, column = 1, pady=10,padx=10)

    retrievelogin = Label(frame2,text="Get Login",font= ('Arial 10 underline'))
    retrievelogin.grid(row = 7, column = 0, pady=8,padx=10)

    getweb = Label(frame2,text="Website: ")
    getweb.grid(row = 8, column = 0, pady=8,padx=10)
    getwebentry = Entry(frame2)
    getwebentry.grid(row = 8, column = 1, pady=8,padx=10)
    webinput = getwebentry.get()

    completedmsg = Label(frame2, text="")
    completedmsg.grid(row = 6, column = 1, pady=10,padx=10)

    viewsaved = Button(frame2, text="Retrieve password", command=lambda:  retrievelog(loginmsg, webinput))
    viewsaved.grid(row = 9, column = 1, pady=2,padx=10)

    loginmsg = Label(frame2)
    loginmsg.grid(row = 10, column = 1, pady=5,padx=10)

    buffer = Label(frame2, text=" ")
    buffer.grid(row = 12, column = 1, pady=10,padx=100)

    webslabel = Label(frame2, text="Remove login", font= ('Arial 10 underline'))
    webslabel.grid(row = 1, column = 3, pady=8,padx=8)

    weblabel = Label(frame2, text="Enter Website or select from the list")
    weblabel.grid(row = 2, column = 3, pady=8,padx=8)

    with open('Practice assessment - Password Manager\Iteration 3\savedpasswords.txt', 'r') as file:
        for line in file:
            saved.append(f"{line.split(' : ')[0]} : {line.split(' : ')[1]}")
    list = ttk.Combobox(frame2, values = [item.split(" : ")[0] for item in saved])
    list.grid(row = 3, column = 3, padx=8, pady=8)

    submit = Button(frame2, text="Remove login", command=lambda: deletelogin(msg, list, saved, view))
    submit.grid(row = 4, column = 3, pady=8,padx=8)

    msg = Label(frame2)
    msg.grid(row = 5, column = 3, padx=8)

    viewlabel = Label(frame2, text="View all logins",font= ('Arial 10 underline'))
    viewlabel.grid(row=7, column=3, padx=8, pady=8)

    view = ttk.Combobox(frame2, values = saved)
    view.grid(row = 8, column = 3, padx=8, pady=8)

    resetlogin = Button(frame2, text="Reset login", command=lambda:[open("Practice assessment - Password Manager\Iteration 3\savedlogin.txt", "w").write(""), frames1(), frame2.grid_forget()])
    resetlogin.place(x=260, y=450, anchor="center")

def login(userentry, passwordentry, message):
    global username
    username = userentry.get()
    if username == "" or passwordentry == "":
        message.config(text="Please fill in all blanks")
    else:
        with open("Practice assessment - Password Manager\Iteration 3\savedlogin.txt", "r") as file:
            files = file.read()
            if not files:
                newsaved = (f"{username} : {passwordentry.get()}")
                with open("Practice assessment - Password Manager\Iteration 3\savedlogin.txt", "a") as f:
                    f.write(newsaved)
                    frames2()
            else:    
                with open("Practice assessment - Password Manager\Iteration 3\savedlogin.txt", "r") as file:
                    for line in file:
                        if userentry.get() == line.split(" : ")[0] and passwordentry.get() == line.split(" : ")[1]:
                            frames2()
                        else:
                            message.config(text="Incorrect username or password")
                            
def createlogin(webentry, logentry, passentry, completedmsg, list, view):
    newsaved = (f"{webentry.get()} : {logentry.get()} : {passentry.get()}\n")
    if webentry.get() == "" or logentry.get() == "" or passentry.get() == "":
        completedmsg.config(text="Please fill in all fields.")
    else:
        with open("Practice assessment - Password Manager\Iteration 3\savedpasswords.txt", "a") as f:
            f.write(newsaved)
        completedmsg.config(text="Password saved!")
        webentry.delete(0,END)
        logentry.delete(0,END)
        passentry.delete(0,END)
        saved = []
        with open('Practice assessment - Password Manager\Iteration 3\savedpasswords.txt', 'r') as file:
            for line in file:
                saved.append(f"{line.split(' : ')[0]} : {line.split(' : ')[1]}")
                view["values"] = [item.split(" : ")[0] for item in saved]
                list["values"] = saved 

def retrievelog(webinput, loginmsg):
    found = False
    if webinput == "":
        loginmsg.config(text="Please enter website.")
    else:
        with open("Practice assessment - Password Manager\Iteration 3\savedpasswords.txt", "r") as file:
            for line in file:
                if webinput == line.split(" : ")[0]:
                    username, password = line.split(" : ")[1:]
                    loginmsg.config(text=f"Username: {username}, Password: {password}")

    if not found:
        loginmsg.config(text=f"Login information for {webinput} not found")

def deletelogin(msg, list, saved, view):
    if list.get() != "":
        with open("Practice assessment - Password Manager\Iteration 3\savedpasswords.txt", "r") as file:
            lines = file.readlines()
        with open("Practice assessment - Password Manager\Iteration 3\savedpasswords.txt", "w") as file:
            for line in lines:
                if list.get() == line.split(" : ")[0]:
                    msg.config(text="Password deleted!")
                else:
                    file.write(line)
        saved = []
        with open('Practice assessment - Password Manager\Iteration 3\savedpasswords.txt', 'r') as file:
            for line in file:
                saved.append(f"{line.split(' : ')[0]} : {line.split(' : ')[1]}")
        list["values"] = [item.split(" : ")[0] for item in saved]
        view["values"] = saved 
        list.delete(0, END)
    else: 
        msg.config(text="Please enter a website or select from list")


frames1()
window.mainloop()