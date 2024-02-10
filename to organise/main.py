from tensorflow.keras.models import load_model
import librosa
import numpy as np
import tensorflow as tf
from pydub import AudioSegment


def get_all_sample(audio_file_paths):
    # Initialize an empty list to store predictions
    predictions_list = []

    # Loop over each audio file
    for audio in audio_file_paths:
        # Load audio with a sample rate of 22050
        #audio, sample_rate = librosa.load(audio_file_path, sr=22050)

        # Compute spectrogram
        d = librosa.stft(audio)
        s_db = librosa.amplitude_to_db(np.abs(d), ref=np.max)
        s_db_with_channel = np.expand_dims(s_db, axis=-1)

        # Reshape for model input
        input_data = s_db_with_channel.reshape(1, 1025, 130, 1)

        # Append input data to the list
        predictions_list.append(input_data)

    return np.vstack(predictions_list)



def split_audio(input_file, segment_duration, start_from_end=False):
    audio = AudioSegment.from_wav(input_file)
    total_duration = len(audio)
    segment_length = segment_duration * 1000  # Convert to milliseconds

    audio_data=[]

    if start_from_end:
        start_times = list(range(total_duration, 0, -segment_length))
    else:
        start_times = list(range(0, total_duration, segment_length))

    for i, start_time in enumerate(start_times):
        end_time = min(start_time + segment_length, total_duration)
        segment = audio[start_time:end_time]
        
        if(segment.duration_seconds==3):
            audio_data.append(segment)
    
    return get_all_sample(audio_data)


audio_file_path = '/Users/dheemankumar/github/audio-ai/private/audio data processor/bangoli/broken_audio/bangoli audio sample 5.wav'

input_data=1

a=split_audio(audio_file_path,3)

print(a)

'''
model_noise=load_model("models/NoiseModel.h5")


noise_predictions = np.argmax(model_noise.predict(input_data))

if noise_predictions:
    print("The given audio is of NOISE. ")
else:
    model_gender=load_model("models/GenderModel.h5")
    model_language=load_model("models/LanguageModel.h5")

    gender_predictions = np.argmax(model_gender.predict(input_data))
    language_predictions = np.argmax(model_language.predict(input_data))

    ans="The given audio is of a "

    if gender_predictions:
        ans+="Female "
    else:
        ans+="Male "
    
    ans+="speaking in "

    if language_predictions==0:
        ans+="English "
    elif language_predictions==1:
        ans+="Hindi "
    elif language_predictions==2:
        ans+="Punjabi "
    else:
        ans+="Bengali "

    ans+="language."

    print(ans)
'''


def break_audio(audio_file_path):
    audio_samples=[]
    return get_all_sample(audio_samples)

