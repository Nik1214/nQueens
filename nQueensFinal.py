# Name: Nikhil Khosla
#  Block: 4th
#  Email: 2018nkhosla@tjhsst.edu
import time
import math
import heapq
from collections import deque
import random

globvarNode_Count = 0
globvarGoal_Count = 0

class nQueens:
    def __init__(self, state=None, choices=None, n= 8,  parent=None):
        """ creates an nQueens board where state is a list of n integers,
            one per column,
            and choices is a list of sets,
            n is the size
            parent is the state predecessor in a search
        """
        global globvarNode_Count
        globvarNode_Count = globvarNode_Count + 1
        self.size = n
        if choices != None:
            self.choices = choices
            self.state = state
        else:
            self.choices = []
            self.state = []
            for x in range (0,n):
                self.choices.insert(0,(set(range(0,self.size))))
                self.state.insert(0, None)



    def assign(self, var, value):
        """ updates the state by setting state[var] to value
            also propgates constraints and updates choices
        """
        self.state[var] = value
        for col in range(0,len(self.choices)):
            self.choices[col].difference_update({value})
            for row in range(0, self.size):#self.choices[col].copy():
                if(abs(col-var) == abs(row-value)):
                    self.choices[col].difference_update({row})
        
    def goal_test(self):
        """ returns True iff state is the goal state """
        global globvarGoal_Count
        globvarGoal_Count = globvarGoal_Count + 1
        if None in self.state:
            return False
        else:
            return True
    def get_next_unassigned_var(self):
        """ returns the index of a column that is unassigned and
            has valid choices available """
        #base 
##        for k in range(0,len(self.state)):
##            if  self.state[k] == None and not len(self.choices[k]) == 0:
##                return k
        
##        #random
##        x = -1 
##        while( self.state[x] != None):
##            x = random.randint(0, self.size - 1)
##        return x
        
        #minChoices
        minLength = self.size
        minIndex = 0
        for x in range(0, self.size):
           if(self.state[x] == None):
               length = len(self.choices[x])
               if(0 < length  and length < minLength):
                   minIndex = x
                   minLength = length
        return minIndex
       
        #sort by abs((self.n/2) - index)
    
        
    def get_choices_for_var(self, var):
        """ returns choices[var], the list of available values
                  for variable var, possibly sorted """
        temp = list(self.choices[var]).reverse()
##        print(self.choices[var])
        #splice method to obtain top to mid first then bottom to mid 
        temp = (list(self.choices[var]))
        x = int((self.size)/2)
        front = temp[:x]
        end = temp[x:]
        end.sort(reverse = True)
        the = end + front
        
        #alternates top and bottom untill middle choice is reached
        #list(self.choices[var]).sort()#reverse = True)
        #the = self.choices[var]
        #the = sorted(the, key = lambda i : abs(i - self.size/2))
        #print(the)
        return(the)
    def __str__(self):
        """ returns a string representation of the object """
        print(self.state)
    

###---------------------------------------------------------------

def dfs_search(board):
    """ sets board as the initial state and returns a
        board containing an nQueens solution
        or None if none exists
    """
    fringe = [board]
    while (len(fringe) != 0):
        current = fringe.pop()
        if(current.goal_test()):
            print("here")
            return current
        var = current.get_next_unassigned_var()
        if var != None:
            the = current.get_choices_for_var(var)         
            for val in the:
                childQueen = createChild(current)
                childQueen.assign(var,val)
                if None not in childQueen.state:
                    #print(childQueen.state)
                    #print("goal")
                    #print("node")
                    #print(globvarNode_Count)
                    
                    return childQueen
                fringe.append(childQueen)
                
                
        
def createChild(p):
    newState = p.state.copy()
    newChoices = []
    for x in range(0, len(p.choices)):
        newChoices.append(p.choices[x].copy())
    return nQueens(newState, newChoices, p.size, p)
# I am not sure if this was just my laptop, but I had to run my code 3 seperate times, one from 70-80, again from 80-90, and then from 90-99. I skipped 91,96,97 as those times were extremly large
for n in range (70,100):
    #print(n)
    temporary = nQueens(None, None, n, None)
    the = createChild(temporary)
    sTime = time.time()
    dfs_search(temporary)
    fTime = time.time()- sTime
    print(str(globvarGoal_Count) + "\t" + str(globvarNode_Count)+ "\t" + str(fTime))
    #print("----------------------------")
