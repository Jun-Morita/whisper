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

## Others
You can adjust the file size limit in Streamlit by modifying the config.toml file. This file is usually located in the following directory:

- Windows: C:\Users\YourUsername\\.streamlit\config.toml
- Mac/Linux: ~/.streamlit/config.toml

To increase the file upload size limit, add or modify the following line in config.toml:
```toml
[server]
maxUploadSize = 1000
```
This sets the maximum upload file size to 1000MB (adjust as needed). If the file does not exist, you can create it manually.

