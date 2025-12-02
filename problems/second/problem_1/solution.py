from data_structures.core.matrix import Matrix
from typing import Tuple, Optional, Any

_DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def _is_valid(matrix: Matrix, r: int, c: int, visited: list[list[bool]], target_value: Any) -> bool:
    
    rows = matrix.num_rows()
    cols = matrix.num_cols()
    
    row_in_bounds = 0 <= r < rows
    col_in_bounds = 0 <= c < cols
    
    if not (row_in_bounds and col_in_bounds):
        return False

    if visited[r][c]:
        return False
    
    current_value = matrix[r, c]
    if current_value == 0 or current_value != target_value:
        return False
        
    return True

def _dfs(matrix: Matrix, r: int, c: int, visited: list[list[bool]], target_value: Any) -> int:

    if not _is_valid(matrix, r, c, visited, target_value):
        return 0
    
    visited[r][c] = True
    area_size = 1
    
    for dr, dc in _DIRECTIONS:
        new_r, new_c = r + dr, c + dc
        area_size += _dfs(matrix, new_r, new_c, visited, target_value)
        
    return area_size

def get_largest_area(matrix: Matrix) -> Tuple[Optional[Any], int]:

    rows = matrix.num_rows()
    cols = matrix.num_cols()
    
    if rows == 0 or cols == 0:
        return (None, 0)
        
    visited = [[False] * cols for _ in range(rows)]
    
    largest_size = 0
    winner_value = None

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                
                target_value = matrix[r, c]
                
                if target_value == 0 or target_value is None:
                    visited[r][c] = True 
                    continue
                    
                component_size = _dfs(matrix, r, c, visited, target_value)
                
                if component_size > largest_size:
                    largest_size = component_size
                    winner_value = target_value

    return (winner_value, largest_size)