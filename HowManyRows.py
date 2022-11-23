
#A= [5,4,3,6,1]
A = [6,4,3,2,1,5,7,8,9]


def solution(A):

    tallestStudent = A[1]
    length = len(A)
    rows = 0


    for height in range(1, length - 1):
        
        if (A[height] > tallestStudent):
            tallestStudent = A[height]
            rows += 1

        else:
            pass

    return rows

print(solution(A)) 