from encodec import EncodecModel
from encodec.utils import convert_audio

import torchaudio
import torch

import os

import logging

infer_log_path="/home/jovyan/honor/big-disk/speech/code/languagecodec/测试比较encodec_encodec.log"

os.system("rm %s"%(infer_log_path))

# 设置输出的格式
LOG_FORMAT = "时间: %(asctime)s - 日志等级: %(levelname)s - 日志信息: %(message)s"
# 对logger进行配置——日志等级&输出格式
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, filename=infer_log_path)


# Instantiate a pretrained EnCodec model
model = EncodecModel.encodec_model_24khz()
# The number of codebooks used will be determined bythe bandwidth selected.
# E.g. for a bandwidth of 6kbps, `n_q = 8` codebooks are used.
# Supported bandwidths are 1.5kbps (n_q = 2), 3 kbps (n_q = 4), 6 kbps (n_q = 8) and 12 kbps (n_q =16) and 24kbps (n_q=32).
# For the 48 kHz model, only 3, 6, 12, and 24 kbps are supported. The number
# of codebooks for each is half that of the 24 kHz model as the frame rate is twice as much.
model = model.cuda()
model.set_target_bandwidth(12.0)

# Load and pre-process the audio waveform
# wav, sr = torchaudio.load("<PATH_TO_AUDIO_FILE>")
input_path = "/home/jovyan/honor/big-disk/speech/code/languagecodec/data/infer/lirbitts_vctk_testclean_500"
out_folder = '/home/jovyan/honor/big-disk/speech/code/languagecodec/result/infer/encodec'
# os.system("rm -r %s"%(out_folder))
# os.system("mkdir -p %s"%(out_folder))
# ll="libritts_testclean500_nq16"
ll = "debug"

tmptmp=out_folder+"/"+ll

os.system("rm -r %s"%(tmptmp))
os.system("mkdir -p %s"%(tmptmp))

with open(input_path,'r') as fin:
    x=fin.readlines()

x = [i.strip() for i in x]

for i in range(20):

    print(i)

    wav, sr = torchaudio.load(x[i])

    wav = wav.cuda()
    wav = convert_audio(wav, sr, model.sample_rate, model.channels)
    wav = wav.unsqueeze(0)

    # Extract discrete codes from EnCodec
    with torch.no_grad():
        encoded_frames = model.encode(wav)
    codes = torch.cat([encoded[0] for encoded in encoded_frames], dim=-1)  # [B, n_q, T]

    if(codes.size()[2]>100):
        logging.info(f"{x[i]}|{codes[:,:2,:]}")
    else:
        logging.info(f"{x[i]}|{codes}")

    # frames=[(codes,None)]

    # with torch.no_grad():
    #     wav_output = model.decode(frames)

    # audio_path = out_folder + '/' + ll + '/' + x[i].split('/')[-1]

    # torchaudio.save(audio_path,wav_output.squeeze(0).cpu(),model.sample_rate)
