# scripts_for_projects
Codes(shell, python, matlab, labview, etc ) made for my projects.

## 1_benchmarking_DFT_functionals
**phase1 Goals:** Report accuracy and performance of different functionals for Density Functional Theory calculation on molecular orbital energies: HOMO (Highest Occupied Molecular Orbitals), LUMO (Lowest Unoccupied Molecular Orbitals) and Bandgap.

Results: 

- Predictions from different functionals on 29 molecules ;

- Linear regression formula for corrections on calculated values (scaling factors) in order to match experimental values;

- HSE06 functional was selected due to the accuracy on both HOMO and Bandgap predictions;

**phase2 Goals:** Random trees and other machine learning methods were tested against traditional DFT/TD-DFT methods;

- HOMOs: RF and DFT have more or less similar MAEs (Mean average error);

- Bandgaps: RF has a larger MAEs than TD-DFT;

## 2_bio-inspired_melanin_design_for_photovoltaic

**Phase1 Goals:** 
Explore the rules behind spectrum change after adding electron donating or withdrawing groups at both ends of a natural black pigment eumelanin; Use the rules to design novel organic photovoltaic molecules with a better solubility and power conversion efficiency.

Results: 

- (phase1) Adding EWGs (electron withdrawing groups) at both ends will change the HOMO (Highest occupied molecular orbitals): the stronger the EWGs the deeper the HOMO;

- (phase1) Adding groups of different properties (EWG or EDG) at each end will change the bandgap: the stronger the EWG and EDG, the narrower the bandgap;

- (phase1) The molecule backbone (framework) based on EndgroupX-benzene-eumelanin-benzene-EndgroupY has the maximum PCE around 9%.

**Phase2 Goals**
Explore other combinations of spacer molecule, while keep the core still be eumelanin.

Results:
- (phase2) with H being the two ends (No EWG or EDG power), the narrowest bandgap is 1.48ev when borole replacing benzene. This essentially boost the PCE to be larger than 11%.

- (phase2) Since borole has the possibility to hydrolysis, we also find substitution for it from the literature.

## 3_top1000_molecule_screening_for_tandem_solar_cells

**Phase1 Goals:**
Explore the correlations between solar spectrum coverage and the built pattern of top-1000 molecules in CEPDB database (Harvard Clean Energy Project Database); Apply the correlation found to discover molecules for tandem solar cell.

**Phase2 Goals:**
Using deep learning package DEEPCHEM to discover more molecule built pattern or spectrum shift rules beyond empirical photochemistry rules.



## 5 Helix melanin

## license
The Codes in this folder adopt MIT license. For details, check website: https://opensource.org/licenses/MIT

The documents in this folder adopt Creative Common 4.0 with : BY-NC-ND

`BY-NC-ND` – [Attribution-NonCommercial-NoDerivatives] 

For details, check website: https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode
