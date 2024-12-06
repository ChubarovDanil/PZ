def shift_right_and_replace_first(A):
    if len(A) == 0:
        return A
    B = [0] * len(A)
    for i in range(1, len(A)):
        B[i] = A[i - 1] 
    return B

A = [10, 20, 30, 40, 50]
B = shift_right_and_replace_first(A)
print(B) 