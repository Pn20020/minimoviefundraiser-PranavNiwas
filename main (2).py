import pandas
# ask user if they want instructions
import pandas as pandas
import random

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
      print("Please choose a method of payment and enter your age (must be over 12 to watch) " 
      "  For kids under 16 payment is $7.50 for under 65 the ticket cost is $10.50 for over 65 the ticket cost is $6.50 please keep in mind that using credit as a method of payment has a 53c surcharge ")
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

# currency formating function
def currency(x):
    return "${:.2f}".format(x)

# set maximum number of tickets below
Max_Tickets = 3
tickets_sold = 0

# dictionaries to hold ticket details
all_name = []
all_ticket_cost = []
all_surcharge = []

mini_movie_dict = {
    "Name": all_name,
    "Ticket Price": all_ticket_cost,
    "surcharge": all_surcharge
}

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


  if pay_method == "cash":
    surcharge = 0
  else:
    # calculate 5% surcharge if users are paying by credit card
    surcharge = ticket_cost * 0.05

  tickets_sold += 1

  # add ticket name, cost and surcharge to lists
  all_name.append(name)
  all_ticket_cost.append(ticket_cost)
  all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit total
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# currency formating (uses currency function)
add_dollars = ['Ticket Price', 'surcharge', 'Total', 'Profit']
for var_item in add_dollars:
  mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# choose a winner from our name list
winner_name = random.choice(all_name)

# get position of winner name in list
win_index = all_name.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

print("---Ticket data ---")
print()

# output table with ticket data
print(mini_movie_frame)

print()
print("----- Ticket Cost / Profit -----")

# output total ticket sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit : ${:.2f}".format(profit))

print()
print('---- Rafle Winner ----')
print("Congratulations {}. You have won ${} ie: your "
     "ticket is free".format(winner_name, total_won))

# output number of tickets sold
if tickets_sold == Max_Tickets:
  print("Congratulations you have sold all the tickets!!!")
else:
  print("You have sold {} ticket.    There is {} more tickets remaning".format(
    tickets_sold, Max_Tickets - tickets_sold))