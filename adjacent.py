def isValid(x,y,n,m):
    if x < 0 or y < 0 or x >= n or y >= m:
        return 0 
    return 1

def neighbours(arr : list, pos_x : int , pos_y: int) -> dict:
    n = len(arr)
    m = len(arr[0])
    alive = "██"
    dead = "  "
    nOfALiveDead = {alive : 0, dead : 0}
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)]
    for dx,dy, in directions:
        x , y = pos_x + dx, pos_y + dy
        if isValid(x ,y ,n , m):
            if arr[x][y] == alive:

                nOfALiveDead[alive] +=1
            else:
                nOfALiveDead[dead] +=1
        else:
 
            nOfALiveDead[dead] +=1
    return nOfALiveDead



