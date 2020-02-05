# circle_clusters

Solution to the following problem:

Given a set of circle coordinates, remove the smallest overlapping circles in a cluster. A cluster is a group of circles that in contact with each other.

The entry Python script to the algorithm is circleclusters.compute_largest_of_clusters. An example case can be found in main.py, showing how to initialize the c-tuple list either directly or by importing from a file. There are also 20+ test cases covering the basic functionality of the script and containing classes.

As demonstrated in main.py, a typical use case is as follows:

tuples = [(1.0, 1.0, 0.4),
          (1.0, 0.8, 0.7),
          (5.8, 7.0, 0.5),
          (0.8, 0.7, 0.6)]


print(c_tuples)

output = compute_largest_of_clusters(c_tuples)

print(output)
