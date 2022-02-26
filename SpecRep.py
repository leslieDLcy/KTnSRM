
# implementation for the Kanai Tajimi model and also
# implementation for Spectral Representation method by Shinozuka

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate

from KT_model import parameterized_KT_model, Envelop_tfunc1, nonsta_model
# np.random.seed(9527)


class SRM:
    def __init__(self, wu=100, N1=1024, fs=200, duration=16):
        self.wu = wu
        self.N1 = N1        
        self.fs = fs
        self.duration = duration
    # print('the cutoff frequency wu set as:', wu)
        self.t_axis_4simu = np.arange(0, self.duration, 1 / self.fs)  # dt = 1 / Fs
        self.w_axis_4simu = np.arange(0, self.wu, self.wu/self.N1)


    # @property
    # def t_axis_4simu(self):
    #     """Create the t-axis of the sample simulation"""
    #     t_axis_simu = np.arange(0, self.duration, 1 / self.fs)  # dt = 1 / Fs
    #     return t_axis_simu


    # # set up the w (rad/s) axis
    # @property
    # def w_axis_4simu(self):
    #     w_axis = np.arange(0, self.wu, self.wu/self.N1)
    #     return w_axis 



    def SpecRepsentation(self, Sww, plot='y'):
        '''
        For now, this func received a spectra as argument,
        which may be obtained from 'getSww_from_a_model' func
        '''
    
        # create the t axis
        n = np.arange(self.N1)
        delta_w = self.wu / self.N1
        w_n = n * delta_w
        A_n = np.sqrt(2 * Sww * delta_w)
        phi_n = np.random.uniform(0, 2 * np.pi, self.N1)
    
        # Note that A0=0 or S(w0)=0
        sum = 0
        for i in range(1, self.N1):
            sum = sum + A_n[i] * np.cos(w_n[i] * self.t_axis_4simu + phi_n[i])
        simulation = sum * np.sqrt(2)
        # print('sampling frequency:', Fs)
        t_upper_limit = 2 * np.pi / (2 * self.wu)
        print("the lower limit of sampling frequency:", math.ceil(1 / t_upper_limit))
        print("the length of the simulation", simulation.shape)
        if plot == 'y':
            plt.plot(self.t_axis_4simu, simulation)
        return simulation

































# # set up a simple function to plot the reference spectrum
# def plot_reference_spectrum(w, wu):
#     """
#     show the reference spectrum of the random process, which is the psd function
#     """
#     plt.plot(w, parameterize_KT_model(w, wg=5 * np.pi, zzeta = 0.63, S0= 0.011), color='red', linewidth=2, label='the reference spectrum of the process')
#     plt.xlim([0, wu])
#     plt.legend()

"""
calculate the upper limit of time step
i.e. Delta t <= 2*pi / 2*wu
time precision -> sampling rate
therefore, the sampling interval `dt` should be less than `t_upper_limit`
the less `dt` then the higher `Fs`
"""



# the relation between `Fs` and `wu`


def getSww_from_a_model(model, w_axis):
    # For now, it's used to give a spectra
    
    ''' stationary Sww -> a shape (N1, ) '''
    # Hint: the simplest case, only care resolution in `w_axis` and no `t_axis` is involved;
    # Since we are using a continuous func `parameterized_KT_model`, any input w will have a value;
    # so all good

    # Sww = PSDF(w_n)

    # back up
    # A_n = np.sqrt(2 * parameterize_KT_model(w_n) * delta_w)


    '''  non-stationary: S(w, t), which should have a shape (N1, t) '''
    # Hint: in this situation, we don't need to worry about t dimension;


    # Sww = EPSD(w_n) -> (N1, t)
    # a hint: for fs=100, duration=16 -> t = (1600, )

    # Sww = nonstatinary_model(w_n)
    return model(w_axis)
