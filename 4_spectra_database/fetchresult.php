<html>
<head>
<title>Result</title>


</head>
<body>

<?php
$host ="localhost";
$user =" ";
$pass =" ";
$databasename=" ";
$tablename=" ";
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

$SMILE=$_POST['$mol_SMILE'];
	
echo "$SMILE";

echo "<br />";
echo "<br />";
	
echo "Spectra absorption is quantized by CR values in the table.";
echo "<br />";
echo "<br />";
echo "The CR of the strongest absorption in the range equals \"1\". ";
echo "<br />";
echo "<br />";
$SQL_command="SELECT * FROM Top1000spectra WHERE SMILE LIKE '$SMILE' ";

$result=mysql_query($SQL_command,$conn);
	
if (!$result) {
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
	
while ($rows=mysql_fetch_array($result))
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
