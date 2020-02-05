from circletesttools import CircleTestCase
from circleclusters import c_tuples_from_file


# additional basic tests to ensure correct algorithmic behavior
class CustomExamples(CircleTestCase):

    def test_signed(self):
        c_tuples = [(-1.5, 1.0, 0.6),
                    (1.0, 1.0, 0.5),
                    (-1.0, 1.0, 0.4),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples[0:2])

    def test_non_intersecting(self):
        c_tuples = [(1.0, 1.0, 0.4),
                    (10.0, 10.0, 0.6),
                    (75.0, 11.0, 0.7),
                    (100.0, 4.0, 5.0),
                    ]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples)

    def test_chained(self):
        filename = 'example4.txt'
        self.verify_largest_of_clusters_algorithm_from_file(filename)

    def test_order_simple(self):
        filename = 'order_simple.txt'
        self.verify_largest_of_clusters_algorithm_from_file(filename)

    def test_order_complex(self):
        filename = 'order_complex.txt'
        self.verify_largest_of_clusters_algorithm_from_file(filename)

    def test_large_set(self):
        filename = 'large_set.txt'
        self.verify_largest_of_clusters_algorithm_from_file(filename)

    def test_large_set2(self):
        filename = 'large_set2.txt'
        self.verify_largest_of_clusters_algorithm_from_file(filename)

