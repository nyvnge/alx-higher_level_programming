#!/usr/bin/python3
"""pascal_triangle function"""


def pascal_triangle(n):
    """Reprs Pascals Triangle of size (n)
    returns list of lists of ints representing formation of the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        tmp = [1]
        for x in range(len(t) - 1):
            tmp.append(t[x] + t[x + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
