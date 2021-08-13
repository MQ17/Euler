f = open("p067_triangle.txt")
large_triangle = [[int(item) for item in line.split()] for line in f.read().split('\n')][-2::-1]
print(large_triangle)

for i in range(1, len(large_triangle)):
    row = large_triangle[i]
    below = large_triangle[i-1]
    for j in range(len(row)):
        row[j] = max(below[j], below[j+1]) + row[j]

print(large_triangle[-1])
# large_triangle = [[1], [2, 3], [4, 5, 6]]
# left_triangle = [row[:-1] for row in large_triangle][1:]
# right_triangle = [row[1:] for row in large_triangle][1:]
# print(left_triangle)
# print(right_triangle)

# def max_triangle(triangle):
#     if len(triangle) == 1:
#         return triangle[0][0]
#     left_triangle = [row[:-1] for row in triangle][1:]
#     right_triangle = [row[1:] for row in triangle][1:]
#     return triangle[0][0] + max(max_triangle(left_triangle), max_triangle(right_triangle))
#
# print(max_triangle(large_triangle))

