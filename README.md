# Sample Code for Whisper Web Application

## Environment Setup

> conda create -n whisper python=3.9  

> conda install -c anaconda numpy  
>  conda install -c anaconda pandas  

For GPU:  
> conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia  

For CPU:  
> conda install pytorch torchvision torchaudio cpuonly -c pytorch  

> conda install -c anaconda ipykernel  
> conda install ffmpeg -c conda-forge  
> pip install git+https://github.com/openai/whisper.git  
> pip install streamlit  

## Execution

> conda activate whisper  
> streamlit run whisper_main.py  

## Reference
[Whisper GitHub Repository](https://github.com/openai/whisper)
