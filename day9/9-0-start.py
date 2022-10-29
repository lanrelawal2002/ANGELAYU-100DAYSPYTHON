
# my_dictionary = {
#     "python": "my very first programming language",
#     "html": "markup language after python",
#     "css": "cascading style sheet"
# }

# # print(my_dictionary)
# # print(my_dictionary["python"])

# my_dictionary["javascript"] = "my second programming language"
# # print(my_dictionary)

# # empty_dictionary = {}
# # empty_dictionary["red"] = "fire, blood or anger"
# # empty_dictionary["blue"] = "sky and water"
# # print(empty_dictionary)

# my_dictionary["python"] = "my first OOP language"
# # print(my_dictionary)

# for key in my_dictionary:
#     print(key)
#     print(my_dictionary[key])
# # print(my_dictionary)

# ************************************************************************

# travel_log = {
#     "France": {"cities_visited": ["Lyon", "Nice", "Lille"], "number_of_visits": 12},
#     "Nigeria": {"cities_visited": ["Benin", "Ikeja", "Jos"], "days_spent": 25}
# }

# print(travel_log)


travel_log2 = [
    {
        "country": "Nigeria",
        "cities_visited": ["Ibadan", "Calabar", "Kano", "Jos"],
        "time_of_visits": {
            "Wednesday": "5:15pm",
            "Saturday": "11:18am",
            "Friday": "3:04pm"
        }
    },
    {
        "country": "England",
        "cities_visited": ["Stoke", "Manchester", "Wigan"],
        "number_of_visits": 12
    },
    [
        "visa", "passport photo", "ID"
    ],
    {
        "course": "SQL and Databases",
        "instructor": "Andrei Neagoie",
        "students": 27814
    }
]

# print(travel_log2)
# print(travel_log2[1]["cities_visited"][0])
print(travel_log2[0]["time_of_visits"]["Saturday"])

# for item in travel_log2[2]:
#     print(item)