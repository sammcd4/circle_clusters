from circleclusters import c_tuples_from_file, compute_largest_of_clusters


if __name__ == '__main__':

    read_from_file = False

    if read_from_file:

        filename = 'tests/input/example1.txt'
        coordinates = c_tuples_from_file(filename)

    else:
        coordinates = [
            (0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (0.5, 0.5, 0.4),
            (0.5, 0.5, 0.1),
        ]

    compute_largest_of_clusters(coordinates)