# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_low = name1.lower()
name2_low = name2.lower()
# testing for "true"
t_name1 = name1_low.count("t")
t_name2 = name2_low.count("t")

r_name1 = name1_low.count("r")
r_name2 = name2_low.count("r")

u_name1 = name1_low.count("u")
u_name2 = name2_low.count("u")

e_name1 = name1_low.count("e")
e_name2 = name2_low.count("e")

first_dg = (t_name1 + t_name2 + r_name1 + r_name2 + u_name1 + u_name2 + e_name1 + e_name2)
# print(first_dg)
# testing for "love"

l_name1 = name1_low.count("l")
l_name2 = name2_low.count("l")

o_name1 = name1_low.count("o")
o_name2 = name2_low.count("o")

v_name1 = name1_low.count("v")
v_name2 = name2_low.count("v")

e_name1 = name1_low.count("e")
e_name2 = name2_low.count("e")

second_dg = (l_name1 + l_name2 + o_name1 + o_name2 + v_name1 + v_name2 + e_name1 + e_name2)
# print(second_dg)

score = int(f"{first_dg}{second_dg}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else: 
    print(f"Your score is {score}.")