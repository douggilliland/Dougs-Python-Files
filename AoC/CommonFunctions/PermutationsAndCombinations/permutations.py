import itertools

newList = list(itertools.permutations([1,2,3,4]))
# [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]
print(len(newList))
# 24

newList = list(itertools.combinations([1,2,3,4],2))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

newList = list(itertools.combinations([1,2,3,4],3))
#[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

newList = list(itertools.combinations_with_replacement([1,2,3,4],3))
#[(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 3, 3), (1, 3, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 3), (2, 3, 4), (2, 4, 4), (3, 3, 3), (3, 3, 4), (3, 4, 4), (4, 4, 4)]
print(len(newList))
# 20

newList = list(itertools.accumulate([1,2,3,4]))
# [1, 3, 6, 10]

for i in itertools.count(1):
	print(i)
	if i==3:
		break
# 1
# 2
# 3

