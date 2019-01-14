## Benchmarking DFT functionals

**Scripts:**

**data extraction:**

- <u>*p1\_extract\_homolumo\_singlefile.py*</u>: Extracting HOMO/LUMO calculation results from Gaussian09 output file;
- <u>*p1\_extract\_homolumo\_folder\_difflevels.py*</u>: Extracting HOMO/LUMO calculation results from the folder containing many Gaussian09 files;
- <u>*p1\_extract\_tdsinglet\_gap\_singlefile.py*</u>:  Extracting Bandgap calculation results from Gaussian09 output file;
- <u>*p1\_extract\_tdsinglet\_gap\_folder\_difflevels.py*</u>: Extracting Bandgap calculation results from the folder containing many Gaussian09 files;

**data reading from files**

- <u>*read_a_cell_in_excel2013.py*</u>; read_data_from_excel2013.py: wrapper for "openpyxl" to read excel file;

**linear regress calculation from different python library**
Also discussed in my blog essay: https://shuod.github.io/post/linear-regression-with-python-lib/

- <u>*p1\_linear\_regression\_using\_numpy\_linalg2*</u>: Using numpy to do linear regression;
- <u>*p1\_scipy\_stats.py*</u>: Using scipy to do linear regression;
- <u>*p1\_sklearn\_linear.py*</u>: Using sklearn to do linear regression (a wrapper of linear regression in scipy);
- <u>*p1\_Linear\ Regression.xls*</u>: Excel file template for linear regression calculation.



### phase2



**Script:**

- <u>*p2\_RF\_on\_gap.py*</u>: Python script to use random forest to predict bandgap.
- <u>*p2\_RF\_on\_HOMO.py*</u>: Python script to use random forest to predict HOMO.
- <u>*p2\_MAE\_plot.py*</u>: Python script to plot grouped bar figure.
