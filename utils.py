import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import mlab

def EPSD_show(Pxx, freqs, t_bins, format):
        """Given the 3 elements returned by plt.specgram
        ie, (Pxx, freqs, t_bins)
                TODO:
        ----
        Change the colorbar
        """
        plt.figure(figsize=(6,4))
        if format=='2d':
            plt.pcolormesh(t_bins, freqs, Pxx, 
                    vmin=0, 
                    vmax=np.max(Pxx), 
                    shading='nearest', 
                    cmap='coolwarm')
            plt.colorbar()
            plt.xlabel('time (s)')
            plt.ylabel('freq (HZ)')
            # plt.grid()
            plt.title(r'the estimated  $S_{wt}$')
        elif format=='3d':
            fig = plt.figure(figsize=(8,8))    
            X, Y = np.meshgrid(t_bins, freqs)
            Z = Pxx
            ax = plt.axes(projection='3d')
            ax.plot_surface(X, Y, Z, cmap='viridis')
            ax.set_xlabel('time (s)')
            ax.set_ylabel('frequency (hz)')
            ax.set_zlabel('PSD')


def specgram3d(y, fs=200, title=None):
        """
        This func is borrowed elsewhere
        """
        ax = plt.axes(projection='3d')
        ax.set_title(title, loc='center', wrap=True)
        spec, freqs, t = mlab.specgram(y, Fs=fs, NFFT=256, noverlap=128)
        X, Y, Z = t[None, :], freqs[:, None], spec
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel('time (s)')
        ax.set_ylabel('frequencies (Hz)')
        ax.set_zlabel('PSD')
#         ax.set_zlim([0, 0.015])
#         ax.set_ylim([0, 10])
#         ax.set_xlim([0, 14])
#         ax.view_init(20, 220)
        ax.invert_xaxis()
#         ax.invert_yaxis()
        return X, Y, Z