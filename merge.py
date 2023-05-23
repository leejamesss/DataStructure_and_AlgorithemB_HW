# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))

# #写个归并排序从大到小进行排序，并计算每个数交换的次数，最后求和
# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst, 0
#     mid = len(lst) // 2
#     left, left_count = merge_sort(lst[:mid])
#     right, right_count = merge_sort(lst[mid:])
#     count = left_count + right_count
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(right[j])
#             j += 1
#         else:
#             result.append(left[i])
#             i += 1
#             count += len(right) - j
#     result += left[i:]
#     result += right[j:]
#     return result, count

# result, count = merge_sort(lst)
# print(result)
# print(lst)
# print(count)






# # 1 5 10 7 6
# # 1 5 6 7 10

class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, nums) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            nums = []
            for i in range(n):
                nums.append(int(input()))
            nums=nums[::-1]
            s = Solution()
            res = s.reversePairs(nums)
            print(res)
        except:
            break

