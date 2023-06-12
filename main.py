# ask user if they want instructions
def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower().strip()
    # assess input
    if response == "yes" or response == "y":
      response = "yes"
      print("Program continues")
      return response

    elif response == "no" or response == "n":
      response = "no"
      print("Display instructions")
      return response

  else:
    print("please enter yes or no")
    return response

question = yes_no("Have you read the instructions")

# checks that the user response is not blank
def not_blank(question):

  while True:
    response = input(question)

    # if the response if blank output an error
    if response == "":
      print("Sorry this cant be blank please enter your name!")
    else:
        return response

# checks users enter an integer to a given question
def num_check(question):

  while True:

    try:
        response =  int(input(question))
        return response

    except ValueError:
        print("Please enter an integer.")

# calculate the ticket price based on their age
def calc_ticket_price(var_age):

  # ticket is $7.50 for users under 16
  if var_age < 16:
      price = 7.5

  # ticket is $10.50 for users between 16 and 64
  elif var_age < 65:
    price = 10.5

  # ticket is $6.50 for 65 and over
  else:
      price = 6.5

  return price

def String_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# main routine starts here
payment_list = ["cash", "credit"]

for case in range(0, 1):
    pay_method = String_checker("Choose your method of payment (cash / credit)",
                                2, payment_list)
    print("You chose", pay_method)


# set maximum number of tickets below
Max_Tickets = 3
tickets_sold = 0

# loop to sell tickets
while tickets_sold  < Max_Tickets:
  name = not_blank("Enter your name (or 'xxx' to quit) ")

  if name == 'xxx':
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

  # calculate ticket cost
  ticket_cost = calc_ticket_price(age)
  print("Age: {}, ticket price: ${:.2f}".format(age, ticket_cost))

  tickets_sold += 1

# output number of tickets sold
if tickets_sold == Max_Tickets:
  print("Congratulations you have sold all the tickets!!!")
else:
  print("You have sold {} ticket.    There is {} more tickets remaning".format(
    tickets_sold, Max_Tickets - tickets_sold))

