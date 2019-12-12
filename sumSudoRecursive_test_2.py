#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from collections import defaultdict
import time
import cProfile,pstats,io

class Struct():
    """Defines a dictionary with the 3X3 blocks for each cell 
    The key is a cell (i,j)
    The value is (blk_row,col_row) that corresponds to the slices for row,col 
    for 3X3 SLICE
    """

    #
    data_val = {}
    #######>>>>>>>>>Row 0>>>
    data_val[(0,0)] = (slice(0,3),slice(0,3))
    data_val[(0,1)] = (slice(0,3),slice(0,3))
    data_val[(0,2)] = (slice(0,3),slice(0,3))
    #####
    data_val[(0,3)] = (slice(0,3),slice(3,6))
    data_val[(0,4)] = (slice(0,3),slice(3,6))
    data_val[(0,5)] = (slice(0,3),slice(3,6))
    ###
    data_val[(0,6)] = (slice(0,3),slice(6,9))
    data_val[(0,7)] = (slice(0,3),slice(6,9))
    data_val[(0,8)] = (slice(0,3),slice(6,9))
    ###>>>>>>>>>>Row 1
    data_val[(1,0)] =  (slice(0,3),slice(0,3))
    data_val[(1,1)] = (slice(0,3),slice(0,3))
    data_val[(1,2)] = (slice(0,3),slice(0,3))
    #####
    data_val[(1,3)] = (slice(0,3),slice(3,6))
    data_val[(1,4)] = (slice(0,3),slice(3,6))
    data_val[(1,5)] = (slice(0,3),slice(3,6))
    ###
    data_val[(1,6)] = (slice(0,3),slice(6,9))
    data_val[(1,7)] = (slice(0,3),slice(6,9))
    data_val[(1,8)] = (slice(0,3),slice(6,9))

    ###>>>>>>>>>>Row 2
    data_val[(2,0)] =  (slice(0,3),slice(0,3))
    data_val[(2,1)] = (slice(0,3),slice(0,3))
    data_val[(2,2)] = (slice(0,3),slice(0,3))
    #####
    data_val[(2,3)] = (slice(0,3),slice(3,6))
    data_val[(2,4)] = (slice(0,3),slice(3,6))
    data_val[(2,5)] = (slice(0,3),slice(3,6))
    ###
    data_val[(2,6)] = (slice(0,3),slice(6,9))
    data_val[(2,7)] = (slice(0,3),slice(6,9))
    data_val[(2,8)] = (slice(0,3),slice(6,9))

    ###>>>>>>>>>>Row 3
    data_val[(3,0)] =  (slice(3,6),slice(0,3))
    data_val[(3,1)] = (slice(3,6),slice(0,3))
    data_val[(3,2)] = (slice(3,6),slice(0,3))
    #####
    data_val[(3,3)] = (slice(3,6),slice(3,6))
    data_val[(3,4)] = (slice(3,6),slice(3,6))
    data_val[(3,5)] = (slice(3,6),slice(3,6))
    ###
    data_val[(3,6)] = (slice(3,6),slice(6,9))
    data_val[(3,7)] = (slice(3,6),slice(6,9))
    data_val[(3,8)] = (slice(3,6),slice(6,9))

    ###>>>>>>>>>>Row 4
    data_val[(4,0)] =  (slice(3,6),slice(0,3))
    data_val[(4,1)] = (slice(3,6),slice(0,3))
    data_val[(4,2)] = (slice(3,6),slice(0,3))
    #####
    data_val[(4,3)] = (slice(3,6),slice(3,6))
    data_val[(4,4)] = (slice(3,6),slice(3,6))
    data_val[(4,5)] = (slice(3,6),slice(3,6))
    ###
    data_val[(4,6)] = (slice(3,6),slice(6,9))
    data_val[(4,7)] = (slice(3,6),slice(6,9))
    data_val[(4,8)] = (slice(3,6),slice(6,9))

    ###>>>>>>>>>>Row 5
    data_val[(5,0)] =  (slice(3,6),slice(0,3))
    data_val[(5,1)] = (slice(3,6),slice(0,3))
    data_val[(5,2)] = (slice(3,6),slice(0,3))
    #####
    data_val[(5,3)] = (slice(3,6),slice(3,6))
    data_val[(5,4)] = (slice(3,6),slice(3,6))
    data_val[(5,5)] = (slice(3,6),slice(3,6))
    ###
    data_val[(5,6)] = (slice(3,6),slice(6,9))
    data_val[(5,7)] = (slice(3,6),slice(6,9))
    data_val[(5,8)] = (slice(3,6),slice(6,9))

    ###>>>>>>>>>>Row 6
    data_val[(6,0)] =  (slice(6,9),slice(0,3))
    data_val[(6,1)] = (slice(6,9),slice(0,3))
    data_val[(6,2)] = (slice(6,9),slice(0,3))
    #####
    data_val[(6,3)] = (slice(6,9),slice(3,6))
    data_val[(6,4)] = (slice(6,9),slice(3,6))
    data_val[(6,5)] = (slice(6,9),slice(3,6))
    ###
    data_val[(6,6)] = (slice(6,9),slice(6,9))
    data_val[(6,7)] = (slice(6,9),slice(6,9))
    data_val[(6,8)] = (slice(6,9),slice(6,9))

    ###>>>>>>>>>>Row 7
    data_val[(7,0)] =  (slice(6,9),slice(0,3))
    data_val[(7,1)] = (slice(6,9),slice(0,3))
    data_val[(7,2)] = (slice(6,9),slice(0,3))
    #####
    data_val[(7,3)] = (slice(6,9),slice(3,6))
    data_val[(7,4)] = (slice(6,9),slice(3,6))
    data_val[(7,5)] = (slice(6,9),slice(3,6))
    ###
    data_val[(7,6)] = (slice(6,9),slice(6,9))
    data_val[(7,7)] = (slice(6,9),slice(6,9))
    data_val[(7,8)] = (slice(6,9),slice(6,9))

    ###>>>>>>>>>>Row 8
    data_val[(8,0)] =  (slice(6,9),slice(0,3))
    data_val[(8,1)] = (slice(6,9),slice(0,3))
    data_val[(8,2)] = (slice(6,9),slice(0,3))
    #####
    data_val[(8,3)] = (slice(6,9),slice(3,6))
    data_val[(8,4)] = (slice(6,9),slice(3,6))
    data_val[(8,5)] = (slice(6,9),slice(3,6))
    ###
    data_val[(8,6)] = (slice(6,9),slice(6,9))
    data_val[(8,7)] = (slice(6,9),slice(6,9))
    data_val[(8,8)] = (slice(6,9),slice(6,9))
    
    def __init__(self):
        pass
    


class Statistic:
    """Defines statistics for the Sudoku recursion"""
    def __init__(self):
        self.backtrack=0 #sum the number of backtracks
        self.end_time=0
        self.start_time=0
        self.backtrack_distr = defaultdict(int) #sum number of backtracks per (i,j)
        
    def get_stats(self):
        exec_time =  self.end_time - self.start_time
        return(self.backtrack,exec_time,self.backtrack_distr)
    
        
#def find_next_cell(grid):
#    """Find next empty cell to be filled row by row.
#       Empty cell contains 0
#    """
#    for indx,v in np.ndenumerate(grid):
#        if not v:
#            return (indx[0],indx[1]) 
#    return (-1,-1)
def find_next_cell(grid):
    """Find next empty cell to be filled row by row.
       Empty cell contains 0
    """
    try:
        res = np.argwhere(grid==0)
        return (res[0][0],res[0][1])
    except IndexError:
        return(-1,-1)
        
def is_valid(grid,i,j,e):
    """ Check if this value e is Sudoku valid in position i,j"""
    col = j
    row = i
    brow,bcol = Struct.data_val[(i,j)] #get slices for a 3X3 submatrix
    comb = set(grid[:,col]).union(set(grid[row]),set(grid[brow,bcol].flat))
    if e in comb:
        return False
    else:
        return True

    
def check_sum(i,j,e,coord):
    """Check if this value "e" fullfills the sum requirement in the cage"""
    if not (i,j) in coord:
        return True
    if (coord[(i,j)].current_sum + e == coord[(i,j)].target) and (coord[(i,j)].chk_status()-1 == 0 ):
        return True
    elif (coord[(i,j)].current_sum + e < coord[(i,j)].target) and (coord[(i,j)].chk_status()-1 > 0 ):

        return True
    else:
        return False
        
        
    
def profiler(fnc):
    """A decorator that uses cProfile for a function fnc"""
    def wrapper(*args,**kvargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args,**kvargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr,stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return wrapper
        
    
    
    
#def sudoku_validate(grid):
#    """
#    check if the initial data is valid
#    if there is an input value > 0:
#    check if the column is unique
#    check if the row is unique
#    check if the square(3X3) is unique
#    Input is 9X9 numpy array 
#    """
#    for ind,val in np.ndenumerate(grid):
#        if val:
#            col= ind[1]
#            row = ind[0]
#            brow,bcol = Struct.get_2D_blk(row,col)
#            #Collect unique values and counts for row col, squares
#            unique_r,counts_r = np.unique(grid[row],return_counts=True)
#            unique_c,counts_c = np.unique(grid[:,col],return_counts=True)
#            unique_sq,counts_sq = np.unique(grid[brow,bcol].flat,return_counts=True)
#            #All counts must be 1 with exception of 0 (first element)
#            if (((counts_r[1:] == 1).all()) & ((counts_c[1:] == 1).all()) & ((counts_sq[1:] == 1).all())):
#                continue
#            else:
#                return False
#        else:
#            continue
#    return True
#@profiler
             
def start_sumSudo(grid,coord):
    """ A wrapper function to reset some data and
        Start the Sumsudoku game
    """
    stat = Statistic()

    stat.start_time = time.time()
    res = sumSudo_solver(grid,coord,stat)
    stat.end_time =  time.time()
    if not res:
        print("Some error in the sudoku solver")
        return(0)
    return stat
    
#This procedure solves the Sudoku one step at the time
  
def sumSudo_solver(grid,coord,stat):
    #find next empty cell to fill
    i,j = find_next_cell(grid)
    if i == -1: return True #The end
    #find possible candidates to fell the next cell
    if (i,j) in coord:
        candidate = coord[(i,j)].find_candidate()
    else:
        candidate = [1,2,3,4,5,6,7,8,9]
        
    for e in candidate:
        if (is_valid(grid,i,j,e)) and check_sum(i,j,e,coord):
            grid[i,j] = e
            if (i,j) in coord:
                coord[(i,j)].inc_sum(e)
            if sumSudo_solver(grid,coord,stat):
                return True
            #failed attempt
            #undo current cell for back track
            stat.backtrack += 1
            if stat.backtrack%3000000 == 0:
                print(stat.backtrack,(i,j))
            stat.backtrack_distr[(i,j)] += 1
            grid[i,j] = 0
            if (i,j) in coord: 
                coord[(i,j)].dec_sum(e)
    return False

    



