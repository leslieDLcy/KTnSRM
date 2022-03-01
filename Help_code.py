from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng()


fs = 10e3
N = 1e5
amp = 2 * np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
x = amp * np.sin(2 * np.pi * freq * time)
x += rng.normal(scale=np.sqrt(noise_power), size=time.shape)

plt.plot(time, x)
plt.show()





# Non-stationary process with separable spectrum
# S(w, t) = S(w) * g(t)^2

import numpy as np
import matplotlib.pyplot as plt


def Envelop_tfunc(t, b=4, c=0.8):
	return b * (np.exp(-c*t) - np.exp(-2*c*t))


# # validation 
# t = np.arange(0, 30, 0.1)
# gt = Envelop_tfunc(t)
# gt2 = gt**2
# print(type(gt))
# plt.plot(t, gt)
# print(gt2.shape)
# plt.show()




# Need to focus on the shape 

A_n = np.sqrt(2 * Sww * delta_w)

# e.g. Sww -> (65, 41)

# self.t_axis_4simu -> (2688, )

A_n[i] * np.cos(w_n[i] * self.t_axis_4simu + phi_n[i])

A_n[i].shape <--> self.t_axis_4simu



# starting from one dimension
# A_n[i].shape <--> self.t_axis_4simu

# step 2: for w_axis
# before (65, x) -> (1024, x)