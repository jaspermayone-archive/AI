#under development
from __future__ import division as _division

import wave as _wave
import numpy as _np

def _array2wav(a, sampwidth):
   
    if sampwidth == 3:
        # `a` must have dtype int32
        if a.ndim == 1:
            # Convert to a 2D array with a single column.
            a = a.reshape(-1, 1)
        # By shifting first 0 bits, then 8, then 16, the resulting output
        # is 24 bit little-endian.
        a8 = (a.reshape(a.shape + (1,)) >> _np.array([0, 8, 16])) & 255
        wavdata = a8.astype(_np.uint8).tostring()
    else:
        # Make sure the array is little-endian, and then convert using
        # tostring()
        a = a.astype('<' + a.dtype.str[1:], copy=False)
        wavdata = a.tostring()
    return wavdata


class Wav(object):

    def __init__(self, data, rate, sampwidth):
        self.data = data
        self.rate = rate
        self.sampwidth = sampwidth

    def __repr__(self):
        s = ("Wav(data.shape=%s, data.dtype=%s, rate=%r, sampwidth=%r)" %
             (self.data.shape, self.data.dtype, self.rate, self.sampwidth))
        return s





_sampwidth_dtypes = {1: _np.uint8,
                     2: _np.int16,
                     3: _np.int32,
                     4: _np.int32}
_sampwidth_ranges = {1: (0, 256),
                     2: (-2**15, 2**15),
                     3: (-2**23, 2**23),
                     4: (-2**31, 2**31)}


def _scale_to_sampwidth(data, sampwidth, vmin, vmax):
    # Scale and translate the values to fit the range of the data type
    # associated with the given sampwidth.

    data = data.clip(vmin, vmax)

    dt = _sampwidth_dtypes[sampwidth]
    if vmax == vmin:
        data = _np.zeros(data.shape, dtype=dt)
    else:
        outmin, outmax = _sampwidth_ranges[sampwidth]
        if outmin != vmin or outmax != vmax:
            vmin = float(vmin)
            vmax = float(vmax)
            data = (float(outmax - outmin) * (data - vmin) /
                    (vmax - vmin)).astype(_np.int64) + outmin
            data[data == outmax] = outmax - 1
        data = data.astype(dt)

    return data


def write(file, data, rate, scale=None, sampwidth=None):

    if sampwidth is None:
        if not _np.issubdtype(data.dtype, _np.integer) or data.itemsize > 4:
            raise ValueError('when data.dtype is not an 8-, 16-, or 32-bit '
                             'integer type, sampwidth must be specified.')
        sampwidth = data.itemsize
    else:
        if sampwidth not in [1, 2, 3, 4]:
            raise ValueError('sampwidth must be 1, 2, 3 or 4.')

    outdtype = _sampwidth_dtypes[sampwidth]
    outmin, outmax = _sampwidth_ranges[sampwidth]

    if scale == "none":
        data = data.clip(outmin, outmax-1).astype(outdtype)
    elif scale == "dtype-limits":
        if not _np.issubdtype(data.dtype, _np.integer):
            raise ValueError("scale cannot be 'dtype-limits' with "
                             "non-integer data.")
        # Easy transforms that just changed the signedness of the data.
        if sampwidth == 1 and data.dtype == _np.int8:
            data = (data.astype(_np.int16) + 128).astype(_np.uint8)
        elif sampwidth == 2 and data.dtype == _np.uint16:
            data = (data.astype(_np.int32) - 32768).astype(_np.int16)
        elif sampwidth == 4 and data.dtype == _np.uint32:
            data = (data.astype(_np.int64) - 2**31).astype(_np.int32)
        elif data.itemsize != sampwidth:
            # Integer input, but rescaling is needed to adjust the
            # input range to the output sample width.
            ii = _np.iinfo(data.dtype)
            vmin = ii.min
            vmax = ii.max
            data = _scale_to_sampwidth(data, sampwidth, vmin, vmax)
    else:
        if scale is None:
            vmin = data.min()
            vmax = data.max()
        else:
            # scale must be a tuple of the form (vmin, vmax)
            vmin, vmax = scale
            if vmin is None:
                vmin = data.min()
            if vmax is None:
                vmax = data.max()

        data = _scale_to_sampwidth(data, sampwidth, vmin, vmax)

   

    if data.ndim == 1:
        data = data.reshape(-1, 1)

    wavdata = _array2wav(data, sampwidth)

    w = _wave.open(file, 'wb')
    w.setnchannels(data.shape[1])
    w.setsampwidth(sampwidth)
    w.setframerate(rate)
    w.writeframes(wavdata)
    w.close()