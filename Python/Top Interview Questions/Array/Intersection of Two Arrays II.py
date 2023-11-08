from collections import Counter

def intersect(nums1, nums2):
    counts1 = Counter(nums1)
    counts2 = Counter(nums2)
    intersection = counts1 & counts2
    return list(intersection.elements())



nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))