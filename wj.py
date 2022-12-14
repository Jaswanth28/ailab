from collections import defaultdict
c=0
jug1, jug2, aim = 4, 3, 3
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2,c):
    c+=1
    if (amt1 == aim and amt2 == aim):
        #print(amt1, amt2)
        print("minimum no of steps:",c)
        return True
    if visited[(amt1, amt2)] == False:
        #print(amt1, amt2)
        visited[(amt1, amt2)] = True
        return (waterJugSolver(0, amt2,c) or waterJugSolver(amt1, 0,c) or waterJugSolver(jug1, amt2,c) or
                        waterJugSolver(amt1, jug2,c) or 
                        waterJugSolver(amt1 + min(amt2, (jug1-amt1)),amt2 - min(amt2, (jug1-amt1)),c) or
                        waterJugSolver(amt1 - min(amt1, (jug2-amt2)),amt2 + min(amt1, (jug2-amt2)),c))
    else:
        return False
waterJugSolver(0, 0,c)
