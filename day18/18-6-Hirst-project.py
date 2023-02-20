# my version of hirst painting project

## RUNNING THE CODE MAY MAKE VSCODE GET STUCK ##
# leave all COLOR EXTRACTION PORTION of hirst painting project code commented


## START COLOR EXTRACTION PORTION OF HIRST PAINTING ##
# import colorgram
#
#
# def image_color_extractor(number_needed, current_position):
#     all_colors = colorgram.extract('hirst_image.jpg', number_needed)
#     selected_color = all_colors[current_position]
#     rgb = selected_color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#
#     color_tuple = (r, g, b)
#     return color_tuple
#
#
# colors_list = []
# color_number_needed = int(input("How many colors to extract from the image? "))
#
# for digit in range(color_number_needed):
#     item = image_color_extractor(color_number_needed, digit)
#     colors_list.append(item)
#
# print(colors_list)


## END COLOR EXTRACTION PORTION OF HIRST PAINTING ##


project_colors = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
                  (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
                  (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
                  (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
                  (46, 73, 62), (47, 66, 82)]

print(len(project_colors))
