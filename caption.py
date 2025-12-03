import torch 
import sounddevice as sd
import soundfile as sf
from transformers import pipeline


cct=pipeline("automatic-speech-recognition",model="openai/whisper-small")

def record_audio(seconds=4, fs=16000):
    print("🎤 Recording...")
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write("temp.wav", audio, fs)
    return "temp.wav"
while True:
    file = record_audio()
    text = cct(file)["text"]
    print("📝 Caption:", text)
    break   # ⬅️ stops after first loop



