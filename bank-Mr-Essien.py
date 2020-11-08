
# class App():

#     user_dict = {
#                     1: {
#                         "name" : "paul",
#                         "balance" : 43120,
#                         "age": 29
#                     }  ,
#                     2: {
#                         "name" : "John",
#                         "balance" : 30000,
#                         "age": 30
#                     }  ,
#                     3: {
#                         "name" : "kunle",
#                         "balance" : 24000,
#                         "age": 40
#                     }  ,
#                     4: {
#                         "name" : "destiny",
#                         "balance" : 14000,
#                         "age": 40
#                     }  ,
#                     5: {
#                         "name" : "atha",
#                         "balance" : 13000,
#                         "age": 40
#                     }  ,
#                 }

#     def __init__(self, name = "nil", age = "nil", balance = "nil"):

#         self.name = self.check_user(name)
#         self.age = age
#         self.balance = balance

#     def check_user(self, name):

#         for key in self.user_dict.keys():# Loop through the user dictionary keys using the keys as the iterator
#             data = self.user_dict[key] # reference the dictionary values using the acquired keys

#             if name == data["name"]: #CHECK IF NAME PROVIDED ACTUALLY MATCHES ANY NAME IN THE LIST
#                 print(f"Hello {name} can loggin.")

#                 return name 
#         else:

#             return "No user found"

# new_user = App(name = "atha")

# print(new_user.name)




class User:
    user_dict = {"Essien":["psw123",123000,"saving"], "Jerry":["psw234",10000,"current"],"Fred":["psw345",40000,"saving"]}

    def __init__(self, name, password):
        self.name = self.sign_in(name, password)
        #self.password = password
    
    # Checking if the username and password exist
    def sign_in(self, name, password):
        for key, val in zip(self.user_dict.keys(), self.user_dict.values()):
            if (name == key) & (password in [i for i in val]):
                print(f"{name}, you are welcome to ABC bank")
                return self.check_balance(name)
            else:
                return f"{name} does not exist"
             
    def check_balance(self, name):
        bal = self.user_dict[name][1]
        print(f"Your balance is {bal}")


    # # Testing sign-in
    # def sign_in(self, name, password):
    #     for key, val in zip(self.user_dict.keys(), self.user_dict.values()):
    #         if name == key or password==[i for i in val]:
    #             print(f"{name}, you are welcome to ABC bank")
    #             return self.check_balance(name)
    #         else:
    #             return f"{name} does not exist"



# name_ = input("Enter your username: ")
# password = input("Enter your password: ")

# new_ = User(name_, password)
# new_



user_dict = {"Essien":["psw123",123000,"saving"], "Jerry":["psw234",10000,"current"],"Fred":["psw345",40000,"saving"]}

name = input("Enter name: ")
pwd = input("Enter password: ")

for key, val in zip(user_dict.keys(), user_dict.values()):
    if (name == key) & (pwd in [i for i in val]):
        print(f"{name} with the password {pwd} is in the database")