# 将librilight的数据切分成八秒中一段

import os
import glob
import torchaudio
import torch

input_path="/home/jovyan/honor/big-disk/speech/Data/DNS/pdns_training_set/raw/clean"
output_path="/home/jovyan/honor/big-disk/speech/Data/DNS/trainclean_split"

aa=glob.glob(os.path.join(input_path,"*/*.wav"))

# os.system("rm -r %s"%(output_path))
# os.system("mkdir -p %s"%(output_path))

sum_audio=0

for i in aa:
    # sum_audio+=1
    # if(sum_audio>10):
    #     break
    wav, sr = torchaudio.load(i)
    if(wav.size()[1]>(sr*8)):
        wav_tmp=wav[:,:wav.size()[1]//(sr*8)*(sr*8)].reshape(-1,sr*8)
        wav_left=wav[:,wav.size()[1]//(sr*8)*(sr*8):]
        name=i.split('/')[-2]
        id=i.split('/')[-1].split('.')[0]
        for id_i in range(wav_tmp.size()[0]):
            out_folder=output_path+"/"+name
            os.makedirs(out_folder, exist_ok=True)
            audio_path=out_folder+"/"+id+"_"+str(id_i+1)+".wav"
            torchaudio.save(audio_path, wav_tmp[id_i].unsqueeze(0), sample_rate=sr)
        if(wav_left.size()[1]>sr):
            audio_path=out_folder+"/"+id+"_"+str(id_i+1+1)+".wav"
            torchaudio.save(audio_path, wav_left, sample_rate=sr)
    else:
        if(wav.size()[1]>sr):
            name=i.split('/')[-2]
            id=i.split('/')[-1].split('.')[0]
            out_folder=output_path+"/"+name
            os.makedirs(out_folder, exist_ok=True)
            audio_path=out_folder+"/"+id+"_1.wav"
            torchaudio.save(audio_path, wav, sample_rate=sr)
 

