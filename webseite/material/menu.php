<?php

	echo "<table height=\"8\" width=\"315px\"><tr><td align=\"center\">";
	echo "<ul class=\"navi\">";
	echo "<li";
	if(isset($_GET['se']) && $_GET['se']==100){
		echo " class=\"m_akt\"";
	}
	echo "><a href=\"index.php?atv=01&se=100\">Bibliothek</a></li>";			// Jeder der eingeloggt ist
	echo "</ul>";
	echo "</td>";
	echo "</tr>";
	echo "</table>";
//	echo "</div>";

?>