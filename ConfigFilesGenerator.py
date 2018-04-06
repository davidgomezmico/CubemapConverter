'''
Created on 21 jul. 2017

@author: Dagomi
'''
import io
import MediaInfo
import Global

LevelProfile_264 = {'720p': '3.1', '1080p': '4', '2k': '4.2','4k': '5.1','8k': '6'}

def create_config_input(CubeFaceWidth,CubeFaceHeight,FramesToBeEncoded,tile):

    eqr_projection = Global.InputFileFullPath
    InputBitDepth = MediaInfo.ObtainStreamsParamaeters(eqr_projection, "bits_per_raw_sample")
    FrameRate = MediaInfo.ObtainStreamsParamaeters(eqr_projection, "frame_rate")
    SourceWidth = MediaInfo.ObtainStreamsParamaeters(eqr_projection, "width")
    SourceHeight = MediaInfo.ObtainStreamsParamaeters(eqr_projection, "height")

    if FramesToBeEncoded == "0":
        FramesToBeEncoded_var = MediaInfo.ObtainStreamsParamaeters(eqr_projection, "nb_frames")
    else:
        FramesToBeEncoded_var = FramesToBeEncoded
    
    profile = h_264_level_profile(SourceWidth)
    
    InputFile = eqr_projection
    OutputFile = Global.OutputFileFullPath
    with io.FileIO(OutputFile + "/" + "config_" + tile + ".cfg", "w") as config:
        config.write("#======== File I/O ===============\n")
        config.write("InputFile                     : %s.yuv\n" % InputFile)
        config.write("InputBitDepth                 : %s\n" % InputBitDepth)
        config.write("InputChromaFormat             : 420\n")
        config.write("FrameRate                     : %s\n" % FrameRate)
        config.write("FrameSkip                     : 0\n")
        config.write("SourceWidth                   : %s\n" % SourceWidth)
        config.write("SourceHeight                  : %s\n" % SourceHeight)
        config.write("FramesToBeEncoded             : %s\n" % FramesToBeEncoded_var)
        config.write("\n")
        config.write("#======== Unit definition ================\n")
        config.write("FaceSizeAlignment             : 1           # face size alignment;\n")
        config.write("\n")
        config.write("#=========== Misc. ============\n")
        config.write("InternalBitDepth              : 8          # codec operating bit-depth\n")
        config.write("\n")
        config.write("#============ 360 video settings ======================\n")
        config.write("#SphereVideo                       : 1                                    # 1: 360 video; 0: traditional video;\n")
        config.write("InputGeometryType                 : 0                                    # 0: equirectangular; 1: cubemap; 2: equalarea; this should be in the cfg of per sequence.\n")
        config.write("SourceFPStructure                 : 1 1   0 0                            # frame packing order: numRows numCols Row0Idx0 ROT Row0Idx1 ROT ... Row1...\n")
        config.write("CodingGeometryType                : 1\n")
        if tile == "ms":
            config.write("#CodingFPStructure                 : 1 1   0 0 #MainFace\n")
        if tile == "ss":
            config.write("CodingFPStructure                 : 6 1   2 90   1 0   3 270   5 0   4 0   6 0   #TrashFaces\n")
        config.write("CodingFaceWidth                   : 480                                 # 0: automatic calculation; 1184 for 8K; 960 for 4K;\n")
        config.write("CodingFaceHeight                   : 480                                 # 0: automatic calculation; 1184 for 8K; 960 for 4K;\n")
        config.write("InterpolationMethodY              : 5                                    # interpolation method for luma, 0: default setting(bicubic); 1:NN, 2: bilinear, 3: bicubic, 4: lanczos2, 5: lanczos3\n")
        config.write("InterpolationMethodC              : 4                                    # interpolation method for chroma, 0: default setting(bicubic); 1:NN, 2: bilinear, 3: bicubic, 4: lanczos2, 5: lanczos3\n")
        config.write("InternalChromaFormat              : 420                                  # internal chroma format for the conversion process;\n")
        config.write("\n")
        config.write("### DO NOT ADD ANYTHING BELOW THIS LINE ###\n")
        config.write("### DO NOT DELETE THE EMPTY LINE BELOW ###\n")
        config.write("\n")

#     with io.FileIO(Config.ConfigFolder + "/"  + source_file + "_equirectangular_2_cubemap.cfg", "w") as projection:
#         projection.write("#======== projection I/O ===============\n")
#         projection.write("OutputFile                    : %s.yuv\n" % OutputFile)
#         projection.write("#Refprojection                        : reference_projection_name\n")
#         projection.write("\n")
#         projection.write("#======== Unit definition ================\n")
#         projection.write("FaceSizeAlignment             : 1 \n")
#         projection.write("\n")
#         projection.write("#=========== Misc. ============\n")
#         projection.write("InternalBitDepth              : 8\n")
#         projection.write("\n")
#         projection.write("#============ 360 video settings ======================\n")
#         projection.write("InputGeometryType                 : 0\n")
#         projection.write("SourceFPStructure                 : 1 1   0 0\n")
#         projection.write("\n")
#         projection.write("CodingGeometryType                : 1\n")
#         projection.write("CodingFPStructure                 : 2 3   4 0 0 0 5 0   3 180 1 270 2 0\n")
#         projection.write("SVideoRotation                    : 0 0 0\n")
#         projection.write("\n")
#         projection.write("CodingFaceWidth                   : %s\n" % CubeFaceWidth)
#         projection.write("CodingFaceHeight                  : %s\n" % CubeFaceHeight)
#         projection.write("#ViewPortSettings                  : 80.0 80.0  -90.0  0.0\n")
#         projection.write("SphFile                           : sphere_655362.txt\n")
#         projection.write("\n")
#         projection.write("### DO NOT ADD ANYTHING BELOW THIS LINE ###\n")
#         projection.write("### DO NOT DELETE THE EMPTY LINE BELOW ###\n")
#         projection.write("\n")

def h_264_level_profile (width):
    if 1 <= width <= 1919:
        return LevelProfile_264['720p']
    if 1920 <= width <= 2047:
        return LevelProfile_264['1080p']
    if 2048 <= width <= 3839:
        return LevelProfile_264['2k']
    if 3840 <= width <= 4095:
        return LevelProfile_264['4k']
    if 4096 <= width <= 8192:
        return LevelProfile_264['8k']
    