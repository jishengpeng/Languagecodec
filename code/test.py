
import torch
import torchaudio
import glob
import os
import soundfile

# path="/home/jovyan/honor/big-disk/speech/Data/commonvoice/cv-corpus-15.0-2023-09-08"

# aa=glob.glob(os.path.join(path,"*/clips/*.mp3"))

# for i in aa:
#     try:
#         y, sr = torchaudio.load(i)
#     except:
#         print(i)
# for i in range(100):
#     print(int(torch.randint(0, 3, (1,)).item()))

# audio_path="/home/jovyan/honor/big-disk/speech/Data/libritts/test-clean/61/70970/61_70970_000007_000001.wav"
# y1, sr1 = soundfile.read(audio_path)
# y2,sr2=torchaudio.load(audio_path)
# y3=torch.tensor(y1).unsqueeze(0)


# print(sr1,sr2)

# print(y1.shape[0],y2.ndim,y3.size())

# for i in range(y3.size()[1]):
#     assert y3[0][i]==y2[0][i]

tensor3d=torch.tensor([[[1.0,2.0,3.0],[4.0,5.0,6.0]],[[1.0,3.0,5.0],[2.0,4.0,6.0]],[[7.0,8.0,9.0],[8.0,5.0,4.0]]])

print(tensor3d.size(),tensor3d.mean(dim=1,keepdim=False).size())

