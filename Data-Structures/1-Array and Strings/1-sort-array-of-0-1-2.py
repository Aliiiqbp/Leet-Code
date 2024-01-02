"""
Q: Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
A: Time: O(n) - Space: O(n)
"""
import random


def sort012(arr):

    n = len(arr)
    cnt_0, cnt_2 = 0, 0

    for x in arr:
        if x == 0:
            cnt_0 += 1
        elif x == 2:
            cnt_2 += 1

    for i in range(cnt_0):
        arr[i] = 0
    for i in range(cnt_0, n - cnt_2):
        arr[i] = 1
    for i in range(n - cnt_2, n):
        arr[i] = 2

    return arr


# check the solution
n = 10
numbers = [0, 1, 2]
arr = []
for i in range(n):
    arr.append(random.choice(numbers))
print("array:", arr)

sorted_array = sort012(arr)
print("sorted array:", sorted_array)
