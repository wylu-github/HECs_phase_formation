# A simple and efficient approach to predict single-phase formation of high-entropy transition metal carbides
![Graphic Abstract](https://github.com/wylu-github/image/blob/main/Graphical%20abstract.jpg)
## 1. Empirical phase formation rules for HECs
#### Filename: parameters_calculation.py
#### Input: 50_senary_HECs.xlsx
#### Output: parameters_50HECs.xlsx
* To establish criteria for discriminating single-phase from multi-phase systems, 50 senary HECs as “testing example” are fabricated under the same process. The 50 systems and corresponding phase compositions are listed in **50_senary_HECs.xlsx**. <br>
* Mixing enthapy and lattice parameter difference can be calculated by **parameters_calculation.py**. <br>
* The calculated results are listed in **parameters_50HECs.xlsx** <br>
* The empirical phase formation rules established by mixing enthalpy and lattice parameter difference:
<br>
<img src="https://github.com/wylu-github/image/blob/main/mix_delta.png" width="500px"> <br>
## 2. Calculations of ML descriptors
#### Filename: descriptors_calculation.py
#### Input: 382_HEC_systems.xlsx
#### Output: ml_dataset_17.xlsx
* **382_HEC_systems.xlsx** lists 382 equimolar HECs containing no less than 4 metal cations. <br>
* The selected descriptors of 382 systmes can be calculated by **descriptors_calculation.py**. <br>
* The calculated results are listed in **ml_dataset_17.xlsx** and the Pearson correlation heatmap of input features can be drawed <br>
<img src="https://github.com/wylu-github/image/blob/main/mix_delta.png" width="500px"> <br>
