from circleclusters import CircleSet


def compute_largest_clustered_circles(c_tuples):

    # construct all circles from c-tuples
    circles = CircleSet(c_tuples)

    # group the circles into clusters
    circles.group()
    print(circles.clusters())
    print(circles.largest())


if __name__ == '__main__':

    read_from_file = True

    if read_from_file:
        coordinates = []
        with open('input/example2.txt', 'r') as f:
            for line in f:
                current = line.split(',')
                coordinates.append((float(current[0]), float(current[1]), float(current[2])))

    else:
        coordinates = [
            (0.5, 0.5, 0.5),
            (1.5, 1.5, 1.1),
            (0.7, 0.7, 0.4),
            (4.0, 4.0, 0.7),
        ]

    compute_largest_clustered_circles(coordinates)