import math
def paint_calc(height, width, cover):
    can_number = (height * width) / cover
    can_number_rounded = math.ceil(can_number)
    print(f"You'll need {can_number_rounded} cans of paint.")
    

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
