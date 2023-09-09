#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# with open("./Input/Names/invited_names.txt", "r") as file:
#     name1 = file.readlines()
#     # print(name1)
#
# name = []
#
# for element in name1:
#     name.append(element.strip('\n'))
#
#
# with open("./Input/Letters/starting_letter.txt") as file:
#     old_text = file.readlines()
#
#     for actual_name in name:
#         final_text = []
#         for lines in old_text:
#             mod = lines.replace("[name]", f"{actual_name}")
#             final_text.append(mod)
#         with open(f"./Output/ReadyToSend/{actual_name}_letter", mode="w") as final_letter:
#             final_letter.writelines(final_text)
#         # print(*final_text)


with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


for name in names:
    actual_name = name.strip()
    with open("./Input/Letters/starting_letter.txt") as sample_letter:
        old_letter = sample_letter.read()
        new_letter = old_letter.replace("[name]", actual_name)
        with open(f"./Output/ReadyToSend/letter_for_{actual_name}.txt", mode="w")as final:
            final.write(new_letter)
