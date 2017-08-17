<?php

	echo "<br>";
	//echo $_GET['item'];
  $items = mitarbeiterStart();
  
  echo "<center>";
  echo '<table style="align: Left">';
  while($row = mysql_fetch_assoc($items)) {
    echo '<tr style="align: Left"><td style="vertical-align: Top; align: Right; padding-top: 40px">';
    echo '<img src="imgs/' . $row['image'] . '" style="max-width:200px; max-height:200px; margin-right: 30px">';
    echo '</td><td style="vertical-align: Top; max-width:400px; align: left; witdh: 600px; padding-top: 40px">';
    echo "<b>" . $row['Vorname'] . " " . $row['Nachname'] . "</b><br><br>";
    echo "Geburtstag: ". $row['Geburtstag']. "<br><br>";
    if (isset($row['Information'])) {
      echo "Info: " . $row['Information']. "<br><br>";
    }
    echo "Angestellt seit: ". $row['Angestellt seit']. "<br><br>";
    echo '</td></tr>';
  }
  echo "</table></center>";

?>