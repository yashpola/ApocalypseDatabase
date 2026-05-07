import random
import itertools

N = 100000
words = list(itertools.permutations("abcdef", 6))
words_length = len(words)

with open("records.csv", mode="a") as f:
    for i in range(N):
        f.write(f'{i}, {"".join(words[random.randint(0, words_length - 1)])}\n')

