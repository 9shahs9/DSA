class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.data_table = [None] * self.size

    def __hash(self, key):
        return sum([ord(c) for c in key]) % self.size

    def show_hash(self, key):
        return self.__hash(key)

    def print_table(self):
        print("=" * 60)
        for i, item in enumerate(self.data_table):
            print(i, item)
        print("=" * 60)

    def set_item(self, key, value):
        hash_value = self.__hash(key)
        if self.data_table[hash_value] is None:
            self.data_table[hash_value] = []
        self.data_table[hash_value].append([key, value])
        return True

    def get_item(self, key):
        hash_value = self.__hash(key)
        if self.data_table[hash_value] is None:
            return None
        hash_list = self.data_table[hash_value]
        for item in hash_list:
            if item[0] == key:
                return item[1]
        return None

    def get_keys(self):
        keys = []
        for i in range(self.size):
            hash_list = self.data_table[i]
            if not hash_list:
                continue
            for item in hash_list:
                keys.append(item[0])
        return keys


def items_in_common(list1, list2):
    list_map = {}
    for i in list1:
        list_map[i] = True

    for j in list2:
        if j in list_map:
            return True
    return False


l = [1, 3, 5]
l2 = [1, 2, 5]
print(items_in_common(l, l2))

h = HashTable()

h.set_item("Shashank", 14)
h.set_item("Srimanasa", 21)
h.set_item("Shikhar", 12)
h.set_item("Akshar", 24)
h.set_item("Sarojini", 19)
h.set_item("BRKRao", 31)
h.print_table()

print(h.get_item("Sarojini"))

print(h.get_keys())
