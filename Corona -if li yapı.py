age =  True
chronic =  False
immune =  True
risk = age and chronic or immune
if risk == True:
    print("You are in risky group")
else:
    print("You are not in risky group")