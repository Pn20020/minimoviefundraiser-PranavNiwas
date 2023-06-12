# checks that users enter a valid response (eg yes / no
# cash / credit) based on a list of options
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

  