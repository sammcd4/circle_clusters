from math import sqrt


class Circle:

    def __init__(self, c_tuple):
        self._c_tuple = c_tuple

        self.cluster = None
        self.largest = True
        self.largestCircle = None

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
        print('Assigned circle to new cluster {}'.format(num_clusters))

        return num_clusters

    def get_interaction(self, circle2, num_clusters):
        x2 = circle2.x
        y2 = circle2.y
        r2 = circle2.r

        d = sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        smallest_r = min(self.r, r2)
        largest_r = max(self.r, r2)

        if d > abs(self.r + r2):
            # circles are not intersecting or nested
            print('circles are not touching')
        elif d + smallest_r < largest_r:
            # circles are nested
            print('nested circles')
        else:
            # circles are intersecting, so update cluster states
            print('circles are intersecting')
            if self.cluster is None and circle2.cluster is None:
                # new cluster for each circle
                num_clusters = self.new_cluster(num_clusters)
                circle2.cluster = self.cluster

            elif self.cluster is None:
                # circle 2 is part of a cluster
                self.cluster = circle2.cluster

            elif circle2.cluster is None:
                # I am part of a cluster
                circle2.cluster = self.cluster

            elif self.cluster != circle2.cluster:
                # Both clusters already have a cluster
                print('Conflicting logic: Intersecting circles with different clusters!')


            # compute largest circle by comparing radii
            self.compare_radius(circle2)
            circle2.compare_radius(self)


            #self.commpare_radius()

        return num_clusters

    def compare_radius(self, circle2):
        # prove that this circle is not the largest

        # only compare size within the same cluster
        if self.cluster != circle2.cluster:
            return

        if self.largest:
            if circle2.r > self.r:
                self.largest = False

                # save largest circle for else condition below
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

    def group(self):
        # Group circles in clusters and determine largest circle within each
        for i, circle in enumerate(self.circles):
            for j in range(0, i):
                print('Get interaction between circles {} and {}'.format(i, j))
                circle2 = self.circles[j]

                # get interaction between two circles and update cluster information
                self.num_clusters = circle.get_interaction(circle2, self.num_clusters)

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

class Cluster:

    def __init__(self, circles):
        self._circles = circles
        self.compute_largest_circle()

    def compute_largest_circle(self):
        # compute the largest circle in the set of circles
        for circle in self.circles:
            pass


def compute_largest_of_clusters(c_tuples):

    # construct all circles from c-tuples
    circles = CircleSet(c_tuples)

    # group the circles into clusters
    circles.group()
    print(circles.clusters())
    print(circles.largest())

    return circles.largest_of_clusters()


def coordinates_from_file(filename):
    coordinates = []
    with open(filename, 'r') as f:
        for line in f:
            current = line.split(',')
            coordinates.append((float(current[0]), float(current[1]), float(current[2])))

    return coordinates