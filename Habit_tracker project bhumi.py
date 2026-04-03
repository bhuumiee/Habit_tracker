print("======================= HABIT TRACKER SYSTEM ======================")
print("*********Small habits tracked daily create big success over time!**********")
#===========================================================================================
#Connectivity 
    
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",
                  password="YOUR_PASSWORD",database="Habit_Tracker")
mycursor=con.cursor()
user=("Create table if not exists users(User_ID int primary key AUTO_INCREMENT, Name varchar(100), Password varchar(100))")
mycursor.execute(user)
habits=("Create table if not exists Habits(Habit_ID int primary key AUTO_INCREMENT,User_ID int, Habit_Name Varchar(250), Created_at Date, FOREIGN KEY(USER_ID) REFERENCES USERS(USER_ID))")
mycursor.execute(habits)
logs=("Create table if not exists Logs(Log_ID int primary key AUTO_INCREMENT, Habit_ID int, Created_at date, Status Boolean, FOREIGN KEY(HABIT_ID) REFERENCES HABITS(HABIT_ID), FOREIGN KEY(CREATED_AT) REFERENCES HABITS(CREATED_AT))")
mycursor.execute(logs)
#===========================================================================================
def register():
    name=input("Enter your name: ")
    psswd=input("Enter your password: ")
    mycursor.execute("INSERT INTO USERS(NAME,PASSWORD) VALUES(%s,%s)",(name,psswd))
    con.commit()
    print("Register Successfully! :)")
    
#============================================================================================
def login():
    name=input("Enter your name: ")
    psswd=input("Enter your password: ")
    mycursor.execute("SELECT*FROM USERS WHERE NAME=%s AND PASSWORD=%s",(name,psswd))
    user=mycursor.fetchone()
    if user:
        print("Login Successfully :)")
        return user[0]
    else:
        print("Invalid credentials")
        return None

#=====================================================================================

def dashboard(user_id):
    while True:
        print("===============================DASHBOARD==============================")
        print("1. Add New Habit")
        print("2. View My Habit")
        print("3. Mark Habit(DONE/MISSED)")
        print("4. View Progress/Analytics")
        print("5. Delete Habit")
        print("6. Logout")
        ab=int(input("Enter your choice: "))
        if ab==1:
            add_habit(user_id)
        elif ab==2:
            view_habits(user_id)
        elif ab==3:
            mark_habit(user_id)
        elif ab==4:
            view_progress(user_id)
        elif ab==5:
            delete_habit(user_id)
        elif ab==6:
            print("Logging out.....")
            break
        else:
            print("Invalid choice :(")

#========================================================================================

def add_habit(user_id):
    i=int(input("Enter how many habits? :"))
    for habit in range(i):
        habit=input("Enter your new habit: ")
        date=input("Enter date(YYYY/MM/DD): ")
        mycursor.execute("INSERT INTO HABITS(User_ID,Habit_Name,Created_at) VALUES (%s,%s,%s)",(user_id,habit,date))
        con.commit()
        print("Habit Added!")

#===============================================================================================

def view_habits(user_id):
    mycursor.execute("SELECT HABIT_ID,HABIT_NAME,CREATED_AT FROM HABITS WHERE USER_ID=%s", (user_id,))
    data=mycursor.fetchall()
    print("\nYour Habits: ")
    for row in data:
        print(row[0],"-",row[1])

#===========================================================================================

def mark_habit(user_id):
    habit_id = int(input("Enter Habit ID: "))
    print("Note: 1 is denoted to done and 0 is denoted to missed.")
    status = input("Enter status (1/0): ")
    mycursor.execute("INSERT INTO LOGS(Habit_ID, Status) VALUES (%s, %s)",(habit_id, status))
    con.commit()
    print("Status updated!")

#==============================================================================================
import matplotlib.pyplot as plt

def view_progress(user_id):
    mycursor.execute("""SELECT Status, COUNT(*) FROM LOGS l
        JOIN HABITS h ON l.Habit_ID = h.Habit_ID
        WHERE h.User_ID = %s
        GROUP BY Status
    """, (user_id,))
    data = mycursor.fetchall()
    labels = []
    values = []
    for row in data:
        labels.append(row[0])   # Done / Missed
        values.append(row[1])   # Count
    plt.bar(labels, values)
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.title("Habit Progress")
    plt.show()

#==========================================================================================
def delete_habit(user_id):
    habit_id = int(input("Enter Habit ID to delete: "))
    mycursor.execute("DELETE FROM HABITS WHERE Habit_ID=%s AND User_ID=%s",(habit_id, user_id))
    con.commit()
    print("Habit deleted!")

#=============================================================================================

while True:
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    ch=int(input("ENTER YOUR CHOICE: "))
    if ch==1:
        user_id=login()
        if user_id:
            print("Welcome user id:", user_id)
            dashboard(user_id)
    elif ch==2:
        register()
    elif ch==3:
        print("HAVE A GOOD DAY! :)")
        break
    else:
        print("Invalid choice :(")
