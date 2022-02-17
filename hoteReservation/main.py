


try:
    import mysql.connector
    from datetime import date
    import matplotlib.pyplot as plt
    from tkinter import *
except:
    raise Exception("You do not have all the modules required to run this file")

# Our Hotel
# 5 room on first floor with AC
# 5 room on fist floow without AC
# 5 room on second floow with AC
# 5 room on second floor without AC


# template
def starter():
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("**                                              **")
    print("**               Hotel Sentinals                **")
    print("**                                              **")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    # hoter

class DBCreator:
    def __init__(self):
        self.connector = mysql.connector.connect(host='localhost', user='root', password='', database='hotel')
        cursor = self.connector.cursor()
        q1 = "create database if not exists hotel"
        cursor.execute(q1)
        query = "create table if not exists roomm(roomNo int, floor varchar(50), charge varchar(12),ac varchar(1), status varchar(1))"
        cursor.execute(query)
        query2 = "create table if not exists inDataProo(roomNo int, name varchar(50), phone varchar(12), date varchar(20), nDays varchar(10))"
        cursor.execute(query2)
        query3 = "create table if not exists reviews(name varchar(50), review varchar(100))"
        cursor.execute(query3)
        # print("COnnected")

    def roomInserter(self, roomNo, floor, charge, ac, status='A'):
        query = "insert into roomm(roomNo, floor, charge, ac, status) values({}, '{}', '{}','{}', '{}')".format(roomNo, floor, charge,ac, status)
        cursor = self.connector.cursor()
        cursor.execute(query)
        self.connector.commit()

    def currentService(self):
        query = "select * from roomm"
        cursor = self.connector.cursor()
        cursor.execute(query)

        for item in cursor:
            print(f'''Room No. : {item[0]}\n
                        Floor : {item[1]}\n
                        Charge : {item[2]}\n
                        AC : {item[3]}\n
                        Status : {item[4]}\n''')
    
    def showInside(self):
        query = "select * from inDataProo"
        cursor = self.connector.cursor()
        cursor.execute(query)

        for item in cursor:
            print(f'''Room No. : {item[0]}\n
                        Name : {item[1]}\n
                        Phone : {item[2]}\n
                        Entery Date : {item[3]}\n
                        No. Days : {item[4]}''')

    def bookroom(self, roomNo, userName, phone, date, nDays, status='O'):
        qu = "select * from roomm where roomNo={}".format(roomNo)
        cursor = self.connector.cursor()
        cursor.execute(qu)
        for item in cursor:
            if item[4] == "O":

                raise Exception("Allready Occupied")
        query = "update roomm set status='{}' where roomNo={}".format(status, roomNo)
        query2 = "insert into inDataProo(roomNo, name, phone, date, nDays) values({},'{}', '{}', '{}', {})".format(roomNo, userName, phone, date, nDays)
        cursor = self.connector.cursor()
        cursor.execute(query)
        cursor.execute(query2)
        self.connector.commit()
    
    def leaveRoom(self, roomNo,phone, status="A"):
        # checking if the room is alloted to the said person
        qu = "select * from roomm where roomNo={}".format(roomNo)
        cursor = self.connector.cursor()
        cursor.execute(qu)
        charge = 0
        for item in cursor:
            charge = item[2]
            if item[4] == "A":
                raise Exception("This room is already available")
        qi = "select * from inDataProo where roomNo={}".format(roomNo)
        cursor = self.connector.cursor()
        cursor.execute(qi)
        noOfDays = 0
        userName = ""
        for item in cursor:
            noOfDays = item[4]
            userName = item[1]
            if item[2] != phone:
                raise Exception("This room is not alloted with this number!!")

        query = "update roomm set status='{}' where roomNo={}".format(status, roomNo)
        cursor.execute(query)
        self.connector.commit()

        # slip part
        t = input("\nPress 1 to see the slip and Press 2 to print the slip")
        # slip = '********************************\n** NAME  :  {}           **\n** Room No  :  {}        **\n** Total Charge  : {}    **\n** No. of Days  :  {}    **\n******************************************'.format(userName, roomNo, charge*noOfDays, noOfDays)
        if t == "1":
            print("Hotel Management System\n")
            print("Name : "+ userName)
            print("Phone : " + str(phone))
            print("Room No : "+ str(roomNo))
            print("No. of Days : "+ noOfDays)
            print("Charge : "+ str(int(noOfDays)*int(charge)))
        elif t == '2':
            fileame = str(date.today()) + userName + '.txt'
            lis = ["Hotel Management System", "Name : "+ userName,"Phone : " + str(phone), "Room No : "+ str(roomNo), "No. of Days : "+ noOfDays, "Charge : "+ str(int(noOfDays)*int(charge))]
            f = open(fileame, 'w')
            for line in lis:

                f.write(line)
                f.write("\n")
            f.close()
    
    def addReview(self, userName, review):
        qu = "insert into reviews(name, review) values('{}', '{}')".format(userName, review)
        cursor = self.connector.cursor()
        cursor.execute(qu)
        self.connector.commit()
    
    def seeReview(self):
        qu = "select * from reviews"
        cursor = self.connector.cursor()
        cursor.execute(qu)
        
        if cursor is None:
            print("There is no review yet.")
        else:
            print("\n")
            for item in cursor:
                print(f"Name : {item[0]}\nReview : {item[1]}\n")


        
    def deleter(self, roomNo):
        query = "delete from user where roomNo={}".format(roomNo)
        # query2 = "delete from inData where roomNo={}"
        print(query)
        cursor = self.connector.cursor()
        cursor.execute(query)
        self.connector.commit()
        print("Deleted")



user = DBCreator()

# room No, Floor, Price, AC

# user.roomInserter(1, '1', '100', 'Y')
# user.roomInserter(2, '1', '100', 'Y')
# user.roomInserter(3, '1', '100', 'Y')
# user.roomInserter(4, '1', '100', 'Y')
# user.roomInserter(5, '1', '100', 'Y')
# user.roomInserter(6, '1', '1000', 'Y')
# user.roomInserter(7, '1', '1000', 'Y')
# user.roomInserter(8, '1', '1000', 'Y')
# user.roomInserter(9, '1', '1000', 'Y')
# user.roomInserter(10, '1', '1000', 'Y')
# user.roomInserter(11, '2', '200', 'Y')
# user.roomInserter(12, '2', '200', 'Y')
# user.roomInserter(13, '2', '200', 'Y')
# user.roomInserter(14, '2', '200', 'Y')
# user.roomInserter(15, '2', '200', 'Y')
# user.roomInserter(16, '2', '2000', 'Y')
# user.roomInserter(17, '2', '2000', 'Y')
# user.roomInserter(18, '2', '2000', 'Y')
# user.roomInserter(19, '2', '2000', 'Y')
# user.roomInserter(20, '2', '2000', 'Y')









def graph():
    # # import matplotlib.pyplot as plt

    # # fig, ax = plt.subplots()
    x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    y = [0, 0.5, 0.3,1,1.5, 2.5, 2,3, 3, 3.5, 4, 5]
    plt.plot(x, y)
    plt.show()



starter()
while True:
    n = input('''\nPress 1 to view the current service available\n
Press 2 to book room\n
Press 3 to view the inside(for admin only)\n
Press 4 to leave the room\n
Press 5 to see the rating\n
Press 6 to add review\n
Press 7 to see reviews\n
Press 8 to quit -- ''')

    if n == '1':
        user.currentService()
        print("*********************************************\n")
    elif n == '2':
        roomNo = int(input("Please input room number -- "))
        userName = input("Please input your name -- ")
        phone = input("Please input you number -- ")
        nDays = input("Please input no. of days you want to stay -- ")
        d = str(date.today())
        print("Date", str(d))
        user.bookroom(roomNo, userName, phone, d, nDays)
        print("Successfully booked your room")
        print("*********************************************\n")
    elif n == '3':
        password = input("\nEnter your password -- ")
        if password == "123456789":
            
            user.showInside()
        else:
            print("Incorrect Password!!")
            print("*********************************************\n")
    elif n == '4':
        roomNo = int(input("Please input room number -- "))
        phone = input("Please input your phone number -- ")

        user.leaveRoom(roomNo, phone)
        print("You have successfully leave the hotel")
        # n = int(input("Press 1 to print the slip"))
        # if n == 1:
        #     user.slip(roomNo, userName)
        print("*********************************************\n")
    elif n == '5':
        graph()
        print("*********************************************\n")
    elif n == '6':
        userName = input("Please input your name -- ")
        review = input("Please input your review -- ")
        user.addReview(userName, review)
        print("Review added successfully\n")
        print("*********************************************\n")
    elif n == '7':
        user.seeReview()
        print("*********************************************\n")
    # elif n == '8':
    #     roomNo = int(input("Please input room number -- "))
    #     userName = input("Please input your name -- ")
    #     user.slip(roomNo, userName)
    #     print("*********************************************\n")
    elif n=="8":
                        print(" ")
                        print("\n"
                              "      \n"
                              "          ##======================================================##\n"
                              "          ||                      THANK YOU                       ||\n"
                              "          ##======================================================##\n"
                              "\n")
                        print('''

    DEVELOPED BY MOHD. BILAL, ANKIT YADAV, DEVANSH DADVAL, KESHU KUMAR, SACHIN GAUR OF CLASS 12TH SCIENCE
                        ''')
                        break
