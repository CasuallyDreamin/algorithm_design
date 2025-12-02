from data_structures.core.matrix import Matrix

def phone_max_depth(K: int, N: int) -> int:
    dp = Matrix(rows=K + 1, cols=N + 1)
    
    for k in range(K + 1):
        dp[k, 0] = 0

    for k in range(K + 1):
        dp[k, 1] = 1
        
    for n in range(N + 1):
        dp[1, n] = n
        
    for k in range(2, K + 1):
        for n in range(2, N + 1):
            min_moves_for_n = float('inf')
            
            for x in range(1, n + 1):
                
                cost_if_breaks = dp[k - 1, x - 1]
                
                cost_if_survives = dp[k, n - x]
                
                worst_case_at_x = 1 + max(cost_if_breaks, cost_if_survives)
                
                min_moves_for_n = min(min_moves_for_n, worst_case_at_x)
                
            dp[k, n] = min_moves_for_n
            
    return dp[K, N]