#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    function to return a list of lists of integers representing pascal triangle of n
    """

    if (n <= 0):
        return []

    """Initializing an empty resulting array"""
    triangle = [[] for x in range(n)]

    for li in range(n):
        for col in range(li+1):
            if(col < li):
                if(col == 0):
                    """ the first column is always set to 1"""
                    triangle[li].append(1)
                else:
                    triangle[li].append(triangle[li-1][col] + triangle[li-1][col-1])
            elif(col == li):
                    """ the diagonal is always set to 1 """
                    triangle[li].append(1)

    return triangle


