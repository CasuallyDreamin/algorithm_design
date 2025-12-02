from .array import StaticArray

class Matrix:
    def __init__(self, rows: int, cols: int):
    
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be positive.")
        
        self._rows = rows
        self._cols = cols
        
        self._matrix = [
            StaticArray(cols) for _ in range(rows)
        ]
        
        for row_array in self._matrix:
            row_array._data = [None] * cols
            row_array._size = cols

    def num_rows(self) -> int:
        return self._rows

    def num_cols(self) -> int:
        
        return self._cols

    def __getitem__(self, index: tuple):

        if not (isinstance(index, tuple) and len(index) == 2):
            raise TypeError("Index must be a tuple (row, col).")
            
        row, col = index
        
        if not (0 <= row < self._rows and 0 <= col < self._cols):
            raise IndexError("Row or column index out of bounds.")

        return self._matrix[row][col]

    def __setitem__(self, index: tuple, value):
        if not (isinstance(index, tuple) and len(index) == 2):
            raise TypeError("Index must be a tuple (row, col).")
            
        row, col = index
        
        if not (0 <= row < self._rows and 0 <= col < self._cols):
            raise IndexError("Row or column index out of bounds.")
        self._matrix[row][col] = value

    def __str__(self) -> str:
        s = []
        for row_array in self._matrix:
            s.append(str(list(row_array._data)))
        return "[\n  " + ",\n  ".join(s) + "\n]"

    def __repr__(self) -> str:
        return f"Matrix({self._rows}x{self._cols})"