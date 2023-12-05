# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log()

# define the model
class MyModel(ACTR):
    
    goal=Buffer()

    #check if goal state is reached
    def finish(self, A , B , C):
        import ast
        disks=ast.literal_eval(C) #convert string to list
        if disks==[1,2,3]: #check if goal state is reached
            print 'Peg A has disks: ',A, ' Peg B has disks: ',B, ' Peg C has disks: ',C
            print 'Goal state reached'
            self.stop() #stop the model
        else:
            print 'Peg A has disks: ',A, ' Peg B has disks: ',B, ' Peg C has disks: ',C
    
    # agorithm step 1: what move between A & C
    def step1(goal='pegA:?A pegB:?B pegC:?C step:1'):
        import ast
        A_disks=ast.literal_eval(A) #convert string to list
        C_disks=ast.literal_eval(C)
        
        #check if we can move a disk from A to C
        if A_disks and (not C_disks or (C_disks and A_disks[-1]>C_disks[-1])):
            C_disks.append(A_disks[-1])
            A_disks.pop()
            print "Disk" , C_disks[-1] , "was moved to peg C"
        #check if we can move a disk from C to A
        elif C_disks and (not A_disks or (A_disks and C_disks[-1]>A_disks[-1])):
            A_disks.append(C_disks[-1])
            C_disks.pop()
            print "Disk" , A_disks[-1] , "was moved to peg A"

        A=str(A_disks) #convert list to string
        C=str(C_disks)

        goal.set('pegA:?A pegB:?B pegC:?C step:2')
        self.finish(A,B,C)
        
    # agorithm step 2: what move between A & B
    def step2(goal='pegA:?A pegB:?B pegC:?C step:2'):
        import ast
        A_disks=ast.literal_eval(A)
        B_disks=ast.literal_eval(B)
        
        if A_disks and (not B_disks or (B_disks and A_disks[-1]>B_disks[-1])):
            B_disks.append(A_disks[-1])
            A_disks.pop()
            print "Disk" , B_disks[-1] , "was moved to peg B"
        elif B_disks and (not A_disks or (A_disks and B_disks[-1]>A_disks[-1])):
            A_disks.append(B_disks[-1])
            B_disks.pop()
            print "Disk" , A_disks[-1] , "was moved to peg A"

        A=str(A_disks)
        B=str(B_disks)
        goal.set('pegA:?A pegB:?B pegC:?C step:3')
        self.finish(A,B,C)
        
    # agorithm step 3: what move between B & C    
    def step3(goal='pegA:?A pegB:?B pegC:?C step:3'):
        import ast
        B_disks=ast.literal_eval(B)
        C_disks=ast.literal_eval(C)
        
        if B_disks and (not C_disks or (C_disks and B_disks[-1]>C_disks[-1])):
            C_disks.append(B_disks[-1])
            B_disks.pop()
            print "Disk" , C_disks[-1] , "was moved to peg C"
        elif C_disks and (not B_disks or (B_disks and C_disks[-1]>B_disks[-1])):
            B_disks.append(C_disks[-1])
            C_disks.pop()
            print "Disk" , B_disks[-1] , "was moved to peg B"

        B=str(B_disks)
        C=str(C_disks)
        goal.set('pegA:?A pegB:?B pegC:?C step:1')
        self.finish(A,B,C)

model=MyModel()
ccm.log_everything(model)
model.goal.set('pegA:[1,2,3] pegB:[] pegC:[] step:1')
model.run()