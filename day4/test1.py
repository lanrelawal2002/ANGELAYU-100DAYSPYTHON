import random

lanny_list = ["linux", "hacking", "python", "web development", "security"]
print(lanny_list)

lanny_list_2 = ["VS CODE", "VIRTUALBOX", "UBUNTU"]
lanny_list.extend(lanny_list_2)
print(lanny_list)

lanny_list_3 = ["research", "critical thinking", "problem solving"]
lanny_list.extend(lanny_list_3)
print(lanny_list)

print(random.choice(lanny_list))



# sentence1 = "Python is great"
# sent_as_list = sentence1.split()
# print(sent_as_list)

# movie_full = "Age, of, Ultron"
# movie = movie_full.split(", ")
# print(movie)
