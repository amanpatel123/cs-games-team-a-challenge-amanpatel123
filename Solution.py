from typing import List

'''
Sample Input: Simply copy this to make your life easy, or you can even copy the Solution class and paste it in leetcode to
check against all 87 testcases of leetcode

3
A B C E
S F C S
A D E E
ABCCED

Output: True
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        '''
            Check function is used to check if the position we are cheching is valid or not. 
            Just making sure that we are not checkig out of the grid 
        '''
        def check( i , j )-> bool:
            return i >= 0 and j >=0 and i < len(board) and j < len(board[0])
        

        '''
            You can guess from the name that this fucntion does dfs from the position provided
            which returns True when the nextNodeToLook == length of the word we are checking, since
            that's when we exploited our word completely and found a match in the grid

            If we can not find the match in any of the 4 possible direction then return False

            we temporarily change the value of visited node to '#' to make sure we dont check that node again

        '''
        def dfs(row, col, nextNodeToLook)-> bool:
        
        
            if nextNodeToLook == len_word:
                return True
            
            if( check(row,col) is False or board[row][col]!=word[nextNodeToLook]):
                return False
            
            tmp = board[row][col]
            board[row][col] = '#'
            

            found = False
            if(dfs(row-1, col, nextNodeToLook+1) or dfs(row, col-1, nextNodeToLook+1) or dfs(row+1, col, nextNodeToLook+1) or dfs(row, col+1, nextNodeToLook+1)):
                found = True
            
            board[row][col] = tmp
        
            return found
             
        
        len_word = len(word)
        row = len(board)
        col = len(board[0])
      
        for i in range(row):
            for j in range(col):          
                if(dfs(i, j , 0)) :                  
                    return True 
        return False

if __name__ == "__main__":
    mysol = Solution()

    # Get num of rows, then board
    len_r = int(input()) 
    board = [[x for x in input().split()] for i in range(len_r)]
    
    word = input()
    print(mysol.exist(board, word))
