from tensorflow.keras.models import load_model
import librosa
import numpy as np
import tensorflow as tf


audio_file_path = '/Users/dheemankumar/github/audio-ai/ab.wav'

#audio_file_path = '/Users/dheemankumar/github/audio-ai/female_eng.wav'  # Adjust the path as needed
audio, sample_rate = librosa.load(audio_file_path, sr=22050)  # Load audio with a sample rate of 22050

d=librosa.stft(audio)

s_db=librosa.amplitude_to_db(np.abs(d),ref=np.max)
s_db_with_channel = np.expand_dims(s_db, axis=-1)

audio_= np.array(s_db_with_channel)

input_data = audio_.reshape(1, 1025, 130, 1)


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





