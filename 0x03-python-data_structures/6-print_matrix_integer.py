#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        if matrix is not None:
                for x in matrix:
                        for val in x:
                                print("{:d}".format(val), end=''
                                      if val == x[len(x) - 1] else ' ')
                        print()
