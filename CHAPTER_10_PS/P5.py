import random

class train:

  def __init__(self, train_no):
    self.train_no = train_no

  def book(self, from_station, to_station):
        print("Your ticket is booked from", from_station, "to", to_station, "on train number", self.train_no)
        

  def get_status(self):
        print("The train number", self.train_no, "is on time.")

  def fare(self):
        print("The fare for train number", self.train_no, "is", random.randint(200,500), "INR.")

t = train(random.randint(10000,99999))
t.book("Delhi", "Mumbai")
t.get_status()
t.fare()

