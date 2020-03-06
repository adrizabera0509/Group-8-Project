from tkinter import *
import mysql.connector

conn = mysql.connector.connect(host="", user="", password="", database="", port="")
mycursor = conn.cursor()

#print(type(mycursor))



class HomeGUI:
    
    def __init__(self, userid, username):
        
        self.root = tk.Tk()
        self.root.title("Home")
        
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)
        
        self.root.configure(background = "#FF9900")
        
        self.Label1 = tk.Label(self.root, text = "Welcome {}".format(username), bg = "#FF9900", fg = "#000000")
        self.Label1.configure(font = ("Helvetica",22,"italic"))
        self.Label1.pack(pady = (15,5)) 
        
        self.lists = tk.Label(self.root,text="",height = 8, bg="#FF9900",fg="#000000", justify = "left")
        self.lists.configure(font=("Constantia",12))
        self.lists.pack(pady=(5,10))
        
            
        
        self.newlist = tk.Entry(self.root)
        self.newlist.pack(ipadx = 40, ipady = 5)
        
        self.add = tk.Button(self.root, text = "Add List" , bg = "#000000" ,fg = "#FFFFFF" , width = 10, height = 2, command = lambda : self.addList(userid))                     
        self.add.configure(font = ("Bebas Neue",10,"bold"))
        self.add.pack(pady = (10,20))
        
        self.viewLabel = tk.Label(self.root, text = "Enter list no to View List", bg = "#FF9900", fg = "#000000")
        self.viewLabel.configure(font = ("Bebas Neue",10))
        self.viewLabel.pack(pady = (5,5)) 
        
        self.viewlist = tk.Entry(self.root)
        self.viewlist.pack(ipadx = 40, ipady = 5)
        
        self.view = tk.Button(self.root, text = "View" , bg = "#000000" ,fg = "#FFFFFF" , width = 10, height = 2, command = lambda : self.viewList(userid))                     
        self.view.configure(font = ("Bebas Neue",10,"bold"))
        self.view.pack(pady = (10,10))
        
        self.viewLabel = tk.Label(self.root, text = "Enter list no to Delete List", bg = "#FF9900", fg = "#000000")
        self.viewLabel.configure(font = ("Bebas Neue",10))
        self.viewLabel.pack(pady = (5,5))
        
        self.dellist = tk.Entry(self.root)
        self.dellist.pack(ipadx = 40, ipady = 5)
        
        self.delete = tk.Button(self.root, text = "Delete" , bg = "#000000" ,fg = "#FFFFFF" , width = 10, height = 2, command = lambda : self.deleteList(userid))                     
        self.delete.configure(font = ("Bebas Neue",10,"bold"))
        self.delete.pack(pady = (10,25))
        
        
        
        self.displayLists(userid)
        
        self.root.mainloop()
    
    def displayLists(self, userid):
        mycursor.execute("SELECT list_id, list_name From `lists` WHERE user_id LIKE {}".format(userid))
        records = mycursor.fetchall()
        #print(records)
        
        if len(records) != 0:
            message = ""
            for ele in records:
                message+= str(ele[0]) + ".  " + "    " + str(ele[1]) + "\n"
        #print(message)
            self.lists.configure(text = message) 
    
        
        
    def addList(self, userid):
        listname = self.newlist.get()
            
        query = "INSERT INTO `lists`(list_id, list_name, user_id) VALUES (NULL, %s, %s)"
        
        val = (listname, userid)
        mycursor.execute(query, val)
        
        conn.commit()
        
        self.displayLists(userid)
        
    def deleteList(self, userid):
        listid = int(self.dellist.get())
        
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
        listid = int(self.viewlist.get())
        ViewGUI(listid)




class ViewGUI:
    
    def __init__(self, listid):
        
        self.root=tk.Tk()
        self.root.title("View Tasks")
        
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)

        self.root.configure(background = "#FF9900")
        
        self.Label1 = tk.Label(self.root, text = "" , bg = "#FF9900", fg = "#000000")
        self.Label1.configure(font = ("Bebas Neue",22))
        self.Label1.pack(pady = (15,20))
        
        mycursor.execute("SELECT list_name FROM `lists` WHERE list_id LIKE {}".format(listid))
        result = mycursor.fetchall()
        self.Label1.configure(text = result[0][0])
        
        self.tasks = tk.Label(self.root,text="", height = 8, bg="#FF9900", fg="#000000", justify = "left")
        self.tasks.configure(font=("Constantia",12))
        self.tasks.pack(pady=(5,10))
        
        self.newtask = tk.Entry(self.root)
        self.newtask.pack(ipadx = 40, ipady = 5)
        
        self.addTasks = tk.Button(self.root, text = "Add New Task" , bg = "#000000" ,fg = "#FFFFFF" , width = 15, height = 2, command = lambda:self.addTask(listid))
        self.addTasks.configure(font = ("Bebas Neue",10,"bold"))
        self.addTasks.pack(pady = (10,25))
        
        self.status = tk.Entry(self.root)
        self.status.pack(ipadx = 40, ipady = 5)
        
        self.StatusButton = tk.Button(self.root, text = "Enter Task no. to Change Task Status" , bg = "#000000" ,fg = "#FFFFFF" , width = 25, height = 2, command = lambda:self.changeStatus(listid))
        self.StatusButton.configure(font = ("Bebas Neue",10,"bold"))
        self.StatusButton.pack(pady = (10,25))
        
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
                    message+= str(ele[0]) + ".    " + " *-*    " +  str(ele[1])  + "\n"
                else:
                    message+= str(ele[0]) + ".    " + " ^-^    " + str(ele[1]) + "\n"
            #print(message)
            self.tasks.configure(text = message)

    def addTask(self, listid):
        description = self.newtask.get()
            
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

class RegistrationGUI:

    def __init__(self):

        self.root=tk.Tk()
        self.root.title("Registration")
        
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)

        self.root.configure(background = "#FF9900")
        
        self.Label1 = tk.Label(self.root, text = "User Name" , bg = "#FF9900", fg = "#000000")
        self.Label1.configure(font = ("Bebas Neue",18))
        self.Label1.pack(pady = (110,10))
        
        self.username = tk.Entry(self.root)
        self.username.pack(ipadx = 40, ipady = 5)
        
        self.Label2 = tk.Label(self.root, text = "Email" , bg = "#FF9900", fg = "#000000")
        self.Label2.configure(font = ("Bebas Neue",18))
        self.Label2.pack(pady = (30,10))
        
        self.new_email = tk.Entry(self.root)
        self.new_email.pack(ipadx = 40, ipady = 5)
        
        self.Label3 = tk.Label(self.root, text = "Password" , bg = "#FF9900", fg = "#000000")
        self.Label3.configure(font = ("Bebas Neue",18))
        self.Label3.pack(pady = (30,10))
        
        self.new_password = tk.Entry(self.root)
        self.new_password.pack(ipadx = 40, ipady = 5)
    
        self.registration = tk.Button(self.root, text = "Register" , bg = "#000000" ,fg = "#FFFFFF" , width = 15, height = 2, command = lambda:self.addUser())
        self.registration.configure(font = ("Bebas Neue",10,"bold"))
        self.registration.pack(pady = (25,25))
        
        self.root.mainloop()
        
    def addUser(self):
        uname = self.username.get()
        newemail = self.new_email.get()
        newpass = self.new_password.get()
        
        query = "INSERT INTO `users`(user_id, username, email, password) VALUES (NULL, %s, %s, %s)"
        val = (uname, newemail, newpass)
        
        mycursor.execute(query, val)
        conn.commit()
        
        mycursor.execute("SELECT * FROM `users`")
        result = mycursor.fetchall()
        for ele in result:
            if(newemail == ele[2] and newpass== ele[3]):
                self.root.destroy()
                HomeGUI(ele[0], ele[1])
                break
        
        #print(mycursor.rowcount, "record(s) inserted.")
        


class LoginGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To Do List")
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)

        self.root.configure(background = "#FF9900")
                            
        self.appName = tk.Label(self.root, text = "Tasky" , bg = "#FF9900", fg = "#000000")
        self.appName.configure(font = ("Bebas Neue",32, "italic"))
        self.appName.pack(pady = (50,5))
        
        self.line = tk.Label(self.root, text = "Manages your tasks ;)" , bg = "#FF9900", fg = "#000000")
        self.line.configure(font = ("Bebas Neue",10, "italic"))
        self.line.pack(pady = (5,10))

        self.Label1 = tk.Label(self.root, text = "Email" , bg = "#FF9900", fg = "#000000")
        self.Label1.configure(font = ("Bebas Neue",18))
        self.Label1.pack(pady = (30,10))
        
        self.email = tk.Entry(self.root)
        self.email.pack(ipadx = 40, ipady = 5)
        
        self.Label2 = tk.Label(self.root, text = "Password" , bg = "#FF9900", fg = "#000000")
        self.Label2.configure(font = ("Bebas Neue",18))
        self.Label2.pack(pady = (30,10))
        
        self.password = tk.Entry(self.root)
        self.password.pack(ipadx = 40, ipady = 5)
        
        
        self.login = tk.Button(self.root, text = "Login" , bg = "#000000" ,fg = "#FFFFFF" , width = 15, height = 2, command = lambda:self.loginButton())
        self.login.configure(font = ("Bebas Neue",10,"bold"))
        self.login.pack(pady = (20,25))
        
        self.Label3 = tk.Label(self.root, text = "" , bg = "#FF9900", fg = "#000000")
        self.Label3.configure(font = ("Bebas Neue",10))
        self.Label3.pack(pady = (5,5))
        
        self.registration = tk.Button(self.root, text = "Register" , bg = "#000000" ,fg = "#FFFFFF" , width = 15, height = 2, command = lambda:self.registrationButton())
        self.registration.configure(font = ("Bebas Neue",10,"bold"))
        self.registration.pack(pady = (5,25))

        self.root.mainloop()

    def loginButton(self):

        e = self.email.get()
        p = self.password.get()

        mycursor.execute("SELECT * FROM `users`")
        result = mycursor.fetchall()
    
        for ele in result:
            if(e== ele[2] and p== ele[3]):
                self.root.destroy()
                obj3 = HomeGUI(ele[0], ele[1])
                break
        else:
            self.Label3.configure(text = "Can't log in? Please register.")
    
    def registrationButton(self):
        self.root.destroy()
        RegistrationGUI()
        
        
    
obj = LoginGUI()

