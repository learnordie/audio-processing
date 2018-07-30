#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Testing read_audio.py """


import sys
import os
import numpy
import pytest

# before importing modules, we need to append this path to the PYTHONPATH
sys.path.append('$HOME/Projects/audio_processing')

import audio


# -------------------------------- #
# Objects needed to do the testing #
# -------------------------------- #

filename1 = os.path.join(os.path.expanduser("~"),
                         "Projects", "audio_processing", "samples",
                         "stereo_44100_16bits.wav")
stereo_44100_16bits = audio.Audio(filename1)

filename2 = os.path.join(os.path.expanduser("~"),
                         "Projects", "audio_processing", "samples",
                         "mono_22050_16bits.wav")

mono_22050_16bits = audio.Audio(filename2)

filename3 = os.path.join(os.path.expanduser("~"),
                         "Projects", "audio_processing", "samples",
                         "mono_44100_32bits.wav")
mono_44100_32bits = audio.Audio(filename3)

filename4 = os.path.join(os.path.expanduser("~"),
                         "Projects", "audio_processing", "samples",
                         "harvard.wav")
harvard = audio.Audio(filename4)

# --------------------- #
# Functions for testing #
# --------------------- #


def test_read_wavfile_1():
    """ Test the function read_wavfile
        when its argument "filename" doesn't exist.
    """

    filename = os.path.join(os.path.expanduser("~"), "empty.file")
    with pytest.raises(Exception):
        empty_audio = audio.Audio(filename)
        print(empty_audio)


def test_read_wavfile_2():
    """ Test the function read_wavfile
        with the file "mono_44100_32bits.wav".

    I just check that not exception is raised.
    """

    filename = os.path.join(os.path.expanduser("~"),
                            "Projects", "audio_processing", "samples",
                            "stereo_44100_16bits.wav")

    stereo_44100_16bits = audio.Audio(filename)
    print(stereo_44100_16bits)


def test_sampling_rate_1():
    """ Test the sampling rate returned by the function read_wavfile
        using the file 'stereo_44100_16bits.wav'.

    """
    assert stereo_44100_16bits.rate == 44100


def test_sampling_rate_2():
    """ Test the sampling rate returned by the function read_wavfile
        using the file 'mono_22050_16bits.wav'.

    """
    assert mono_22050_16bits.rate == 22050


def test_is_mono_1():
    """ Test if an audio file is mono or not using the file
        mono_22050_16bits.wav', which actually is mono.

    """
    assert mono_22050_16bits.is_mono()


def test_is_mono_2():
    """ Test if an audio file is mono or not using the file
        'stereo_44100_16bits.wav', which actually is stereo.

    """
    assert not stereo_44100_16bits.is_mono()


def test_is_stereo_1():
    """ Test if an audio file is stereo or not using the file
        'stereo_44100_16bits.wav', which actually is stereo.

    """
    assert stereo_44100_16bits.is_stereo()


def test_is_stereo_2():
    """ Test if an audio file is stereo or not using the file
        mono_22050_16bits.wav', which actually is mono.

    """
    assert not mono_22050_16bits.is_stereo()


def test_number_of_sampling_points_1():
    """ Test the number of sampling points using the file
        'stereo_44100_16bits.wav', which actually is stereo.

    """
    assert stereo_44100_16bits.number_of_sampling_points() == 294909


def test_number_of_sampling_points_2():
    """ Test the number of sampling points using the file
        mono_22050_16bits.wav', which actually is mono.

    """
    assert mono_22050_16bits.number_of_sampling_points() == 147455


def test_data_type_1():
    """ Test the data type of the file 'mono_44100_32bits',
        which actually is int32.

    """
    assert mono_44100_32bits.data_type() == "int32"


def test_data_type_2():
    """ Test the data type of the file 'mono_22050_16bits.wav',
        which actually is int16.

    """
    assert mono_22050_16bits.data_type() == "int16"


def test_duration_1():
    """ Test the duration (in seconds) of the file
    'mono_22050_16bits.wav', which actually is 6.6873015873015875.

    """
    precision = 1e-15
    assert (mono_22050_16bits.duration() - 6.6873015873015875) < precision


def test_duration_2():
    """ Test the duration (in seconds) of the file
    'harvard.wav', which actually is 18.356190476190477.

    """
    precision = 1e-15
    assert (harvard.duration() - 18.356190476190477) < precision


def test_left_channel_1():
    """ Test the left_channel method of a mono file 'mono_22050_16bits.wav',
    where mono_22050_16bits.data is the only channel.

    """
    assert numpy.array_equal(mono_22050_16bits.left_channel(),
                             mono_22050_16bits.data)


def test_left_channel_2():
    """ Test the left_channel method of a stereo file 'harvard.wav',
    where harvard.data[:, 0]  is the left channel.

    """
    assert numpy.array_equal(harvard.left_channel(),
                             harvard.data[:, 0])


def test_right_channel_1():
    """ Test the right_channel method of a mono file 'mono_22050_16bits.wav',
    where mono_22050_16bits.data is the only channel.

    """
    assert numpy.array_equal(mono_22050_16bits.right_channel(),
                             mono_22050_16bits.data)


def test_right_channel_2():
    """ Test the rigth_channel method of a stereo file 'harvard.wav',
    where harvard.data[:, 1]  is the right channel.

    """
    assert numpy.array_equal(harvard.right_channel(),
                             harvard.data[:, 1])


def test_max_1():
    """ Test the maximum PCM (amplitude) value of the file
    'mono_22050_16bits.wav', which actually is 32767.

    """
    assert mono_22050_16bits.max() == 32767


def test_max_2():
    """ Test the maximum PCM (amplitude) value of the file
    'harvard.wav', which actually is 20329.

    """
    assert harvard.max() == 20329


def test_min_1():
    """ Test the minimum PCM (amplitude) value of the file
    'mono_22050_16bits.wav', which actually is -32768.

    """
    assert mono_22050_16bits.min() == -32768


def test_min_2():
    """ Test the minimum PCM (amplitude) value of the file
    'harvard.wav', which actually is -32768.

    """
    assert harvard.min() == -32768
