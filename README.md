# Forest Fire Simulation

In this project, I developed a graphical simulation that analyzes how forest fires spread and how forests regrow after fires. Each time step of the simulation represents one day.

On each day, if a tree is on fire, it might turn to ashes on the next day. If a tree is ashes, it might turn into a sprout (i.e. baby tree). If a tree is a sprout, it might start growing into a sapling. If a tree is a sapling, it might reach maturity. If a tree is mature and at least one of its neighbors is on fire, it might ignite (i.e. catch on fire).

This simulation shows how the forest evolves over time, represented by a square N x N matrix.

Color encoding:
* black - ASHES
* light green - SPROUT
* green - SAPLING
* dark green - MATURE
* red - ON_FIRE

<img width="400" alt="Figure 1" src="https://user-images.githubusercontent.com/60496370/73511692-d75abe00-43a3-11ea-9147-84c8e7282bf7.png">

Each snapshot above is a time step of the simulation shown in a 750 by 750 window (in pixels). The window is "divided" up into 10 x 10 squares. Each of these 100 squares represents one tree in the simulated forest.

update_trees(trees,p_cools,p_grows,p_ignites,p_jump) takes the parameter trees, which is a 2D matrix representing the current state of our forest. The parameters p_cools, p_grows, p_ignites represent decimal probabilities from 0 to 1 that indicate the likelihood of a tree cooling, growing, or igniting, respectively. This function update_trees returns a new 2D matrix new_trees representing the forest during the next time step (i.e. after one day has passed).

jump_feature(trees,new_trees,row,col,p_jump) implements a jump feature for a specific tree, the tree at trees[row][col]. new_trees represents the 2D matrix for the next stage of the forest. p_jump represents a decimal probability from 0.0 to 1.0 that the jump feature will occur.
