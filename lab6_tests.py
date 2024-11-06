import data
import lab6
import unittest
from data import Book
from lab6 import selection_sort_books, swap_case, str_translate, histogram


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books(self):
        self.assertEqual(selection_sort_books([Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens'),
                              Book(["J.K. Rowling"], "Harry Potter and the Chamber of Secrets"),
                              Book(["tester"], "Wahoo!!"), Book([], "Bello")]), [Book([], 'Bello'), Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens'), Book(['J.K. Rowling'], 'Harry Potter and the Chamber of Secrets'), Book(['tester'], 'Wahoo!!')])
    def test_selection_sort_books_2(self):
        self.assertEqual(selection_sort_books([]), None)

        # Part 2
    def test_swap_case(self):
        self.assertEqual(swap_case("hi"), "HI")
    def test_swap_case_2(self):
        self.assertEqual(swap_case("heLLo! GoOd to SEE you"), "HEllO! gOoD TO see YOU")
    # Part 3
    def test_str_translate(self):
        self.assertEqual(str_translate("hello!", "l", "p"), "heppo!")
    def test_str_translate_2(self):
        self.assertEqual(str_translate("welcome!", "q", "m"), "welcome!")
    # Part 4
    def test_histogram(self):
        self.assertEqual(histogram("hello my name is name"), {'hello': 1, 'my': 1, 'name': 2, 'is': 1})
    def test_histogram_2(self):
        self.assertEqual(histogram("hello i! am a tlkaking cat!!"), {'hello': 1, 'i!': 1, 'am': 1, 'a': 1, 'tlkaking': 1, 'cat!!': 1})



if __name__ == '__main__':
    unittest.main()
