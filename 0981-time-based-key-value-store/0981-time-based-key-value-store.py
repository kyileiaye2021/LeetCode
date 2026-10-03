class TimeMap:

    def __init__(self):
        # hashmap ={str: list}
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        list_to_find = self.map[key]
        l = 0
        r = len(list_to_find) - 1
        res = ''

        while l <= r:
            mid = (l + r) // 2

            if list_to_find[mid][0] == timestamp:
                return list_to_find[mid][1]

            elif list_to_find[mid][0] < timestamp:
                res = list_to_find[mid][1]
                l = mid + 1

            else:
                r = mid - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)