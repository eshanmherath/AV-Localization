# Inspired by Self-Driving-Car Nano Degree from Udacity


# Assume a 1D world with 5 states
# Robot doesnt know where it is.
# Assume the world is Cyclic

# Prior Probabilities
p = [0, 1, 0, 0, 0]

# World State
world = ['green', 'red', 'red', 'green', 'green']

# Now Robot gets a series of measurements
Z = ['red', 'green']

# We define these
p_hit = 0.6
p_miss = 0.2


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
    # To account for Cyclic Nature
    U = U % len(p)

    q = p[-U:] + p[:-U]

    return q


print(f"Before Move: {p}")
print(f"After Move: {move(p, 1)}")
