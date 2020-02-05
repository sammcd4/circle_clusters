from math import sqrt


# Circle class for computing and managing interaction between other circles
class Circle:

    def __init__(self, c_tuple):
        self._c_tuple = c_tuple

        assert self.r > 0, 'Radius must be greater than zero'

        self.cluster = None
        self.largest = True
        self.largestCircle = None
        self.intersecting_circles = []

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
    def xy(self):
        return self.x, self.y

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
            return 'none'
        elif d + smallest_r < largest_r:
            # circles are nested
            return 'nested'
        else:
            # circles are intersecting, forming a cluster

            # take note of connected circles
            self.intersecting_circles.append(circle2)
            circle2.intersecting_circles.append(self)

            return 'intersecting'

    def compare_radius(self, circle2):
        # compare radius to another circle to determine which is largest

        # only compare size within the same cluster
        if self.cluster != circle2.cluster:
            return

        if self.largest:
            # prove that this circle is not the largest

            # circles of different radius
            if circle2.r > self.r:
                self.largest = False
                self.largestCircle = circle2

        elif self.largestCircle is not None:
            # save on more iteration by storing largest circle and comparing to it directly
            self.largestCircle.compare_radius(circle2)
            circle2.compare_radius(self.largestCircle)


# Class that maintains the c-tuple order and facilitates operations between circles
class CircleSet:

    def __init__(self, c_tuples):
        # Create a list of circles from list of c-tuples
        self.circles = [Circle(c_tuple) for c_tuple in c_tuples]
        self.num_clusters = 0

    def get_circle(self, idx):
        return self.circles[idx]

    def update_cluster_info(self, circle):

        existing_cluster = None

        if circle.cluster is not None:
            existing_cluster = circle.cluster

        # loop over circles in cluster to determine the correct cluster number
        for c in circle.intersecting_circles:
            if c.cluster is not None:
                if existing_cluster is None:
                    existing_cluster = c.cluster
                elif c.cluster != existing_cluster:
                    # choose lowest cluster value
                    existing_cluster = min(c.cluster, existing_cluster)

        # if truly no existing cluster, then create one
        if existing_cluster is None:
            # start a new cluster
            self.num_clusters = circle.new_cluster(self.num_clusters)
            existing_cluster = circle.cluster

        # update all circles to the existing cluster
        circle.cluster = existing_cluster
        for c in circle.intersecting_circles:
            c.cluster = existing_cluster

            # compute largest circle within cluster
            circle.compare_radius(c)
            c.compare_radius(circle)

    def group(self):
        # Group circles in clusters and determine largest circle within each
        for i, circle in enumerate(self.circles):
            for j in range(i+1, len(self.circles)):
                circle2 = self.circles[j]

                # if intersecting, log self in each other's intersecting_circles list
                circle.get_interaction(circle2)

            # found all intersecting circles with circle, so update cluster information
            self.update_cluster_info(circle)

    def clusters(self):
        return [circle.cluster for circle in self.circles]

    def largest(self):
        return [circle.largest for circle in self.circles]

    def largest_of_clusters(self):
        largest_of_clusters = []
        for circle in self.circles:
            if circle.largest:
                largest_of_clusters.append(circle.c_tuple)
        return largest_of_clusters


# entry point to run algorithm
def compute_largest_of_clusters(c_tuples):

    # construct all circles from c-tuples
    circles = CircleSet(c_tuples)

    # group the circles into clusters
    circles.group()

    return circles.largest_of_clusters()


# import a comma-separated list from a file
def c_tuples_from_file(filename):
    c_tuples = []
    with open(filename, 'r') as f:
        for line in f:
            current = line.split(',')
            c_tuples.append((float(current[0]), float(current[1]), float(current[2])))

    return c_tuples
