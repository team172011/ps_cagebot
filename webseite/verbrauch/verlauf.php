<?php
	echo "<br>";
  $items = verbrauchVerlauf();
  
  echo "<center>";
  echo '<table style="align: Left">';
  while($row = mysql_fetch_assoc($items)) {
    echo '<tr style="align: Left"><td style="vertical-align: Top; align: Right; padding-top: 10px">';
    echo '<a href="index.php?se=111&item='. $row['mat_id'] . '"><img src="imgs/' . $row['materials_groups_image'] . '" style="max-width:50px; max-height:50px; margin-right: 10px"></a>';			// Jeder der eingeloggt ist
    echo '</td><td style="vertical-align: Top; max-width:400px; align: left; witdh: 600px; padding-top: 10px">';
    echo "<b>" . $row['materials_transfer_date']. "</b> " . $row['materials_groups_name'] . " <b>An:</b> " . $row['Vorname'] . " " . $row['Nachname'] . "<br><br>";
    echo '</td></tr>';
  }
  echo "</table></center>";

?>