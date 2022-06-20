def solution(A,B):
    A.sort()
    B.sort(reverse= True)
    print(A, B)
    answer = 0
    for a in range(len(A)):
        answer += A[a]*B[a]
    return answer
