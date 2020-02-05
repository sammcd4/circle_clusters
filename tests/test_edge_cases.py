from circletesttools import CircleTestCase


class EdgeCases(CircleTestCase):

    def test_empty_list(self):
        self.verify_largest_of_clusters_algorithm([], [])

    def test_identical_circles_in_cluster(self):
        c_tuples = [(1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5)]
        self.verify_largest_of_clusters_algorithm(c_tuples, [c_tuples[0]])

    def test_tangent_circles(self):
        c_tuples = [(1.0, 1.0, 1.0),
                    (2.5, 1.0, 0.5)]
        self.verify_largest_of_clusters_algorithm(c_tuples, [c_tuples[0]])

    def test_identical_tangent_circles(self):
        pass

    def test_nested_circles(self):
        pass
