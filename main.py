from circleclusters import c_tuples_from_file, compute_largest_of_clusters


# simple example showing the entry point to the compute_largest_of_clusters algorithm
if __name__ == '__main__':

    read_from_file = True

    if read_from_file:

        filename = 'tests/input/example3.txt'
        c_tuples = c_tuples_from_file(filename)

    else:
        c_tuples = [(1.0, 1.0, 0.4),
                    (1.0, 0.8, 0.7),
                    (5.8, 7.0, 0.5),
                    (0.8, 0.7, 0.6)]

    c_tuples.reverse()
    print(c_tuples)
    output = compute_largest_of_clusters(c_tuples)
    print(output)
