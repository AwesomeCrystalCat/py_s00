bkpr = "BRIDGEKEEPER: "
print(bkpr + "Stop.\nWho would cross the Bridge of Death must answer "
      + "me these questions three.")
name = input(bkpr + "What is your name?\n")
quest = input(bkpr + "What is your quest?\n")
color = input(bkpr + "What is your favorite color?\n")
print("-" * 10)
print("Traveler info:")
print(f"Your name is {name}")
print(f"Your quest is {quest}")
print(f"Your favorite color is {color}")
print("-" * 10)
print(bkpr + "Right. Off you go.")
