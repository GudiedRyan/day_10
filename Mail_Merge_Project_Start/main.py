#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as name_source:
    names = name_source.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    template = letter.read()

for name in names:
    name = name.rstrip("\n")
    added_template = template.replace("[name]",name)
    with open(f"Output/ReadyToSend/{name}_invite.txt", mode="w") as product:
        product.write(added_template)


