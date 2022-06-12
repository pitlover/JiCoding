# 수식 최대화
# Fail -> 모범답안 분석

#######################################

import re
from itertools import permutations

def solution1(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)
#######################################
def calc(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b


def solution2(expression):
    answer = 0

    # +, -, * 에 대한 연산 우선 순위
    priors = [[0, 1, 2], [0, 2, 1],[1, 0, 2], [1, 2, 0],[2, 0, 1],[2, 1, 0]]
    operands = ['*', '+', '-']

    # 문자열 에서 숫자들만 split 하여 추출
    nums_split = expression
    nums_split = nums_split.replace('+', ' ')
    nums_split = nums_split.replace('*', ' ')
    nums_split = nums_split.replace('-', ' ')
    nums_split = nums_split.split(' ')
    nums = [int(num) for num in nums_split]

    # 문자열에서 +, -, * 만 추출
    operands_split = [op for op in expression if not op.isdecimal()]

    # +, -, * 에 대한 모든 우선순위 조합에 대해서
    for prior in priors:

        _nums = nums
        _operands = operands_split

        # 정해진 우선순위 대로 계산 실행
        for i in range(3):
            stack_num = []
            stack_op = []

            stack_num.append(_nums[0])

            # 스택에 숫자와 연산자를 넣다가, 현재 계산해야 하는 연산자 일 시 
            # 숫자 스택에 위의 2개, 연산자 스택의 위의 1개가 현재 계산해야 하는 식 이다
            for j in range(len(_operands)):
                stack_num.append(_nums[j+1])
                stack_op.append(_operands[j])

                # 현재 연산자가 계산해야 하는 경우
                if stack_op[-1] == operands[prior[i]]:
                    num1 = stack_num.pop(-1)
                    num2 = stack_num.pop(-1)
                    op = stack_op.pop(-1)

                    # 계산 결과를 다시 숫자 스택에 넣어줌
                    stack_num.append(calc(num2, num1, op))

            # 계산 결과 저장
            _nums = stack_num
            _operands = stack_op

        # _nums 배열에는 정상적인 계산 결과 1개의 숫자만이, _operands 는 비어있어야 한다
        assert(len(_nums) == 1)
        assert(len(_operands) == 0)
        answer = max(answer, abs(_nums[0]))

    return answer
##############################
# def get_value(op, a, b):
#     a, b = int(a), int(b)
#     if op == "*":
#         return a*b
#     elif op == "+":
#         return a+b
#     else:
#         return a-b
    
# def cal(ops, expression):
#     tmp = expression[:]
    
#     while(len(tmp) != 1):
#         for op in ops:
#             indexs = [i for i, value in enumerate(tmp) if value == op]\
#             for i, index in enumerate(indexs):
#                 if i!= 0:
#                     index -=2
#                 x = get_value(op, tmp[index-1], tmp[index+1])

#                 tmp[index] = x

#                 del tmp[index+1]
#                 del tmp[index-1]
        
#     return abs(tmp[0])

# def solution(expression):
#     digit = []
#     operator = []
#     for s in expression:
#         if not s.isdigit():
#             operator.append(s)
#             digit.append(" ")
#         else:
#             digit.append(s)
#     digit = "".join(digit).split(" ")
#     total = []
#     for a in range(len(digit)-1):
#         total.append(digit[a])
#         total.append(operator[a])
#     total.append(digit[-1])
#     operator = set(operator)
#     from itertools import permutations
#     operator = list(permutations(operator))
#     max_ = 0
#     for a in operator:
#         tmp = cal(a, total)
#         if tmp > max_:
#             max_ = tmp
#     return max_
