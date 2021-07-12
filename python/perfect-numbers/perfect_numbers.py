def classify(number):
    if number < 1:
        raise ValueError('This classification is only for natural numbers.')
    
    till = number//2 + 1

    lst = [i for i in range(1, till) if number % i == 0]
    
    aliquot = sum(lst)

    if aliquot == number:
        return 'perfect'

    if aliquot > number:
        return 'abundant'

    if aliquot < number:
        return 'deficient'
