##### Forest Fire #####

import random, time, tkinter

# GLOBALS #
ASHES = 0
SPROUT = 1
SAPLING = 2
MATURE = 3
ON_FIRE = 4

TREE_SIDE = 50
TREE_SPACE = 5
WIDTH = 750
HEIGHT = 750

def setup_graphics():
  window = tkinter.Tk()
  c = tkinter.Canvas(window, width=WIDTH, height=HEIGHT)
  c.pack()
  return c

def get_left_margin(N):
  return (WIDTH - (N*TREE_SIDE + (N-1)*TREE_SPACE)) // 2

def get_top_margin(N):
  return (HEIGHT - (N*TREE_SIDE + (N-1)*TREE_SPACE)) // 2

"""
  inputs:
    N - side length of 2D list
    num_saplings - number of saplings in starting forest
    num_mature - number of mature trees in starting forest
    num_on_fire - number of trees on fire in starting forest
  output:
    returns 2D list representing starting state of forest
"""

from random import shuffle
# setup_trees randomly generates a 2D matrix representing 
# the starting state of the forest 
def setup_trees(N, num_saplings, num_mature, num_on_fire):
    trees=[]
    lst1=num_saplings*[SAPLING]+num_mature*[MATURE]+num_on_fire*[ON_FIRE]
    lst2=(N**2-(num_saplings + num_mature + num_on_fire))*[SPROUT]
    lst3=trees+lst1+lst2
    shuffle(lst3)
    count=0
    for i in range(N):
        row=[]
        for j in range(N):
            row.append(lst3[count])
            count=count+1
        trees.append(row)
    return trees

"""
  inputs:
    trees - 2D list representing current state of forest
    c - Canvas for Tkinter
    day - current day of simulation
  output:
    displays current state of trees on c, the Tkinter Canvas
    returns None
"""

# display_trees displays the current state of the forest 
# using the Tkinter Canvas
def display_trees(trees, c, day):
    c.delete(tkinter.ALL) 
    c.pack()
    N=len(trees)
    colors={ASHES:'black', SPROUT:'light green', SAPLING:'green',
                MATURE:'dark green',ON_FIRE:'red'}
    for i in range(0,N):
        for j in range(0,N):
            color=colors[trees[i][j]]
            width_of_text_box=5*TREE_SIDE + 3*TREE_SPACE + get_left_margin(N)
            c.create_text((width_of_text_box,50), text="FOREST FIRE")
            c.create_text((width_of_text_box,650), text=('Day',day))
            topleft_x=(get_left_margin(N) + j*TREE_SIDE)
            topleft_y=(get_top_margin(N) + i*TREE_SIDE)
            downright_x=(get_left_margin(N)+(j+1)*TREE_SIDE)
            downright_y=(get_top_margin(N)+(i+1)*TREE_SIDE)
            c.create_rectangle(topleft_x, topleft_y, downright_x, downright_y,
                        fill=color, outline='white', width=TREE_SPACE)
    c.update()

"""
  inputs:
    trees - 2D list representing current state of forest
    p_cools - probability of a tree cooling
    p_grows - probability of a tree growing
    p_ignites - probability of a tree igniting on fire
    p_jump - probability of a tree using the jump feature
  output:
    returns a new 2D list representing the next state of the forest
"""

def update_trees(trees, p_cools, p_grows, p_ignites, p_jump):
    N = len(trees)
    new_trees = list(trees)
    for i in range(0,N):
        for j in range(0,N):
            if trees[i][j]==MATURE:
                above=i-1 
                left=j-1 
                right=j+1 
                down=i+1 
                if above>=0: #check top cell
                    if trees[above][j]==ON_FIRE:
                        if event(p_ignites)==True:
                            new_trees[i][j]=ON_FIRE
                if left>=0: #check left cell
                    if trees[i][left]==ON_FIRE:
                        if event(p_ignites)==True:
                            new_trees[i][j]=ON_FIRE
                if down<N: #check bottom cell
                    if trees[down][j]==ON_FIRE:
                        if event(p_ignites)==True:
                            new_trees[i][j]=ON_FIRE
                if right<N: #check right cell  
                    if trees[i][right]==ON_FIRE:
                        if event(p_ignites)==True:
                            new_trees[i][j]=ON_FIRE
                jump_feature(trees, new_trees, i, j, p_jump)
            if trees[i][j]!=MATURE and trees[i][j]!=ON_FIRE:
                if event(p_grows)==True:
                    if trees[i][j]==ASHES:
                        new_trees[i][j]=SPROUT
                    else:
                        if trees[i][j]==SPROUT:
                            new_trees[i][j]=SAPLING
                        else:
                            if trees[i][j]==SAPLING:
                                new_trees[i][j]=MATURE
                else: 
                    new_trees[i][j]=trees[i][j]
            if trees[i][j]==ON_FIRE:
                if event(p_cools)==True:
                    new_trees[i][j]=ASHES
                else:
                    new_trees[i][j]=ON_FIRE
    return new_trees

# event(p) is a helper function that takes in a decimal p as an argument and 
# returns True with probability p and False otherwise
def event(p):
    if random.random()<p:
        return True
    else:
        return False

"""
  inputs:
    trees - 2D list representing current state of forest
    new_trees - 2D list representing next stage of the forest
    row - row of current tree being considered for jump feature
    col - col of current tree being considered for jump feature
    p_jump - probability of current tree using the jump feature
  output:
    modifies new_trees if jump feature is successful (based on writeup)
    returns None
"""

def jump_feature(trees, new_trees, i, j, p_jump):
    N = len(trees)   
    if trees[i][j]==MATURE: 
        if event(p_jump)==True:
            if i>=2:
                x=random.randint(0,i-2) #check upwards from trees[i][j]
                if trees[x][j]==ON_FIRE:
                    new_trees[i][j]=ON_FIRE
            if i<N-3 and N>1:
                y=random.randint(i+2,N-1) #check upwards from trees[i][j]
                if trees[y][j]==ON_FIRE:
                  new_trees[i][j]=ON_FIRE
            if j>=2:
                z=random.randint(0,j-2) #check left from trees[i][j]
                if trees[i][z]==ON_FIRE:
                    new_trees[i][j]=ON_FIRE
            if j<N-3 and N>1:
                e=random.randint(j+2,N-1) #check right from trees[i][j]
                if trees[i][e]==ON_FIRE:
                    new_trees[i][j]=ON_FIRE
        else:
            new_trees[i][j]= MATURE
    return None

# Run
def run_sim(iterations, N, num_saplings, num_mature, num_on_fire, p_cools,
            p_grows, p_ignites, p_jump):
  random.seed(15110)
  c = setup_graphics()
  if iterations < 0 or N <= 0:
    print("Invalid iterations or N.")
    return None
  if not (0 <= p_cools <= 1 and 0 <= p_grows <= 1 and 0 <= p_ignites <= 1):
    print("Invalid probabilities.")
    return None
  total_non_sprouts = num_saplings + num_mature + num_on_fire
  total_trees = N**2
  if not (0 <= num_saplings and 0 <= num_mature and 0 <= num_on_fire 
                and 0 <= total_non_sprouts <= total_trees):
    print("Invalid numbers of saplings, mature, and on fire trees.")
    return None
  trees = setup_trees(N, num_saplings, num_mature, num_on_fire)
  display_trees(trees, c, 0)
  for i in range(iterations):
    time.sleep(1)
    trees = update_trees(trees, p_cools, p_grows, p_ignites, p_jump)
    display_trees(trees, c, i+1)
