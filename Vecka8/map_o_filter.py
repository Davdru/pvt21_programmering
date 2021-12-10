

list_of_nums = list(range(1000))

# Ta fram alla tal ur list_of_nums som är jämna list_of_even_nums
# Alla tal som är udda list_of_odd_nums


def even(n: int) -> bool:
    return n % 2 == 0


def odd(n: int) -> bool:
    return not even(n)

#
# list_of_even_nums = []
# for i in list_of_nums:
#     if even(i):
#         list_of_even_nums.append(i)


def square(n):
    return n*n


list_of_even_nums = list(filter(even, list_of_nums))
list_of_odd_nums = list(filter(odd, list_of_nums))

print(list_of_even_nums)
print(list_of_odd_nums)


res = list(map(square, list_of_odd_nums))
print(res)