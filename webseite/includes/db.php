<?php
/*	db.php
datenbankfunktionen für Surrogate

Gunter Sachse 2017
*/
// Konstanten einlesen
//include_once("konst.php");

class cagedb {
	var $dbverbindung;
	/* Konstruktor */
	function cagedb(){
	// mit Datenbank verbinden
		$this->dbverbindung = mysql_connect(mysqlhost, mysqluser, mysqlpasswd) or die(mysql_error());
		mysql_query("SET NAMES 'utf8'");
		mysql_select_db("ps_cagebot", $this->dbverbindung) or die(mysql_error());
	}
	
	public function query($query){
		$mysqltmp = mysql_query($query, $this->dbverbindung) OR die ("<pre>\n".$query."</pre>\n".mysql_error());
		//echo "<pre>\n".$query."</pre>\n".mysql_error();
		RETURN $mysqltmp;
		
	}

	public function debug(){
		echo "datenbank->debug() erfolgreich aufgerufen";
	}

	public function letzteID(){
		$tempid=mysql_insert_id();
		RETURN $tempid;
	}

}
/* Create database connection */
$datenbank = new cagedb;
?>