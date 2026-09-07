class Solution:

  def uniqueOccurrences(self, arr: list[int]) -> bool:
    arr.sort()
    v = []
    i = 0

    while i < len(arr):
      count = 1
      while i + 1 < len(arr) and arr[i] == arr[i + 1]:
        count += 1
        i += 1
      v.append(count)
      i += 1

    v.sort()
    for j in range(1, len(v)):
      if v[j] == v[j - 1]:
        return False

    return True