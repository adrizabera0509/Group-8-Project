from tkinter import *
import mysql.connector

conn = mysql.connector.connect(host="", user="", password="", database="", port="")
mycursor = conn.cursor()

#print(type(mycursor))



class LoginGUI:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Google Keep")
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)

        self.root.configure(background = "#00a65a")

        self.Label1 = Label(self.root, text = "Email" , bg = "#00a65a", fg = "#ffffff")
        self.Label1.configure(font = ("Helvetica",20,"bold"))
        self.Label1.pack(pady = (30,10))
        
        self.email = Entry(self.root)
        self.email.pack(ipadx = 40, ipady = 5)
        
        self.Label2 = Label(self.root, text = "Password" , bg = "#00a65a", fg = "#ffffff")
        self.Label2.configure(font = ("Helvetica",20,"bold"))
        self.Label2.pack(pady = (30,10))
        
        self.password = Entry(self.root)
        self.password.pack(ipadx = 40, ipady = 5)
        
        
        self.login = Button(self.root, text = "Login" , bg = "#1c2833" ,fg = "#ffffff" , width = 15, height = 2, command = lambda:self.loginButton())
        self.login.configure(font = ("Helvetica",10,"bold"))
        self.login.pack(pady = (25,25))
        

        self.loginMessage = Label(self.root, text = "", bg = "#00a56a", fg = "#ffffff")
        self.loginMessage.configure(font = ("Helvetica",12))
        self.loginMessage.pack(pady = (5,10))
        

        self.registration = Button(self.root, text = "Registration" , bg = "#1c2833" ,fg = "#ffffff" , width = 15, height = 2, command = lambda:self.registerButton())
        self.registration.configure(font = ("Helvetica",10,"bold"))
        self.registration.pack(pady = (25,25))

        

        self.root.mainloop()

        

    def loginButton(self):

        loginEmail = self.email.get()
        loginPassword = self.password.get()

        mycursor.execute("SELECT * FROM `users`")
        result = mycursor.fetchall()

        #print(result)

        for ele in result:
            if(loginEmail==ele[2] and loginPassword==ele[3]):
                statusMessage = "Login successful"
                self.loginMessage.configure(text = statusMessage)
                #self.root.destroy()
                listsObj = ListsGUI(ele[0], ele[1])
                break
        else:
            statusMessage = "Incorrect credentials"
            self.loginMessage.configure(text = statusMessage)

        


    def registerButton(self):
        regObj = RegisterGUI()
        




class RegisterGUI:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Google Keep")
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)

        self.root.configure(background = "#00a65a")

        self.Label1 = Label(self.root, text = "Enter username", bg = "#00a56a", fg = "#ffffff")
        self.Label1.configure(font = ("Babas Neue",20,"bold"))
        self.Label1.pack(pady = (30,10))

        self.newUsername = Entry(self.root)
        self.newUsername.pack(ipadx = 40, ipady = 5)

        self.Label2 = Label(self.root, text = "Enter email" , bg = "#00a65a", fg = "#ffffff")
        self.Label2.configure(font = ("Helvetica",20,"bold"))
        self.Label2.pack(pady = (30,10))
        
        self.newEmail = Entry(self.root)
        self.newEmail.pack(ipadx = 40, ipady = 5)
        
        self.Label3 = Label(self.root, text = "Choose password" , bg = "#00a65a", fg = "#ffffff")
        self.Label3.configure(font = ("Helvetica",20,"bold"))
        self.Label3.pack(pady = (30,10))
        
        self.newPassword = Entry(self.root)
        self.newPassword.pack(ipadx = 40, ipady = 5)

        

        self.registration = Button(self.root, text = "Register" , bg = "#1c2833" ,fg = "#ffffff" , width = 15, height = 2, command = lambda:self.newRegistration())
        self.registration.configure(font = ("Helvetica",10,"bold"))
        self.registration.pack(pady = (25,25))


        self.regMessage = Label(self.root, text = "", bg = "#00a56a", fg = "#ffffff")
        self.regMessage.configure(font = ("Helvetica",10))
        self.regMessage.pack(pady = (5,10))
        

        

        self.root.mainloop()


    def newRegistration(self):

        regUsername = self.newUsername.get()
        regEmail = self.newEmail.get()
        regPassword = self.newPassword.get()

        query = "INSERT INTO `users`(user_id, username, email, password) VALUES(NULL, %s, %s, %s)"
        value = (regUsername, regEmail, regPassword)

        mycursor.execute(query, value)
        conn.commit()

        regStatus = "Registration complete, please proceed to login"
        self.regMessage.configure(text = regStatus)
        

        


        
class ListsGUI:

    def __init__(self, userid, username):
        self.root=Tk()
        self.root.title("My Lists")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)

        self.root.configure(background="#00a65a")

        self.label1=Label(self.root,text="Welcome {}".format(username),bg="#00a65a",fg="#ffffff")
        self.label1.configure(font=("Helvetica",20,"bold"))
        self.label1.pack(pady=(30,10))


        self.listsInfo=Label(self.root,text="",bg="#00a65a",fg="#ffffff",justify="left")
        self.listsInfo.configure(font=("Helvetica",14))
        self.listsInfo.pack(pady=(5,10))


        
        self.addListName=Entry(self.root)
        self.addListName.pack(ipadx=40,ipady=5)

        self.addLists=Button(self.root,text="Add",bg="#1c2833",fg="#ffffff",width=25,height=2, command=lambda:self.addList(userid))
        self.addLists.configure(font=("Helvetica",10))
        self.addLists.pack(pady=(10,20))


        self.viewListId=Entry(self.root)
        self.viewListId.pack(ipadx=40,ipady=5)

        self.viewLists=Button(self.root,text="View",bg="#1c2833",fg="#ffffff",width=25,height=2, command=lambda:self.viewList(userid))
        self.viewLists.configure(font=("Helvetica",10))
        self.viewLists.pack(pady=(10,20))


        self.deleteListId=Entry(self.root)
        self.deleteListId.pack(ipadx=40,ipady=5)

        self.deleteLists=Button(self.root,text="Delete",bg="#1c2833",fg="#ffffff",width=25,height=2, command=lambda:self.deleteList(userid))
        self.deleteLists.configure(font=("Helvetica",10))
        self.deleteLists.pack(pady=(10,20))


        self.displayLists(userid)
        
        self.root.mainloop()


    def displayLists(self, userid):
        mycursor.execute("SELECT list_id, list_name From `lists` WHERE user_id LIKE {}".format(userid))
        records = mycursor.fetchall()
        #print(records)
        
        if(len(records) != 0):
            message = ""
            for ele in records:
                message+= str(ele[0]) + "  " + str(ele[1]) + "\n"
            #print(message)
            self.listsInfo.configure(text = message)


    def addList(self, userid):
        listname = self.addListName.get()
            
        query = "INSERT INTO `lists`(list_id, list_name, user_id) VALUES (NULL, %s, %s)"
        val = (listname, userid)
        mycursor.execute(query, val)
        
        conn.commit()
        
        self.displayLists(userid)
        
        
    def deleteList(self, userid):
        listid = int(self.deleteListId.get())
        
        query1 = "DELETE FROM `tasks` WHERE list_id LIKE %s"
        val1 = (listid,)
        mycursor.execute(query1, val1)
        conn.commit()
       
        query2 = "DELETE FROM `lists` WHERE list_id LIKE %s"
        val2 = (listid,)
        mycursor.execute(query2, val2)
        conn.commit()
        
        self.displayLists(userid)            

    def viewList(self, userid):
        listid = int(self.viewListId.get())
        tasksObj = TasksGUI(listid)


class TasksGUI:
    
    def __init__(self, listid):
        
        self.root=Tk()
        self.root.title("View Tasks")
        
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)

        self.root.configure(background = "#00a65a")
        
        self.Label1 = Label(self.root, text = "" , bg = "#00a65a", fg = "#ffffff")
        self.Label1.configure(font = ("Helvetica",22,"bold"))
        self.Label1.pack(pady = (30,10))
        
        mycursor.execute("SELECT list_name FROM `lists` WHERE list_id LIKE {}".format(listid))
        result = mycursor.fetchall()
        self.Label1.configure(text = result[0][0])
        
        self.tasksList = Label(self.root,text="",bg="#00a65a",fg="#ffffff",justify="left")
        self.tasksList.configure(font=("Helvetica",12))
        self.tasksList.pack(pady=(5,10))
        
        self.newTask = Entry(self.root)
        self.newTask.pack(ipadx = 40, ipady = 5)
        
        self.addTasks = Button(self.root, text = "Add New Task" , bg = "#1c2833" ,fg = "#ffffff" , width = 15, height = 2, command = lambda:self.addTask(listid))
        self.addTasks.configure(font = ("Helvetica",10,"bold"))
        self.addTasks.pack(pady = (25,25))
        
        self.status = Entry(self.root)
        self.status.pack(ipadx = 40, ipady = 5)
        
        self.statusButton = Button(self.root, text = "Change Status" , bg = "#1c2833" ,fg = "#ffffff" , width = 15, height = 2, command = lambda:self.changeStatus(listid))
        self.statusButton.configure(font = ("Helvetica",10,"bold"))
        self.statusButton.pack(pady = (25,25))
        
        self.displayTasks(listid)
        
        self.root.mainloop()
    
    def displayTasks(self, listid):
        mycursor.execute("SELECT task_id, description, task_status FROM `tasks` WHERE list_id LIKE {}".format(listid))
        records = mycursor.fetchall()
        #print(records)
        
        if len(records) != 0:
            message = ""
            for ele in records:
                if ele[2] == 0:
                    message+= str(ele[0]) + "  " + " " + "  " + str(ele[1]) + "\n"
                else:
                    message+= str(ele[0]) + "  " + "*" + "  " + str(ele[1]) + "\n"
            #print(message)
            self.tasksList.configure(text = message)

    def addTask(self, listid):
        description = self.newTask.get()
            
        query = "INSERT INTO `tasks`(task_id, description, task_status, list_id) VALUES (NULL, %s, %s, %s)"
        
        val = (description, 0, listid)
        mycursor.execute(query, val)
        
        conn.commit()
        
        self.displayTasks(listid)

    def changeStatus(self, listid):
        taskid = self.status.get()
        
        mycursor.execute("SELECT task_status FROM `tasks` WHERE task_id LIKE {}".format(taskid))
        result = mycursor.fetchall()
        
        if result[0][0] == 0:
            query1 = "UPDATE `tasks` SET `task_status`= 1 WHERE task_id LIKE %s"
            val1 = (taskid,)
            mycursor.execute(query1, val1)
            conn.commit()
        else:
            query2 = "UPDATE `tasks` SET `task_status`= 0 WHERE task_id LIKE %s"
            val2 = (taskid,)
            mycursor.execute(query2, val2)
            conn.commit()
        
        self.displayTasks(listid)




loginObj = LoginGUI()
