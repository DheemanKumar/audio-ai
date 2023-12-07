import librosa
import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.dirname(os.path.abspath(__file__))

audio, sr = librosa.load("/Users/dheemankumar/Desktop/FILE/audio-ai/3sec_audio/hindi_sample_1.wav")
y = pd.Series(audio)

# Plot the audio waveform
plt.figure(figsize=(10, 5))
y.plot()
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.title("Audio Waveform")
plt.savefig(os.path.join(path,"output.png"))