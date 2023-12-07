import librosa
import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.dirname(os.path.abspath(__file__))


def lodeimage(audio_file):
    audio, sr = librosa.load(audio_file)
    y = pd.Series(audio)

    # Plot the audio waveform
    plt.figure(figsize=(10, 5))
    y.plot()
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.title("Audio Waveform")

    # Save the image to a file (e.g., 'output.png')
    plt.savefig(os.path.join(path,"output.png"))

    return (os.path.join(path,"output.png"))



