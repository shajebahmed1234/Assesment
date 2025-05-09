matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
var = [j for i in matrix for j in i]
var.sort()
print(var[k-1])



matrix = [
  [1, 2, 3, 4],
  [5, 1, 2, 3],
  [9, 5, 1, 2]
]

rows = len(matrix)
cols = len(matrix)
var = True
for i in range(rows-1):
  for j in range(cols-1):
    if matrix[i][j] != matrix[i+1][j+1]:
      var = False
      break
    if not var:
      break
print(var)



from itertools import permutations
input = "abc"
var = ["".join(i) for i in permutations(input)]
print(var)




