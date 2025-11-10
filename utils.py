from math import floor, ceil

def transpose(A):
        n = len(A[0])
        A_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                A_new[i][j] = A[j][i]

        return A_new

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
    
    R = A + transpose(A)
    return R

def turan_graph(n, r): # n - count of vertex, r - count of subsets

    m = floor((r-1)*n**2 / 2*r) # |E| = m
    count_of_vertex = [0] * r # chtob ponimat' skol'ko otstupat'
    
    count_of_vertex_ceil = ceil(n/r)
    vertex_ceil = n % r

    count_of_vertex_floor = floor(n/r)
    vertex_floor = n - (n % r)

    # namutim shtucku chtobi otstupi delat' potom
    for i in range(count_of_vertex_floor):
        count_of_vertex[i] = vertex_ceil

    for i in range(count_of_vertex_ceil - 1, r):
        count_of_vertex[i] = vertex_floor

    R = [[0] * n for _ in range(n)]
    count_for_m = 0

    for i in range(n):
        for j in range(count_of_vertex[i], n):
            if count_for_m < m:
                if i > j:
                    R[i][j] = 1

    R = R + transpose(R)

    return R

def muna_mosera_graph():
    pass



    
    

                

