import numpy as np
import pandas as pd

mix = np.array([[0, 55.178, 37.901, 1.566, -9.708, -39.739, 24.677, -12.019, -8.924],
                [55.178, 0, 3.575, 124.301, 3.927, 3.427, 143.363, 53.212, 51.094],
                [37.901, 3.575, 0, 108.077, 1.171, -8.277, 144.206, 65.936, 56.263],
                [1.566, 124.301, 108.077, 0, 38.134, 22.392, 4.933, 15.571, 10.576],
                [-9.708, 3.927, 1.171, 38.134, 0, -4.691, 63.229, 13.977, 31.356],
                [-39.739, 3.427, -8.277, 22.392, -4.691, 0, 49.878, 24.755, 43.745],
                [24.677, 143.363, 144.206, 4.933, 63.229, 49.878, 0, 16.044, 6.351],
                [-12.019, 53.212, 65.936, 15.571, 13.977, 24.755, 16.044, 0, -2.012],
                [-8.924, 51.094, 56.263, 10.576, 31.356, 43.745, 6.351, -2.012, 0]])


# Mixing enthalpy
def enthalpy(compo):
    h_mix = 0
    compo_sum = np.sum(compo)
    for i in range(9):
        for j in range(i + 1, 9):
            h_mix = h_mix + mix[i][j] * (compo[0][i] / compo_sum) * (compo[0][j] / compo_sum)
    return h_mix


# Mixing entropy
def entropy(compo):
    compo_sum = np.sum(compo)
    s = 0
    for i in range(9):
        if compo[0][i] != 0:
            s = s + compo[0][i]/compo_sum * (np.log(compo[0][i]/compo_sum))
            s_mix = -8.314 * s
    for i in range(9):
        for j in range(i + 1, 9):
            s_mix = s_mix - ((mix[i][j] * 1000 * (compo[0][i] / compo_sum) * (compo[0][j] / compo_sum)) ** 2)/(12 * 8.314 * (2273 ** 2))
    return s_mix


# Solid-solution formation temperature
def ssf_temperature(compo):
    tf = enthalpy(compo) * 1000 / entropy(compo)
    return tf


# Standard deviation of mixing enthalpy
def dev(compo):
    h_deviation2 = 0
    compo_sum = np.sum(compo)
    for i in range(9):
        for j in range(i + 1, 9):
            h_deviation2 = h_deviation2 + (compo[0][i] / compo_sum) * (compo[0][j] / compo_sum) * (mix[i][j] - enthalpy(compo)) ** 2
            h_dev = h_deviation2 ** 0.5
    return h_dev


# Standard deviation of mixing enthalpy (with different definition)
def dev0(compo):
    h_deviation2 = 0
    compo_sum = np.sum(compo)
    for i in range(9):
        for j in range(i + 1, 9):
            h_deviation2 = h_deviation2 + (compo[0][i] / compo_sum) * (compo[0][j] / compo_sum) * (mix[i][j] - 0) ** 2
            h_dev0 = h_deviation2 ** 0.5
    return h_dev0


# Standard deviation of positive mixing enthalpy
def dev1(compo):
    h_deviation2 = 0
    compo_sum = np.sum(compo)
    for i in range(9):
        for j in range(i + 1, 9):
            if mix[i][j] > 0:
                h_deviation2 = h_deviation2 + (compo[0][i] / compo_sum) * (compo[0][j] / compo_sum) * (mix[i][j] - 0) ** 2
                h_dev1 = h_deviation2 ** 0.5
    return h_dev1


# Standard deviation of negative mixing enthalpy
def dev2(compo):
    h_deviation2 = 0
    compo_sum = np.sum(compo)
    for i in range(9):
        for j in range(i + 1, 9):
            if mix[i][j] < 0:
                h_deviation2 = h_deviation2 + (compo[0][i] / compo_sum) * (compo[0][j] / compo_sum) * (mix[i][j] - 0) ** 2
                h_dev2 = h_deviation2 ** 0.5
    return h_dev2


# Average lattice constant of carbide components
def lattice_mean(compo):
    a = np.array([[4.3380230327, 4.7233386150, 4.6500763935, 4.1593368387, 4.4987425765, 4.4680269405, 3.9665547640,
                   4.2737536062, 4.2339216847]])
    compo_sum = np.sum(compo)
    a_ave = 0
    for i in range(9):
        a_ave = a_ave + compo[0][i] * a[0][i] / compo_sum
    return a_ave


# Lattice constant standard deviation of carbide components
def lattice_distortion(compo):
    a = np.array([[4.3380230327, 4.7233386150, 4.6500763935, 4.1593368387, 4.4987425765, 4.4680269405, 3.9665547640,
                   4.2737536062, 4.2339216847]])
    compo_sum = np.sum(compo)
    a_ave = 0
    diff2 = 0
    for i in range(9):
        a_ave = a_ave + compo[0][i] * a[0][i] / compo_sum
    for j in range(9):
        diff2 = diff2 + compo[0][j] * ((1 - a[0][j] / a_ave) ** 2) / compo_sum
    diff = diff2 ** 0.5
    return diff


# Average melting point of carbide components
def tm_mean(compo):
    tm = np.array([[3067, 3420, 3928, 2830, 3600, 3950, 1810, 2520, 2870]])
    compo_sum = np.sum(compo)
    tm_ave = 0
    for i in range(9):
        tm_ave = tm_ave + compo[0][i] * tm[0][i] / compo_sum
    return tm_ave


#  Melting point standard deviation of carbide components
def tm_dev(compo):
    tm = np.array([[3067, 3420, 3928, 2830, 3600, 3950, 1810, 2520, 2870]])
    compo_sum = np.sum(compo)
    tm_ave = 0
    diff2 = 0
    for i in range(9):
        tm_ave = tm_ave + compo[0][i] * tm[0][i] / compo_sum
    for j in range(9):
        diff2 = diff2 + compo[0][j] * ((tm[0][j] - tm_ave) ** 2) / compo_sum
    diff = diff2 ** 0.5
    return diff


# Average electronegativity of carbide components
def ele_negativity_mean(compo):
    x = np.array([[2.23, 2.05, 2.01, 2.08, 2.59, 2.32, 2.12, 2.47, 2.42]])
    compo_sum = np.sum(compo)
    x_ave = 0
    for i in range(9):
        x_ave = x_ave + compo[0][i] * x[0][i] / compo_sum
    return x_ave


# Electronegativity standard deviation of carbide components
def ele_negativity(compo):
    x = np.array([[2.23, 2.05, 2.01, 2.08, 2.59, 2.32, 2.12, 2.47, 2.42]])
    compo_sum = np.sum(compo)
    x_ave = 0
    diff2 = 0
    for i in range(9):
        x_ave = x_ave + compo[0][i] * x[0][i] / compo_sum
    for j in range(9):
        diff2 = diff2 + compo[0][j] * ((x[0][j] - x_ave) ** 2) / compo_sum
    diff = diff2 ** 0.5
    return diff


# Average valence electron concentration of carbide components
def vec(compo):
    veci = np.array([[4, 4, 4, 5, 5, 5, 6, 6, 6]])
    compo_sum = np.sum(compo)
    vec_ave = 0
    for i in range(9):
        vec_ave = vec_ave + compo[0][i] * veci[0][i] / compo_sum
        vec_mean = vec_ave + 4
    return vec_mean


# Valence electron concentration Standard deviation of carbide components
def vec_dev(compo):
    veci = np.array([[4, 4, 4, 5, 5, 5, 6, 6, 6]])
    compo_sum = np.sum(compo)
    vec_ave = 0
    diff2 = 0
    for i in range(9):
        vec_ave = vec_ave + compo[0][i] * veci[0][i] / compo_sum
    for j in range(9):
        diff2 = diff2 + compo[0][j] * ((veci[0][j] - vec_ave) ** 2) / compo_sum
    diff = diff2 ** 0.5
    return diff


# Average relative molecular mass of carbide components
def mass_mean(compo):
    mass = np.array([[59.88, 103.23, 190.51, 62.95, 104.92, 192.51, 64.01, 107.97, 195.91]])
    compo_sum = np.sum(compo)
    mass_ave = 0
    for i in range(9):
        mass_ave = mass_ave + compo[0][i] * mass[0][i] /compo_sum
    return mass_ave


# Relative molecular mass standard deviation of carbide components
def mass_dev(compo):
    mass = np.array([[59.88, 103.23, 190.51, 62.95, 104.92, 192.51, 64.01, 107.97, 195.91]])
    compo_sum = np.sum(compo)
    mass_ave = 0
    diff2 = 0
    for i in range(9):
        mass_ave = mass_ave + compo[0][i] * mass[0][i] / compo_sum
    for j in range(9):
        diff2 = diff2 + compo[0][j] * ((mass[0][j] - mass_ave) ** 2) / compo_sum
    diff = diff2 ** 0.5
    return diff


# 'systems.xlsx' contains the chemical formula and compositions of high-entropy carbides
systems = pd.read_excel('382_HEC_systems.xlsx')
formula = list(systems.iloc[:, 1])
comp = systems.iloc[:, 2:-1].values
phase = list(systems.iloc[:, -1])

data_sum = np.zeros((382, 17))
for h in range(382):
    data_sum[h][0] = enthalpy(comp[h].reshape(1, 9))
    data_sum[h][1] = entropy(comp[h].reshape(1, 9))
    data_sum[h][2] = ssf_temperature(comp[h].reshape(1, 9))
    data_sum[h][3] = dev(comp[h].reshape(1, 9))
    data_sum[h][4] = dev0(comp[h].reshape(1, 9))
    data_sum[h][5] = dev1(comp[h].reshape(1, 9))
    data_sum[h][6] = dev2(comp[h].reshape(1, 9))
    data_sum[h][7] = lattice_mean(comp[h].reshape(1, 9))
    data_sum[h][8] = lattice_distortion(comp[h].reshape(1, 9))
    data_sum[h][9] = tm_mean(comp[h].reshape(1, 9))
    data_sum[h][10] = tm_dev(comp[h].reshape(1, 9))
    data_sum[h][11] = ele_negativity(comp[h].reshape(1, 9))
    data_sum[h][12] = ele_negativity_mean(comp[h].reshape(1, 9))
    data_sum[h][13] = vec(comp[h].reshape(1, 9))
    data_sum[h][14] = vec_dev(comp[h].reshape(1, 9))
    data_sum[h][15] = mass_mean(comp[h].reshape(1, 9))
    data_sum[h][16] = mass_dev(comp[h].reshape(1, 9))
data_sum = np.around(data_sum, 3)
dataset = pd.DataFrame(data_sum)
dataset.index = range(1, 383)
dataset.columns = ['enthalpy', 'entropy', 'ssf_temperature', 'dev', 'dev0', 'dev+', 'dev-', 'lattice_mean',
                   'lattice_distortion', 'tm_mean', 'tm_dev', 'ele_negativity', 'ele_negativity_mean', 'vec',
                   'vec_dev', 'mass_mean', 'mass_dev']
dataset.insert(loc=0, column='formula', value=formula)
dataset.insert(loc=18, column='phase', value=phase)
dataset.to_excel("ml_dataset_17.xlsx")