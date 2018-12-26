## Benchmarking functionals

Goal: Report accuracy and performance of different functionals for Density Functional Theory calculation on molecular orbital energies: HOMO (Highest Occupied Molecular Orbitals), LUMO (Lowest Unoccupied Molecular Orbitals) and Bandgap.



### phase 1 : 

Title: Accurate predictions on the performance of organic photovoltaic materials: Benchmarking studies from DFT and TD-DFT

Results:

- Predictions from different functionals on 29 molecules ;
- Linear regression formula for corrections on calculated values (scaling factors) in order to match experimental values;
- HSE06 functional was selected due to the accuracy on both HOMO and Bandgap predictions;

**Scripts:**

**data extraction:**

- <u>*extract_homolumo_singlefile.py*</u>: Extracting HOMO/LUMO calculation results from Gaussian09 output file;

- <u>*extract_homolumo_folder_difflevels.py*</u>: Extracting HOMO/LUMO calculation results from the folder containing many Gaussian09 files;

- <u>*extract_tdsinglet_gap_singlefile.py*</u>:  Extracting Bandgap calculation results from Gaussian09 output file;

- <u>*extract_tdsinglet_gap_folder_difflevels.py*</u>: Extracting Bandgap calculation results from the folder containing many Gaussian09 files;

**data reading from files**

- <u>*read_a_cell_in_excel2013.py*</u>; read_data_from_excel2013.py: wrapper for "openpyxl" to read excel file;

**linear regress calculation from different python library**
Also discussed in my blog essay: https://shuod.github.io/post/linear-regression-with-python-lib/

- <u>*linear_regression_using_numpy_linalg2*</u>: Using numpy to do linear regression;
- <u>*scipy_stats.py*</u>: Using scipy to do linear regression;
- <u>*sklearn_linear.py*</u>: Using sklearn to do linear regression (a wrapper of linear regression in scipy);
- <u>*Linear Regression.xls*</u>: Excel file template for linear regression calculation.

![Result from linear_regression_using_numpy_linalg2](linear_regression_using_numpy_linalg2.png)

### phase2

Goal: Gradient boosted random trees and other machine learning methods were tested against traditional DFT/TD-DFT methods;