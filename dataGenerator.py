import numpy as np

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Author: Peter Bowman-Davis, Nov 20, 2023                          #
# Helper class to generate data for use in timeseries exploration   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class dataGenerator:
    def __init__(self, **kwargs):
        self.resolution = kwargs.get('resolution', 1000)
        self.amplitude_min = kwargs.get('amplitude_min', 0.0)
        self.amplitude_max = kwargs.get('amplitude_max', 1.0)
        self.scale_min = kwargs.get('scale_min', 0)
        self.scale_max = kwargs.get('scale_max', 999)
        self.noise = kwargs.get('noise', 0.2)
        self.samples = kwargs.get('samples', 21)
        self.t_min = kwargs.get('t_min', 0)
        self.t_max = kwargs.get('t_max', 2)
        self.fxn = kwargs.get('fxn', lambda x: np.sin(2 * np.pi *x)+1)

        seed = kwargs.get('seed')
        if seed is not None:
            np.random.seed(seed)

    def generate(self):
        t = np.linspace(self.t_min, self.t_max, self.resolution)
        amplitude = self.amplitude_min + (self.amplitude_max - self.amplitude_min) * self.fxn(t)
        amplitude = amplitude + self.noise * np.random.rand(self.resolution)
        scaled_amplitude = np.interp(amplitude, (amplitude.min(), amplitude.max()), (self.scale_min, self.scale_max))
        sample_indices = np.linspace(0, self.resolution-1, self.samples) 
        sample_indices = sample_indices.astype(int)
        sample_time = t[sample_indices]
        sampled_amplitude = scaled_amplitude[sample_indices]
        sampled_amplitude = sampled_amplitude.astype(int)
        return (sample_time,sampled_amplitude)

    def generateStringOutput(self):
        (sample_time,sampled_amplitude) = self.generate()
        return " ".join(str(x) for x in sampled_amplitude)
