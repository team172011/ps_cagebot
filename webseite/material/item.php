<?php
if (isset($_GET['item'])) {
	echo "<br>";
	//echo $_GET['item'];
  $items = zeigeItem($_GET['item']);
  
  echo "<center>";
  while($row = mysql_fetch_assoc($items)) {
    echo '<table><tr><td style="vertical-align: Top">';
    echo '<img src="imgs/' . $row['materials_groups_image'] . '" style="max-width:200px; max-height:400px; margin-right: 30px">';
    echo '</td><td style="max-width:400px">';
    
    echo $row['materials_groups_name']. "<br><br>";
    echo $row['materials_groups_description']. "<br><br>";
    echo "Hersteller: " . $row['materials_producers_name']. "<br><br>";
    echo "Kategorie: " . $row['materials_types_name']. "<br><br>";
    echo "Ablaufdatum: " . $row['best_before']. "<br><br>";
    echo '</td></tr></table>';
  }
  echo "</center>";
}
?>