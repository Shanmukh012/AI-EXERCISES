#PROBLEM 1
#1.Create a variable called major and use it to store the name of your major.
major=("ARTIFICIAL INTELLIGENCE")
#2.Create a variable called tacosRating. Assign an integer between 0 and 10 that reflects your feelings about tacos.
tacosRating=7
#3.Create another variable called sleepRating and assign an integer value between 0 and 10 that reflects how much you like sleep.
sleepRating=9
#4.Test that this code works by running it and printing out the values of your variables in the console (not in the file itself).
print(major)
print(tacosRating)
print(sleepRating)

#PROBLEM 2
#1.Use the input() function to store the user's first name in a variable called first_name.
first_name=input("Enter First name:")
#2.Use the input() function again to store the user's last name in a variable called last_name.
last_name=input("Eneter Last name:")
#3.Use the + operator to combine the two variables that you created and store the result in a variable called full_name.
full_name=first_name+last_name
print(full_name)

#PROBLEM 3
#1.Use the + operator to combine the two variables that you created and store the result in a variable called full_name.
print(type(major))
print(type(tacosRating))
print(type(sleepRating))
print(type(first_name))
print(type(last_name))
#2.Calculate the average of the tacosRating and the sleepRating.
avg=(tacosRating+sleepRating)/2
print(avg)
#3.Calculate the average of the tacosRating and the sleepRating.
print("My name is",first_name,"and I give tacos a score of",tacosRating,"out of 10! I am",full_name,"and my sleeping enjoyment rating is",sleepRating,
      " / 10! Based on the factors above, my happiness rating is" ,avg,"out of 10,or",avg*10," %!")