# import os
#
# # Create a subdirectory for the Christmas cards
# output_folder = "Cards"
# os.makedirs(output_folder, exist_ok=True)
#
# # Read the names from the file
# with open("names.txt", "r") as names_file:
#     names = names_file.read().splitlines()
#
# # Read the template
# with open("template.txt", "r") as template_file:
#     template = template_file.read()
#
#
# for name in names:
#     card_content = template.replace("NAME", name)
#
#
#     card_filename = os.path.join(output_folder, f"{name}.txt")
#     with open(card_filename, "w") as card_file:
#         card_file.write(card_content)
#
#
# # Save the output in a file
# output_filename = os.path.join(output_folder)
# with open(output_filename, "w") as output_file:
#     for name in names:
#         output_file.write(f"{name}.txt")
#


import os


output_folder = "Cards"


with open("names.txt", "r") as names_file:
    names = names_file.read().splitlines()

with open("template.txt", "r") as template_file:
    template = template_file.read()


for name in names:

    card = template.replace("NAME", name)
    card_name = os.path.join(output_folder, f"{name}.txt")

    with open(card_name, "w") as card_file:
        card_file.write(card)


output_card = os.path.join(output_folder)
with open(output_card, "w") as output_file:
    for name in names:
        output_file.write(f"{name}.txt")



