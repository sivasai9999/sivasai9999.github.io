import random
def roll():
    min_value=2
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
while True:
    player=input("enter the no of player (2-4): ")
    if player.isnumeric():
        player=int(player)
        if player >=2 and player <=4 :
            break
        else:
            print("must be entered player 2-4")
    else:
        print("invalid ,try again")

max_score = 100
player_scores = [0 for _ in range(player)]

while max(player_scores) < max_score:
    for player_idx in range(player):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)