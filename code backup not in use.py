from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt


'''code backup for 1d interpolation on t axis'''


        for i in range(1, self.N1):
            f = interpolate.interp1d(t_bins, 
                 A_n[i], 
                 kind='next', 
                 bounds_error=False, 
                 fill_value='extrapolate')

            A_new = f(self.t_axis_4simu)
            sum = sum + A_new * np.cos(w_n[i] * self.t_axis_4simu + phi_n[i])




# for backing up

# X, Y = np.meshgrid(t_bins, freqs)
# Z = Pxx

# fig = plt.figure(figsize=(8,8))
# ax = plt.axes(projection='3d')
# ax.plot_surface(X, Y, Z, cmap='viridis')
# ax.set_title('plot surface');

"""For 2D representation"""

# import matplotlib
# fig = plt.figure(figsize=(6,4))

# # nnormalize_instance = matplotlib.colors.Normalize()

# plt.pcolormesh(t_bins, freqs, Pxx, vmin=0, vmax=np.max(Pxx), shading='nearest', cmap='coolwarm')
# plt.colorbar()
# plt.xlabel('time (s)')
# plt.ylabel('freq (HZ)')
# # plt.grid()
# plt.title(r'$S_{wt}$')
# plt.show()