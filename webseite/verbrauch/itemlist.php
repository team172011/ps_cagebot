<?php

	echo "<br>";
	//echo $_GET['item'];
  $items = zeigeItemliste($_GET['item']);
  

  while($row = mysql_fetch_assoc($items)) {
    echo '<table><tr><td style="vertical-align: Top;width:120px">';
     echo '<a href="index.php?se=111&item='. $row['mat_id'] . '"><img src="imgs/' . $row['materials_groups_image'] . '" style="max-width:80px; max-height:100px; margin-right: 20px"></a>';			// Jeder der eingeloggt ist
    echo '</td><td style="max-width:400px; align: left">';
    if (isset($row['dummy']) && !is_null($row['dummy'])) {
    echo $row['dummy']. "<br><br>";
    }
    echo $row['materials_groups_name']. "<br><br>";
    echo $row['materials_groups_description']. "<br><br>";
    echo "Hersteller: " . $row['materials_producers_name']. "<br><br>";
    echo "Kategorie: " . $row['materials_types_name']. "<br><br>";
    echo "Ablaufdatum: " . $row['best_before']. "<br><br>";
    echo '</td></tr></table>';
  }


?>