#Emmy'sjanak


def gameOfXor(self, N , A):
    result = 0
    for i in range(N):
        # Total count of occurrences of A[i]
        total = (i + 1) * (N - i)
        if total % 2 == 1:
            result ^= A[i]
    return result

a=gameOfXor(0,2,[1,2])
print(a)