#under development
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from .record import *
import sounddevice as sd
#load pre-trained model and tokenizer
tokenizer = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def speech(audio="recording.wav",freq = 44100,duration = 5):
    recording = sd.rec(int(duration * freq), 
                    samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()
    write(audio, recording, freq, sampwidth=2)
    #load any audio file of your choice
    speech, rate = librosa.load(audio,sr=16000)
    input_values = tokenizer(speech, return_tensors = 'pt').input_values
    #Store logits (non-normalized predictions)
    logits = model(input_values).logits
    #Store predicted id's
    predicted_ids = torch.argmax(logits, dim =-1)
    #decode the audio to generate text
    transcriptions = tokenizer.decode(predicted_ids[0])
    return transcriptions