import re


class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_email(self):
        regular = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regular, self.email):
            print("Valid email")
        else:
            print("Invalid email")

    def check_password(self):
        regpass = '^[a-z0-9]+[$*_]?[a-z0-9]'
        if 6 < len(self.password) < 20:
            if re.search(re.compile(regpass), self.password):
                print("Valid password")
        else:
            print("Invalid password")

    def show_info(self):
        print("email: ", self.email)
        print("password: ", self.password)
