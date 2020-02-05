from math import sqrt


class Circle:

    def __init__(self, c_tuple):
        self._c_tuple = c_tuple

        self.cluster = None
        self.largest = True
        self.largestCircle = None

    def __eq__(self, other):
        if self.c_tuple == other.c_tuple:
            return True
        else:
            return False

    @property
    def c_tuple(self):
        return self._c_tuple

    @property
    def x(self):
        return self._c_tuple[0]

    @property
    def y(self):
        return self._c_tuple[1]

    @property
    def r(self):
        return self._c_tuple[2]

    def new_cluster(self, num_clusters):
        num_clusters += 1
        self.cluster = num_clusters
        return num_clusters

    def get_interaction(self, circle2):
        x2 = circle2.x
        y2 = circle2.y
        r2 = circle2.r

        d = sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        smallest_r = min(self.r, r2)
        largest_r = max(self.r, r2)

        if d > abs(self.r + r2):
            # circles are not intersecting or nested
            print('circles are not touching')
            return 'none'
        elif d + smallest_r < largest_r:
            # circles are nested
            print('nested circles')
            # TODO: identical circles get caught here
            return 'nested'
        else:
            return 'intersecting'

    def compare_radius(self, circle2, check_identical=False):
        # prove that this circle is not the largest

        # only compare size within the same cluster
        if self.cluster != circle2.cluster:
            return

        if self.largest:

            # circles of different radii
            if circle2.r > self.r:
                self.largest = False
                self.largestCircle = circle2

            # circles of identical radii
            if check_identical and self == circle2:
                self.largest = False
                self.largestCircle = circle2

        elif self.largestCircle is not None:
            self.largestCircle.compare_radius(circle2)


class CircleSet:

    def __init__(self, c_tuples):
        # Create a list of circles from list of c-tuples
        self.circles = []
        for c_tuple in c_tuples:
            self.circles.append(Circle(c_tuple))

        self.num_clusters = 0

    def update_cluster_info(self, c1, c2):
        interaction = c1.get_interaction(c2)

        if interaction == 'none':
            # circles are not intersecting or nested
            pass

        elif interaction == 'nested':
            # circles are nested
            pass

        elif interaction == 'intersecting':
            # circles are intersecting, so update cluster states
            print('circles are intersecting')
            if c1.cluster is None and c2.cluster is None:
                # new cluster for each circle
                self.num_clusters = c1.new_cluster(self.num_clusters)
                c2.cluster = c1.cluster

            elif c1.cluster is None:
                # circle 2 is part of a cluster
                c1.cluster = c2.cluster

            elif c2.cluster is None:
                # I am part of a cluster
                c2.cluster = c1.cluster

            elif c1.cluster != c2.cluster:
                # Both clusters already have a cluster
                print('Conflicting logic: Intersecting circles with different clusters!')


            # compute largest circle by comparing radii, throwing out any identical circles
            c1.compare_radius(c2, True)
            c2.compare_radius(c1)

    def group(self):
        # Group circles in clusters and determine largest circle within each
        for i, circle in enumerate(self.circles):
            for j in range(0, i):
                print('Get interaction between circles {} and {}'.format(i, j))
                circle2 = self.circles[j]

                # get interaction between two circles and update cluster information
                self.update_cluster_info(circle, circle2);

            # Assign cluster number if circle is not touching any others
            if circle.cluster is None:
                self.num_clusters = circle.new_cluster(self.num_clusters)

    def clusters(self):
        clusters = []
        for circle in self.circles:
            clusters.append(circle.cluster)
        return clusters

    def largest(self):
        largest = []
        for circle in self.circles:
            largest.append(circle.largest)
        return largest

    def largest_of_clusters(self):
        largest_of_clusters = []
        for circle in self.circles:
            if circle.largest:
                largest_of_clusters.append(circle.c_tuple)
        return largest_of_clusters


def compute_largest_of_clusters(c_tuples):

    # construct all circles from c-tuples
    circles = CircleSet(c_tuples)

    # group the circles into clusters
    circles.group()
    print(circles.clusters())
    print(circles.largest())

    return circles.largest_of_clusters()


def c_tuples_from_file(filename):
    c_tuples = []
    with open(filename, 'r') as f:
        for line in f:
            current = line.split(',')
            c_tuples.append((float(current[0]), float(current[1]), float(current[2])))

    return c_tuples
