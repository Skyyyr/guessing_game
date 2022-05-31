import random

# Define your GuessingGame class here...
class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.correct = False

    def guess(self, user_guess):
        guess = int(user_guess)
        answer = int(self.answer)
        if guess == answer:
            self.correct = True
        elif guess > answer:
            return "High"
        elif guess < answer:
            return "Low"
    def solved(self):
        return self.correct == True


# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")