import math
# def perp(a, origin, b):
#     avector = (a[0]-origin[0], a[1]-origin[1])
#     bvector = (b[0]-origin[0], b[1]-origin[1])
#     dot = avector[0]*bvector[0] + avector[1]*bvector[1]
#     return dot == 0
# def triangle(n):
#     count = 0
#     for x1 in range(n+1):
#         for y1 in range(n+1):
#             for x2 in range(n+1):
#                 for y2 in range(n+1):
#                     origin = (0, 0)
#                     a = (x1, y1)
#                     b = (x2, y2)
#                     if a==b or a==origin or b==origin:
#                         continue
#                     if perp(a, origin, b) or perp(origin, b, a) or perp(b, a, origin):
#                         count += 1
#     print(count/2)

def triangle(n):
    s = 0
    for x in range(1, n+1):
        for y in range(1, n):
            g = math.gcd(x, y)
            k = x/y;
            if k*x + y > n:
                s += g*(n-y)//x
            else:
                s += g*x//y
    return 2*s + 3*n**2

print(triangle(50))
