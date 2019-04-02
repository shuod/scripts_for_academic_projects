<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Search moleclues for tandem solar cell </title>
</head>

<body>

<h2>1. Search moleclues for two layer tandem solar cell:</h2>
<h3></h3>
<li id="mol4tandem" font-size=12><span>Moleclues with complementary spectra for tandem solar cells.</span></li>

<li id="mol4tandem" font-size=12><span>  Each layer of tandem cells absorbs light in a certain range and the combination of them can be a total absorption of the sunlight:</span></li>
<img src="./static/moleclues_for_tandem.png" height="300"> </img>

<li id="search" font-size=12><span>Searching criteria for two layer tandem solar cells:</span></li>

The top layer and the bottom layer should have complementary CR values:
<br/>
molecular absorption is

<table>
<tr>
<td> The UV range (4.43 - 3.16eV) is absorbed by : </td>
<td>
<form action="fetchresult_mol4layers.php" method="post">
<select name="UV_abs">
<option value="Top"> Top </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="Bottom"> Bottom </option>
</select>
</td>
</tr>


<tr>

<td> The VIS I range (3.15 - 2.69eV) is absorbed by: </td>
<td>
<form action="#" method="post">
<select name="VISI_abs">
<option value="Top"> Top </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="Bottom"> Bottom </option>
</select>
</td>
</tr>



<tr>
<td> The VIS II range (2.68 - 1.59eV) is absorbed by: </td>
<td>
<select name="VISII_abs">
<option value="Top"> Top </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="Bottom"> Bottom </option>
</select>
</td>
</tr>



<tr>

<td> The IR range (1.58 - 0.31eV) is absorbed by: </td>
<td>
<select name="IR_abs">
<option value="Top"> Top </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="Bottom"> Bottom </option>
</select>
</td>
</tr>
	



<input type="submit" name="submit" value="Locate moleclues" />
</form>
</table>


</body>
</html>