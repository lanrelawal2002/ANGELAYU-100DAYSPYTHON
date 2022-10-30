# my code for project 9-2-Dictionary-in-list

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(first_par, second_par, third_par):
    new_dictionary = {
        "country": first_par,
        "visits": second_par,
        "cities": third_par,
    }

    travel_log.append(new_dictionary)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)