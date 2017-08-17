<?php
if (isset($_GET['group'])) {
	echo "<br>";
	//echo $_GET['item'];
  $items = zeigeGroup($_GET['group']);
  
  echo "<center>";
  while($row = mysql_fetch_assoc($items)) {
    echo '<table><tr><td style="vertical-align: Top">';
    echo '<img src="imgs/' . $row['materials_groups_image'] . '" style="max-width:200px; max-height:400px; margin-right: 30px">';
    echo '</td><td style="max-width:400px">';
    
    echo "<b>" . $row['materials_groups_name'] . "</b><br><br>";
    echo $row['materials_groups_description'] . "<br><br>";
    echo "Hersteller: " . $row['materials_producers_name'] . "<br><br>";
    echo "Kategorie: " . $row['materials_types_name'] . "<br><br>";
    if (isset($row['materials_groups_application'])) {
      echo "Anwendung: " . $row['materials_groups_application'] . "<br><br>";
    };
    if (isset($row['materials_groups_warning'])) {
      echo "<b>Anwendung: " . $row['materials_groups_warning'] . "</b><br><br>";
    };
    echo '</td></tr></table>';
  }
  echo "</center>";
}
?>