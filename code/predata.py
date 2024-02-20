# 准备好训练的list
import os
import glob
import random


# # 训练集
# inputpath1="/home/jovyan/honor/big-disk/speech/Data/libritts/train-clean-100"
# inputpath2="/home/jovyan/honor/big-disk/speech/Data/libritts/train-clean-360"
# inputpath3="/home/jovyan/honor/big-disk/speech/Data/libritts/train-other-500"
# inputpath4="/home/jovyan/honor/big-disk/speech/Data/vctk/wav48"

# outputpath="/home/jovyan/honor/big-disk/speech/code/languagecodec/data/train/vctk"

# os.system("rm %s"%(outputpath))
# os.system("touch %s"%(outputpath))

# aa1=glob.glob(os.path.join(inputpath1,"*/*/*.wav"))
# aa2=glob.glob(os.path.join(inputpath2,"*/*/*.wav"))
# aa3=glob.glob(os.path.join(inputpath3,"*/*/*.wav"))
# aa4=glob.glob(os.path.join(inputpath4,"*/*.wav"))

# aa=aa1+aa2+aa3+aa4

# aa=aa4

# random.shuffle(aa)

# # print(len(aa),aa[:10])

# with open(outputpath,'w') as fin:
#     for i in aa:
#         fin.write(i+"\n")


# # 验证集
# inputpath1="/home/jovyan/honor/big-disk/speech/Data/LibriSpeech/test-clean"
# inputpath2="/home/jovyan/honor/big-disk/speech/Data/LibriSpeech/test-other"

# outputpath="/home/jovyan/honor/big-disk/speech/code/languagecodec/data/train/lirbitts_vctk_val"

# os.system("rm %s"%(outputpath))
# os.system("touch %s"%(outputpath))

# aa1=glob.glob(os.path.join(inputpath1,"*/*/*.flac"))
# aa2=glob.glob(os.path.join(inputpath2,"*/*/*.flac"))


# aa=aa1+aa2

# random.shuffle(aa)

# # print(len(aa),aa[:10])

# with open(outputpath,'w') as fin:
#     for i in aa:
#         fin.write(i+"\n")

# 测试集
# inputpath1="/home/jovyan/honor/big-disk/speech/Data/libritts/test-clean"

# outputpath="/home/jovyan/honor/big-disk/speech/code/languagecodec/data/train/lirbitts_vctk_test"

# os.system("rm %s"%(outputpath))
# os.system("touch %s"%(outputpath))

# aa1=glob.glob(os.path.join(inputpath1,"*/*/*.wav"))

# aa=aa1

# random.shuffle(aa)

# # print(len(aa),aa[:10])

# with open(outputpath,'w') as fin:
#     for i in aa:
#         fin.write(i+"\n")


# # 测试集
# inputpath1="/home/jovyan/honor/big-disk/speech/Data/LJSpeech-1.1/wavs"

# outputpath="/home/jovyan/honor/big-disk/speech/code/languagecodec/data/train/ljspeech"

# os.system("rm %s"%(outputpath))
# os.system("touch %s"%(outputpath))

# aa1=glob.glob(os.path.join(inputpath1,"*.wav"))

# aa=aa1

# random.shuffle(aa)

# # print(len(aa),aa[:10])

# with open(outputpath,'w') as fin:
#     for i in aa:
#         fin.write(i+"\n")


# 搞一份所有的作为language_codec训练的
inputpath1="/home/jovyan/honor/big-disk/speech/Data/libritts/train-clean-100"
inputpath2="/home/jovyan/honor/big-disk/speech/Data/libritts/train-clean-360"
inputpath3="/home/jovyan/honor/big-disk/speech/Data/libritts/train-other-500"
inputpath4="/home/jovyan/honor/big-disk/speech/Data/vctk/wav48"
inputpath5="/home/jovyan/honor/big-disk/speech/Data/librilight/small/small_split"
inputpath6="/home/jovyan/honor/big-disk/speech/Data/librilight/medium/medium_split"
inputpath7="/home/jovyan/honor/big-disk/speech/Data/commonvoice/cv-corpus-16.1-2023-12-06"
inputpath8="/home/jovyan/honor/big-disk/speech/Data/commonvoice/cv-corpus-15.0-2023-09-08"
inputpath9="/home/jovyan/honor/big-disk/speech/Data/DNS/trainclean_split"

outputpath="/home/jovyan/honor/big-disk/speech/code/languagecodec/data/train/languagecodec_large"

os.system("rm %s"%(outputpath))
os.system("touch %s"%(outputpath))

aa1=glob.glob(os.path.join(inputpath1,"*/*/*.wav"))
aa2=glob.glob(os.path.join(inputpath2,"*/*/*.wav"))
aa3=glob.glob(os.path.join(inputpath3,"*/*/*.wav"))
aa4=glob.glob(os.path.join(inputpath4,"*/*.wav"))

aa5=glob.glob(os.path.join(inputpath5,"*/*.flac"))
aa6=glob.glob(os.path.join(inputpath6,"*/*.flac"))
aa7=glob.glob(os.path.join(inputpath7,"*/clips/*.mp3"))
aa8=glob.glob(os.path.join(inputpath8,"*/clips/*.mp3"))
aa9=glob.glob(os.path.join(inputpath9,"*/*.wav"))

aa=aa1+aa2+aa3+aa4+aa5+aa6+aa7+aa8+aa9

random.shuffle(aa)

# print(len(aa),aa[:10])

with open(outputpath,'w') as fin:
    for i in aa:
        fin.write(i+"\n")








