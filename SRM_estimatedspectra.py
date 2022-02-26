def SpecRepsentation(self, Sww, t_bins=None, plot='y'):
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
    if Sww.shape[-1] == self.t_axis_4simu.shape[0]:
        for i in range(1, self.N1):
            sum = sum + A_n[i] * np.cos(w_n[i] * self.t_axis_4simu + phi_n[i])
    elif Sww.shape[-1] < self.t_axis_4simu.shape[0]:
        # assert(t_bins != None)
        for i in range(1, self.N1):
            f = interpolate.interp1d(t_bins, 
                                     A_n[i], 
                                     kind='next', 
                                     bounds_error=False, 
                                     fill_value='extrapolate')
            A_new = f(self.t_axis_4simu)
            sum = sum + A_new * np.cos(w_n[i] * self.t_axis_4simu + phi_n[i])
    

    simulation = sum * np.sqrt(2)
    # print('sampling frequency:', Fs)
    t_upper_limit = 2 * np.pi / (2 * self.wu)
    print("the lower limit of sampling frequency:", math.ceil(1 / t_upper_limit))
    print("the length of the simulation", simulation.shape)
    if plot == 'y':
        plt.plot(self.t_axis_4simu, simulation)
    return simulation