""""
Given: array with non-negative values / K
output: a continuous sub-array with sum=K
Time: O(N)
"""


def sub_sum_k(arr, k):

    n = len(arr)
    tmp_sum = arr[0]
    pt1, pt2 = 0, 0

    for i in range(2 * n - 2):

        if tmp_sum < k and pt2 < n - 1:
            pt2 += 1
            tmp_sum += arr[pt2]
        elif tmp_sum > k and pt1 < n - 1:
            tmp_sum -= arr[pt1]
            pt1 += 1
        elif tmp_sum == k:
            return arr[pt1:pt2+1]

    return None


# test
arr = [2, 0, 1, 3, 5, 5, 2, 1, 4]
k = 2
print(sub_sum_k(arr, k))
