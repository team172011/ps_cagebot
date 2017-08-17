<?php
/*
* konst.php
* 
* Platz für die Konfiguration
*
*Gunter Sachse 2017
*
*/
 
/*
* Datenbankkonstanten immer an's aktuelle Projekt anpassen
*/
define("mysqlhost", "localhost");
define("mysqluser", "ps_cagebot");
define("mysqlpasswd", "ps_cagebot2017");

// Surrogate datenbank
define("atvdbname", "ps_cagebot");
// beschlussbuch datenbank



// atv servername
//define("atvserver", "http://localhost/");

/*
* Cookies
*
* <http://www.php.net/manual/en/function.setcookie.php>
*/
define("COOKIE_EXPIRE", 60*60*24*100);  //läuft nach 100 Tagen ab
define("COOKIE_PATH", "/");  //für die ganze Domain

?>