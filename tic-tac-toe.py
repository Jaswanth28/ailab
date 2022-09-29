board=[['0','1','2'],['3','4','5'],['6','7','8']]
users=[]
chances=0
place=['X','O']
def display():
    for i in board:
        for j in i:
            print(j,"|",end=" ")
        print("\n"+"-"*11)
    print()

def check():
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            return True 
        if board[0][i]== board[1][i]  and board[1][i]== board[2][i] :
            return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        return True
    return False
   
display()
while chances<9:
    while True:
        while len(users)<2:
            print(f'enter player {len(users)+1} name')
            users.append(input())
        index=int(input(users[chances%2]+str(chances%2+1)+" : Enter the cell you want to mark "+place[chances%2]+" :  "))
        r=int(index/3)
        c=index%3
        if board[r][c].isdigit():
            board[r][c]=place[chances%2]
            break
        else:
            print("The following cell is already occupied. Choose another")
    
    display()
    if check():
        print("User",users[chances%2],"WINNER! ") 
        break
    chances+=1
if chances==9:
    print("Draw!!")
