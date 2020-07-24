import datetime


class Selection_Ticket:
    def __init__(self, date, destination, origin, count):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.count = count

    def show_cost(self):
        print("your cost:", 5000000 * self.count)

    def show_ticketinfo(self):
        print("your path:", self.origin, "to", self.destination)
        print("Selected date:", self.date)
        print("Number of tickets:", self.count)
