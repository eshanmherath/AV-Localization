# Inspired by Self-Driving-Car Nano Degree from Udacity


# Assume a 1D world with 5 states
# Robot doesnt know where it is.
# Assume the world is Cyclic

# Prior Probabilities
p = [0.2, 0.2, 0.2, 0.2, 0.2]

# World State
world = ['green', 'red', 'red', 'green', 'green']

# Now Robot gets a series of measurements
Z = ['red', 'green']

motion = [1, 1]  # 1 means move to right

"""
In other words, think 
Robot sees red
Move 1
Robot sees green
Move 1
Now whats the posterior distribution
"""

# We define these
p_hit = 0.6
p_miss = 0.2

p_exact = 0.8
p_overshoot = 0.1
p_undershoot = 0.1


def sense(p, z):
    q = []
    for p1, w1 in zip(p, world):
        if w1 == z:
            q.append(p1 * p_hit)
        else:
            q.append(p1 * p_miss)

    # To make q a proper probability distribution, we normalize it
    summation = sum(q)

    q = [i / summation for i in q]

    return q


# We get the posterior distribution (given the fact that Robot has observed a measurement)

# for current_z in Z:
#     posterior = sense(p, current_z)
#     print(posterior)
#     p = posterior


# Move
# U is the number of steps to be taken by the robot ( U can be zero positive or negative integer)
def move(p, U):
    q = []
    for i in range(len(p)):
        s = p_exact * p[(i - U) % len(p)]
        s = s + p_overshoot * p[(i - U - 1) % len(p)]
        s = s + p_undershoot * p[(i - U + 1) % len(p)]
        q.append(s)

    return q


n_steps = 200

print(f"Before Move: {p}\n")
for measurement, motion_value in zip(Z, motion):
    p = sense(p, measurement)
    print(f"After Measurement {measurement}: {p}")
    p = move(p, 1)
    print(f"After Move {motion_value}: {p}\n")

message = """
Looking at the world and the two measurements, Red and Green, we can see that the most
probable the Robot would have started is 3rd grid-cell.
If that was the case, then after two moves, the Robot should now be in 5th Gird-Cell.
When we look at the final posterior probability, we see that Robot think so too,
as the probability value of the 5th grid-cell is the highest indicating that Robot
thinks with a higher confidence that it's current location is grid-cell 5 
"""

print(message)
