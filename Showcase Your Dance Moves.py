# Task 1 Code Correction

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!") # this line needs to be indented
else:
    print("Take an umbrella!") # this line needs to be indented


# Task 2 Your Mood Today

# step 1 figure out how to use the input function
# step 2 incorporate the input function into the code
# step 3 figure out the order in which to code the lines

mood = ["happy", "sad"]

user_mood = input("Please tell us your mood today:")
print("Your mood today is: " + user_mood)

if user_mood == "happy":
    print("That's great to hear!")
else:
    print("I hope your day gets better!")