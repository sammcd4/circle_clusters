from circletesttools import CircleTestCase
from circleclusters import c_tuples_from_file


class FileRead(CircleTestCase):

    def test_empty_file(self):
        filename = 'empty.txt'
        self.verify_c_tuple_fileread(filename, [])

    def test_correct_format(self):
        filename = 'example1.txt'
        expected_output = [(0.5, 0.5, 0.5),
                           (1.5, 1.5, 1.1),
                           (0.7, 0.7, 0.4),
                           (4.0, 4.0, 0.7),
                           ]
        self.verify_c_tuple_fileread(filename, expected_output)

    def test_incorrect_format(self):
        filename = 'input/bad.txt'
        with self.assertRaises(Exception) as context:
            c_tuples_from_file(filename)

        self.assertTrue('could not convert string to float' in str(context.exception))