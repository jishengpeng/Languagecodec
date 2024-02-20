# Language-Codec: Reducing the Gaps Between Discrete Codec Representation and Speech Language Models

[Audio samples](https://languagecodec.github.io) |
Paper [[abs]](https://arxiv.org/abs/2402.12208) [[pdf]](https://arxiv.org/pdf/2402.12208.pdf)


## Installation

To use Language-Codec, install it using:

```bash
conda create -n xxx python=3.8
conda activate xxx
pip install -r requirement.txt
```

## Infer

### Part1: Reconstruct audio from raw wav

```python

from encodec.utils import convert_audio
import torchaudio
import torch
from vocos.pretrained import Vocos

device=torch.device('cpu')

config_path = "xxx/languagecodec/configs/languagecodec.yaml"
model_path = "xxx/xxx.ckpt"
audio_outpath = "xxx"
vocos = Vocos.from_pretrained0802(config_path, model_path)
vocos = vocos.to(device)

wav, sr = torchaudio.load(audio_path)
wav = convert_audio(wav, sr, 24000, 1) 
bandwidth_id = torch.tensor([0])
wav=wav.to(device)
features,discrete_code= vocos.encode(wav, bandwidth_id=bandwidth_id)
audio_out = vocos.decode(features, bandwidth_id=bandwidth_id) 
torchaudio.save(audio_outpath, audio_out, sample_rate=24000, encoding='PCM_S', bits_per_sample=16)
```


### Part2: Generating discrete codecs
```python

from encodec.utils import convert_audio
import torchaudio
import torch
from vocos.pretrained import Vocos

device=torch.device('cpu')

config_path = "xxx/languagecodec/configs/languagecodec.yaml"
model_path = "xxx/xxx.ckpt"
vocos = Vocos.from_pretrained0802(config_path, model_path)
vocos = vocos.to(device)

wav, sr = torchaudio.load(audio_path)
wav = convert_audio(wav, sr, 24000, 1) 
bandwidth_id = torch.tensor([0])
wav=wav.to(device)
_,discrete_code= vocos.encode(wav, bandwidth_id=bandwidth_id)
print(discrete_code)
```



### Part3: Audio reconstruction through codecs
```python
# audio_tokens [n_q,1,t]/[n_q,t]
features = vocos.codes_to_features(audio_tokens)
bandwidth_id = torch.tensor([0])  
audio_out = vocos.decode(features, bandwidth_id=bandwidth_id)
```




## Pre-trained models

Currently, we have only released the results from our paper, and we plan to release additional checkpoints trained on a larger training dataset within the next two months.

| Model Name                                                                          | Dataset       | Training Iterations 
-------------------------------------------------------------------------------------|---------------|---------------------
| [languagecodec_paper_8nq](https://huggingface.co/charactr/vocos-mel-24khz)         | 3W Hours      | 2.0 M           
<!-- | [charactr/vocos-encodec-24khz](https://huggingface.co/charactr/vocos-encodec-24khz) | DNS Challenge | 2.5 M               | 7.9 M       -->

## Training

### Step1: Prepare train dataset
```python
# Process the data into a form similar to xxx/languagecodec/data/libritts_testother.txt
```

### Step2: Modifying configuration files
```python
# xxx/languagecodec/configs/languagecodec.yaml
# Modify the values of parameters such as batch_size, filelist_path, save_dir, device
```

### Step3: Start training process
Refer to [Pytorch Lightning documentation](https://lightning.ai/docs/pytorch/stable/) for details about customizing the
training pipeline.

```bash
cd xxx/languagecodec
python train.py fit --config xxx/languagecodec/configs/languagecodec.yaml
```



## Citation

If this code contributes to your research, please cite our work:

```
@misc{ji2024languagecodec,
      title={Language-Codec: Reducing the Gaps Between Discrete Codec Representation and Speech Language Models}, 
      author={Shengpeng Ji and Minghui Fang and Ziyue Jiang and Rongjie Huang and Jialung Zuo and Shulei Wang and Zhou Zhao},
      year={2024},
      eprint={2402.12208},
      archivePrefix={arXiv},
      primaryClass={eess.AS}
}
```

## License

The code in this repository is released under the MIT license as found in the
[LICENSE](LICENSE) file.