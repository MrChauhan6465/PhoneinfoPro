import phonenumbers 
from phonenumbers import geocoder,carrier,timezone 


print("Welcome to phone_numbers_details getter ")

def phone_details_getter(number):

    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)

    car = carrier.name_for_number(phone,'en')

    registration = geocoder.description_for_number(phone,'en')

    print(" \n The following are the details for your number ")

    print(f"\n{phone} ,\n{time},\n{car},\n{registration}")
       
while True:   
    user_number = input("Enter the number (with +__) (enter 'stop' to quit): ")

    if user_number == "stop":
        break
    else:
        phone_details_getter(user_number)   