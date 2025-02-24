import os
import streamlit as st
import whisper
import tempfile
import warnings

warnings.filterwarnings(
    "ignore", category=UserWarning, 
    message="FP16 is not supported on CPU; using FP32 instead")

# アプリのタイトルを設定
st.title("音声解析アプリ")

# サイドバーでモデルサイズを選択
model_size = st.sidebar.selectbox(
    "Whisperモデルサイズを選択してください",
    ("large", "medium", "small", "base", "tiny")
)

# Whisperモデルの読み込み
model = whisper.load_model(model_size)

# 音声ファイルのアップロード
audio_file = st.file_uploader(
    "音声ファイルをアップロードしてください", 
    type=["m4a", "mp3", "webm", "mp4", "mpga", "wav"])

if audio_file is not None:
    if st.button("音声文字起こしを実行する"):
        with st.spinner("音声文字起こしを実行中です..."):
            # 一時ファイルとして保存（大きなファイルでもメモリ効率を考慮）
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
                temp_audio_file.write(audio_file.read())
                temp_audio_path = temp_audio_file.name
            
            # Whisperモデルを遅延ロード（最初の実行時のみ）
            model = whisper.load_model(model_size)

            # Whisperモデルを使って音声をテキストに変換
            result = model.transcribe(temp_audio_path)
            
            # 変換結果を表示
            st.success("音声文字起こしが完了しました！")
            st.text_area("文字起こし結果", result["text"], height=300)

            # テキストをファイルとして保存
            text_file_path = tempfile.mktemp(suffix=".txt")
            with open(text_file_path, "w") as text_file:
                text_file.write(result["text"])

            # ダウンロードボタンの作成
            with open(text_file_path, "rb") as text_file:
                st.download_button(
                    label="文字起こし結果をダウンロード",
                    data=text_file,
                    file_name="transcription.txt",
                    mime="text/plain"
                )

            # 一時ファイルを削除
            os.remove(temp_audio_path)
            os.remove(text_file_path)
