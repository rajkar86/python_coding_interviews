# 1041. Robot Bounded In Circle
 
# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

# Example 1:

# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.


instructions = "GGLLGG"

def isRobotBounded(instructions: str) -> bool:

  x, y = 0, 0
  vx, vy = 0, 1

  for i in instructions:
    if i == 'G':
      x, y = x + vx, y + vy
    elif i == 'L':
      vx, vy = -vy, vx
    elif i == 'R':
      vx, vy = vy, -vx

  return((x==0 and y==0) or not (vx == 0 and vy == 1))

    
print(isRobotBounded(instructions))
