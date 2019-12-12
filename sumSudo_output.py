# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:00:00 2019

@author: Andre
"""
import tkinter as tk


###################Configure the "Result Frame"

#Table  with offsets to convert frame position into matrix coordinates
offset_table={0:(0,0),1:(0,3),2:(0,6),
         3:(3,0),4:(3,3),5:(3,6),
         6:(6,0),7:(6,3),8:(6,6)}

#A result Frame contains a (9x9) matrix with the game results
#The result matrix is divided into 9 sub matrices (3X3)
#Each sub matrix is an own frame with 9 labels
#Each label contains one result
#The labels with initial data are highlighted
def gen_sumOutput(fr,data,coord_dic):
    
    """
    Generate a matrix (9x9) with the sumSudoku results.
    The matrix is placed in the "result Frame"
    The input are:
        -A Frame (fr) that will contain the result matrix
        -A numpy 2D array(data) with the game results. It is a 9X9 array.
        -A dictionary with cages
    """
    
    tk.Label(fr,text="Result",font='helvetica 18').grid(row=0,columnspan=3)
    frame = []

    for cr in ((1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)):
        frame_temp=tk.Frame(fr, highlightbackground="blue", highlightcolor="blue", highlightthickness=1, width=200, height=200, bd= 0)
        frame_temp.grid(row=cr[0],column=cr[1])
        frame.append(frame_temp)
    
    for ind,f in enumerate(frame):
        offset=offset_table[ind]
        for cr in ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)):
            if  coord_dic.get((offset[0]+cr[0],offset[1]+cr[1]),""):
                txt = tk.Label(master=f,width=3,height=1,text=data[(offset[0]+cr[0],offset[1]+cr[1])],font='Helvetica 10 bold italic',
                                                                   bg =coord_dic[(offset[0]+cr[0],offset[1]+cr[1])].get_color())
            else:
                txt = tk.Label(master=f,width=3,height=1,text=data[(offset[0]+cr[0],offset[1]+cr[1])],font='Helvetica 10')
            txt.grid(row=cr[0],column=cr[1])


    