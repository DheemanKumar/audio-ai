import librosa
import numpy as np
from scipy.special import softmax
from tensorflow.keras.models import load_model
from pydub import AudioSegment
from collections import Counter


 

def load_and_predict(audio_file_path):
    # Load audio with a sample rate of 22050
    audio, original_sample_rate = librosa.load(audio_file_path, sr=22050)

    # Calculate the duration of each 3-second segment
    segment_duration = 3  # seconds

    # Calculate the number of samples per segment
    samples_per_segment = int(segment_duration * 22050)

    # Initialize an empty list to store predictions
    predictions_list = []

    # Loop over each 3-second segment
    for i in range(0, len(audio), samples_per_segment):
        # Extract a 3-second segment
        audio_segment = audio[i:i + samples_per_segment]


        # Check if the segment has enough samples, skip if not
        if len(audio_segment) == samples_per_segment:
            # Compute spectrogram
            d = librosa.stft(audio_segment)
            s_db = librosa.amplitude_to_db(np.abs(d), ref=np.max)
            s_db_with_channel = np.expand_dims(s_db, axis=-1)

            # Reshape for model input
            input_data = s_db_with_channel.reshape(1, 1025, 130, 1)

            predictions_list.append(input_data)

            # Make predictions

    return np.vstack(predictions_list)


audio_file_path = '/Users/dheemankumar/github/audio-ai/private/audio data processor/bangoli/broken_audio/bangoli audio sample 5.wav'
predictions = load_and_predict(audio_file_path)

model_noise = load_model("models/NoiseModel.h5") 

noise_predictions = model_noise.predict(predictions,verbose=0)

noise_predicted_class = np.argmax(noise_predictions, axis=1)

noise=0

for i in noise_predicted_class:
    if i:
        noise+=1
    else:
        noise-=1


if noise<0:
    model_gender = load_model("models/GenderModel.h5") 
    model_language = load_model("models/LanguageModel.h5") 

    gender_predictions = model_noise.predict(predictions,verbose=0)
    language_predictions = model_noise.predict(predictions,verbose=0)

    gender_predicted_class = np.argmax(noise_predictions, axis=1)
    language_predicted_class = np.argmax(noise_predictions, axis=1)

    male=0
    female=0

    for i in gender_predicted_class:
        if i:
            male+=1
        else:
            female+=1



    if (male>(1.5*female)):
        print("Gender : Male")
    elif (female>(1.5*male)):
        print("Gender : Female")
    else:
        print("not conform")
    
    language=[0,0,0,0]
    
    for i in language_predicted_class:
        language[i]+=1

    print(language)












