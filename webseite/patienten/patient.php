i bims 1 Patient!!!<br>
<?php
if (isset($_GET['patient'])) {
	echo "<br>";
  $items = zeigePatient($_GET['patient']);
  
  echo "<center>";
  while($row = mysql_fetch_assoc($items)) {
    echo '<table><tr><td style="vertical-align: Top">';
    echo '<img src="imgs/' . $row['patient_image'] . '" style="max-width:200px; max-height:400px; margin-right: 30px">';
    echo '</td><td style="max-width:400px">';
    
      echo "<b>" . $row['Vorname'] . " " . $row['Nachname'] . "</b><br><br>";
    echo "Geburtstag: ". $row['Geburtstag']. "<br><br>";
    echo "Diagnose: " . $row['Grund']. "<br><br>";
    if (isset($row['Information'])) {
      echo "Info: " . $row['Information']. "<br><br>";
    }
    $allergyItems = zeigePatientAllergie($_GET['patient']);
    if (isset($allergyItems) && !is_null(mysql_fetch_assoc($allergyItems))) {
      echo '<b>Bekannte Unverträglichkeiten:</b><br>';
      echo '<table style="align: Left">';
      while($rowa = mysql_fetch_assoc($allergyItems)) {
        
        echo '<tr style="align: Left"><td style="vertical-align: Top; align: Right; padding-top: 40px">';
        echo '<a href="index.php?se=122&group='. $rowa['material_groups_id'] . '"><img src="imgs/' . $rowa['materials_groups_image'] . '" style="max-width:100px; max-height:100px; margin-right: 20px"></a>';			// Jeder der eingeloggt ist
        echo '</td><td style="vertical-align: Top; max-width:400px; align: left; witdh: 600px; padding-top: 10px">';
        
        echo "<b>" . $rowa['materials_groups_name']. "</b><br><br>";
        echo $rowa['materials_groups_description']. "<br><br>";
        echo '</td></tr>';
      }
      echo '</table>';
    }
    echo '</td></tr></table>';
  }
  echo "</center>";
}
?>