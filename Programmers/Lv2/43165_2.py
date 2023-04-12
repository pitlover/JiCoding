def solution(numbers, target):
    result = []
    for i in range(2 ** len(numbers)):
        bit_i = bin(i)[2:]
        bit_i = ("0" * (len(numbers) - len(bit_i))) + bit_i
        bit_i = list(bit_i)

        tmp = 0
        for idx, j in enumerate(numbers):
            if bit_i[idx] == "1":
                tmp += j
            else:
                tmp -= j
        result.append(tmp)
    return result.count(target)


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
