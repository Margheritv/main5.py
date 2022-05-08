def power(a, b):

    if b == 0:
        return 1
    elif a < 0 or b < 0:
        return -1
    else:
        return a*power(a, b-1)


a = 5
b = 2
print("result: ", power(a, b))


# 2


def binary_search(numbers, num, start, end):

    if end >= start:    # checks base case
        middle = (end+start)//2

        if numbers[middle] == num:  # checks if num is in the very middle
            return middle
        elif numbers[middle] > num:  # if num < middle, then it is in left subarray
            return binary_search(numbers, num, start, middle -1)
        else:
            return binary_search(numbers, num, middle +1, end)  # if num > middle then it is in right subarray

    else:
        return -1   # if num NOT in array


numbers = [1, 2, 3, 4, 5, 6]
num = 3
print(binary_search(numbers, num, 0, len(numbers) -1))


# ab 3

class HashTable:
    def __init__(self):
        self.max = 9
        self.arr = [[] for i in range(self.max)]
        # print(self.arr)

    def __my_hash(self, element):
        if type(element) == int:
            key = element % 10
            # print(key)
            return key

        elif type(element) == str:
            key = len(element)
            # print(key)
            return key

    def insert(self, element):
        key = self.__my_hash(element)   # die Funk my.hash wird in der Funk insert aufgerufen and the type of added elem (down) will be checked dank my_hash
        if self.arr[key] != None:     # wenn key schon besetzt ist, append not delete el!
            self.arr[key].append(element)
        else:
            self.arr[key] = [element]    # wenn platz leer ist, insert el into position
        #print(self.arr)

    def get_element(self, element):
        key = self.__my_hash(element)
        # print(key)
        # print(len(self.arr[key]))

        if len(self.arr[key]) == 0:   # wenn el in einem leeren Bucket stehen würde - meldung wrong
            #print("Wroooooong")
            return False
        else:
            try:
                return self.arr[key].remove(element)   # removes the given element
            except:
                #print("Element is not in the list")
                return False

    def get_size(self):
        length = 0
        for key in range(self.max):
            if len(self.arr[key]) == 0:    # Fall einer leeren Liste --> length (0) +1 for jedes El (=nr leere [])
                length += 1
        #print(length)
            else:
                length += len(self.arr[key])    # zur menge leerer [] werden einzelne el aus den buckets addiert
        # print(length)
        return length


hash = HashTable()
hash.insert('heyheyy')
hash.insert(56)
hash.insert(66)
hash.insert(76)
hash.get_element(66)
hash.get_size()
#print(hash.arr)