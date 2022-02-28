from art import logo,vs
from game_data import data
import random
from replit import clear

#Art
print(logo)
score = 0
#Format data
def format_data(account):
  account_name = account["name"]
  account_discr = account["description"]
  account_country = account["country"]
  return(f"{account_name}, a {account_discr}, from {account_country}")


#Check
def check_answer(guess, a_follwers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
account_b = random.choice(data)
    
game_should_continue = True  
while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  print(f"Compare A: {format_data(account_a)}")  
  
  print(vs)
  
  print(f"Against B : {format_data(account_b)}") 
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_followers =account_a ["follower_count"]
  b_followers =account_b ["follower_count"]
  is_correct = check_answer(guess, a_followers, b_followers)
  
  clear()
  print(logo)
  if is_correct:
    score += 1
    print(f"You're right! Current score:{score} .")
    
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score:{score}")