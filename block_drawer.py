
# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block
import random

TNT = mcpi.block.TNT.id
STONE = mcpi.block.STONE.id
SHELF = mcpi.block.BOOKSHELF.id
AIR = mcpi.block.AIR.id
ICE = mcpi.block.ICE.id
LAVA = mcpi.block.LAVA.id

GRID_SIZE = 16
OFFSET = 5

mc = minecraft.Minecraft.create()

def write_to_screen(message):
	mc.postToChat(message)

def explode():
	print "explode"
	# mc.player.setPos(1,25,25) # Move player to be in front of TNT
	# mc.player.

def set_view():
	mc.player.setPos(26, 8, 25)

def save_checkpoint():
	mc.saveCheckpoint()

def restore_checkpoint():
	# restores state of world to last saved checkpoint
	mc.restoreCheckpoint()

def clear():
	for i in range(GRID_SIZE*2):
		for j in range(GRID_SIZE*2):
			mc.setBlock(0,i+ OFFSET,j,AIR)

def draw_block(x,y,inside):
	rx= random.choice([-1,1])
	ry= random.choice([-1,1])
	x = (int(x*GRID_SIZE)*rx)+ GRID_SIZE 
	y = (int(y*GRID_SIZE)*ry) + GRID_SIZE

	if inside:
		block = TNT
	else:
		block = ICE

	
	mc.setBlock(0,x+ OFFSET, y, block, 1) # Set to 1 to live

