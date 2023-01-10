# A simple and efficient approach to predict single-phase formation of high-entropy transition metal carbides
![Graphic Abstract](https://github.com/wylu-github/image/blob/main/Graphical%20abstract.jpg)
## 1. Empirical phase formation rules for HECs
#### Filename: parameters_calculation.py
#### Input: 50_senary_HECs.xlsx
#### Output: parameters_50HECs.xlsx
* To establish criteria for discriminating single-phase from multi-phase systems, 50 senary HECs as “testing example” are fabricated under the same process. The 50 systems and corresponding phase compositions are listed in **"50_senary_HECs.xlsx"**. <br>
* Mixing enthapy and lattice parameter difference can be calculated by **"parameters_calculation.py"**. <br>
* The calculated results are listed in **"parameters_50HECs.xlsx"** <br>
* The empirical phase formation rules established by mixing enthalpy and lattice parameter difference: <br>
<img src="https://github.com/wylu-github/image/blob/main/mix-delta.png" width="500px">

## 2. Calculations of ML descriptors
#### Filename: descriptors_calculation.py
#### Input: 382_HEC_systems.xlsx
#### Output: ml_dataset_17.xlsx
* **"382_HEC_systems.xlsx"** lists 382 equimolar HECs containing no less than 4 metal cations. <br>
* The selected descriptors of 382 systmes can be calculated by **"descriptors_calculation.py"**. <br>
* The calculated results are listed in **"ml_dataset_17.xlsx"** <br>
* The Pearson correlation heatmap of input features: <br>
<img src="https://github.com/wylu-github/image/blob/main/116heatmap.jpg" width="550px">

## 3. SFS feature selection
#### Filename: SFS.py
#### Input: ml_dataset_17.xlsx
#### Output: ml_dataset_LR.xlsx, ml_dataset_NB.xlsx, ml_dataset_RF.xlsx, ml_dataset_SVM_linear.xlsx, ml_dataset_SVM_rbf.xlsx, ml_dataset_SVM_sigmoid.xlsx
* **"ml_dataset_17.xlsx"** lists listed the original 17 descriptors selected for ML. <br>
* The SFS feature selection can be conducted by **"SFS.py"**. <br>
* The feature selection results are listed in **"ml_dataset_LR.xlsx", "ml_dataset_NB.xlsx", "ml_dataset_RF.xlsx", "ml_dataset_SVM_linear.xlsx", "ml_dataset_SVM_rbf.xlsx" and "ml_dataset_SVM_sigmoid.xlsx"** <br>
* The SFS learning curves of accuracy: <br>
<img src="https://github.com/wylu-github/image/blob/main/SFS%E5%AD%A6%E4%B9%A0%E6%9B%B2%E7%BA%BF.jpg" width="800px">

## 4. Phase prediction of 116 HECs
#### Filename: 116_accuracy.py
#### Input: ml_dataset_LR.xlsx, ml_dataset_NB.xlsx, ml_dataset_RF.xlsx, ml_dataset_SVM_linear.xlsx, ml_dataset_SVM_rbf.xlsx, ml_dataset_SVM_sigmoid.xlsx
#### Output: phase_prediction_116.xlsx
* The accuracy of selected six ML models before and after SFS feature selection can be calculated by **"SFS.py"**. <br>
* The calculated results are listed in **"phase_prediction_116.xlsx"** <br>
* The accuracy of six ML and DS evidence theory models using original 17 descriptors and descriptor subsets selected by SFS: <br>
<img src="https://github.com/wylu-github/image/blob/main/accuracy.png" width="600px">

## 5. Phase prediction of 382 HECs
#### Filename: 382_prediction.py
#### Input: ml_dataset_LR.xlsx, ml_dataset_NB.xlsx, ml_dataset_RF.xlsx, ml_dataset_SVM_linear.xlsx, ml_dataset_SVM_rbf.xlsx, ml_dataset_SVM_sigmoid.xlsx
#### Output: phase_prediction_382.xlsx
* The phase compostions of 382 HECs can be calculated by **"382_prediction.py"**. <br>
* The calculated results are listed in **"phase_prediction_382.xlsx"** <br>
* The predicted percentages of single-phase for HECs with different number of components: <br>
