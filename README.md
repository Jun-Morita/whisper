# whisperウェブアプリのサンプルコード

## 環境設定

> conda create -n whisper python=3.9 

> conda install -c anaconda numpy 
>  conda install -c anaconda pandas 

> conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia 
(CPU版)
> conda install pytorch torchvision torchaudio cpuonly -c pytorch 

> conda install -c anaconda ipykernel 

> conda install ffmpeg -c conda-forge 

> pip install git+https://github.com/openai/whisper.git 

> pip install streamlit 

## 実行

> conda activate whisper 
> streamlit run whisper_main.py

## Ref.
https://github.com/openai/whisper
