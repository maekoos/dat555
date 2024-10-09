def transpose(M: list[list[int]]):
    if M == []:
        return []

    T = []
    for columnIndex in range(0, len(M[0])):
        T.append([])
        for rowIndex in range(0, len(M)):
            T[columnIndex].append(M[rowIndex][columnIndex])

    return T


def powers(list: list[int], start: int, end: int):
    T = []
    for idx, base in enumerate(list):
        T.append([])
        for exponent in range(start, end+1):
            T[idx].append(base**exponent)
    return T


def matmul(A: list[list[int]], B: list[list[int]]):
    C = []

    # För varje rad i A
    for i in range(0, len(A)):
        C.append([])
        # För varje kolonn i B
        for j in range(0, len(B[0])):
            C[i].append(0)
            for x in range(0, len(B)):
                C[i][j] += A[i][x]*B[x][j]

    return C


def invert(A: list[list[int]]):
    a, b = A[0]
    c, d = A[1]
    det = a*d-b*c
    if det == 0:
        return []
    return [[d/det, -b/det], [-c/det, a/det]]


def loadtxt(fp: str):
    A = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            B = []
            for n in line.split('\t'):
                B.append(float(n))
            A.append(B)

    return A
