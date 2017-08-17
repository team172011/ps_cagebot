<?php
//statusabfragen 1=Fux/Aktiver (nur lesen) 10=Schreibrechte(Artikel eintragen) 20=Schriftwart(Keyword bearbeiten) 255=Superadmin

	//if($_SESSION["atvuser_aktiv"]>0){
		echo "<div id=\"menutable\">";
		echo "<table height=\"35\" width=\"700px\"><tr><td>";
		echo "<ul class=\"navi\">";
		echo "<li";
		if(isset($_GET['atv']) && $_GET['atv']==01){
			echo " class=\"m_akt\"";
		}
		echo "><a href=\"index.php?atv=01&se=100\">Medikamente</a></li>";			// Jeder der eingeloggt ist
		echo "<li";
		if(isset($_GET['atv']) && $_GET['atv']==02){
			echo " class=\"m_akt\"";
		}
		echo "><a href=\"index.php?atv=02&se=200\">Verbandswagen</a></li>";				// Jeder der eingeloggt ist
		echo "<li";
		if(isset($_GET['atv']) && $_GET['atv']==03){
			echo " class=\"m_akt\"";
		}
		echo "><a href=\"index.php?atv=03&se=300\">Patienten</a></li>";				// Jeder der eingeloggt ist
		echo "<li";
		if(isset($_GET['atv']) && $_GET['atv']==04){
			echo " class=\"m_akt\"";
		}
		echo "><a href=\"index.php?atv=04&se=400\">Mitarbeiter</a></li>";					// Jeder der eingeloggt ist
		echo "</ul>";
		echo "</td>";
		echo "</tr>";
		echo "</table>";
		echo "</div>";
?>