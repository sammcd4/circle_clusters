from circletesttools import CircleTestCase
from circleclusters import Circle


# additional basic tests to ensure correct algorithmic behavior
class CustomExamples(CircleTestCase):

    def test_negative_radius(self):
        c_tuple = (-1.0, 1.0, -0.5)
        with self.assertRaises(AssertionError) as context:
            Circle(c_tuple)

        self.assertTrue('Radius must be greater than zero', str(context.exception))

    def test_signed(self):
        c_tuples = [(-1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5),
                    (1.0, 1.0, 0.5)]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples[0:2])

    def test_all_apart(self):
        c_tuples = [(1.0, 1.0, 0.5),
                    (10.0, 10.0, 0.5),
                    (75.0, 11.0, 0.5),
                    (100.0, 4.0, 5.0)]
        self.verify_largest_of_clusters_algorithm(c_tuples, c_tuples)

    def test_chained_loop(self):
        filename = 'example4.txt'
        self.verify_largest_of_clusters_algorithm_from_file(filename)
