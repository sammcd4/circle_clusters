from math import sqrt


class Circle:

    def __init__(self, c_tuple):
        self._x = c_tuple[0]
        self._y = c_tuple[1]
        self._r = c_tuple[2]

        self.cluster = None
        self.largest = True

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def r(self):
        return self._r

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
            #return 'none'
        elif d + smallest_r < largest_r:
            # circles are nested
            #return 'nested'
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
            self.compare_radius(circle2.r)
            circle2.compare_radius(self.r)

            #return 'intersecting'
        return num_clusters

    def compare_radius(self, r2):
        # prove that this circle is not the largest
        if self.largest and r2 > self.r:
            self.largest = False

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
            for j in range(i+1, len(self.circles)):
                print('Get interaction between circles {} and {}'.format(i, j))
                circle2 = self.circles[j]

                # get interaction between two circles and update cluster information
                self.num_clusters = circle.get_interaction(circle2, self.num_clusters)
                print(self.num_clusters)
                # assign cluster number to each circle, if intersecting

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

class Cluster:

    def __init__(self, circles):
        self._circles = circles
        self.compute_largest_circle()

    def compute_largest_circle(self):
        # compute the largest circle in the set of circles
        for circle in self.circles:
            pass

