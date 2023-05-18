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

