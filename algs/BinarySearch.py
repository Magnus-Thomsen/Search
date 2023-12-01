from math import floor
class BinarySearch:
    def search(self, list, start, end, target) -> str:
        if (start > end):
            return "Target not in list"
        
        middle = floor((start + end) / 2)

        if (list[middle] == target):
            return f"Found at index {middle}"
        
        if (list[middle] > target):
            return self.search(list, start, middle - 1, target)
        
        if (list[middle] < target):
            return self.search(list, middle + 1, end, target)


            