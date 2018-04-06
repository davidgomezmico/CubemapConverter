'''
Created on 14 nov. 2016

@author: Pc
'''
#===============================================================================
# Obtain media information to the source imput
#===============================================================================
import json
import os

import Global

profile_idc = {'Constrained Baseline':'42','Baseline profile':'4D','Main profile':"4D"}
profile_iop = {'Constrained Baseline':'c','Baseline profile':'c','Main profile':"4D"}

def GenerateJson (mediaFile):
    comand = "ffprobe %s -v quiet -print_format json -show_format -show_streams" % mediaFile
    jsonString = os.popen(comand).read()
    jsonDatatry = json.loads(jsonString)
    return jsonDatatry

def ObtainFormatParamaeters (mediaFile,parameter):
    jsonDatatry = GenerateJson (mediaFile)
    
    #frame rate
    if parameter == 'duration':
        duration = []
        #Video duration
        duration_unformated = jsonDatatry['format']['duration']
        time= (duration_unformated.split('.'))
        #minutes
        duration.append(str(((int(time[0]))/60)))
        #seconds
        duration.append(str(((float(time[1]))/100000)))
        return duration
    param = jsonDatatry['format'][parameter]

    return param

def ObtainStreamsParamaeters (mediaFile,parameter):
    jsonDatatry = GenerateJson (mediaFile)
    if parameter == 'frame_rate':
        frame_rate = jsonDatatry['streams'][0]['r_frame_rate']  
        frame_rate_split= (frame_rate.split('/'))
        
        '''
        TODO: Change a dynamic fps in a future, fix the origin lecture
        '''
        frame_rate_split[0] = "25"
        return frame_rate_split[0] 
    if parameter == 'language':
        try:
            language = jsonDatatry['streams'][0]['tags']['language']  
            return language
        except KeyError:
            return "und"
        
    if parameter == 'time_base':
        time_base = jsonDatatry['streams'][0]['time_base']  
        time_base_split= (time_base.split('/'))
        return time_base_split[1]     
    
    param = jsonDatatry['streams'][0][parameter]
    return param

def ObtainCodec (mediaFile):
    print ("-- ObtainCodec --")
#     jsonDatatry = GenerateJson (mediaFile)
#     print jsonDatatry
#     codec_tag_string = jsonDatatry['streams'][0]['codec_tag_string']
#     print codec_tag_string
#     profile_tag =  jsonDatatry['streams'][0]['profile']
#     print profile_tag
#     profile = profile_idc[profile_tag]
#     Flag_constrained = profile_iop[profile_tag]
#     level = format(jsonDatatry['streams'][0]['level'], 'x') 
#     codec = codec_tag_string + "." + profile + Flag_constrained + "0" + level
    codec = "avc1.42c01e"
    
    #CMD = "MediaInfo.exe --Output=Video;%Format_Profile% %s" % mediaFile
    #"Video;%DisplayAspectRatio%"  for Video Aspect Ratio
    #os.system(CMD)
    
    return codec
    
        