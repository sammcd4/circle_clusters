from circleclusters import Circle, CircleSet

# construct flat list of c-tuples
c_tuples = [
    (0.5, 0.5, 0.5),
    (1.5, 1.5, 1.1),
    (0.7, 0.7, 0.4),
    (4.0, 4.0, 0.7),
]

# construct all circles from c-tuples
circles = CircleSet(c_tuples)

# group the circles into clusters
circles.group()
print(circles.clusters())
print(circles.largest())

# for each cluster, determine the largest circle and return it

# plot the result