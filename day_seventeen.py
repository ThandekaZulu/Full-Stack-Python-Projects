class User:
  def __init__(self,user_id,username):
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self,user): # object = self
    user.followers += 1
    user.following += 1

user_1 = User("001", "Thandeka") # PascalCase for class naming
user_2  = User("002","Toto")
# print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)




# print(user_1.id)
# user_1.id = "001"
# user_1.username = "Sgwili"

# print(user_1.username)

# user_2 = User() # PascalCase for class naming
# user_2.id = "002"
# user_2.username = "Toto"