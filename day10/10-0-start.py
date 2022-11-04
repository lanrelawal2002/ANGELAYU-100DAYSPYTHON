# Functions with Outputs
# And practicing Docstrings

def format_name(f_name, l_name):
    """A function that takes the first and last name and converts
    them into a title case version."""
    if f_name == "" and l_name == "":
        return f"Please fill in both name fields."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"The name is {formated_f_name} {formated_l_name}."
    

print(format_name(input("What is your first name? ").lower(), input("What is your last name? ").lower()))


# def string_concat(first_name, last_name):
#     """A function that prints GP's first name and last name only."""
#     print(f"The full name is {first_name} {last_name}.")

# string_concat("Gerard", "Pique")

# counter = len("profiler")


# REVIEWE OF NESTING DICTIONARIES AND LISTS IN A LIST

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