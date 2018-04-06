'''
Created on 6 Apr 2018

@author: anonimo

CLI_EXAMPLE:

python .\CuCo.py -i E:\DAGOMI\CubeMap\Develop\cube.mp4  -o E:\DAGOMI\CubeMap\Develop -cw 20 -ch 20 -f 25 -r 25 -v true

'''
#Python
import argparse
import time

#Cuco
import Global
import ConfigFilesGenerator
#External Tools
## \mainpage CubemapConverter \version 0.01
#
# \author David Gomez david.gomez@i2cat.com
## 
#===============================================================================
# CLI inputs
#===============================================================================
parser = argparse.ArgumentParser(description='CubemapConverter (CuCo)',
                                 epilog='david.gomez@i2cat')
##InputFileFullPath: Path of the Source Equirectangular file
parser.add_argument('-i', '--InputFileFullPath',
                    help="InputFileFullPath: Path of the Source Equirectangular file", required = True)
##OutputFileFullPath: Output \n
parser.add_argument('-o', '--OutputFileFullPath',
                    help="OutputFileFullPath: Output ", required = True)
parser.add_argument('-f', '--FramesToBeEncoded',help= "Number od frames to encode, 0 encode all frames")
##Width of a face Cube\n
parser.add_argument('-cw', '--CubeFaceWidth',help= "Width of a face Cube")
##Height of a face Cube\n
parser.add_argument('-ch', '--CubeFaceHeight',help= "Height of a face Cube")
##Frame rate of the output Cubemap video projection\n
parser.add_argument('-r', '--FrameRate',help= "Frame rate of the output Cubemap video projection")
parser.add_argument('-v', '--Verbose',
                    help="Verbose", required = False)
args = parser.parse_args()

class Dasher:
    '''
    Main Procces of the Dasher
    '''
    #===============================================================================
    # Main process
    #===============================================================================
    if __name__ == '__main__':
        startTime = time.time()
        #Save Paths
        Global.Verbose = args.Verbose
        Global.InputFileFullPath = args.InputFileFullPath
        Global.OutputFileFullPath = args.OutputFileFullPath
        
        #Orchestrator
        ConfigFilesGenerator.create_config_input(args.CubeFaceWidth,args.CubeFaceHeight,args.FramesToBeEncoded,"ms")
        ConfigFilesGenerator.create_config_input(args.CubeFaceWidth,args.CubeFaceHeight,args.FramesToBeEncoded,"ss")
        
        Global.globalPrint()
        elapsedTime = time.time() - startTime
        print("-> Total time elapsed: " + time.strftime('%H:%M:%S', time.gmtime(elapsedTime)))
