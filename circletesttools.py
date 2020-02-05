import unittest
from circleclusters import coordinates_from_file, compute_largest_of_clusters


class CircleTestCase(unittest.TestCase):

    def verify_largest_of_clusters_algorithm(self, filename):
        coordinates = coordinates_from_file('input/' + filename)
        output = compute_largest_of_clusters(coordinates)
        output_baseline = coordinates_from_file('baseline_output/' + filename)

        self.assertEqual(output, output_baseline, 'Baseline mismatch')