<?php

	echo "<br>";
	//echo $_GET['item'];
  $items = patientenStart();
  
  echo "<center>";
  echo '<table style="align: Left">';
  while($row = mysql_fetch_assoc($items)) {
    echo '<tr style="align: Left"><td style="vertical-align: Top; align: Right; padding-top: 40px">';
    echo '<a href="index.php?se=311&patient='. $row['id'] . '"><img src="imgs/' . $row['patient_image'] . '" style="max-width:200px; max-height:200px; margin-right: 30px"></a>';			// Jeder der eingeloggt ist
    echo '</td><td style="vertical-align: Top; max-width:400px; align: left; witdh: 600px; padding-top: 40px">';
    echo "<b>" . $row['Vorname'] . " " . $row['Nachname'] . "</b><br><br>";
    echo "Geburtstag: ". $row['Geburtstag']. "<br><br>";
    echo "Diagnose: " . $row['Grund']. "<br><br>";
    if (isset($row['Information'])) {
      echo "Info: " . $row['Information']. "<br><br>";
    }
    echo '</td></tr>';
  }
  echo "</table></center>";

?>