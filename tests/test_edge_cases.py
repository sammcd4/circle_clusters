from circletesttools import CircleTestCase


# few edge cases to ensure algorithm is working properly
class EdgeCases(CircleTestCase):

    def test_empty_list(self):
        self.verify_largest_of_clusters_algorithm([], [])

    def test_single_c_tuple(self):
        c_tuple = [(12.0, 11.0, 10.0)]
        self.verify_largest_of_clusters_algorithm(c_tuple, c_tuple)

    def test_tangent_circles(self):
        c_tuples = [(1.0, 1.0, 1.0),
                    (2.5, 1.0, 0.5),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, [c_tuples[0]])

    def test_nested_circles(self):
        c_tuples = [(1.0, 1.0, 1.0),
                    (1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.3),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples)

    def test_nested_tangent_circles(self):
        c_tuples = [(1.0, 1.0, 1.0),
                    (0.5, 1.0, 0.5),
                    (0.25, 1.0, 0.25),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, [c_tuples[0]])
