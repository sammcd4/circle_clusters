import unittest
from circleclusters import c_tuples_from_file, compute_largest_of_clusters


class CircleTestCase(unittest.TestCase):

    def verify_largest_of_clusters_algorithm_from_file(self, filename, *args, **kwargs):
        c_tuples = c_tuples_from_file('input/' + filename)
        expected_output = c_tuples_from_file('baseline_output/' + filename)

        self.verify_largest_of_clusters_algorithm(c_tuples, expected_output, *args, **kwargs)

    def verify_largest_of_clusters_algorithm(self, c_tuples, expected_output, *args, **kwargs):
        actual_output = compute_largest_of_clusters(c_tuples, *args, **kwargs)

        self.assertEqual(expected_output, actual_output, 'Baseline mismatch')

    def verify_c_tuple_fileread(self, filename, expected_output):
        c_tuples = c_tuples_from_file('input/' + filename)

        self.assertEqual(expected_output, c_tuples)
