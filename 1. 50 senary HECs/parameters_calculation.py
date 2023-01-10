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


# Lattice constant standard deviation of carbide components
def lattice_distortion(compo):
    a = np.array([[4.3380230327, 4.7233386150, 4.6500763935, 4.1593368387, 4.4987425765, 4.4680269405, 3.9665547640,
                   4.2737536062, 4.2339216847]])
    # a = np.array([[4.336313497, 4.723338615, 4.650076394, 4.160823896, 4.50608517, 4.480954251, 4.070232395,
    #                4.382501575, 4.390166008]])
    compo_sum = np.sum(compo)
    a_ave = 0
    diff2 = 0
    for i in range(9):
        a_ave = a_ave + compo[0][i] * a[0][i] / compo_sum
    for j in range(9):
        diff2 = diff2 + compo[0][j] * ((1 - a[0][j] / a_ave) ** 2) / compo_sum
    diff = diff2 ** 0.5
    return diff


# 'systems.xlsx' contains the chemical formula and compositions of high-entropy carbides
systems = pd.read_excel('50HECs.xlsx')
formula = list(systems.iloc[:, 1])
comp = systems.iloc[:, 2:-1].values
phase = list(systems.iloc[:, -1])

data_sum = np.zeros((50, 2))
for h in range(50):
    data_sum[h][0] = enthalpy(comp[h].reshape(1, 9))
    data_sum[h][1] = lattice_distortion(comp[h].reshape(1, 9))
data_sum = np.around(data_sum, 3)
dataset = pd.DataFrame(data_sum)
dataset.index = range(1, 51)
dataset.columns = ['mixing_enthalpy', 'lattice_parameter_difference']
dataset.insert(loc=0, column='formula', value=formula)
dataset.insert(loc=3, column='phase', value=phase)
dataset.to_excel("parameters_50HECs.xlsx")