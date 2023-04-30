from Classes.login import Login
from Classes.selection_ticket import Selection_Ticket
from Classes.reserv import Reserv

email = input("enter your mail:")
password = input("enter your password:")

l1 = Login(email, password)
l1.check_email()
l1.check_password()
l1.show_info()

date = input("Enter selected date: ")
destination = input("Enter selected destination: ")
origin = input("Enter selected origin: ")
count = int(input("Enter selected count: "))

s1 = Selection_Ticket(date, destination, origin, count)
s1.show_ticketinfo()

Firstname = input("Enter selected Firstname: ")
Lastname = input("Enter selected Lastname: ")
Date_of_birth = input("Enter selected Date of birth: ")
National_Code = int(input("Enter selected National Code: "))


for x in range(0, count, 1):
    x = Reserv(Firstname, Lastname, Date_of_birth, National_Code)
    x.show_forminfo()


s1.show_cost()
