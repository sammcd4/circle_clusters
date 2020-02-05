from circleclusters import c_tuples_from_file, compute_largest_of_clusters


if __name__ == '__main__':

    read_from_file = False

    if read_from_file:

        filename = 'tests/input/example1.txt'
        c_tuples = c_tuples_from_file(filename)

    else:
        c_tuples = [(1.0, 1.0, 1.0),
                    (3.0, 1.0, 1.0),
                    (5.0, 1.0, 1.0)]

    compute_largest_of_clusters(c_tuples)
