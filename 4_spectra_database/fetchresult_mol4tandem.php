<html>
<head>
<title>Result</title>


</head>
<body>

<?php
$host =" ";
$user =" ";
$pass =" ";
$databasename=" ";
$tablename=" ";
	
$criteria_high = 0.5;
$criteria_low = 0.35;
	
$conn=mysql_connect($host,$user,$pass) or die ("<p> logging on has not succeeded.</p>");


if ($db=mysql_select_db($databasename))
	{
		echo "<br> $databasename is the current database now.<br />";
	}
else	
	{	
		$error_message =mysql_error();
		$error_number=mysql_errno();
		echo "<br> $error_number:$error_message</br>";
		die ("<br> Database $databasename unknown.</br>");
	}	


echo "Following record(s) is based on the user input: ";

echo "<br/>";
echo "<br/>";
	
$UV_layer=$_POST['UV_abs'];
$VISI_layer=$_POST['VISI_abs'];
$VISII_layer=$_POST['VISII_abs'];
$IR_layer=$_POST['IR_abs'];

	
echo "$IR_layer";
	
echo "<br />";
echo "<br />";
	
echo "Spectra absorption is quantized by CR values in the table.";
echo "<br />";
echo "<br />";
echo "The CR of the strongest absorption in the range equals \"1\". ";
echo "<br />";
echo "<br />";
	
	
	
$SQL_command0="SELECT * FROM Top1000spectra ";
	
	
if ($UV_layer == 'Top'){
	$SQL_commandUV_4top = "where UV > $criteria_high ";	
	$SQL_commandUV_4bottom = "where UV < $criteria_low ";
}
else{
	$SQL_commandUV_4top = "where UV < $criteria_low ";
	$SQL_commandUV_4bottom = "where UV > $criteria_high ";
}
	

	

if ($VISI_layer == 'Top'){
	$SQL_commandVISI_4top = "and VISI > $criteria_high ";	
	$SQL_commandVISI_4bottom = "and VISI < $criteria_low ";
}
else{
	$SQL_commandVISI_4top = "and VISI < $criteria_low ";
	$SQL_commandVISI_4bottom = "and VISI > $criteria_high ";
}
	
	
if ($VISII_layer == 'Top'){
	$SQL_commandVISII_4top = "and VISII > $criteria_high ";	
	$SQL_commandVISII_4bottom = "and VISII < $criteria_low ";
}
else{
	$SQL_commandVISII_4top = "and VISII < $criteria_low ";
	$SQL_commandVISII_4bottom = "and VISII > $criteria_high ";
}
	
	
if ($IR_layer == 'Top'){
	$SQL_commandIR_4top = "and IR > $criteria_high ";	
	$SQL_commandIR_4bottom = "and IR < $criteria_low ";
}
else{
	$SQL_commandIR_4top = "and IR < $criteria_low ";
	$SQL_commandIR_4bottom = "and IR > $criteria_high ";
}


$SQL_command_4top = $SQL_command0.$SQL_commandUV_4top.$SQL_commandVISI_4top.$SQL_commandVISII_4top.$SQL_commandIR_4top;
	
echo "$SQL_command_4top";
echo "<br />";
echo "<br />";
	
echo "According to the criteria above, the moleclues selected for the top layers are:";
$result_4top=mysql_query($SQL_command_4top,$conn);
	
if (!$result_4top) {
    die('Query results: ' . mysql_error());
}
	

	
echo "<table border=1 name='table' id='table'>";
echo "<tr><th>ID</th>";
echo "<th>SMILE code </th>";
echo "<th>Formula</th>";
echo "<th>UV</th>";
echo "<th>VISI</th>";
echo "<th>VISII</th>";
echo "<th>IR</th></tr>";

$counter=1;
	
while ($rows=mysql_fetch_array($result_4top))
	{	
		

		if ($counter%2)
		{
		echo "<tr Bgcolor=#00FFFF><td>$rows[0]</td>";
		echo "<td>$rows[1]</td>";
		echo "<td>$rows[2]</td>";
		echo "<td>$rows[3]</td>";
		echo "<td>$rows[4]</td>";
		echo "<td>$rows[5]</td>";
		echo "<td>$rows[6]</td></tr>";
		}
		else
		{
		echo "<tr Bgcolor=#FFFFFF><td>$rows[0]</td>";
		echo "<td>$rows[1]</td>";
		echo "<td>$rows[2]</td>";
		echo "<td>$rows[3]</td>";
		echo "<td>$rows[4]</td>";
		echo "<td>$rows[5]</td>";
		echo "<td>$rows[6]</td></tr>";
		}
		$counter=$counter+1;
	}
echo "</table>";
echo $counter-1,"record(s) find.<br />";
	
	
$SQL_command_4bottom = $SQL_command0.$SQL_commandUV_4bottom.$SQL_commandVISI_4bottom.$SQL_commandVISII_4bottom.$SQL_commandIR_4bottom;

echo "<br />";
echo "<br />";
	
echo "$SQL_command_4bottom";	

echo "<br />";
echo "<br />";
	
echo "According to the criteria above, the moleclues selected for the bottom layers are:";
	
$result_4bottom=mysql_query($SQL_command_4bottom,$conn);
	
if (!$result_4bottom) {
    die('Query results: ' . mysql_error());
}
	

	
echo "<table border=1 name='table' id='table'>";
echo "<tr><th>ID</th>";
echo "<th>SMILE code </th>";
echo "<th>Formula</th>";
echo "<th>UV</th>";
echo "<th>VISI</th>";
echo "<th>VISII</th>";
echo "<th>IR</th></tr>";

$counter=1;
	
while ($rows=mysql_fetch_array($result_4bottom))
	{	
		

		if ($counter%2)
		{
		echo "<tr Bgcolor=#00FFFF><td>$rows[0]</td>";
		echo "<td>$rows[1]</td>";
		echo "<td>$rows[2]</td>";
		echo "<td>$rows[3]</td>";
		echo "<td>$rows[4]</td>";
		echo "<td>$rows[5]</td>";
		echo "<td>$rows[6]</td></tr>";
		}
		else
		{
		echo "<tr Bgcolor=#FFFFFF><td>$rows[0]</td>";
		echo "<td>$rows[1]</td>";
		echo "<td>$rows[2]</td>";
		echo "<td>$rows[3]</td>";
		echo "<td>$rows[4]</td>";
		echo "<td>$rows[5]</td>";
		echo "<td>$rows[6]</td></tr>";
		}
		$counter=$counter+1;
	}
echo "</table>";
echo $counter-1,"record(s) find.<br />";
	
	
?>
</body>
</html>
