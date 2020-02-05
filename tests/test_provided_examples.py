from circletesttools import CircleTestCase


class ProvidedExamples(CircleTestCase):

    def test_two_clusters(self):
        filename = 'example1.txt'
        self.verify_largest_of_clusters_algorithm(filename)

    def test_no_clusters_touching(self):
        filename = 'example2.txt'
        self.verify_largest_of_clusters_algorithm(filename)

    def test_all_clusters_touching(self):
        filename = 'example3.txt'
        self.verify_largest_of_clusters_algorithm(filename)
