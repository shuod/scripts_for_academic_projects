<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Search moleclues for tandem solar cell </title>
</head>

<body>

<h2>1. Search moleclues for two layer tandem solar cell:</h2>
<h3></h3>
<li id="mol4tandem" font-size=12><span>Moleclues with complementary spectra:</span></li>
<img src="./static/moleclues_for_tandem.png" height="300"> </img>

<li id="search" font-size=12><span>Searching criteria for two layer tandem solar cells:</span></li>

The top layer and the bottom layer should have complementary CR values:
<br/>
molecular absorption is

<table>
<tr>
<td> The top layer UV range: </td>
<td>
<form action="fetchresult_mol4tandem.php" method="post">
<select name="layer1_UV_abs">
<option value="0.75"> High (CR > 0.75) </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="0">No (0.25 > CR )</option>
</select>
</td>
<td> and </td>
<td> the bottom layer UV range: </td>
<td>
<form action="#" method="post">
<select name="layer2_UV_abs">
<option value="0.75"> High (CR > 0.75) </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="0">No (0.25 > CR )</option>
</select>
</td>


</tr>

<tr>
<td> The top layer VIS I range: </td>
<td>
<select name="layer1_VISI_abs">
<option value="0.75"> High (CR > 0.75) </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="0">No (0.25 > CR )</option>
</select>
</td>

<td> and </td>
<td> The bottom layer VIS I range: </td>
<td>
<select name="layer2_VISI_abs">
<option value="0.75"> High (CR > 0.75) </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="0">No (0.25 > CR )</option>
</select>
</td>
</tr>
	

<tr>
<td> The top layer VIS II range: </td>
<td>
<select name="layer1_VISII_abs">
<option value="0.75"> High (CR > 0.75) </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="0">No (0.25 > CR )</option>
</select>
</td>
<td> and </td>
<td> the bottom layer VIS II range: </td>
<td>
<select name="layer2_VISII_abs">
<option value="0.75"> High (CR > 0.75) </option>
<!--
<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->
<option value="0">No (0.25 > CR )</option>
</select>
</td>
</tr>


<tr>
<td> The top layer IR range: </td>
<td>
<select name="layer1_IR_abs">
<option value="0.75"> High (CR > 0.75) </option>

<!--<option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->

<option value="0">No (0.25 > CR)</option>
</select>
</td>
<td> and </td>
<td> the bottom layer IR range: </td>
<td>
<select name="layer2_IR_abs">
<option value="0.75"> High (CR > 0.75) </option>

<!-- <option value="0.5"> Medicore ( 0.75 > CR  > 0.5) </option>
<option value="0.25"> Low ( 0.5 > CR > 0.25 )</option> -->

<option value="0">No (0.25 > CR )</option>
</select>
</td>

</tr>


<input type="submit" name="submit" value="Locate moleclues" />
</form>
</table>


<?php
$selected_val = $_POST['layer1_UV_abs'];
echo "You have selected :" .$selected_val;
?>

</body>
</html>