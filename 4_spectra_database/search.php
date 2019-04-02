
<form method="post" action="fetchresult.php">

<tr>
<td>
<h2>Begin:</h2>
Year:
<SELECT name="byear">
<?php
for ($i=2000;$i<2009;$i++)
{
echo("<option value='$i'>".sprintf("%02d",$i)."</option>");
}
?>
</td>
<td>
Month:
<SELECT name="bmonth">
<?php
for ($i=1;$i<13;$i++)
{
echo("<option value='$i'>".sprintf("%02d",$i)."</option>");
}
?>
</td>
<td>
Day:
<SELECT name="bday">
<?php
for ($i=1;$i<32;$i++)
{
echo("<option value='$i'>".sprintf("%02d",$i)."</option>");
}
?>
</td>

</tr>
<br />
<br />

<tr>
<td>
<br />
<h2>End:</h2>
<br />
<td> Year:
<SELECT name="eyear">
<?php
for ($i=2000;$i<2009;$i++)
{
echo("<option value='$i'>".sprintf("%02d",$i)."</option>");
}
?>
</td>

<td> Month:
<SELECT name="emonth">
<?php
for ($i=1;$i<13;$i++)
{
echo("<option value='$i'>".sprintf("%02d",$i)."</option>");
}
?>
</td>
<td>Day:
<SELECT name="eday">
<?php
for ($i=1;$i<32;$i++)
{
echo("<option value='$i'>".sprintf("%02d",$i)."</option>");
}
?>
</td>

</tr>
<br></br>
<input type="submit" value="Check Now!">
<br>
<?php
echo 'value'.$_POST['byear'].'<br>';
?>





