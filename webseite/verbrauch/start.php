<?php

	echo "<br>";
	//echo $_GET['item'];
  $items = verbrauchStart();
  
  echo "<center>";
  echo '<table style="align: Left">';
  while($row = mysql_fetch_assoc($items)) {
    echo '<tr style="align: Left"><td style="vertical-align: Top; align: Right; padding-top: 40px">';
    echo '<a href="index.php?se=122&group='. $row['material_group_id'] . '"><img src="imgs/' . $row['materials_groups_image'] . '" style="max-width:200px; max-height:200px; margin-right: 30px"></a>';			// Jeder der eingeloggt ist
    echo '</td><td style="vertical-align: Top; max-width:400px; align: left; witdh: 600px; padding-top: 40px">';
    echo "<b>" . $row['materials_groups_name']. "</b><br><br>";
    echo $row['materials_groups_description']. "<br><br>";
    echo "Hersteller: " . $row['materials_producers_name']. "<br><br>";
    echo "Kategorie: " . $row['materials_types_name']. "<br><br>";
    echo "Anzahl: " . $row['Anzahl']. "<br><br>";
    echo '</td></tr>';
  }
  echo "</table></center>";

?>