from data_structures.core.matrix import Matrix
from data_structures.core.heap import MaxHeap
from data_structures.core.array import DynamicArray, StaticArray 

def _deep_copy_dynamic_array(source: DynamicArray) -> DynamicArray:
    new_array = DynamicArray()
    for i in range(len(source)):
        new_array.append(source[i])
    return new_array

class Node:
    
    def __init__(self, level: int, current_profit: int, assignment_path: DynamicArray, upper_bound: int):
        self.level = level 
        self.current_profit = current_profit
        self.assignment_path = assignment_path 
        self.upper_bound = upper_bound 

    def __lt__(self, other):
        return self.upper_bound < other.upper_bound
        
    def __gt__(self, other):
        return self.upper_bound > other.upper_bound

def _calculate_upper_bound(bid_matrix: Matrix, level: int, current_profit: int, assigned_buyers: DynamicArray) -> int:
    
    N = bid_matrix.num_rows()
    upper_bound = current_profit
    
    is_buyer_assigned = StaticArray(N) 
    for i in range(N):
        is_buyer_assigned[i] = 0
        
    for i in range(len(assigned_buyers)):
        buyer_idx = assigned_buyers[i]
        is_buyer_assigned[buyer_idx] = 1
    
    for piece_idx in range(level, N):
        
        max_remaining_bid = 0
        
        for buyer_idx in range(N):
            if is_buyer_assigned[buyer_idx] == 0:
                bid = bid_matrix[piece_idx, buyer_idx] 
                
                if bid > max_remaining_bid:
                    max_remaining_bid = bid
                    
        upper_bound += max_remaining_bid
        
    return upper_bound


def max_auction_profit(B: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
    
    if not B:
        return 0, []
        
    N = len(B)
    
    bid_matrix = Matrix(N, N)
    for i in range(N):
        for j in range(N):
            bid_matrix[i, j] = B[i][j]

    pq = MaxHeap()
    
    empty_path = DynamicArray()
    
    initial_ub = _calculate_upper_bound(bid_matrix, 0, 0, empty_path)
    root = Node(
        level=0, 
        current_profit=0, 
        assignment_path=empty_path, 
        upper_bound=initial_ub
    )
    pq.insert(root)
    
    max_profit = 0
    best_assignment_path = empty_path
    
    while not pq.is_empty():
        
        current_node = pq.extract_max()
        
        if current_node.upper_bound <= max_profit:
            continue
            
        if current_node.level == N:
            if current_node.current_profit > max_profit:
                max_profit = current_node.current_profit
                best_assignment_path = _deep_copy_dynamic_array(current_node.assignment_path)
            continue

        current_piece_index = current_node.level
        
        for buyer_index in range(N):
            
            is_buyer_assigned = False
            for i in range(len(current_node.assignment_path)):
                if current_node.assignment_path[i] == buyer_index:
                    is_buyer_assigned = True
                    break
            
            if not is_buyer_assigned:
                
                new_profit = current_node.current_profit + bid_matrix[current_piece_index, buyer_index]
                
                new_path = _deep_copy_dynamic_array(current_node.assignment_path)
                new_path.append(buyer_index)
                
                new_level = current_piece_index + 1
                new_ub = _calculate_upper_bound(bid_matrix, new_level, new_profit, new_path)
                
                if new_ub > max_profit:
                    new_node = Node(new_level, new_profit, new_path, new_ub)
                    pq.insert(new_node)
    
    final_assignment = []
    for piece_index in range(N):
        if piece_index < len(best_assignment_path):
            final_assignment.append((piece_index, best_assignment_path[piece_index]))
        
    return max_profit, final_assignment