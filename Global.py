'''
Created on 6 Apr 2018

@author: Dagomi
'''

#PATH
InputFileFullPath=""
OutputFileFullPath=""

#Flags
Verbose = "True" # 0 False ,1 True 

def globalPrint():
#if __name__ == '__main__':
    if True:
        print("\n")
        print("GLOBAL VARIABLES:")
        print("+---------------")
        print("| InputFileFullPath: " + InputFileFullPath )
        print("| OutputFileFullPath: " + OutputFileFullPath)