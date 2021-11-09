"""
Your module description
"""
userReplay = input("would you like to buy stamps, buy an envelope, or make a copy?) ")
if userReplay == "stamps":
    print("we have many stamp design to choose from.")
elif userReplay == "envelop":
    print("we have many envolope sizes to choose from.")
elif userReplay == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("here are {} copies.".format(copies))
else:
    print("thank you, please come again.")
    
    
