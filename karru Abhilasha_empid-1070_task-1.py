#Asking user detials
name = input("Enter your Name: ")
age = int(input("Enter your Age:"))
city = input ("Enter your City:")
fav_Subj = ("Enter your Favourite Subject:")
#calculating birth year
birth_year = 2026-age
#creating a profile card using detials
print("\n=======PROFILE CARD=======")
print(f"NAME : {name}")
print(f"AGE : {age} ")
print(f"CITY : {city}")
print(f"FAVOURITE SUBJECT : {fav_Subj}")
print(f"BIRTH YEAR : {birth_year}")
print("============================")