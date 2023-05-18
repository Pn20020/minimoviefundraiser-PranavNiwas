# main routine goes here

# set maximum number of tickets below
Max_Tickets = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < Max_Tickets:
  name = input("Please enter your name or 'xxx' to quit: ")

  if name == 'xxx':
    break

  tickets_sold += 1

# output number of tickets sold
if tickets_sold == Max_Tickets:
  print("Congratulations you sold all the tickets")
else:
  print("You have sold {} ticket.    There is {} more tickets remaning".format(
    tickets_sold, Max_Tickets - tickets_sold))
