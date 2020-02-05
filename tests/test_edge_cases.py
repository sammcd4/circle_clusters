from circletesttools import CircleTestCase


class EdgeCases(CircleTestCase):

    def test_empty_list(self):
        self.verify_largest_of_clusters_algorithm([], [])

    def test_identical_circles_in_cluster(self):
        c_tuples = [(1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, [c_tuples[0]])

    def test_keep_identical_circles_in_cluster(self):
        c_tuples = [(1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples, remove_identical_circles=False)

    def test_keep_all_equal_area_circles_in_cluster(self):
        c_tuples = [(1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5),
                    (1.0, 1.0, 1.0),
                    (3.0, 1.0, 1.0),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples,
                                                  remove_equal_area_circles=False,
                                                  remove_identical_circles=False)

    def test_tangent_circles(self):
        c_tuples = [(1.0, 1.0, 1.0),
                    (2.5, 1.0, 0.5),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, [c_tuples[0]])

    def test_equal_area_tangent_circles(self):
        c_tuples = [(1.0, 1.0, 1.0),
                    (3.0, 1.0, 1.0),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, [c_tuples[0]])

    def test_keep_equal_area_tangent_circles(self):
        c_tuples = [(1.0, 1.0, 1.0),
                    (3.0, 1.0, 1.0),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples, remove_equal_area_circles=False)

    def test_nested_circles(self):
        c_tuples = [(1.0, 1.0, 1.0),
                    (1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.3),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples)
