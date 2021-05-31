# Small programme to check if its a leap year or not
year = int(input("Which year do you want to check? "))

## There are different methods to check if given year is leap year or not.

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
       print("Leap year")
    else:
      print("Not leap")
  else:
    print("Leap year")
else:
  print("Not Leap")
