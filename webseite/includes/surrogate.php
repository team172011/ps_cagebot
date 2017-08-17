<?php

/*
* 2017 Gunter Sachse
*
*/

if (!defined("SYS_INIT_CAGEBOT")) exit;	// prüfen ob "legal" aufgerufen

/*######## Funktionen ########*/
//
// function datumListe ($prf_d)
// gibt datum select feld aus
//
//
//
//
/*######## Funktionen ########*/

function zeigeItem ($itemnr) {

	$sql = "SELECT *
FROM materials
LEFT JOIN materials_groups ON materials.material_group_id = materials_groups.id
LEFT JOIN materials_producers ON materials_groups.producer_id = materials_producers.id
LEFT JOIN materials_types ON materials_groups.type_id = materials_types.id
WHERE materials.id = " .$itemnr;
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function materialStart ($itemnr) {

	$sql = "SELECT *
FROM materials_groups
LEFT JOIN materials ON materials.material_group_id = materials_groups.id
LEFT JOIN materials_producers ON materials_groups.producer_id = materials_producers.id
LEFT JOIN materials_types ON materials_groups.type_id = materials_types.id
GROUP BY materials_groups.id";
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function verbrauchStart ($itemnr) {

	$sql = "SELECT *, count(materials_groups.id) as Anzahl
FROM materials
LEFT JOIN materials_groups ON materials.material_group_id = materials_groups.id
LEFT JOIN materials_producers ON materials_groups.producer_id = materials_producers.id
LEFT JOIN materials_types ON materials_groups.type_id = materials_types.id
WHERE materials.committed = 0
GROUP BY materials_groups.id";
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function verbrauchVerlauf () {

	$sql = "SELECT materials.id AS mat_id, materials_groups.materials_groups_image, materials_transfers.materials_transfer_date, materials_groups.materials_groups_name, patients.Vorname , patients.Nachname
FROM materials
LEFT JOIN materials_groups ON materials.material_group_id = materials_groups.id
LEFT JOIN materials_transfers ON materials.id = materials_transfers.materials_id
LEFT JOIN patients ON patients.id = materials_transfers.patients_id
WHERE materials.committed = 1
ORDER BY materials_transfers.materials_transfer_date DESC";
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function verbrauchAblauf () {

	$sql = "SELECT materials.id AS mat_id, materials_groups.materials_groups_image, materials.best_before, materials_groups.materials_groups_name
FROM materials
LEFT JOIN materials_groups ON materials.material_group_id = materials_groups.id
LEFT JOIN materials_producers ON materials_groups.producer_id = materials_producers.id
LEFT JOIN materials_types ON materials_groups.type_id = materials_types.id
WHERE materials.committed = 0
ORDER BY materials.best_before ASC";
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}


function zeigeGroup ($itemgrpnr) {

	$sql = "SELECT *
FROM materials_groups
LEFT JOIN materials_producers ON materials_groups.producer_id = materials_producers.id
LEFT JOIN materials_types ON materials_groups.type_id = materials_types.id
WHERE materials_groups.id = " . $itemgrpnr;
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function zeigeItemInhalt ($itemgrpnr) {

	$sql = "SELECT *
FROM materials
LEFT JOIN materials_groups ON materials.material_group_id = materials_groups.id
LEFT JOIN materials_producers ON materials_groups.producer_id = materials_producers.id
LEFT JOIN materials_types ON materials_groups.type_id = materials_types.id
WHERE materials.id = " .$itemnr;
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function zeigeItemliste ($itemgrpnr) {

	$sql = "SELECT materials.id AS mat_id, materials.best_before, materials.dummy, materials_groups.materials_groups_image, materials_groups.materials_groups_name, materials_groups.materials_groups_description, materials_producers.materials_producers_name, materials_types.materials_types_name
FROM materials
LEFT JOIN materials_groups ON materials.material_group_id = materials_groups.id
LEFT JOIN materials_producers ON materials_groups.producer_id = materials_producers.id
LEFT JOIN materials_types ON materials_groups.type_id = materials_types.id
WHERE materials.committed = 0";
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function committItem ($itemid) {

	$sql = "UPDATE materials
SET committed = 1
WHERE materials.id = ".$itemid." ;
INSERT INTO materials_transfers (materials_id, patients_id, materials_transfer_type, materials_transfer_date)
VALUES ('".$itemid."', '12', '1', '2017-08-16');" ;
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}



function patientenStart ($itemnr) {

	$sql = "SELECT *
FROM patients";
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function zeigePatient ($patientnr) {

	$sql = "SELECT *
FROM patients
WHERE patients.id = " . $patientnr;
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function zeigePatientAllergie ($patientallergienr) {

	$sql = "SELECT *
FROM patients
LEFT JOIN patients_allergy ON patients.id = patients_allergy.patients_id
LEFT JOIN ingredients ON ingredients.id = patients_allergy.ingredients_id
LEFT JOIN materials_ingredients ON materials_ingredients.id = ingredients.id
LEFT JOIN materials_groups ON materials_groups.id = materials_ingredients.material_groups_id
WHERE patients.id = " . $patientallergienr;
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function mitarbeiterStart () {

	$sql = "SELECT *
FROM employee";
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

function mitarbeiterSelect ($mitarbeiterId) {

	$sql = "SELECT *
    FROM employee
    WHERE id = ". $mitarbeiterId;
	
	//$result = mysql_query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	global $datenbank;
	$result = $datenbank->query($sql) OR die ("<pre>\n".$sql."</pre>\n".mysql_error());
	RETURN $result;
}

?>