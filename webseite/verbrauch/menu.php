<?php

	echo "<table height=\"8\" width=\"315px\"><tr><td align=\"center\">";
	echo "<ul class=\"navi\">";
	echo "<li";
	if(isset($_GET['se']) && $_GET['se']==200){
		echo " class=\"m_akt\"";
	}
	echo "><a href=\"index.php?atv=02&se=200\">Vorhanden</a></li>";			// Jeder der eingeloggt ist
	echo "<li";
	if(isset($_GET['se']) && $_GET['se']==201){
		echo " class=\"m_akt\"";
	}
	echo "><a href=\"index.php?atv=02&se=201\">Verlauf</a></li>";				// Jeder der eingeloggt ist
  echo "<li";
	if(isset($_GET['se']) && $_GET['se']==203){
		echo " class=\"m_akt\"";
	}
	echo "><a href=\"index.php?atv=02&se=203\">Items</a></li>";				// Jeder der eingeloggt ist
  	echo "<li";
	if(isset($_GET['se']) && $_GET['se']==202){
		echo " class=\"m_akt\"";
	}
	echo "><a href=\"index.php?atv=02&se=202\">Ablauf</a></li>";				// Jeder der eingeloggt ist
	echo "</ul>";
	echo "</td>";
	echo "</tr>";
	echo "</table>";
//	echo "</div>";

?>