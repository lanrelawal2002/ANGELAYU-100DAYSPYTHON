
class Person:
    def __init__(self, user_id, user_name, user_country):
        self.user_id = user_id
        self.user_name = user_name
        self.user_country = user_country
        self.followers = 0
        self.following = 0

    def follow_someone(self, exp1, exp2):
        # print("modifying corresponding user information")
        # self.followers += 15
        # self.following += 39
        # place_name = self.user_name
        # self.user_name = place_name + " **modified"
        self.following += 1
        exp1.followers += 1
        exp1.user_country = "country changed as proof of followership"
        exp2.user_name = "name changed as proof of followership"

# user_one = User(1, "Joe Thomas", "Canada")
# print(user_one.user_name)
# print(user_one.following)
# print(user_one.followers)
# user_one.follow_someone()
# print(user_one.user_name)
# print(user_one.following)
# print(user_one.followers)


user_one = Person(11, "Matthew", "Italy")
user_two = Person(22, "James", "Canada")
user_three = Person(33, "Vincent", "Angola")
user_four = Person(44, "Carlos", "Mauritius")

print(user_three.followers)
print(user_three.following)
print(user_three.user_country)
print(user_one.followers)
print(user_one.following)
print(user_one.user_country)
print(user_four.user_name)
print("*******")
user_three.follow_someone(user_one, user_four)
print(user_three.followers)
print(user_three.following)
print(user_three.user_country)
print(user_one.followers)
print(user_one.following)
print(user_one.user_country)
print(user_four.user_name)
