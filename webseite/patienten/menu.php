<?php

	echo "<table height=\"8\" width=\"315px\"><tr><td align=\"center\">";
	echo "<ul class=\"navi\">";
	echo "<li";
	if(isset($_GET['se']) && $_GET['se']==300){
		echo " class=\"m_akt\"";
	}
	echo "><a href=\"index.php?atv=03&se=300\">Patientenübersicht</a></li>";			// Jeder der eingeloggt ist
	echo "</ul>";
	echo "</td>";
	echo "</tr>";
	echo "</table>";
//	echo "</div>";

?>