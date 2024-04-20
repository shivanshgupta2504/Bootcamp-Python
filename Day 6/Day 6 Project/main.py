# See this the code for the maze challenge in Reeborg's World
# Link -> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world.json&url=user_world%3Aproblem_world.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# This block is written to deliberately make
# robot to have a wall on right side at start
while front_is_clear():
    move()
turn_left()

# The secret is to have Reeborg follow along the right edge of the maze,
# turning right if it can, going straight ahead if it can’t turn right,
# or turning left as a last resort.
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
# Problem in this block is if robot has no wall
# at right side at start, then it loops infinitely
