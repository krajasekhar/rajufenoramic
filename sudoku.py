import math
class Solution:
    #Validates the selection for duplicates
    def ValidCell(self,sel):
        mysel=[]
        mysel=sel[:]
        while mysel.count(0)>0:
            mysel.remove(0)
        tset=list(set(mysel))
        if len(tset)!=len(mysel):
            print(mysel)
            return 0
        return 1
        
    def ValidSudoku(self,input1):
        ns=len(input1)
        n=int(math.sqrt(ns))
        matrix=[]
        #Row Validations
        for row in input1:
            rowArr=[]
            for each in row:
                if each==".":
                    num=0
                else:
                    num=int(each)
                    if num > ns:
                        return 0
                rowArr.append(num)
            matrix.append(rowArr)
        for row in matrix:
            if self.ValidCell(row)==0:
                return 0
        #Column Validations
        colArr=[]
        colArr=zip(*matrix)
        colArr=[list(row) for row in colArr]
        for col in colArr:
            if self.ValidCell(col)==0:
                return 0
        #Sub matrices validations
        boxArr=[[]*ns]*ns
        for i in range(0,ns):
            for j in range(0,ns):
                index=((i)/n)*n + j/n
                boxArr[index]=boxArr[index]+[matrix[i][j]]
        
        for box in boxArr:
            if self.ValidCell(box)==0:
                return 0
        return 1
    
    
ip1_rows = 0
ip1_cols = 0
# ip1_rows = int(raw_input())
# ip1_cols = int(raw_input())
# ip1 = []
# for ip1_i in xrange(ip1_rows):
#     ip1_temp = map(int,raw_input().strip().split(' '))
#     ip1.append(ip1_temp)
# ip1 = [[1, 2, 3, 0], [4, 3, 0,0], [3, 4, 1, 2], [2,1, 4, 3]]
A=["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
tp=tuple(A)
print(tp)
sol=Solution()
output = sol.ValidSudoku(tp)
print(str(output))