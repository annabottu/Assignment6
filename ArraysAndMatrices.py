#Array Implementation
# A simple array class to demonstrate basic operations
# This class supports insertion, deletion, and access of elements
class MyArray:
    def __init__(self):
        self.data = []
    
    def insert(self, index, value):
        self.data.insert(index, value)
    
    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        return None
    
    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None
    
    def __repr__(self):
        return str(self.data)

#Matrix Implementation
# A simple matrix class to demonstrate basic operations
# This class supports insertion, access, and deletion of elements
class MyMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]
    
    def insert(self, row, col, value):
        self.data[row][col] = value
    
    def access(self, row, col):
        return self.data[row][col]
    
    def delete(self, row, col):
        self.data[row][col] = 0
    
    def __repr__(self):
        return "\n".join(str(r) for r in self.data)


arr = MyArray()
arr.insert(0, 10)
arr.insert(1, 20)
arr.delete(0)
print("Array:", arr)

mat = MyMatrix(2, 3)
mat.insert(0, 1, 5)
mat.insert(1, 2, 9)
print("Matrix:\n", mat)