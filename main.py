from test/circletesttools import circleclusters


if __name__ == '__main__':

    read_from_file = True

    if read_from_file:

        filename = 'input/example1.txt'
        coordinates = coordinates_from_file(filename)

    else:
        coordinates = [
            (0.5, 0.5, 0.5),
            (1.5, 1.5, 1.1),
            (0.7, 0.7, 0.4),
            (4.0, 4.0, 0.7),
        ]

    compute_largest_of_clusters(coordinates)