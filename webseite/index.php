<?php
// Seite initialisieren
session_start ();
//error_reporting(E_ALL);
//ini_set('display_errors', 1);
define("SYS_INIT_CAGEBOT", TRUE); //wird in den functionen und includes geprüft wenn false-> abbruch
date_default_timezone_set('Europe/Berlin');
header("Content-Type: text/html; charset=UTF-8");

include_once 'includes/konst.php';					// funktionen einbinden
include_once 'includes/db.php';						// funktionen einbinden
global $datenbank;
include_once 'includes/surrogate.php';					// funktionen einbinden

// projekt übergeben
$atv = array();
$atv['01'] = 'material/menu.php';
$atv['02'] = 'verbrauch/menu.php';
$atv['03'] = 'patienten/menu.php';
$atv['81'] = 'mitarbeiter/menu.php';


//	seiten übergeben
$se = array();
// oberseite
$se['000'] = 'start.php';
$se['001'] = 'login.php';
$se['002'] = 'admin/eigen.php';
$se['003'] = 'admin/bearbeite.php';

//	Material
$se['100'] = 'material/start.php';
$se['101'] = 'material/medikamente.php';
$se['102'] = 'material/inventur.php';
$se['111'] = 'material/item.php';
$se['122'] = 'material/group.php';


//	Verbrauch
$se['200'] = 'verbrauch/start.php';
$se['201'] = 'verbrauch/verlauf.php';
$se['202'] = 'verbrauch/ablauf.php';
$se['203'] = 'verbrauch/itemlist.php';


// Patienten
$se['300'] = 'patienten/start.php';
$se['301'] = 'patienten/allergy.php';
$se['311'] = 'patienten/patient.php';

// Mitarbeiter
$se['400'] = 'mitarbeiter/start.php';
$se['411'] = 'mitarbeiter/employee.php';

include 'header.html'; // doctype, <html> und das komplette <head>-element +CSS Dateien (müssen für jedes unterprojekt mit angegeben werden
echo "<body>\n";
echo "<div id=\"atvall\">\n";
echo "	<div id=\"atvmenu\">\n";
// menü einbinden
include 'menu.php';
echo "	</div>\n";
// wenn Projekt gewählt Untermenü einbinden
if (isset($_GET['atv'], $atv[$_GET['atv']])) {
	echo "	<div id=\"subatvmenu\">\n";
	include $atv[$_GET['atv']];
	echo "</div>\n";
}
echo "	<div id=\"atvspacer\">&nbsp;</div>\n";
echo "	<div id=\"atvcontent\">\n";

//gewünschte Seiten einfügen
if (isset($_GET['se'], $se[$_GET['se']])) {
	include $se[$_GET['se']];
} else {
	include $se['000'];
}
echo "	</div>\n";
echo "	<div id=\"atvspacer\">&nbsp;</div>\n";
echo "	<div id=\"atvfooter\">\n";
echo "	</div>\n";
echo "</div>\n";
echo '</body>';
echo '</html>';
?>