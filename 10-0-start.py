# Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return f"Please fill in both name fields."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"The name is {formated_f_name} {formated_l_name}."
    

print(format_name(input("What is your first name? ").lower(), input("What is your last name? ").lower()))
















# nest_dict_in_list = [
#     {
#         "Monday": "Blue",
#         "Tuesday": "Green",
#         "Wednesday": "Orange",
#         "Thursday": "Purple",
#         "Friday": ["Brown", "Black", "White", "Yellow"],
#         "Sunday": 5,
#     },
#     {
#         "Umpire": "Man",
#         "Referee": "Woman",
#         "Judge": {
#             "Abia": 2,
#             "Enugu": 3,
#             "Ekiti": 1,
#             "Jos": 5, 
#         }
#     },
#     [
#         "State", "Federal", "Local"
#     ]
# ]

# print(nest_dict_in_list)