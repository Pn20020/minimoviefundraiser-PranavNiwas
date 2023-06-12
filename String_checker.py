# functions go here 
def cash_credit(question):

  while True:
    response = input(question).lower()

    if response == "cash" or response == "ca":
        return "cash"

    elif response == "credit" or response == "cr":
        return response 

    else:
        print("Sorry that is not a valid method of payment, Please choose cash (ca) or credit card (cr)")


# main routine goes here 
while True:
    payment_method = cash_credit("Choose a payment method (cash "
                                "or credit):  ")

    print("You choose", payment_method)

    print("program continues...")
    print()