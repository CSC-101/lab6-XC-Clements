import data
from typing import Optional
from data import Book

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def first_letter(title:str):
    title_list = list(title)
    return title_list[0].lower()

def selection_sort_books(book_list:list[Book]) -> list[Book]:
    if book_list == []:
        return None
    for idx in range(len(book_list) - 1):
        mindex = idx
        for j in range(idx, len(book_list)):
            if first_letter(book_list[j].title) < first_letter(book_list[mindex].title):
                mindex = j
        temp = book_list[idx]
        book_list[idx] = book_list[mindex]
        book_list[mindex] = temp
    return book_list

print(selection_sort_books([Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens'), Book(["J.K. Rowling"], "Harry Potter and the Chamber of Secrets"), Book(["tester"], "Wahoo!!"), Book([],"Bello")]))


# Part 2

def swap_case(string:str) -> Optional[str]:
    input_list = list(string)
    output_list = []
    for n in input_list:
        if not n.isalpha():
            output_list.append(n)
        if n.isupper():
            output_list.append(n.lower())
        if n.islower():
            output_list.append(n.upper())
    return "".join(output_list)

print(swap_case("hi"))
print(swap_case("heLLo! GoOd to SEE you"))




# Part 3
def str_translate(input_string:str,old:str,new:str) -> str:
    input_list = list(input_string)
    output_list = []
    for n in input_list:
        if n == old:
            output_list.append(new)
        else:
            output_list.append(n)
    return "".join(output_list)

print(str_translate("hello!", "l", "p"))
print(str_translate("wahoo!!!", "o", "p"))


# Part 4

def histogram(input_str:str) -> dict[str:int]:
    input_list = input_str.split()
    output = dict()
    for n in input_list:
        if n not in output:
            output[n] = 1
        else:
            output[n] += 1
    return output

print(histogram("hello my name is name"))
print(histogram("hello i! am a tlkaking cat!!"))
