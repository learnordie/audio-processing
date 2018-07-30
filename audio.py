#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Declaration of the class Audio """


from scipy.io import wavfile


class Audio:
    def __init__(self, filename):
        """ Initialize the class only reading a WAV file.

            Args:
                filename: WAV audio file.

        """
        # scipy handles exceptions if a problem with the file happens
        rate, data = wavfile.read(filename)
        self.rate = rate
        self.data = data

    def sampling_rate(self):
        """ Return the sampling rate (in samples/sec, or Hz). """
        return self.rate

    def is_mono(self):
        """ Check if a WAV audio file is mono. """
        # data.shape returns a tuple like (number_of_points,)
        # if there is only one channel
        return len(self.data.shape) == 1

    def is_stereo(self):
        """ Check if the audio is stereo or not. """
        # data.shape returns a tuple: (number_of_points, number_of_channels)
        # if the audio data is stereo (has two channels).
        return len(self.data.shape) == 2

    def number_of_sampling_points(self):
        """ Return the number of sampling points. """
        return self.data.shape[0]

    def data_type(self):
        """ Return the data type of an audio. """
        return self.data.dtype

    def duration(self):
        """ Return the duration (in seconds) of an audio. """
        npoints = self.number_of_sampling_points()
        return npoints / self.rate

    def left_channel(self):
        """ Return the left channel of an audio. """
        if self.is_stereo():
            return self.data[:, 0]
        else:
            return self.data

    def right_channel(self):
        """ Return the right channel of an audio."""
        if self.is_stereo():
            return self.data[:, 1]
        else:
            return self.data

    def max(self):
        """ Return the maximum PCM (amplitude) value of the data. """
        return self.data.max()

    def min(self):
        """ Return the minimum PCM (amplitude) value of the data. """
        return self.data.min()
