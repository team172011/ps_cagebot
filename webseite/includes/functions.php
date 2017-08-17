<?php

/*
* 2011 Gunter Sachse v. imba
* Funktionen für das Beschlussbuch
*/

if (!defined("SYS_INIT_CAGEBOT")) exit;	// prüfen ob "legal" aufgerufen
//include 'db_login.php';				// db logins usw.

/*######## Funktionen ########*/
//
// function datumListe ($prf_d)
// gibt datum select feld aus
//
// function isLoggedin ()
// abfrage ob editrechte vorhanden sind
//
// function isEditor ()
// abfrage ob editrechte vorhanden sind
//
// function isSchriftwart ()
// abfrage ob Schriftwartrechte vorhanden sind
//
// function isAdmin ()
// abfrage ob adminrechte vorhanden sind
//
//
//
/*######## Funktionen ########*/



function dbSlashes($query){
	if(!get_magic_quotes_gpc()) {
		$query = addslashes($query);
	}
	RETURN $query;
}

//### xx ###
// function datumListe ($prf_d)
// gibt datum select feld aus
//
//	Eingaben:
//			$prf_d	->	Präfix
//
//		optional:
//			$tag_t -> tag im format tt (05)
//			$mon_t -> monat im format mm (01)
//			$jah_t -> jahr im format jjjj (1981)
//
//	Ausgabe:
//			gibt ein datums-dropdownfeld per echo zurück (dank präfix auch für mehrere eingabefelder möglich)
//			präfix+tt für tag
//			präfix+mm für monat
//			präfix+jjjj für jahr
//
// function datumListe ($prf_d)

function datumListe ($prf_d, $tag_t='00', $mon_t='00', $jah_t='0000'){
	if($tag_t=='00'){
		$tag_t=date("j",time());
	}
	if($mon_t=='00'){
		$mon_t=date("n",time());
	}
	if($jah_t=='0000'){
		$jah_t=date("Y",time());
	}

	echo "<select name=\"".$prf_d."tt\" size=\"1\">\n";
	for($k=1; $k<=31; $k++) {
		echo " <option";
		if($k==(int)$tag_t){	//evtl. ausfallsicher machen (variable vorher abfragen und hier übergeben falls vorhanden
			echo " selected=\"selected\"";
		}
		echo ">";
		if($k<10){
			echo '0';
		}
		echo $k;
		echo "</option>\n";
	 }
	echo "</select>\n";
	echo "<select name=\"".$prf_d."mm\" size=\"1\">\n";
	for($k=1; $k<=12; $k++) {
		echo " <option";
		if($k==(int)$mon_t){	//evtl. ausfallsicher machen (variable vorher abfragen und hier übergeben falls vorhanden
			echo " selected=\"selected\"";
		}
		echo ">";
		if($k<10){
			echo '0';
		}
		echo $k;
		echo "</option>\n";
	}	
	echo "</select>\n";
	echo "<select name=\"".$prf_d."jjjj\" size=\"1\">\n";
	for($k=1997; $k<=2200; $k++) {
		echo " <option";
		if($k==(int)$jah_t){	//evtl. ausfallsicher machen (variable vorher abfragen und hier übergeben falls vorhanden
			echo " selected=\"selected\"";
		}
		echo ">";
		if($k<10){
			echo "0";
		}
		echo $k;
		echo "</option>\n";
	}
	echo "</select>\n";
}

//### xx ###
// function isDate ($inputdate, $date_format = 'Ymd')
// schauen ob datum gültig ist (format und das datum -> 31.02.2010 wäre ungültig)
// -> problem -> benutzt unix timestamp -> Zeitfenster: 13.12.1901 - 19.01.2038
//
//	Eingaben:
//			$inputdate ->	(string->datum)
//				in beliebiger form die aber wenn sie von Ymd (19810105) abweicht spezifizert werden muss
//
//		optional:
//			$date_format -> (string->format des datums)
//				z.b. Ymd oder Y-m-d oder d.m.Y oder was auch immer date schluckt
//
// function isDate ($inputdate, $date_format = 'Ymd')

function isDate ($inputdate, $date_format = 'Ymd'){
	if(isset($inputdate) && trim($inputdate)!='' && trim($inputdate)>0){
		$inputdate = trim($inputdate);
		$time = strtotime($inputdate);
		if(date($date_format, $time) == $inputdate) RETURN TRUE;
		else RETURN FALSE;
	}
}

//### xx ###
// function zeigeNutzer ()
// liest revi.txt aus und gibt last changed revsion(verzeichniss)  und lastchanged date aus
//
// es muss eine revi.txt existieren (z.b. per batch beim export erstellen):
//		svn info D:\xamppatv\htdocs\beschluss --revision HEAD >d:\xamppatv\htdocs\bbuch\revi.txt
//
//	Eingaben:
//			$atr ->	(int)
//				0= alles
//				1= rev
//				2= datum
//
//		optional:
//			$date_format -> (string->format des datums)
//				z.b. Ymd oder Y-m-d oder d.m.Y oder was auch immer date schluckt
//
// function svnRev ($atr=0)

function zeigealleNutzer (){
	global $datenbank;
	global $atv_locations;
	global $atv_status;
	global $atv_rechte;
	global $atv_aktiv;
	global $atv_bbuchrechte;

	$nutzersql = "SELECT
					id,
					vname,
					nname,
					bname,
					email,
					status,
					location,
					aktiv,
					rechte,
					rueckmeldung,
					bbuchstatus
				FROM
					".atvdbname.".".Benutzerzusatz."benutzer
				ORDER BY
					bname ASC,
					nname ASC
				";

	$nutzerresult = $datenbank->query($nutzersql);
	echo "<table border=1><tr>
	<th>#</th>
	<th>ID</th>
	<th>Name</th>
	<th>ATV Status</th>
	<th>Location</th>
	<th>Aktiv</th>
	<th>Globale Rechte</th>
	<th>gültig bis</th>
	</tr>\n";
	$nnr=1;
	while($row = mysql_fetch_assoc($nutzerresult)) {
		echo "<tr>
		<td>".$nnr."</td>
		<td>".$row['id']."</td>
		<td><a href=\"index.php?atv=81&se=006&id=".$row['id']."\">";
		if(trim($row['bname']!='')) echo $row['bname'];
		else echo $row['vname']." ".$row['nname']." v.N.N.";
		echo "</a></td><td>".$atv_status[(int)$row['status']]."</td>
		<td>".$atv_locations[(int)$row['location']]."</td>
		<td>".$atv_aktiv[(int)$row['aktiv']]."</td>
		<td>".$atv_rechte[(int)$row['rechte']]."</td>
		<td>".substr($row['rueckmeldung'],8,2).".".substr($row['rueckmeldung'],5,2).".".substr($row['rueckmeldung'],0,4)."</td>
		</tr>\n";
		$nnr++;
	}
	 echo "</table>";
}


// function holeMailadressen($mailart)
//
// Eingabe:
//		$mailart (int)
//			1 = Alle
//			2 = Alle Aktiven
//			3 = Fuxen
//			4 = Burschen
//			5 = Vorstand
//			6 = Alle in Halle
//			7 = Aktive in Halle


function holeMailadressen($mailart){
	global $datenbank;
	$mailsql = "SELECT
					vname,
					nname,
					bname,
					email,
					status,
					location,
					aktiv,
					rechte,
					rueckmeldung,
					bbuchstatus
				FROM
					".atvdbname.".".Benutzerzusatz."benutzer
				WHERE
				";

	if($mailart==1 || $mailart==6) $mailsql .= "
					status>0
				";


	if($mailart==2 || $mailart==7) $mailsql .= "
					status>=20
				AND
					status<80
				";


	if($mailart==3) $mailsql .= "
					status=20
				";


	if($mailart==4) $mailsql .= "
					status>=30
				AND
					status<80
				";

	if($mailart==5) $mailsql .= "
					status>=60
				AND
					status<80
				";


	if($mailart==6 || $mailart==7) $mailsql .= "
				AND
					location <= 2
				";

	$mailsql .= "
				ORDER BY
					bname ASC,
					nname ASC,
					vname ASC
				";

	$mailresult = $datenbank->query($mailsql);
	$mailstring='';
	while($row = mysql_fetch_assoc($mailresult)) {
		$mailstring.=$row['email']."; ";
	}
	if($mailstring!=''){
	echo "E-Mailheader per Hand kopieren:<br>".$mailstring;
	echo "<br><br><a href=\"mailto:".$mailstring."\">Mail Programm mit den ausgewählten Adressen öffnen</a>";
	} else echo "keine Mails gefunden";
}


function eigeneSpeichern($id=FALSE,$vname=FALSE,$nname=FALSE,$bname=FALSE,$location=FALSE){
	global $datenbank;
	if($id && $id!='' && $vname && $vname!='' && $nname && $nname!='' && $bname && $bname!='' && $location && $location!=''){
		$sql = "UPDATE
					".atvdbname.".".Benutzerzusatz."benutzer
				SET
					vname='".dbSlashes($vname)."',
					nname='".dbSlashes($nname)."',
					bname='".dbSlashes($bname)."',
					location='".dbSlashes($location)."'
				WHERE
					id='".(int)$id."'
			";
	$datenbank->query($sql);
	$_SESSION["atvuser_vname"] = $vname;
	$_SESSION["atvuser_nname"] = $nname;
	$_SESSION["atvuser_bname"] = $bname;
	$_SESSION["atvuser_location"] = $location;
	RETURN TRUE;
	} else RETURN FALSE;
}

function speichereNutzer($id=FALSE, $login=FALSE, $bname=FALSE, $vname=FALSE, $nname=FALSE, $email=FALSE, $status=FALSE, $location=FALSE, $aktiv=FALSE, $rueckmeldung=FALSE, $rechte=FALSE, $bbuchstatus=FALSE, $bierstatus=FALSE){
	global $datenbank;

/*
$id=FALSE,
$login=FALSE,
$bname=FALSE,
$vname=FALSE,
$nname=FALSE,
$email=FALSE,
$status=FALSE,
$location=FALSE,
$aktiv=FALSE,
$rueckmeldung=FALSE,
$rechte=FALSE,
$bbuchstatus=FALSE,
$bierstatus=FALSE
*/

	if(	$id && $id!='' &&
		$login && $login!='' &&
		$vname && $vname!='' &&
		$nname && $nname!='' &&
		$email && $email!='' &&
		$status!='' &&
		$location!='' &&
		$aktiv!='' &&
		$rueckmeldung!='' &&
		$rechte!='' &&
		$bbuchstatus!='' &&
		$bierstatus!=''){
		$sql = "UPDATE
					".atvdbname.".".Benutzerzusatz."benutzer
				SET
					login='".dbSlashes($login)."',
					bname='".dbSlashes($bname)."',
					vname='".dbSlashes($vname)."',
					nname='".dbSlashes($nname)."',
					email='".dbSlashes($email)."',
					status='".dbSlashes($status)."',
					location='".dbSlashes($location)."',
					aktiv='".dbSlashes($aktiv)."',
					rueckmeldung='".dbSlashes($rueckmeldung)."',
					rechte='".dbSlashes($rechte)."',
					bbuchstatus='".dbSlashes($bbuchstatus)."',
					bierstatus='".dbSlashes($bierstatus)."',
					editid='".dbSlashes($_SESSION["atvuser_id"])."',
					edittime=now()
				WHERE
					id='".(int)$id."'
			";
	$datenbank->query($sql);
	RETURN TRUE;
	} else RETURN FALSE;
}

function neuerNutzer ($passwort=FALSE, $login, $vname, $nname, $bname, $email, $status, $location, $aktiv, $rechte, $bbuchstatus, $bierstatus){
	global $datenbank;
	if(!$passwort) $temppw=erzeugeZufallsPW();
	else $temppw=$passwort;

	$sql = "INSERT INTO
				".atvdbname.".".Benutzerzusatz."benutzer
				(login,
				passwort,
				vname,
				nname,
				bname,
				email,
				status,
				location,
				editid,
				edittime,
				aktiv,
				rechte,
				rueckmeldung,
				bbuchstatus,
				bierstatus)
			VALUES
				('".dbSlashes($login)."',
				'".md5($temppw)."',
				'".dbSlashes($vname)."',
				'".dbSlashes($nname)."',
				'".dbSlashes($bname)."',
				'".dbSlashes($email)."',
				'".dbSlashes($status)."',
				'".dbSlashes($location)."',
				'".dbSlashes($_SESSION["atvuser_id"])."',
				now(),
				'".dbSlashes($aktiv)."',
				'".dbSlashes($rechte)."',
				'".date("Y-m-d", mktime(0, 0, 0, date("m")+6, date("d"), date("y")))."',
				'".dbSlashes($bbuchstatus)."',
				'".dbSlashes($bierstatus)."')
			";
	$datenbank->query($sql);

// php mail -> durch funktion ersetzen?
	$empfaenger = dbSlashes($email);
	$betreff = 'Anmeldung für den internen Bereich der ATV';
	$nachricht = "Hallo ".dbSlashes($vname).",\n\ndein Account wurde Erfolgreich erstellt.\nBitte benutze folgende Daten für den Login:\n\nLogin: ".dbSlashes($login)."\nPasswort: ".$temppw."\n\nMit freundlichen Grüßen,\nDas Serverlein";
//$nachricht = wordwrap($nachricht, 70);
	$header = 'From: atvgothia@googlemail.com' . "\r\n" .
		'Reply-To: noreply@atv-gothia.de' . "\r\n" .
		'X-Mailer: PHP/' . phpversion();
	mail($empfaenger, $betreff, $nachricht, $header);
	RETURN TRUE;
}

function erzeugeZufallsPW() {
    $zeichen = "abcdefghijkmnopqrstuvwxyz023456789";
    srand((double)microtime()*1000000);
    $i = 0;
    $randompw = '' ;
    while ($i <= 7) {
        $num = rand() % 33;
        $tmp = substr($zeichen, $num, 1);
        $randompw = $randompw . $tmp;
        $i++;
    }
    return $randompw;
}

function benutzerRueckmelden($mailadd, $hashkey){
	global $datenbank;
	$rresult = $datenbank->query("SELECT id, email, randomhash, hashdate FROM ".atvdbname.".benutzer WHERE email='".dbSlashes($mailadd)."' AND randomhash='".dbSlashes($hashkey)."'");
	if($rresult && mysql_numrows($rresult) == 1 && $mailadd!='' && $hashkey!=''){
		$dbarray = mysql_fetch_assoc($rresult);
		if($dbarray['email']==$mailadd && $dbarray['randomhash']==$hashkey){
			//echo $dbarray['hashdate']."<br>";
			$tempdate = date("Ymd", mktime(0, 0, 0, date("m")+6, date("d"), date("y")));
			$rsql = "UPDATE
						".atvdbname.".".Benutzerzusatz."benutzer
					SET
						rueckmeldung='".$tempdate."',
						randomhash='',
						hashdate=''
					WHERE
						id='".(int)$dbarray['id']."'
					";
			$datenbank->query($rsql);
			RETURN TRUE;
		} else RETURN FALSE;
	} else RETURN FALSE;
}

function mailerRueckmelden(){
	global $datenbank;
	$tempcode = md5(erzeugeZufallsPW());
	$empfaenger = dbSlashes($_SESSION["atvuser_email"]);
	$betreff = 'ATV - E-Mail bestätigen';
	$nachricht = "Hallo ".dbSlashes($_SESSION["atvuser_vname"]).",\n\nBitte bestätige dein E-Mail um weiter auf den internen Bereich der ATV zugreifen zu können.\nKlicke den Link: <a href=\"".atvserver."rueckmelden.php?bier=".dbSlashes($_SESSION["atvuser_email"])."&junge=".$tempcode."\"></a>\n\nE-Mail: ".dbSlashes($_SESSION["atvuser_email"])."\nCode: ".$tempcode."\n\nMit freundlichen Grüßen,\nDas Serverlein";
//$nachricht = wordwrap($nachricht, 70);
	$header = 'From: atvgothia@googlemail.com' . "\r\n" .
		'Reply-To: noreply@atv-gothia.de' . "\r\n" .
		'X-Mailer: PHP/' . phpversion();
	mail($empfaenger, $betreff, $nachricht, $header);
	$rmsql = "UPDATE
						".atvdbname.".".Benutzerzusatz."benutzer
					SET
						randomhash='".$tempcode."',
						hashdate=now()
					WHERE
						id='".(int)$_SESSION["atvuser_id"]."'
					";
	$datenbank->query($rmsql);

}

// function download($id)
//
// Eingabe:
//		$id (int)
//			id der datei übergeben
//
// Ausgabe:
//			übergibt die datei als download

function download ($id=FALSE, $art=FALSE){
	global $datenbank;
	global $atv_ordnername;

	$dlsql = "SELECT
					id,
					name,
					verz,
					savename,
					art,
					rechte,
					ulsize
				FROM
					".dldbname.".".Dateienzusatz."dateien
				WHERE
					id='".(int)$id."'
				";

	$dlresult = $datenbank->query($dlsql);
	$row = mysql_fetch_array($dlresult) or die(mysql_error());
	echo $row['id']. " - ".$row['name']. " - ".$atv_ordnername[(int)$row['verz']]. " - ".$row['savename']. " - ".$row['art']. " - ". $row['rechte'];
	
/*	

	$atv_locations[(int)$row['verz']]

	$res_kw = $datenbank->query("SELECT * FROM ".bbuchdbname.".keyw ORDER BY keyword");
	$num_kw = mysql_num_rows($res_kw);
	
	$row = mysql_fetch_array($result) or die(mysql_error());
	echo $row['name']. " - ". $row['age'];
*/

// dl script

//	$file = 'phpdownload/convente/308.jpg';		//debug
	$file = "phpdownload/".$atv_ordnername[(int)$row['verz']]."/".$row['savename'];		//debug
	echo "<br> Datei:".$file."<br>";

	if (file_exists($file)) {
		header('Content-Description: File Transfer');
		header('Content-Type: application/octet-stream');		// anpassen für darstellung im browser
		//header('Content-Disposition: attachment; filename='.basename($file));
		header('Content-Disposition: attachment; filename='.$row['name']);
		header('Content-Transfer-Encoding: binary');
		header('Expires: 0');
		header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
		header('Pragma: public');
		header('Content-Length: ' . filesize($file));
		ob_clean();
		flush();
		readfile($file);
	//	exit;			// raus sonst blöd
	}
	RETURN TRUE;
}

function upload ($_FILES, $sname=FALSE, $verz=FALSE, $info=FALSE,  $art=FALSE, $rechte=FALSE, $endung=FALSE){
	global $datenbank;
	global $atv_ordnername;

	if($sname==FALSE){
		// dateinamen bereinigen
		$SafeFile = $_FILES['updatei']['name'];
		$SafeFile = str_replace("#", "Nr", $SafeFile);
		$SafeFile = str_replace("$", "Dollar", $SafeFile);
		$SafeFile = str_replace("€", "Euro", $SafeFile);
		$SafeFile = str_replace("%", "Prozent", $SafeFile);
		$SafeFile = str_replace("^", "", $SafeFile);
		$SafeFile = str_replace("&", "und", $SafeFile);
		$SafeFile = str_replace("*", "", $SafeFile);
		$SafeFile = str_replace("?", "", $SafeFile);
		$SafeFile = str_replace(" ", "_", $SafeFile);
	} else {
		$SafeFile = $sname;
	}

	$uploaddir = "phpdownload/".$atv_ordnername[$verz]."/";		//verzeichniss ändern je nach art
	$path = $uploaddir.$SafeFile;

	if(copy($_FILES['updatei']['tmp_name'], $path)){ 			//wenn erfolgreich kopiert

		//GET FILE SIZE
		$theFileSize = $_FILES['updatei']['size'];

		if ($theFileSize>1048575){ //IF GREATER THAN 999KB, DISPLAY AS MB
			$theDiv = $theFileSize / 1048576;
			$theFileSize = round($theDiv, 1)." MB"; //round($WhatToRound, $DecimalPlaces)
		} else { //OTHERWISE DISPLAY AS KB
			$theDiv = $theFileSize / 1024;
			$theFileSize = round($theDiv, 1)." KB"; //round($WhatToRound, $DecimalPlaces)
		}

		echo "<font color=\"#009900\"><b>Upload Successful</b><br>";
		echo "<b>Dateiname: </b>".$SafeFile."<br>";
		echo "<b>Größe: </b>".$theFileSize."<br>";
		echo "<b>Verzeichniss: </b>".$uploaddir."<br>";

		//noch übergeben!:		name info rechte (0 alle 1 aktive 2 burschen 3 vorstand usw.)
		// brauch ich das??:	endung
		$info = "Das ist ein Platzhalter für die Infos!!";
		//$sname = "";			// unter welchem namen wird die datei auf dem server gespeichert?
		$dname = $SafeFile;			// unter welchem namen wird die datei heruntergeladen

		$sql = "INSERT INTO
					".dldbname.".".Dateienzusatz."dateien
					(name,
					verz,
					savename,
					info,
					art,
					rechte,
					upid,
					upldate,
					endung,
					ulsize)
				VALUES
					('".dbSlashes($dname)."',
					".(int)$verz.",
					'".dbSlashes($SafeFile)."',
					'".dbSlashes($info)."',
					".(int)$art.",
					".(int)$rechte.",
					".(int)$_SESSION["atvuser_id"].",
					now(),
					".(int)$endung.",
					".(int)$_FILES['updatei']['size'].")
				";
		$datenbank->query($sql);

		} else {
			//PRINT AN ERROR IF THE FILE COULD NOT BE COPIED
			echo "<font color=\"#C80000\"><b>Datei konnte nicht hochgeladen werden (Copy)</b></font>";
		}



	RETURN TRUE;
}

?>