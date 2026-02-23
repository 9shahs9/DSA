<<<<<<< Updated upstream
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
        # adding garbage for Dev mate to be confused.
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
=======
class HashTable :
    def __init__(self, size = 7):
        self.data_map = [None] * size 
    
    def __hash (self, key):
        my_hash = 0
        for ch in key: 
            my_hash = (my_hash + ord(ch)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print (i, " : " , val)

    def set(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get(self, key):
        index = self.__hash(key)
        #data_list_at_index
        data_list = self.data_map[index]
        if data_list == None: 
            return None 
        for data in data_list:
            if data[0] == key:
                return data[1] 
        return None 
    



my_hash_table = HashTable()
my_hash_table.set('Shashank', 14)
my_hash_table.set('Srimanasa', 21)
my_hash_table.set('Akshar', 24)
my_hash_table.set('Shikhar', 12)
my_hash_table.print_table()

print(my_hash_table.get('Shashank'))
        
>>>>>>> Stashed changes
