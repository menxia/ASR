import numpy as np 
import scipy.fftpack 
import utils
import matplotlib.pyplot as plt 


def choose_frequencies():
    freq1 = 1
    freq2 = 5
    freq3 = 25

    return [freq1, freq2, freq3]

def add_the_waves(freqs):
    _, _, t = utils.get_wave_timing()
    w1, w2, w3 = utils.make_waves(t, freqs)
    sum_waves = w1 + w2 + w3
    return [w1, w2, w3,sum_waves]

def demo_fft(sum_waves):
    num_samples, spacing, t = utils.get_wave_timing()
    y_fft = scipy.fftpack.fft(sum_waves)

    x_ftt = np.linspace(0, 1.0/(2*spacing), num_samples/2)
    return x_ftt, y_fft


if __name__ == '__main__':
    num_samples, spacing, t = utils.get_wave_timing()
    freqs = choose_frequencies()
    w1, w2, w3,sum_waves = add_the_waves(freqs)
    x_ftt, y_fft = demo_fft(sum_waves)


    # utils.display_sinusoids(t, w1, w2, w3, sum_waves)
    utils.display_fft(x_ftt, y_fft)


