import pandas
import random 

# list to hold ticket details 
all_name = ["a", "b", "c", "d", "e"]
all_ticket_cost = [7.50, 7.50, 10.50, 10.50, 6.50,]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_name,
    "Ticket Price": all_ticket_cost, 
    "surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# choose a winner from our name list 
winner_name = random.choice(all_name)

# get position of winner name in list
win_index = all_name.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at the end (before printing)
mini_movie_frame =  mini_movie_frame.set_index('Name')
print(mini_movie_frame)

print()
print('---- Rafle Winner ----')
print("Congratulations {}. You have won ${} ie: your "
     "ticket is free".format(winner_name, total_won))