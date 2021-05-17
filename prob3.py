# ba str miram vaght shod file migiram
import sys


def swapcase_decorator(gen):
    def wrapper(*args, **kwargs):
        f = gen(*args, **kwargs)
        yield f.swapcase()

    yield wrapper
# TypeError: 'generator' object is not callable ?????????????????????????????????

# @swapcase_decorator
def duplicate_words_gen(string: str):
    # duplicates = {}
    # chars = "abcdefghijklmnopqrstuvwxyz"
    # for i in chars:
    #     duplicates[i] = 0
    # for char in chars:
    #     for chrrr in string.split():
    #         if char in chrrr:
    #             duplicates[char] += 1
    #     for key, value in duplicates.items():
    #         if value > 1:
    #             yield key, value
    duplicates = []
    for char in string:
        if string.count(char) > 1:
            if char not in duplicates:
                yield char
    # print(*duplicates)


# for i in duplicate_words_gen('salaaam dadashsh'):
#     print(i)

for i in duplicate_words_gen('salaaam dadashsh'):
    print(i)

if __name__ == '__main__':
    print(sys.argv)
