from itertools import combinations
import timeit

def has_sum_pair(numbers: list[int], target: int) -> bool:
    # Generate pairs of numbers using itertools combinations
    pairs = combinations(numbers, 2)
    for pair in pairs:
        if sum(pair) == target:
            return True
    return False

def has_sum_pair_v2(numbers: list[int], target: int) -> bool:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False

def has_sum_pair_v3(numbers: list[int], target: int) -> bool:
    for num in numbers:
        complement = target - num 
        if complement in numbers:
            return True
    return False
def has_sum_pair_v4(numbers: list[int], target: int) -> bool:
    stack =[]
    for num in numbers:
        complement = target - num 
        if  complement in stack:
            return True
        
        stack.append(num)
            
    return False
def has_sum_pair_v5(numbers: list[int], target: int) -> bool:#1
    stack =[]
    for num in numbers:
        complement = target - num
        if complement in stack:
            return True
        
        stack.append(num)
    return False
def has_sum_pair_v6(numbers: list[int], target: int) -> bool:
    number_set = set(numbers)
    stack = set()
    for num in number_set:
        complement = target - num
        if complement in stack:
                return True
        stack.add(num)
    return False
def has_sum_pair_v7(numbers: list[int], target: int) -> bool:#1
    for i,num in enumerate(numbers):
        complement = target - num
        if  complement in numbers[:i]:
            return True
    return False



def measure_the_execution():
    numbers: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,-200,
                      110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
                      210, 220, 230, 240, 250, 260, 270, 280, 290, 300,
                      310, 320, 330, 340, 350, 360, 370, 380, 390, 400,
                      410, 420, 430, 440, 450, 460, 470, 480, 490, 500,
                      510, 520, 530, 540, 550, 560, 570, 580, 590, 600,
                      610, 620, 630, 640, 650, 660, 670, 680, 690, 700,
                      710, 720, 730, 740, 750, 760, 770, 780, 790, 800,
                      810, 820, 830, 840, 850, 860, 870, 880, 890, 5000]
    target: int = 1800


    # Measure the execution time of has_sum_pair
    functions = {
        1: has_sum_pair,
        2: has_sum_pair_v2,
        3: has_sum_pair_v3,
        4: has_sum_pair_v4,
        5: has_sum_pair_v5,
        6: has_sum_pair_v6,
        7: has_sum_pair_v7,
    }

    for i in range(1, len(functions)+1):
        function = functions[i]
        time_function = timeit.timeit(lambda: function(numbers, target), number=100000)
        result_function = function(numbers, target)
        print(f"Execution time of {function.__name__}: {result_function}, {time_function}")

def test_functions(numbers: list[int], target: int,result:bool)->bool:

    result_has_sum_pair = has_sum_pair_v7(numbers, target)
    if result_has_sum_pair !=result:
        print(f"has_sum_pair_v6: {result_has_sum_pair}, target= {target},numbers= {numbers},result: =[{(result_has_sum_pair, result)}]")
    return result_has_sum_pair == result

def test_test():
    test_functions([10, 20, 30, 40, 50], 100, False)
    test_functions([10, 20, 30, 40, 50], 90, True)
    test_functions([10, 20, 30, 40, 50], 200, False)
    test_functions([], 100, False)
    test_functions([100], 100, False)
    test_functions([50, 50], 100, True)
    test_functions([40, 50], 100, False)
    test_functions([-10, 20, 30, -40, 50,+10], 0, True)
    test_functions([10, 20, 30, 40, 50], 0, False)
    test_functions([0.5, 1.5, 2.5, 3.5, 4.5], 4, True)
    test_functions([10, 10, 10, 10, 10], 40, False)
    test_functions([-10, -20, -30, -40, -50], -80, True)
    test_functions([1, 2, 3, 4, 5], 10, False)
    test_functions([100, 90, 80, 70, 60], 150, True)
    test_functions([10, 20, 30, 40, 50], 55, False)
    test_functions([10, 20, 30, 40, 50, 10], 60, True)
    test_functions([0, 20, 0, 40, 0], 40, True)
    test_functions([-10, 20, -30, 40, -50], 10, True)
    test_functions([42, 17, 6, 33, 98, 51, 23, 11, 74, 29], 100, False)
    test_functions([42, 17, 0, 33, 0, 51, 23], 74, True)
    test_functions([42, 17, -6, 33, -98, 51, 23], -53, False)

test_test()
#print(has_sum_pair_v6([10, 20, 30, 40, 50], 90,))
#measure_the_execution()