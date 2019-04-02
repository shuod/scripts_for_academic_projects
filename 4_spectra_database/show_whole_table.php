<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>show_whole_table</title>
</head>

<body>

<?php
$host =" ";
$user =" ";
$pass =" ";
$databasename=" ";
$tablename=" ";
$conn=mysql_connect($host,$user,$pass) or die ("<p> logging on has not succeeded.</p>");
echo "<p> $user has Logged on succeessfully.</p><br />";

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


echo "Following record(s) is based on the SMILE input: <br/>";

$input_SMILE=$_POST['$mol_SMILE'];
	
echo "$input_SMILE <br />";

$SQL_command="SELECT * FROM Top1000spectra WHERE SMILE like '$input_SMILE' ";

$result=mysql_query($SQL_command);
	
if (!$result) {
    die('Invalid query: ' . mysql_error());
}
	
$rows=mysql_affected_rows($conn);
	
$colums=mysql_num_fields($result);

echo "<table><tr>";
        for($i=0; $i < $colums; $i++){
            $field_name=mysql_field_name($result,$i);
            echo "<th>$field_name</th>";
        }
        echo "</tr>";
        while($row=mysql_fetch_row($result)){
            echo "<tr>";
            for($i=0; $i<$colums; $i++){
                echo "<td>$row[$i]</td>";
            }
            echo "</tr>";
        }
        echo "</table>";

	
	

?>

</body>
</html>