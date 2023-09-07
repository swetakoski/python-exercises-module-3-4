
#Module 3 question 1

# size_limit=42
# zander_length=float(input("Enter the length of the Zander in centimeters: "))
# if zander_length>=size_limit:
#     print("Congratulations! The Zander meets the size limit")
# else:
#    centimeters_below_limit=size_limit-zander_length
#    print(f"The Zander is {centimeters_below_limit: .2f} centimetres below the size limit")
#    print("Print release the fish back into the lake.")

#Module 3 question 2
# cabin_class=input("Enter the cabin class (LUX, A, B, or C): ")
# if cabin_class == 'LUX':
#     print("You have selected a LUX cabin: upper deck cabin with a balcony")
# elif cabin_class == 'A':
#     print("You have selected A cabin: above the car deck equipped with a window.")
# elif cabin_class == 'B':
#     print("You have selected B cabin: windowless cabin above the car deck.")
# elif cabin_class =='C':
#     print("You have selected C cabin: windowless cabin below the car deck. ")
# else:
#     print("Invalid cabin class: Please enter one of the valid options (LUX, A, B, or C) ")

#Module 3 question 3
# normal_ranges={
#     "male":[134, 167],
#     "female":[117, 155]
# }
# lower_range={
#     "male":'134',
#     "female":'117'
# }
# upper_range={
#     "male":'167',
#     "female":'155'
#
# }
#
# gender=input("Enter you gender (male/female): ").lower()
# hemoglobin_value=float(input("Enter your hemoglobin value (g/l): "))
# lower_range, upper_range == normal_ranges[gender]
#
# if hemoglobin_value < lower_range :
#     print ("Your Hemoglobin is low. ")
# elif hemoglobin_value>= normal_ranges<= upper_range :
#     print("Your hemoglobin is normal. ")
# else:
#     print("Your hemoglobin value is high: ")

#module 3 question 4
# year=int(input("Enter a year: "))
# if(year % 4 ==0) or (year % 100==0 and year % 400 == 0):
#     print(f"{year} is a leap year. ")
# else:
#     print(f"{year} is not a leap year: ")

#module 4 question 1
# number=1
# while number in range (1, 1000):
#     if number%3==0:
#         print(number, end="\n")
#     number=number+ 1



#module 4 question 2
# def inch_to_cm(inch):
#     return inch * 2.54
#
# while True:
#      inch_value=float(input("Enter a length in inches: "))
#      if inch_value < 0:
#          print("Program Terminated. ")
#          break
#      print(f"{inch_value} inches is equal to {inch_to_cm (inch_value)} centimeters.")

#module 4 question 3
#
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#        break
#
#     try:
#      ifnum=num
#     except:
#      print("Invalid number. ")
#
#     if largest is None:
#      largest=num
#     elif largest<num:
#      largest=num
#     if smallest is None:
#      smallest=num
#     elif smallest>num:
#      smallest=num
# print("Maximum is :", largest)
# print("Minimum is :" , smallest)




#module 4 question no. 4

# import random
# random_number=random.randint(1, 10)
# print(random_number)
# while True:
#      guess_number=int(input("Guess the number between 1 and 10:  "))
#      if random_number == guess_number:
#          print("Correct! You win. ")
#          break
#      elif random_number>guess_number:
#          print("Too low! Try again. ")
#      else:
#          print("Too high! Try again. ")

#module 4 question 5
# correct_username="python"
# correct_password="rules"
# user=input("Enter you username: ")
# password=input("Enter your password: ")
# attempt=0
# if user!=correct_username and password!=correct_password:
#         attempt = attempt + 1
# while attempt<5:
#     if user != correct_username and password != correct_password:
#         user=input("Enter your username: ")
#         password=input("Enter your password: ")
#         attempt=attempt +1
#
#     elif user==correct_username and password==correct_password:
#         print("Welcome! ")
#         break
#
# if attempt>=5:
#    print("Access denied. You have exceeded the login attempts. ")
