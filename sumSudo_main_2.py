# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:00:00 2019

@author: Andre
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from sumSudo_output import gen_sumOutput
from sumSudoRecursive_test_2 import start_sumSudo
from datetime import datetime
import random
import sys

sudoku = np.zeros((9,9),dtype=np.int16)
coord_dict = {}
cage_dict  = {}



class Cage():
    #DEfines possible colours to color cages
    color = ['pink3', 'orange','gray','light sky blue','dark khaki','LightCyan2','LightYellow2',
            'LightPink1','light sea green','pale goldenrod','PaleGreen4','SeaGreen3',
            'coral','MediumPurple1','orchid2','slate blue']
   
   #Defines a dictionary of all possible sums of 2 numbers (1-9)
    sum2_dict = {}
    sum2_dict[2] = [1]
    sum2_dict[3] = [1,2]
    sum2_dict[4] = [1,2,3]
    sum2_dict[5] = [1,2,3,4]
    sum2_dict[6] = [1,2,3,4,5]
    sum2_dict[7] = [1,2,3,4,5,6]
    sum2_dict[8] = [1,2,3,4,5,6,7]
    sum2_dict[9] = [1,2,3,4,5,6,7,8]
    sum2_dict[10] =[1,2,3,4,5,6,7,8,9]
    sum2_dict[11] =[2,3,4,5,6,7,8,9]
    sum2_dict[12] =[3,4,5,6,7,8,9]
    sum2_dict[13] =[4,5,6,7,8,9]
    sum2_dict[14] =[5,6,7,8,9]
    sum2_dict[15] =[6,7,8,9]
    sum2_dict[16] =[7,8,9]
    sum2_dict[17] =[8,9]
    sum2_dict[18] =[9]
    
    #Defines a dictionary of all possible sums of 3 numbers (1-9)
    sum3_dict = {}
    sum3_dict[3] = [1]
    sum3_dict[4] = [1,2]
    sum3_dict[5] = [1,2,3]
    sum3_dict[6] = [1,2,3,4]
    sum3_dict[7] = [1,2,3,4,5]
    sum3_dict[8] = [1,2,3,4,5,6]
    sum3_dict[9] = [1,2,3,4,5,6,7]
    sum3_dict[10] =[1,2,3,4,5,6,7,8]
    sum3_dict[11] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[12] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[13] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[14] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[15] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[16] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[17] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[18] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[19] =[1,2,3,4,5,6,7,8,9]
    sum3_dict[20] =[2,3,4,5,6,7,8,9]
    sum3_dict[21] =[3,4,5,6,7,8,9]
    sum3_dict[22] =[4,5,6,7,8,9]
    sum3_dict[23] =[5,6,7,8,9]
    sum3_dict[24] =[6,7,8,9]
    sum3_dict[25] =[7,8,9]
    sum3_dict[26] =[8,9]
    sum3_dict[27] =[9]
    

    def __init__(self, kind,coord,target=0):
        self.kind = kind
        self.color = 0
        self.coord_list = []
        self.coord_list.append(coord)
        self.target = int(target)
        self.current_sum = 0
        self.current_nr = 0 #number of cells currently used
        
        
        
    def set_target(self,target):
        self.target = int(target)
        
    def set_coord(self,coord):
        self.coord_list.append(coord)
    
    def set_color(self,color):
        self.color = color
    
    def get_color(self):
        return self.color
        
    def inc_sum(self,val):
        self.current_sum += val
        self.current_nr += 1
        
    def dec_sum(self,val):
        self.current_sum -= val
        self.current_nr -= 1
            
    def chk_status(self):
        return (len(self.coord_list) - self.current_nr) 
    
    def find_candidate(self):
        """
        Find sum candidates for the free cells in a cage.
        There are two special cases with reduced candidates:
            -if the cage has two free cells or
            -if the cage has three free cells
            -one free cell
        Otherwise return the digits 1-9 
        """
        if (len(self.coord_list) - self.current_nr) == 3:
            return Cage.sum3_dict[self.target-self.current_sum]
        elif (len(self.coord_list) - self.current_nr) == 2:
            return Cage.sum2_dict[self.target-self.current_sum]
        elif (len(self.coord_list) - self.current_nr) == 1:
            return [self.target - self.current_sum]
        else: return [1,2,3,4,5,6,7,8,9]
            
            
        



def start():
    """
    Read data from the Entries.
    Start the Sudoku game
    """
    global sudoku
    sudoku.fill(0)
    
    #scan all entries and collect cages and sum targets
    #format is a10
    for k,v in ent_dict.items():
        txt = v.get()
        if txt:
            if txt.isalpha():
                txt1 = txt
                target=0
            elif (txt[0].isalpha()) & (txt[1:].isdigit()):
                txt1 = txt[0]
                target = txt[1:]
            else:
                print("Error when reading in data")
                print(txt)
            
            if not txt1 in cage_dict:
                cage_dict[txt1] = Cage(txt1,k,target)
                coord_dict[k] = cage_dict[txt1]
            else:
                coord_dict[k] = cage_dict[txt1]
                cage_dict[txt1].set_coord(k)
                if target:
                    cage_dict[txt1].set_target(target)
   #All cage configuration and sum data collected
   #START
    st.config(state=tk.DISABLED)
    res_stat = start_sumSudo(sudoku,coord_dict)
    if not res_stat: sys.exit()
    define_cageColors()
    gen_sumOutput(fr_result,sudoku,coord_dict)
    #Display statistics
    time_stamp = "Game at "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n" 
    txt_res.insert(tk.INSERT,time_stamp)
    backtrack,exec_time,distr_dict= res_stat.get_stats()
    txt_var1 = "the number of recursion steps are:  " + str(backtrack) + "\n" 
    txt_res.insert(tk.INSERT,txt_var1)
    exec_time = round(exec_time,2)
    if exec_time < 0.5:
        exec_time = " less than 0.5 seconds "
    txt_var2 = "the approximated execution time in seconds :  " + str(exec_time) + "\n" + "\n" 
    txt_res.insert(tk.INSERT,txt_var2)
    for k,val in distr_dict.items():
        print(k,val)
   

def define_cageColors():
    """
    Scan all the entries and define colors for each cage
    Each neighboring cages should not have the same colors 
    """
    random.shuffle(Cage.color)
    allColors_codeSet = {1,2,3,4} #symbolic color codeset
    for _ ,cage in cage_dict.items():
        #if the cage already has a color proceed to the next
        if cage.get_color():
            continue
        neigh = find_neighbors(cage)
        #find all colors used by neighbouring cages
        colors = set()
        for n_cage in neigh:
            if n_cage.get_color():
                colors.add(n_cage.get_color())
        avail_c = allColors_codeSet - colors
        if avail_c:
            
            cage.set_color(avail_c.pop())
        else:
            #All colors used, add new
            t = len(allColors_codeSet)
            allColors_codeSet.add(t+1)
            cage.set_color(t+1)
    #Control print of colors >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    for t,cage in cage_dict.items():
        cage.set_color(Cage.color[cage.get_color()])
        print(t,cage.get_color())
        
def find_neighbors(cage):
    """
    Find the neighbouring cages to the cage c.
    The input is the identity of a cage 
    Return a list of neighboring cage object-id
    """
    neigboursCage_list = []
    for a,b in cage.coord_list:
        neigb = ((a+1,b+1),(a,b+1),(a+1,b),(a-1,b-1),(a-1,b),(a,b-1),(a+1,b-1),(a-1,b+1))
        for  n_c in neigb:
            obj = coord_dict.get(n_c,"")
            if (obj == cage) or (obj == ""):
                continue
            neigboursCage_list.append(coord_dict[n_c])
    return neigboursCage_list
            
            
        
    
    
            
            
            
    
    
              
# =============================================================================
#     #All initial data collected
#     #Set the Start button to disabled
#     st.config(state=tk.DISABLED)
#     #start the game
#     if  sudoku_validate(sudoku):
#         start_sudoku(sudoku)
#         gen_output(fr_result,sudoku,set(init))
#         time_stamp = "Game at "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n" 
#         txt_res.insert(tk.INSERT,time_stamp)
#         backtrack,exec_time = get_stats()
#         txt_var1 = "the number of recursion steps are:  " + str(backtrack) + "\n" 
#         txt_res.insert(tk.INSERT,txt_var1)
#         exec_time = round(exec_time,2)
#         if exec_time < 0.5:
#             exec_time = " less than 0.5 seconds "
#         txt_var2 = "the approximated execution time in seconds :  " + str(exec_time) + "\n" + "\n" 
#         txt_res.insert(tk.INSERT,txt_var2)
#         
#     else:
#         print(">>>>>>>>Invalid initial data>>>>>>>>>")
#         txt_var3 = "Invalid Initial data configuration.\nPress Clear "+ "\n"+ "Enter new correct configuration"
#         txt_res.insert(tk.INSERT,txt_var3)
# 
# =============================================================================
    
def clear_input():
    """
    Clear the input matrix 
    Clear the the input FRame
    """
    global sudoku
    sudoku.fill(0)
    st.config(state=tk.NORMAL)
    #Clear the input frame
    for k,v in ent_dict.items():
        if v.get():
            v.config({"background": "White"})
            v.delete(0,'end')



#Table  convert frame position into matrix 
offset_table={0:(0,0),1:(0,3),2:(0,6),
         3:(3,0),4:(3,3),5:(3,6),
         6:(6,0),7:(6,3),8:(6,6)}

window = tk.Tk()
window.title('Sudoku')
window.geometry("1200x900")
###The window is structured into four main frames:
#1-Main text
fr_title = tk.Frame(window,width=100, height=100)
label_title = tk.Label(fr_title,text="My Sudoku solver",font=("Courier", 30,"bold"))
fr_title.grid(row=0)
label_title.grid(row=0,columnspan=4,ipadx=100)
#2-Sudoku initial configuration  and control buttoms
fr_init = tk.Frame(window,width=500, height=500, bd= 1,highlightbackground="green")
fr_init.grid(row=2,column=0,ipady=80)
tk.Label(fr_init,text="Initial data",font="helvetica 15").grid(row=0,columnspan=3)
#3-Game result
fr_result = tk.Frame(window,width=300, height=300, bd= 1,highlightbackground="red")
fr_result.grid(row=2,column=1,ipady=80)
#4-Some info txt about result
fr_txt = tk.Frame(window,width =300,height =100,highlightcolor="blue", highlightthickness=1)
fr_txt.grid(row=3,column=0)

########Configure the "Initial Frame"
#A Sudoku matrix (9x9) for initial data is placed in the initial FRame.
#The matrix divided into 9 sub matrices (3x3). 
#Each sub matrix is an own frame with 9 Entries
#The user enters the initial data in the corresponding Entries
frame_l = [] #list with the frames for the sub matrices
ent_dict = {}
#Create the 9  frames, one for each 3X3 sub matrix 
for cr in ((1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)):
    frame_in=tk.Frame(fr_init, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
    frame_in.grid(row=cr[0],column=cr[1])
    frame_l.append(frame_in)
#Configure all the entries
#Each Entry is placed in a corresponding sub matrix (3X3)
for ind,f in enumerate(frame_l):
    for cr in ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)):
        ent1 = ttk.Entry(master=f,width=3)
        ent1.grid(row=cr[0],column=cr[1])
        ##transform GUI position to matrix indices
        ##Store corresponding matrix indices,Entry
        offset=offset_table[ind]
        ent_dict[(offset[0]+cr[0],offset[1]+cr[1])] = ent1
        

# #Start Buttom command
st = ttk.Button(fr_init,text = "Start  ",command=start)
st.grid(row=5,column=0,columnspan=2,sticky='w')
 #Clear
ct = ttk.Button(fr_init,text = "Clear ",command=clear_input)
ct.grid(row=5,column=2,columnspan=2)

#########Configure the FRame with the text
#Txt with info about result 
txt_res = tk.Text(master=fr_txt,width = 60 ,height = 10,font="Helvetica 10")
txt_res.grid(column=0,row=0)




window.mainloop()
