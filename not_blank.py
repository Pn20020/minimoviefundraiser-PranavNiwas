# functions go here 

# checks that the user response is not blank 
def not_blank(question):

  while True:
    response = input(question)

    # if the response if blank output an error
    if response == "":
      print("Sorry this cant be blank please enter your name!")
    else:
        return response 

# main routine goes here 
while True:
  name = not_blank("Enter your name (or 'xxx' to quit) ")
  if name == 'xxx':
    break 


print("we are done")