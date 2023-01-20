# class User:
#     def __init__(self):
#         print("pulling out a \"BRAND NEW USER\"")

# user1 = User()
# user1.id = 198_224
# user1.username = "Jerome"
# print(user1.username)

# user2 = User()
# user2.id = 736_050
# user2.username = "Manuel"
# print(user2.id)





# class Company:
#     def __init__(self):
# 	    pass

# bluegate_tech = Company()

# bluegate_tech.city = "Paris"
# bluegate_tech.employees = 18_970
# bluegate_tech.ceo = "Mr. Lanre Lawal"

# print(bluegate_tech.cee)


class Company:
    def __init__(self, ceo, city, employees):
        self.ceo = ceo
        self.city = city
        self.employees = employees
        self.funds = "money"


# company_1
xplorer_intent = Company("Mr. Lanre Lawal", "Berlin", 19_002)
print(f"{xplorer_intent.ceo} heads the {xplorer_intent.city} branch with {xplorer_intent.employees} employees.")


# company_2
replay = True

tesla = Company("Elon Musk", "San Francisco", "25_394")
founder = tesla.ceo
hqtr = tesla.city
goal = tesla.funds

while replay:
    trivia = input("Who founded the company Tesla? ")
    if trivia == founder:
        print(f"You are correct. {founder} did.\nPlus it is headquarterd in {hqtr}.")
    else:
        print(f"You are wrong. It was actually {founder}.")
        print(f"The company still made {goal}")

    rerun = True
    while rerun:
        retry = input("Go again? 'y' or 'n' ")
        if retry == "y":
            rerun = False
        elif retry == "n":
            rerun = False
            replay = False
        else:
            print("enter either 'y' or 'n'")
