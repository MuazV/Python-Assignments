
print("\t *** Hello! Welcome to the Coronavirus Risk Analyze Program \n"
"\tGive answer only True and False. True means = Yes, False means = No***")
    
age = input("Are you a cigarette addict older than 75 years old? : ")
chronic = input("Do you have a severe chronic disease? : ")
immune = input("Is your immune system too weak? : ")
risk = age and chronic and immune
print(risk)

  