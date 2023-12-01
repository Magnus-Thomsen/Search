class LinearSearch:
    def search(self, list, target) -> str:
        i = 0
        for x in list:
            if (x == target):
                return f"Found at index {i}"
            i += 1
        return "Target not in list"
    