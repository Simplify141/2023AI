def BinarySearch(nums, target):
    size=len(nums)
    low=0
    high=size-1
    while nums[(int)((low+high)/2)]!=target:
        if nums[(int)((low+high)/2)]<target:
            low=(int)((low+high)/2)+1
        else: high=(int)((low+high)/2)-1 
    return (int)((low+high)/2)

def MatrixAdd(A, B):
    if len(A)!=len(B)|len(A[0])!=len(B[0]): 
        return []
    matrix=[[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            matrix[i][j]=A[i][j]+B[i][j]
    return matrix

def MatrixMul(A, B):
    if len(A[0])!=len(B): 
        return []
    matrix=[[0 for i in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                matrix[i][j]+=A[i][k]*B[k][j]
    return matrix

def ReverseKeyValue(dict1):
    newDict={}
    for name, code in dict1.items():
        newDict[code]=name
    return newDict


if __name__ == "__main__":
    print("输出", BinarySearch([-1, 0, 3, 5, 9, 12, 17, 22], 17), "答案", 4)
    print("输出", MatrixAdd([[1,0,22],[0,1,0]], [[1,2,3],[3,4,7]]), "答案", [[2, 2], [3, 5]])
    print("输出", MatrixMul([[1,0,1],[0,1,0]], [[1,2],[3,4],[5,6]]), "答案", [[1, 2], [3, 4]])
    print("输出", ReverseKeyValue({'Alice':'001', 'Bob':'002'}), "答案", {'001':'Alice', '002':'Bob'})