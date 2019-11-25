from python_speech_features import mfcc
import scipy.io.wavfile as wav 

def wav_to_mfcc(wav_filename, num_cepstrum):
    (rate, sig) = wav.read(wav_filename)
    mfcc_features = mfcc(sig, rate, numcep=num_cepstrum)
    return mfcc_features