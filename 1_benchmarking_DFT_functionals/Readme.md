## Benchmarking functionals

Goal: Report accuracy and performance of different functionals for Density Functional Theory calculation on molecular orbital energies: HOMO (Highest Occupied Molecular Orbitals), LUMO (Lowest Unoccupied Molecular Orbitals) and Bandgap.



phase 1 : 

Title: Accurate predictions on the performance of organic photovoltaic materials: Benchmarking studies from DFT and TD-DFT

Results:

- Predictions from different functionals on 29 molecules ;
- Linear regression formula for corrections on calculated values (scaling factors) in order to match experimental values;
- HSE06 functional was selected due to the accuracy on both HOMO and Bandgap predictions;

**Scripts:**

**data extraction:**

- extract_homolumo_singlefile.py: Extracting HOMO/LUMO calculation results from Gaussian09 output file

- extract_homolumo_folder_difflevels.py: Extracting HOMO/LUMO calculation results from the folder containing many Gaussian09 files

- extract_tdsinglet_gap_singlefile.py:  Extracting Bandgap calculation results from Gaussian09 output file

- extract_tdsinglet_gap_folder_difflevels.py: Extracting Bandgap calculation results from the folder containing many Gaussian09 files

**data reading from file**
- read_a_cell_in_excel2013.py; read_data_from_excel2013.py: wrapper for "openpyxl" to read excel file;

**linear regress calculation from different python library**
- linear_regression_using_numpy_linalg2: Using numpy to do linear regression
- scipy_stats.py: Using scipy to do linear regression 
- sklearn_linear.py: Using sklearn to do linear regression (a wrapper of linear regression in scipy)
- Linear Regression.xls

![Result from linear_regression_using_numpy_linalg2](linear_regression_using_numpy_linalg2.png)
