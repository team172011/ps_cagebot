<?php

/*
* 2011 Gunter Sachse v. imba
* Funktionen für das Beschlussbuch
*/

if (!defined("SYS_INIT_CAGEBOT")) exit;	// prüfen ob "legal" aufgerufen
/*
include_once("db.php");
include_once("konst.php");
*/

class BenutzerKlasse
{
	var $ist_eingeloggt;      		//	wenn true = eingeloggt
	var $benutzerinfos = array();	// benutzerinfos in array speichern

	/* Konstruktor */
	function BenutzerKlasse(){
	// mit Datenbank verbinden
	//	$this->connection = mysql_connect(mysqlhost, mysqluser, mysqlpasswd) or die(mysql_error());
	//	mysql_select_db(mysqldbname, $this->connection) or die(mysql_error());
	}

	function Ausloggen(){
		global $datenbank;
		$datenbank->query("UPDATE ".atvdbname.".".Benutzerzusatz."benutzer SET sessionid = '' WHERE id = '".$_SESSION["atvuser_id"]."'");
		$_SESSION = array();
		session_unset();
		session_destroy();
		header("location: index.php");
	}

	function Einloggen($atv_nutzer, $atv_pass){
		global $datenbank;  //Datenbank
		$atvpwcode = $this->pruefeLoginPasswort($atv_nutzer, $atv_pass);
		if($atvpwcode == 1885){
			$idresult = $datenbank->query("SELECT id FROM ".atvdbname.".".Benutzerzusatz."benutzer WHERE login = '".dbSlashes($atv_nutzer)."'");
			$idarray = mysql_fetch_array($idresult);
			$this->benutzerinfos = $this->holeBenutzer((int)$idarray['id']);
			$_SESSION["atvuser_id"] = $this->benutzerinfos['id'];
			$_SESSION["atvuser_vname"] = $this->benutzerinfos['vname'];
			$_SESSION["atvuser_nname"] = $this->benutzerinfos['nname'];
			$_SESSION["atvuser_bname"] = $this->benutzerinfos['bname'];
			$_SESSION["atvuser_email"] = $this->benutzerinfos['email'];
			$_SESSION["atvuser_status"] = $this->benutzerinfos['status'];
			$_SESSION["atvuser_location"] = $this->benutzerinfos['location'];
			$_SESSION["atvuser_aktiv"] = $this->benutzerinfos['aktiv'];
			$_SESSION["atvuser_rechte"] = $this->benutzerinfos['rechte'];
			$_SESSION["atvuser_rueckmeldung"] = $this->benutzerinfos['rueckmeldung'];
			$_SESSION["atvuser_bbuchstatus"] = $this->benutzerinfos['bbuchstatus'];
			session_regenerate_id();
			$datenbank->query("UPDATE ".atvdbname.".".Benutzerzusatz."benutzer SET sessionid = '".session_id()."' WHERE id = '".$_SESSION["atvuser_id"]."'");
			header("location: index.php?atv=01&se=102");
		}
		//$datenbank->debug();
		//else if($atvpwcode==1) header("location: index.php?fehler=0001");
		//else if($atvpwcode==2) header("location: index.php?fehler=0002");
		//else header("location: index.php?fehler=0003");
	}

	function IstEinloggt($checkdate=1){		//eleganter und sicherer machen!
		global $datenbank;
		if(isset($_SESSION["atvuser_bname"]) && trim($_SESSION["atvuser_bname"])!=''){
			$sql_session = $datenbank->query("SELECT sessionid FROM ".atvdbname.".".Benutzerzusatz."benutzer WHERE id = '".dbSlashes($_SESSION["atvuser_id"])."'");
			$tmp_session = mysql_fetch_array($sql_session);
			if(session_id() != $tmp_session['sessionid']){
				$this->Ausloggen();
			}
			if(isset($_SESSION["atvuser_rueckmeldung"]) && $_SESSION["atvuser_rueckmeldung"]<=date('Y-m-d') && $checkdate==1){
				header("location: index.php?atv=81&se=069");
			}
			else RETURN TRUE;
		}
		else RETURN FALSE;
	}

	function IstAdmin(){
		if(	isset($_SESSION["atvuser_bname"]) &&
			trim($_SESSION["atvuser_bname"])!='' &&
			isset($_SESSION["atvuser_rechte"]) &&
			trim($_SESSION["atvuser_rechte"])>=100
		) RETURN TRUE;
		else RETURN FALSE;
	}
	
	function IstImba(){
		if(	isset($_SESSION["atvuser_bname"]) &&
			trim($_SESSION["atvuser_bname"])!='' &&
			isset($_SESSION["atvuser_rechte"]) &&
			trim($_SESSION["atvuser_rechte"])==255
		) RETURN TRUE;
		else RETURN FALSE;
	}
	
	function IstBursch(){
		if(	isset($_SESSION["atvuser_bname"]) &&
			trim($_SESSION["atvuser_bname"])!='' &&
			isset($_SESSION["atvuser_status"]) &&
			trim($_SESSION["atvuser_status"])>=30
		) RETURN TRUE;
		else RETURN FALSE;
	}
	
	function IstFux(){
		if(	isset($_SESSION["atvuser_bname"]) &&
			trim($_SESSION["atvuser_bname"])!='' &&
			isset($_SESSION["atvuser_status"]) &&
			trim($_SESSION["atvuser_status"])==20
		) RETURN TRUE;
		else RETURN FALSE;
	}

	function holeBenutzer($benutzerid){
		global $datenbank;  //Datenbank
		$result = $datenbank->query("SELECT * FROM ".atvdbname.".".Benutzerzusatz."benutzer WHERE id = '".(int)$benutzerid."'");
		/* Es darf nur ein Datensatz exisiteren sonst fehler */
		if(!$result || (mysql_numrows($result) < 1)){
		 RETURN NULL;
		}
		/* Array mit den Daten übergeben */
		$dbarray = mysql_fetch_assoc($result);
		RETURN $dbarray;
	}
/*
* function pruefeLoginPasswort($username, $password)
*	Eingabe
*		$username -> login (string)
*		$password -> passwort (string)
*
*	Ausgabe 
*		1885 = Login erfolgreich
*		1 = Falscher Benutzername
*		2 = Falsches Passwort
* 
*/
	function pruefeLoginPasswort($username, $password){
		global $datenbank;  //Datenbank
		/* addslash wenn nötig */
		$username = dbSlashes($username);
		echo $username."<br>";

		/* Benutzer suchen */
		$result = $datenbank->query("SELECT passwort FROM ".atvdbname.".".Benutzerzusatz."benutzer WHERE login = '".$username."'");
		if(!$result || (mysql_numrows($result) !=1)){
			RETURN 1; //Falscher Benutzername bzw. Login nicht eindeutig
		}

		/* Passwort auslesen */
		$dbarray = mysql_fetch_array($result);
		//$dbarray['passwort'] = stripslashes($dbarray['passwort']);
		//$password = stripslashes($password);

		/* Passwort vergleichen */
		if(md5($password) == $dbarray['passwort']){
		echo md5($password)."<br>";
		echo $dbarray['passwort'];
			RETURN 1885; //Login erfolgreich
		}
		else{
			RETURN 2; //Passwort falsch
		}
	}

};

/* Create database connection */
$benutzer = new BenutzerKlasse;

?>