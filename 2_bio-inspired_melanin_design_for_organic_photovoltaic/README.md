# Bio-inspired melanin design for organic photovoltaic



## Scripts
**data extraction:**

  - <u>*p1\_extract\_homolumo\_singlefile.py*</u>: Extracting HOMO/LUMO calculation results from Gaussian09 output file;
  - <u>*p1\_extract\_homolumo\_folder\_difflevels.py*</u>: Extracting HOMO/LUMO calculation results from the folder containing many Gaussian09 files;
  - <u>*p1\_extract\_tdsinglet\_gap\_singlefile.py*</u>:  Extracting Bandgap calculation results from Gaussian09 output file;
  - <u>*p1\_extract\_tdsinglet\_gap\_folder\_difflevels.py*</u>: Extracting Bandgap calculation results from the folder containing many Gaussian09 files;

**data reading from files**

- <u>*read\_a\_cell\_in\_excel2013.py*</u>; read_data_from_excel2013.py: wrapper for "openpyxl" to read excel file;

**data calculation**

- *<u>4\_2mt\_cal\_abs.c, 4\_10mt\_cal\_abs.c</u>*: Bash script cannot be parallel executed; This program is using C to start multiple threads, and each thread run a bash script; therefore, the power of multi-cores CPU can be fully utilized.

**plot figures**
- *<u>heatmap\_of\_PCE.py</u>*: generate a heatmap of PCE values for all combinations of end groups.
- *<u>place\_PCE\_on\_scharberM\_exa2\_xGap\_yLUMO.py</u>*: plot the contour map of Scharber's Model (Theoretical model of organic photovoltaic) and place our result molecules on the map.

