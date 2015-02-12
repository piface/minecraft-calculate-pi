'''
Multiprocessing based code to estimate the value of PI
using monte carlo sampling
Ref: http://math.fullerton.edu/mathews/n2003/montecarlopimod.html
Uses workers:
http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
'''
 
import random
import multiprocessing
from multiprocessing import Pool
# import minecraftcircle
# import mcpi.minecraft as minecraft
# import mcpi.block
import block_drawer


# TNT = mcpi.block.TNT.id
# STONE = mcpi.block.STONE.id
# mc = minecraft.Minecraft.create()

def start_monte_carlo(n=500000):
    #TODO setup connection to minecraft

    np = multiprocessing.cpu_count()
    print 'You have {0:1d} CPUs'.format(np)
    block_drawer.save_checkpoint()
    # Number of shots


    #TODO wait for piface to press button to start

    #TODO eventually this will be in a loop which keeps running
    # make a clear a area of blocks (eventually do this by blowing up TNT from the last run)
    # where we will draw in minecraft
    # set viewer position to see it


    #create an array of n/np duplicated np times
    # i.e. for np = 4, creates [n/4,n/4,n/4,n/4]
    part_count=[n/np for i in range(np)]
 
    #Create the worker pool
    # http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
    pool = Pool(processes=np)

    print "starting to calculate"
    block_drawer.set_view()

 
    #this sets things off -- beware ctrl-c won't stop it again!
    count=pool.map(monteCarloShots, part_count)
 
    #TODO only show a few decimal places
    pi = sum(count)/(n*1.0)*4
    print "Pi estimated pi as ", pi


    block_drawer.write_to_screen("Pi estimated pi as " + str(pi))
    block_drawer.explode()


    #TODO turn on piface relay to drive indicator

    #TODO wait for piface button 
    #(turn off relay) and reset    
 
def monteCarloShots(n):
    print("hello")
    count = 0
    #take n potshots -- and return how many are inside the circle
    for i in range(n):
        x=random.random()
        y=random.random()
        # Check if lies inside circle
        if x*x + y*y <= 1:
            count=count+1

        if i%100 == 0:
    #     blockx = random(0,100)
    #     blocky = random(0,100)
            if x*x + y*y <= 1:
                block_drawer.draw_block(x, y, True)
            else:
                block_drawer.draw_block(x, y, False)

        #TODO maybe every now and again e.g. every 10000th point or similar do the equivalent of the above in minecraft
        # blockx = random(contrained to 0-100)
        # blocky = random(contrained to 0-100)
        ##if blockx*blockx + blocky*blocky <= 1:
        #    mcpi.drawblock(x,y,TNT)
#        else:
        #    mcpi.drawblock(x,y,BLACK)
    return count
 
 
if __name__=='__main__':

    start_monte_carlo()


