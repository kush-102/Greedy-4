class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # #time complexity is O(m*n) where m is len of source and n is len of target
        # #space complexity is O(m)
        i = 0
        j = 0  # i-source, j-target
        count = 0
        hash_set = set()
        for c in source:
            hash_set.add(c)

        while j < len(target):
            schar = source[i]
            tchar = target[j]

            if tchar not in hash_set:
                return -1
            if schar == tchar:
                i += 1
                j += 1
                if j == len(target):
                    return count + 1
            else:
                i += 1
            if i == len(source):
                i = 0
                count += 1
        return -1
        hash_map = {}

        # Create hashmap storing character -> list of indices is the value and characters in the source is the key
        for k in range(len(source)):
            c = source[k]
            if c not in hash_map:
                hash_map[c] = []
            hash_map[c].append(k)

        i = 0
        j = 0  # i -> source, j -> target
        count = 0

        while j < len(target):
            schar = source[i]
            tchar = target[j]

            # If target character is not in source at all, return -1
            if tchar not in hash_map:
                return -1

            # get the list associated with the current character in the target
            list_of_indices = hash_map[tchar]
            k = self.binary_search(
                list_of_indices, i
            )  # returns the index of the next matching target character in source

            if k == len(list_of_indices):  # Need to restart from the beginning
                i = 0
                count += 1
            else:
                i = list_of_indices[k] + 1
                j += 1
                if j == len(target):
                    return count + 1
                if i == len(source):  # If source is exhausted, reset
                    i = 0
                    count += 1

        return -1

    def binary_search(self, li, target):
        low, high = 0, len(li) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if li[mid] == target:
                return mid
            elif li[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low  # Return index where target would be inserted

    # time complexity is O(nlogk) where k is the avg length of the list of indices of the source characters
    # space complexity is O(n)
