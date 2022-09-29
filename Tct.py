import random

b=[[i for i in range(j,j+3)] for j in range(0,9,3)]

def display():

for i in b:

for j in i:

print(j,'|',end=' ')

print('\n'+'-'*11)

print()

def check():

for i in range(3):

if b[0][i]==b[1][i] and b[1][i]==b[2][i]:

return True

if b[i][0]==b[i][1] and b[i][1]==b[i][2]:

return True

if b[0][0]==b[1][1] and b[1][1]==b[2][2]:

return True

if b[0][2]==b[1][1] and b[1][1]==b[2][0]:

return True

return False

choices=[[i,j] for i in range(1,4) for j in range(1,4)]

play=['X','Y']

display()

print('you are X')

i=0

while choices:

cur=play[i]

if i==0:

x=int(input("Enter row:"))

y=int(input("Enter col:"))

else:

x,y = random.choice(choices)

if type(b[x-1][y-1])==int:

choices.remove([x,y])

else:

print('Choose again')

continue

b[x-1][y-1]=cur

display()

if check():

print(cur,'Wins')

break

i = int(not i)

if choices==[]:

print('Draw')
