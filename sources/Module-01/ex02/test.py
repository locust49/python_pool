from vector import Vector
import sys

sys.tracebacklimit = 0

# Variables of values
integer_ = 3
range_ = (10, 15)
range_wrong = (20, 15)
list_ = [0.0, 1.0, 2.0, 3.0]
listoflist = [[0.0], [1.0], [2.0], [3.0]]
empty_list = []
empty_listoflist = [[]]

dashed_line = 39 * '--'

print(dashed_line)
vect_int = Vector(integer_)
print(vect_int)
print(dashed_line)
vect_range = Vector(range_)
print(vect_range)
print(dashed_line)
vect_list = Vector(list_)
print(vect_list)
print(dashed_line)
vect_listoflist = Vector(listoflist)
print(vect_listoflist)
print(dashed_line)
vect_empty_list = Vector(empty_list)
print(vect_empty_list)
print(dashed_line)
vect_empty_listoflist = Vector(empty_listoflist)
print(vect_empty_listoflist)
print(dashed_line)
listoflist_2d_uni = [[0.0, 0.5], [1.0, 1.5], [2.0, 2.5], [3.0, 3.5]]
vect_listoflist_2d_uni = Vector(listoflist_2d_uni)
print(vect_listoflist_2d_uni)
print(dashed_line)
# listoflist_2d_notuni = [[0.0], [1.0], [2.0, 2.5], [3.0, 3.5, 3.8]]
# vect_listoflist_2d_notuni = Vector(listoflist_2d_notuni)
# print(vect_listoflist_2d_notuni)
# print(dashed_line)
# wrong_list = ['hi']
# vect_wronglist = Vector(wrong_list)
# print(vect_wronglist)
vect_range_wrong = Vector(range_wrong)
print(vect_range_wrong)
