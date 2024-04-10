##Prints name, age, City, and State. You then turn it into a sentence. ##

print ("Hello World!")
name = "Luke"
age = int(42)
City = "Spokane"
State = "Washington"
print("My name is " +name+ "I am " +str(age)+ " Years old")
print("I am from " +City+ "in the state of " +State)

## This next line loops through numbers 1 through 100 and prints every third number ##
for i in range(1, 100, 3):
  print(i)


 ##For the sake of practice, This line of code asks if one is happy with their current place in life and gets an answer. ##
  name =input("Enter your name")
  print("Welcome " +name)
  job =input("What do you do for a living?")
  print("That's a good choice.")
  choice =input("Are you happy with it?")
  if choice == "Yes":
    print("It's great to love what you do.")
  elif choice == "No":
    print("That's okay. There's plenty of opportunities out there to pursue.")
  else:
    print("If you're undecided, sometimes these decisions take time.")

