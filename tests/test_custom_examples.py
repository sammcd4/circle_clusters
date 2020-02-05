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

    def test_all_apart(self):
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
        c_tuples = c_tuples_from_file('input/' + filename)
        expected_output = c_tuples_from_file('baseline_output/' + filename)

        self.verify_largest_of_clusters_algorithm(c_tuples, expected_output)

    def test_order_complex(self):
        filename = 'order_complex.txt'
        c_tuples = c_tuples_from_file('input/' + filename)
        expected_output = c_tuples_from_file('baseline_output/' + filename)

        self.verify_largest_of_clusters_algorithm(c_tuples, expected_output)

    def test_large_set(self):
        filename = 'large_set.txt'
        c_tuples = c_tuples_from_file('input/' + filename)
        expected_output = c_tuples_from_file('baseline_output/' + filename)

        #self.verify_largest_of_clusters_algorithm(c_tuples, expected_output)


