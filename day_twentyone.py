# Class Inheritance
# Chef and PastryChef classes demonstrating inheritance in Python
# Methods for Chef bake(),stir(),measure()
# PastryChef inherits from Chef and adds decorate(),knead(),whsk()

class Animal:
  def __init__(self):
    self.num_eyes = 2

  def breathe(self):
    print("Inhale... Exhale...")

class Fish(Animal):
  def __init__(self):
    super().__init__()

  def breathe(self):
    super().breathe()
    print("The fish is breathing underwater.")

  def swim(self):
    print("The fish is swimming.")

nemo = Fish()
nemo.swim()  
nemo.breathe()
print(f"Nemo has {nemo.num_eyes} eyes.")