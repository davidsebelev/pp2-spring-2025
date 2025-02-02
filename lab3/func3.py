numheads = int(input())
numlegs = int(input())

#so the puzzle we solve like this, if we have 35 head we will have 70 legs , 94-70 = 24 so 
#now we need to do this 24/2 = 12 its rabbits and 35-12 = 23 chichkens
def puzzle(numheads,numlegs):
    allhlegs = numheads * 2
    legsstill = numlegs-allhlegs
    rabbits = legsstill/2
    return rabbits, numheads - rabbits

print(puzzle(numheads,numlegs))