# 随机选择一些作为demo展示

import os

input_path="/home/jovyan/honor/big-disk/speech/code/languagecodec/result/infer/languagecodec/libritts_testclean_nq4_large_epoch24"
input_path2="/home/jovyan/honor/big-disk/speech/code/languagecodec/result/infer/encodec/libritts_testclean500_nq8"
output_path="/home/jovyan/honor/big-disk/speech/code/languagecodec/result/infer/demo"

os.system("rm -r %s"%(output_path))
os.system("mkdir -p %s"%(output_path))
x=os.listdir(input_path2)

# print(x[0])

for i in range(400):
    out1=output_path+"/"+"encodec_"+x[i]
    out2=output_path+"/"+"languagecodec_"+x[i]
    int2=os.path.join(input_path,x[i])
    int1=os.path.join(input_path2,x[i])
    os.system("cp %s %s"%(int1,out1))
    os.system("cp %s %s"%(int2,out2))


