# from hashlib import new

class Car(object):
  def __init__(self,model,color,company,speed_limit) :
      self.c = color
      self.model = model
      self.company = company
      self.speed_limit =speed_limit


  def start(self):
    print("started") 

  def accelarate(self):
    print("accelarating...")
  # "accelarator functionality here"

  def change_gear(self, gear_type):
    print("gear changed")
    # " gear related functionality here"


lamborgini = Car("Aventador","black",'lamborgini',300)
print(lamborgini.c)
# print(lamborgini.model)
# print(lamborgini.accelarate())


  

# class Car(object):
#   """
#     blueprint for car
#   """

#   def __init__(self, model, color, company, speed_limit):
#     self.color = color
#     self.company = company
#     self.speed_limit = speed_limit
#     self.model = model

#   def start(self):
#     print("started")

#   def stop(self):
#     print("stopped")

#   def accelarate(self):
#     print("accelarating...")
#     "accelarator functionality here"

#   def change_gear(self, gear_type):
#     print("gear changed")
#     " gear related functionality here"


# audi = Car("A6", "red", "audi", 80)

# print(audi.start())
# # print(audi.color)
# # print(audi.speed_limit)