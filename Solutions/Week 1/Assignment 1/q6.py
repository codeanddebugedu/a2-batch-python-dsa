"""
Ask number of games played in a tournament. 
Ask the user number of games won and number of games loss. 
Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)
"""

total_games = int(input("Enter the total number of games played in the tournament = "))

wins = int(input("Enter the number of games won = "))

losses = total_games - wins

ties = total_games - wins - losses

total_points = wins * 4 + ties * 2

print(f"Number of games tied = {ties}")
print(f"Total points earned = {total_points}")
