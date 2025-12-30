###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp7's 5th&6th excrcise
prompt = f" -----WELCOME TO OUR MOVIE THETRE----- \n         ---ENTER YOUR AGE--- \nSo we can tell you the ticket price \nFor you: "
status = True
#checks the massage 
while status:
    massage = input(prompt).strip()
    massage = int(massage)
    if massage < 4:
        price = 'Free'
    elif massage <= 12:
        price = '$10'
    elif massage > 100:
        print("\n      !!!ENTER A VALID AGE!!! ")
        break
    else:
        price = '$15'
    status = False
#print the price
    print(f"\nYour ticket price is {price}")
    print(f"\n\n\n\n\n\n\n\n                    --Dev SUBHAJIT HORE")