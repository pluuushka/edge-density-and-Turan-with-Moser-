# n - count of vertex, p - edge density
def generator_of_unoriented_graph(n, p):
    m = n * (n - 1) * p / 2 # |E| = m, G = (V, E)

    A = [[0] * n for _ in range(n)]

    count = 0 # counter, stop cond while cond < m
    for i in range(n):
        for j in range(n):
            if (i > j):
                if (count < m):
                    A[i][j] = 1

    def transpose(A):
        A_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                A_new[i][j] = A[j][i]

        return A_new
    
    A_new = transpose(A) # to being unoriented R = A + A_transpose
    R = A + A_new
    return R


    
    

                

