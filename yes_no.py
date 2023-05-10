# functions go here

# main routine

want_instructions = input("Do you want to read the instructions?").lower()

if want_instructions == "yes" or want_instructions == "y":
  print("instructions go here")
elif want_instructions == "no" or want_instructions == "n":
  pass
else:
  print("Please enter yes/no")

print("we are done")
