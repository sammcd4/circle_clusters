from circletesttools import CircleTestCase
from circleclusters import Circle, CircleSet


# additional basic tests to ensure correct algorithmic behavior
class CircleTests(CircleTestCase):

    def test_negative_radius(self):
        c_tuple = (-1.0, 1.0, -0.5)
        with self.assertRaises(AssertionError) as context:
            Circle(c_tuple)

        self.assertTrue('Radius must be greater than zero', str(context.exception))

    def test_not_intersecting(self):
        c_tuple = (1.0, 1.0, 0.5)
        c_tuple2 = (-1.0, -1.0, 0.5)
        c1 = Circle(c_tuple)
        c2 = Circle(c_tuple2)

        interaction = c1.get_interaction(c2)
        self.assertEqual('none', interaction)

    def test_intersecting(self):
        c_tuple = (1.0, 1.0, 0.5)
        c_tuple2 = (1.5, 1.0, 0.5)
        c1 = Circle(c_tuple)
        c2 = Circle(c_tuple2)

        interaction = c1.get_interaction(c2)
        self.assertEqual('intersecting', interaction)

    def test_nested(self):
        c_tuple = (1.0, 1.0, 0.5)
        c_tuple2 = (1.0, 1.0, 0.05)
        c1 = Circle(c_tuple)
        c2 = Circle(c_tuple2)

        interaction = c1.get_interaction(c2)
        self.assertEqual('nested', interaction)

    def test_largest(self):
        c_tuple = (1.0, 1.0, 0.5)
        c_tuple2 = (1.5, 1.0, 0.55)
        c1 = Circle(c_tuple)
        c2 = Circle(c_tuple2)

        # needs to be intersecting to compare within cluster
        interaction = c1.get_interaction(c2)
        self.assertEqual('intersecting', interaction)

        # verify that c2 is largest
        c1.compare_radius(c2)
        self.assertTrue(c2.largest)

    def test_circle_set_methods(self):

        # taken from provided example1
        c_tuples = [
            (0.5, 0.5, 0.5),
            (1.5, 1.5, 1.1),
            (0.7, 0.7, 0.4),
            (4.0, 4.0, 0.7),
        ]

        # construct all circles from c-tuples
        circles = CircleSet(c_tuples)

        # group the circles into clusters
        circles.group()

        # confirm that the method output is accurate
        self.assertEqual([1, 1, 1, 2], circles.clusters())
        self.assertEqual([False, True, False, True], circles.largest())