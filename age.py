# functions go here 

# checks users enter an integer to a given question 
def num_check(question):

  while True:

    try:
        response =  int(input(question))
        return response 

    except ValueError:
        print("Please enter an integer.")


# Main routine goes here 
tickets_sold = 0 

while True: 

  name = input("Enter your name / xxx to quit: ")

  if name == "xxx":
      break

  age = num_check("Age: ")

  if 12 <= age <= 120:
      pass
  elif age < 12:
      print("Sorry you are to young for this moive")
      continue 
  else:
      print("? That looks like a typo please try again ") 
      continue

  tickets_sold += 1 

print("You have sold {} tickets".format(tickets_sold))
      