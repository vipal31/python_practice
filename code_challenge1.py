print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
bill = 0
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == 'S' or size == 's':
  bill = 15
  if add_pepperoni == 'Y' or 'y':
    bill += 2
elif size == 'M' or size == 'm':
  bill = 20
  if add_pepperoni == 'Y' or 'y':
    bill += 3
else:
  bill = 25
  if add_pepperoni == 'Y' or size == 'y':
    bill += 3

if extra_cheese == 'Y' or 'y':
  bill += 1

print(f"your final bill is {bill}")
