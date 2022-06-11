def find_positive_and_negative(*args):
    positive = 0
    negative = 0

    for el in args:
        if el > 0:
            positive += el
        else:
            negative += el
    return positive, negative


nums = [int(x) for x in input().split()]

positive, negative = find_positive_and_negative(*nums)  # Паква ми ги
print(negative)
print(positive)

if abs(negative) > positive:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
