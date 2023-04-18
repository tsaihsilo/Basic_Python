def is_prime(user_input):
    container = []
    for i in range(1, user_input + 1):
        s = user_input / i
        if s.is_integer():
            container.append(int(s))
            continue
        continue
    return bool(len(container) <= 2)

def are_relatively_prime(user_input1, user_input2):
    container1 = []
    container2 = []
    for i in range(1, user_input1):
        s = user_input1 / i
        if s.is_integer():
            container1.append(int(s))
        continue
    for i in range(1, user_input2):
        s = user_input2 / i
        if s.is_integer():
            container2.append(int(s))
        continue
    for j in container1:
        for k in container2:
            if j == k:
                r = False
                break
            else:
                r = True
            continue
        continue
    return r

def primes(user_input3):
    container3 = []
    for i in range(2, user_input3 + 1):
        n = is_prime(i)
        if n == True:
            container3.append(i)
            continue
    return container3

def prime_decomposition(user_input4):
    container4 = []
    prime_nums = primes(user_input4)
    start = True
    while start:
        if user_input4 in prime_nums:
            start = False
            container4.append(user_input4)
            container4.sort()
            return container4
        elif user_input4 == 1:
            start = False
            container4.sort()
            return container4
        else:
            for i in prime_nums:
                if user_input4 % i == 0:
                    container4.append(i)
                    user_input4 = user_input4 // i 
                    continue