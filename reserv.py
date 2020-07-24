import datetime
import re


class Reserv:
    def __init__(self, Firstname, Lastname, Date_of_birth, National_Code):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Date_of_birth = Date_of_birth
        self.National_Code = National_Code

    def show_forminfo(self):
        print("your name:", self.Firstname, self.Lastname)
        print("your Date of birth:", self.Date_of_birth)
        print("your National Code:", self.National_Code)

    def check_National_Code(self, National_Code):
        regcode = '^[0-9]'
        if len(National_Code) == 6:
            if re.search(regcode, self.National_Code):
                print("Valid National_Code")
        else:
            print("Invalid National_Code")
