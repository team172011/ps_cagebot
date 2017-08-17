-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server Version:               10.1.19-MariaDB - mariadb.org binary distribution
-- Server Betriebssystem:        Win32
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Exportiere Datenbank Struktur für ps_cagebot
CREATE DATABASE IF NOT EXISTS `ps_cagebot` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `ps_cagebot`;

-- Exportiere Struktur von Tabelle ps_cagebot.consumption
CREATE TABLE IF NOT EXISTS `consumption` (
  `id` int(11) NOT NULL,
  `currentValue` int(11) DEFAULT NULL,
  `min_Value` int(11) DEFAULT NULL COMMENT 'Minimalbestand',
  `max_Value` int(11) DEFAULT NULL,
  `unit` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Exportiere Daten aus Tabelle ps_cagebot.consumption: ~3 rows (ungefähr)
DELETE FROM `consumption`;
/*!40000 ALTER TABLE `consumption` DISABLE KEYS */;
INSERT INTO `consumption` (`id`, `currentValue`, `min_Value`, `max_Value`, `unit`) VALUES
	(20001, 100, 20, 250, 'Milliliter'),
	(20002, 3, 5, 40, 'Stueck'),
	(20003, 100, 50, 365, 'Stueck');
/*!40000 ALTER TABLE `consumption` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.employee
CREATE TABLE IF NOT EXISTS `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Vorname` varchar(50) DEFAULT NULL,
  `Nachname` varchar(50) DEFAULT NULL,
  `Berufsbezeichnung` varchar(50) DEFAULT NULL,
  `Geburtstag` date DEFAULT NULL,
  `QR-Code` int(11) DEFAULT NULL,
  `Information` varchar(100) DEFAULT NULL,
  `Angestellt seit` date DEFAULT NULL,
  `E-Mail` varchar(50) DEFAULT NULL,
  `Skype` varchar(50) DEFAULT NULL,
  `image` text,
  `Quelle` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10006 DEFAULT CHARSET=latin1;

-- Exportiere Daten aus Tabelle ps_cagebot.employee: ~5 rows (ungefähr)
DELETE FROM `employee`;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` (`id`, `Vorname`, `Nachname`, `Berufsbezeichnung`, `Geburtstag`, `QR-Code`, `Information`, `Angestellt seit`, `E-Mail`, `Skype`, `image`, `Quelle`) VALUES
	(10001, 'Simon-J.', 'Wimmer', 'Masterstudent Wirtschaftsinformatik', '1991-12-20', 10001, 'Mitglied Projektseminar WI-Cagebot', '2010-10-10', 'simon-justus.wimmer@student.uni-halle.de', NULL, 'simon.png', 'Foto'),
	(10002, 'Antje', 'Fackler', 'Masterstudent Wirtschaftsinformatik', '1990-01-01', 10002, 'Mitglied Projektseminar WI-Cagebot', '2010-01-01', 'antje.fackler@student.uni-halle.de', NULL, 'antje.png', 'https://yt3.ggpht.com/-MocF3NREr-g/AAAAAAAAAAI/AAAAAAAAAAA/RMbyvt5IDDc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
	(10003, 'Gunter', 'Sachse', 'Bachelorstudent Wirtschaftsinformatik', '1990-01-01', 10003, 'Mitglied Projektseminar WI-Cagebot', '2010-01-01', 'gunter.sachse@student.uni-halle.de', NULL, 'gunter.png', 'Foto'),
	(10004, 'Karsten', 'Helbig', 'Dipl.-Wirtsch.-Inf. Karsten Helbig', '1990-01-01', 10004, 'Leiter Projektseminar WI-Cagebot', '2000-01-01', 'karsten.helbig@wiwi.uni-halle.de', NULL, 'karsten.png', 'http://wior.wiwi.uni-halle.de/im/1437149625_1947_00_800.jpg'),
	(10005, 'Taieb', 'Mellouli', 'Professor der MLU Halle', '1983-06-21', 10005, 'Lehrstuhlinhaber WI und OR', '2004-01-01', 'mellouli@wiwi.uni-halle.de', '', 'mellouli.png', 'http://wior.wiwi.uni-halle.de/im/1437149625_1947_00_800.jpg');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.ingredients
CREATE TABLE IF NOT EXISTS `ingredients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ingredients_name` text NOT NULL,
  `ingredients_description` text NOT NULL,
  `ingredients_warning` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle ps_cagebot.ingredients: ~22 rows (ungefähr)
DELETE FROM `ingredients`;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` (`id`, `ingredients_name`, `ingredients_description`, `ingredients_warning`) VALUES
	(1, 'Levocetirizin dihydrochlorid', 'evocetirizin ist ein Arzneistoff aus der Gruppe der Antihistaminika, der zur symptomatischen Behandlung allergischer Erkrankungen eingesetzt wird. Stereochemisch ist Levocetirizin das aktive Enantiomer (Eutomer) des Cetirizins.', NULL),
	(2, 'Lactose', '', NULL),
	(3, 'Magnesium stearat', '', NULL),
	(4, 'Cellulose', '', NULL),
	(5, 'Opadry', '', NULL),
	(6, 'Hypromellose', '', NULL),
	(7, 'Titan dioxid', '', NULL),
	(8, 'Macrogol 400', '', NULL),
	(9, 'Silicium dioxid', '', NULL),
	(10, 'Azelastin hydrochlorid', 'Azelastin ist ein Arzneistoff. Es ist ein selektives Antihistaminikum vom Typ der H1-Blocker der zweiten Generation. Es wird bei leichter, mittelschwerer und schwerer saisonaler und bei leichter ganzjähriger Rhinitis eingesetzt. Azelastin gibt es als Nasenspray (0,1-prozentige und in USA auch als 0,15-prozentige Lösung) und als Augentropfen (0,05-prozentige Lösung). In einigen Ländern sind das Nasenspray und die Augentropfen auch rezeptfrei in den Apotheken erhältlich.', NULL),
	(11, 'Citronensäure', '', NULL),
	(12, 'Dinatrium edetat 2-Wasser', '', NULL),
	(13, 'Hypromellose', '', NULL),
	(14, 'Natrium chlorid', '', NULL),
	(15, 'Xylometazolin hydrochlorid', 'Xylometazolin ist eine chemische Verbindung aus der Gruppe der Imidazol-Derivate. Sie wird als Arzneistoff zum Abschwellen der Nasenschleimhaut eingesetzt. Als direktes α-Sympathomimetikum ist es ein α1-Adrenozeptor-Agonist und bewirkt die Kontraktion von glatter Muskulatur. Dadurch werden die lokal gelegenen Blutgefäße in der Nase verengt (Vasokonstriktion) und die geringere Durchblutung lässt die Schleimhäute abschwellen.', NULL),
	(16, 'Benzalkonium chlorid', '', NULL),
	(17, 'Wasser', '', NULL),
	(18, 'Glycerin', '', NULL),
	(19, 'Alkohol', '', NULL),
	(20, 'Vitamin D3', '', NULL),
	(21, 'Sonnenblumenöl', '', NULL),
	(22, 'Gelatine', '', NULL);
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.materials
CREATE TABLE IF NOT EXISTS `materials` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `material_group_id` int(11) unsigned NOT NULL,
  `best_before` date NOT NULL,
  `rfid` text NOT NULL,
  `committed` tinyint(3) unsigned NOT NULL,
  `dummy` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

-- Exportiere Daten aus Tabelle ps_cagebot.materials: ~19 rows (ungefähr)
DELETE FROM `materials`;
/*!40000 ALTER TABLE `materials` DISABLE KEYS */;
INSERT INTO `materials` (`id`, `material_group_id`, `best_before`, `rfid`, `committed`, `dummy`) VALUES
	(1, 1, '2018-08-15', '04:FB:A7:8A:30:4C:80', 0, NULL),
	(2, 1, '2022-02-11', '04:F6:A7:8A:30:4C:80', 0, NULL),
	(3, 2, '2014-08-15', '04:16:A6:8A:30:4C:81', 0, NULL),
	(4, 3, '2018-01-06', '04:11:A6:8A:30:4C:81', 0, NULL),
	(5, 4, '2021-03-01', '04:02:A7:8A:30:4C:81', 0, NULL),
	(6, 5, '2020-04-01', '04:0D:A7:8A:30:4C:81', 0, NULL),
	(7, 6, '2018-09-01', '04:07:A7:8A:30:4C:81', 0, NULL),
	(8, 7, '2017-08-31', '04:F1:A7:8A:30:4C:80', 0, NULL),
	(9, 8, '2018-11-01', '04:1A:A5:8A:30:4C:81', 0, NULL),
	(10, 9, '2019-11-01', '04:1F:A5:8A:30:4C:81', 0, NULL),
	(11, 10, '2019-12-01', '04:25:A5:8A:30:4C:81', 0, NULL),
	(12, 4, '2017-03-01', '04:02:A7:8A:30:4C:11', 1, NULL),
	(13, 2, '2018-10-01', '04:02:A7:8A:30:4C:12', 1, NULL),
	(14, 8, '2018-11-01', '04:02:A7:8A:30:4C:13', 1, NULL),
	(15, 8, '2019-11-01', '04:02:A7:8A:30:4C:14', 1, NULL),
	(16, 6, '2017-11-01', '04:02:A7:8A:30:4C:15', 1, NULL),
	(17, 1, '2018-08-01', '04:02:A7:8A:30:4C:16', 1, NULL),
	(18, 1, '2019-08-01', '04:02:A7:8A:30:4C:17', 1, NULL),
	(19, 2, '2027-04-16', '04:02:A7:8A:30:4C:18', 1, NULL),
	(20, 12, '2021-01-01', '04:C7:A7:8A:30:4C:80', 0, 'Dummy 1'),
	(21, 12, '2022-02-02', '04:CE:A7:8A:30:4C:80', 0, 'Dummy 2'),
	(22, 12, '2023-03-03', '04:D3:A7:8A:30:4C:80', 0, 'Dummy 3'),
	(23, 12, '2024-04-04', '04:D8:A7:8A:30:4C:80', 0, 'Dummy 4'),
	(24, 12, '2025-05-05', '04:C2:A7:8A:30:4C:80', 0, 'Dummy 4');
/*!40000 ALTER TABLE `materials` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.materials_groups
CREATE TABLE IF NOT EXISTS `materials_groups` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type_id` int(11) unsigned NOT NULL,
  `producer_id` int(11) unsigned NOT NULL,
  `materials_groups_name` text NOT NULL,
  `materials_groups_description` text,
  `materials_groups_image` text,
  `materials_groups_application` text,
  `materials_groups_warning` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle ps_cagebot.materials_groups: ~11 rows (ungefähr)
DELETE FROM `materials_groups`;
/*!40000 ALTER TABLE `materials_groups` DISABLE KEYS */;
INSERT INTO `materials_groups` (`id`, `type_id`, `producer_id`, `materials_groups_name`, `materials_groups_description`, `materials_groups_image`, `materials_groups_application`, `materials_groups_warning`) VALUES
	(1, 2, 0, 'Dreiecktuch weiß', 'Dreiecktuch Standard', 'dreieck01.png', NULL, NULL),
	(2, 2, 1, 'Dreiecktuch XL', 'Dreiecktuch 90cm x 90cm x 127cm', 'dreieck02.png', NULL, NULL),
	(3, 0, 1, 'Pflaster breit ', 'Pflaster 7,5cm', 'pflaster01.png', 'Gewünschte länge abschneiden.', NULL),
	(4, 0, 3, 'Pflaster schmal', 'Pflaster 6cm', 'pflaster02.png', 'Gewünschte länge abschneiden.', NULL),
	(5, 0, 4, 'Pflaster Strips', 'Pflaster Strips', 'pflaster03.png', NULL, NULL),
	(6, 1, 2, 'Vitamin D3', 'Vitamin D3 Softkapseln', 'nahrungs01.png', 'Nehmen Sie eine Vitamin D3 Softgel-Kapsel täglich mit einem vollen Glas Wasser und am besten mit ihrem Frühstück zusammen ein.', 'Höchstdosis 2 Kapseln!'),
	(7, 3, 4, 'Handcreme Kamille', 'Handcreme Kamille mit Bienenwachs', 'creme01.png', NULL, NULL),
	(8, 4, 6, 'Levocetrizin', 'Levocetirizin Dihydrochlorid', 'levo01.png', '2x täglich eine Tablette', 'Überempfindlichkeitsreaktionen inklusive Anaphylaxie, Dyspnoe, Übelkeit, Quincke-Ödem, Juckreiz, Hautausschlag, Urtikaria, Gewichtszunahme, Palpitationen, Sehstörungen, Hepatitis, erhöhte Leberfunktionstests, Aggressivität, Erregung, epileptische Anfälle, Muskelschmerzen.'),
	(9, 5, 7, 'Vividrin akut', 'Vividrin Akut 0,5mg', 'vividrin01.png', '3x täglich', 'Das Präparat darf nicht angewendet werden, wenn Sie überempfindlich (allergisch) gegen den Wirkstoff Azelastinhydrochlorid oder einen der sonstigen Bestandteile sind und bei Kindern unter 6 Jahren.'),
	(10, 6, 8, 'Otriven', 'Otriven Nasentropfen', 'otriven01.png', '2x täglich', 'Das Arzneimittel darf nicht angewendet werden, wenn Sie allergisch gegen Xylometazolinhydrochlorid oder einen der sonstigen Bestandteile dieses Arzneimittels sind oder wenn Sie unter einer trockenen Entzündung der Nasenschleimhaut mit Borkenbildung (Rhinitis sicca) leiden oder bei Säuglingen und Kindern unter 6 Jahren.'),
	(11, 2, 1, 'Dreiecktuch S', 'Dreiecktuch 50cm x 50cm x 85cm', 'dreieck03.png', NULL, NULL),
	(12, 7, 3, 'Dummyobjekt', 'Dummyobjekte zum testen', 'dummy01.png', NULL, NULL);
/*!40000 ALTER TABLE `materials_groups` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.materials_ingredients
CREATE TABLE IF NOT EXISTS `materials_ingredients` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `material_groups_id` int(11) unsigned NOT NULL,
  `ingredient_id` int(11) unsigned NOT NULL,
  `materials_ingredients_active_ingredient` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `materials_ingredients_dose` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `material_id` (`material_groups_id`),
  KEY `ingredient_id` (`ingredient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle ps_cagebot.materials_ingredients: ~23 rows (ungefähr)
DELETE FROM `materials_ingredients`;
/*!40000 ALTER TABLE `materials_ingredients` DISABLE KEYS */;
INSERT INTO `materials_ingredients` (`id`, `material_groups_id`, `ingredient_id`, `materials_ingredients_active_ingredient`, `materials_ingredients_dose`) VALUES
	(1, 8, 1, 1, 5),
	(2, 8, 2, 0, NULL),
	(3, 8, 3, 0, NULL),
	(4, 8, 4, 0, NULL),
	(5, 8, 5, 0, NULL),
	(6, 8, 6, 0, NULL),
	(7, 8, 7, 0, NULL),
	(8, 8, 8, 0, NULL),
	(9, 8, 9, 0, NULL),
	(10, 9, 10, 1, 1),
	(11, 9, 11, 0, NULL),
	(12, 9, 12, 0, NULL),
	(13, 9, 13, 0, NULL),
	(14, 9, 14, 0, NULL),
	(15, 10, 15, 1, 1),
	(16, 10, 16, 0, NULL),
	(17, 10, 17, 0, NULL),
	(18, 10, 12, 0, NULL),
	(19, 10, 14, 0, NULL),
	(20, 7, 17, 0, NULL),
	(21, 7, 18, 0, NULL),
	(22, 7, 19, 0, NULL),
	(23, 7, 11, 0, NULL),
	(24, 6, 20, 1, 25),
	(25, 6, 21, 0, NULL),
	(26, 6, 22, 0, NULL);
/*!40000 ALTER TABLE `materials_ingredients` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.materials_producers
CREATE TABLE IF NOT EXISTS `materials_producers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `materials_producers_name` text NOT NULL,
  `materials_producers_description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle ps_cagebot.materials_producers: ~8 rows (ungefähr)
DELETE FROM `materials_producers`;
/*!40000 ALTER TABLE `materials_producers` DISABLE KEYS */;
INSERT INTO `materials_producers` (`id`, `materials_producers_name`, `materials_producers_description`) VALUES
	(0, 'HARTMANN', 'Die HARTMANN GRUPPE hat ihren Ursprung im Jahr 1818. In diesem Jahr erwarb unser Unternehmensgründer, der Industriepionier Ludwig von Hartmann, die Spinnerei Meebold.'),
	(1, 'Steroplast Healthcare Ltd', 'Just a decade ago, Steroplast offered only a few – half a dozen or so – commodity products. At that time, our focus was as a contract manufacturer for some of the world’s biggest companies, including 3M, Seton Healthcare (inventor of Tubigrip) and Johnson & Johnson. But, as our reputation for quality and service grew, so did the demand for more lines. So we became a manufacturer and distributor of medical disposables, and – more recently – pharmaceuticals and diagnostic equipment.'),
	(2, 'NU U Nutrition Ltd', 'Our company is the expression of a deeply held, very personal desire to create a lasting difference to the health of our customers and family. This is not a company driven by profit.'),
	(3, 'Edeka', 'Die Edeka-Gruppe (Eigenschreibweise: EDEKA) ist ein genossenschaftlich organisierter kooperativer Unternehmensverbund im deutschen Einzelhandel. Zur Edeka-Gruppe zählen die Edeka Zentrale AG & Co. KG und die sieben Regionalgesellschaften (Großhandelsgeschäft) und deren Regiebetriebe (Filialen), die in neun Genossenschaften organisierten und von den regionalen Handelsgesellschaften belieferten selbständigen Einzelhändler sowie die Netto Marken-Discount AG & Co. KG (Netto).'),
	(4, 'Rossmann', 'Die Dirk Rossmann GmbH, allgemein als Rossmann bezeichnet, ist die zweitgrößte Drogeriemarktkette Deutschlands mit Sitz im niedersächsischen Burgwedel bei Hannover. In Deutschland verfügt die von Dirk Roßmann 1972 gegründete Kette über 2.055 Drogerien mit 30.000 Mitarbeitern. Insgesamt gibt es 3.627 Rossmann-Filialen mit 50.500 Mitarbeitern.[4] Weitere Absatzmärkte sind in fünf europäischen Ländern (Albanien,[5] Polen, Tschechien, Ungarn und in der Türkei) ansässig.'),
	(6, 'Glenmark', 'Glenmark Pharmaceuticals Ltd. ist ein internationales forschendes Pharmaunternehmen mit Sitz in Mumbai, Indien. Der Fokus des Unternehmens liegt auf der Erforschung innovativer chemischer und biologischer Wirkstoffe. Darüber hinaus bietet Glenmark ein breites Portfolio von patentfreien Arzneimitteln. Glenmark beschäftigt rund 11.000 Mitarbeiter in über 80 Ländern und betreibt neben 17 Produktionsstätten auch fünf hochmoderne Forschungszentren, eines davon in Neuchâtel in der Schweiz. Glenmark Pharmaceuticals Ltd. zählt zu den 80 umsatzstärksten Pharma- und Biotechnologieunternehmen weltweit.'),
	(7, 'Bausch und Lomb', 'Das 1853 in den USA gegründete Unternehmen Bausch und Lomb ist ein international operierender Hersteller von Kontaktlinsen und weitere Produkte der Medizintechnik (Medikamente, Implantate für Augenerkrankungen) ausgebaut. Bekannt geworden ist Bausch & Lomb zudem über die berühmte Brillenmarke Ray-Ban, die 1999 an die italienische Luxottica-Gruppe verkauft wurde.'),
	(8, 'GlaxoSmithKline', 'Die GlaxoSmithKline plc. (GSK) ist ein britisches Pharmaunternehmen mit Hauptsitz in London und derzeit weltweit das sechstgrößte Pharmaunternehmen. Das Unternehmen hat weitere Produktionsstätten in Europa sowie in Nordamerika und Asien. Außer Arzneimitteln und Impfstoffen werden auch Gesundheitsprodukte und Hygieneartikel hergestellt. Am 22. April 2014 verkündet der Konzern einen Großumbau per Tauschgeschäft: Für insgesamt 16 Milliarden US-Dollar übernimmt Novartis die Krebsmedikamente des Konzerns, der im Gegenzug 7,1 Milliarden Dollar plus Umsatzbeteiligung für die Novartis-Impfstoffe zahlt. Sein OTC-Arzneimittel-Geschäft bringt Novartis in ein Joint Venture mit GSK ein.');
/*!40000 ALTER TABLE `materials_producers` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.materials_transfers
CREATE TABLE IF NOT EXISTS `materials_transfers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `materials_id` int(11) unsigned NOT NULL,
  `patients_id` int(11) unsigned NOT NULL,
  `materials_transfer_type` tinyint(3) unsigned NOT NULL,
  `materials_transfer_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle ps_cagebot.materials_transfers: ~8 rows (ungefähr)
DELETE FROM `materials_transfers`;
/*!40000 ALTER TABLE `materials_transfers` DISABLE KEYS */;
INSERT INTO `materials_transfers` (`id`, `materials_id`, `patients_id`, `materials_transfer_type`, `materials_transfer_date`) VALUES
	(1, 12, 1, 1, '2017-08-01'),
	(2, 13, 2, 1, '2017-08-07'),
	(3, 14, 5, 1, '2017-08-07'),
	(4, 15, 1, 1, '2017-08-08'),
	(5, 16, 12, 1, '2017-08-08'),
	(6, 17, 1, 1, '2017-08-09'),
	(7, 18, 2, 1, '2017-08-13'),
	(8, 19, 12, 1, '2017-08-15');
/*!40000 ALTER TABLE `materials_transfers` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.materials_types
CREATE TABLE IF NOT EXISTS `materials_types` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `materials_types_name` text NOT NULL,
  `materials_types_description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle ps_cagebot.materials_types: ~8 rows (ungefähr)
DELETE FROM `materials_types`;
/*!40000 ALTER TABLE `materials_types` DISABLE KEYS */;
INSERT INTO `materials_types` (`id`, `materials_types_name`, `materials_types_description`) VALUES
	(0, 'Pflaster', 'Ein Wundschnellverband (WSV), umgangssprachlich auch Pflaster, ist ein Stück Wundauflage, das mit einem Klebeband verbunden ist. Er wird dazu verwendet, kleine Wunden abzudecken.'),
	(1, 'Nahrungsergänzungsmittel', 'Nahrungsergänzungsmittel sind Produkte zur erhöhten Versorgung des menschlichen Stoffwechsels mit bestimmten Nähr- oder Wirkstoffen im Grenzbereich zwischen Arzneimitteln und Lebensmitteln.'),
	(2, 'Dreiecktuch', 'Das Dreiecktuch oder Dreieckstuch ist ein Verbandmittel und Bestandteil eines Verbandkastens.\r\nEs hat die Form eines annähernd rechtwinkligen, gleichschenkligen Dreiecks mit einer Basislänge von meist etwas über 1,3 m und Kathetenlängen von knapp unter 1 m. Es besteht aus Baumwolle oder modernem Faserstoff. Die Farbe ist in der Regel naturweiß, schwarz oder beim Militär oliv.'),
	(3, 'Hautcreme', 'Eine Hautcreme ist eine halbfeste streichfähige Zubereitung zum Auftragen auf die Haut und besteht aus einer wässrigen (hydrophilen) und einer öligen bzw. fetten (lipophilen) Komponente, von der die eine emulsionsartig in der anderen verteilt ist.'),
	(4, 'Antiallergikum', 'Ein Antiallergikum ist ein Medikament, das die Symptome einer allergischen Erkrankung beseitigt oder zumindest lindert.'),
	(5, 'Augentropfen', 'Augentropfen (Oculoguttae) sind  sterile pharmazeutische Zubereitungen eines Wirkstoffes oder mehrerer Wirkstoffe, die zur tropfenweisen Anwendung am Auge vorgesehen sind,.Das Eintropfen erfolgt entweder in den Bindehautsack oder auf die Hornhaut des Auges. Es handelt sich dabei um flüssige Zubereitungen in Form von wässrigen oder öligen Lösungen, Emulsionen oder Suspensionen.'),
	(6, 'Nasentropfen', 'Nasentropfen sind eine Darreichungsform für flüssige Zubereitungen zur Anwendung in der Nase. Die Flüssigkeit wird mittels einer Saugpipette, Einzeldosispipette oder einer Dosierpumpe in die Nase eingebracht.'),
	(7, 'Dummys', 'Sammlung von Dummyobjekten');
/*!40000 ALTER TABLE `materials_types` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.patients
CREATE TABLE IF NOT EXISTS `patients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Vorname` varchar(50) DEFAULT NULL,
  `Nachname` varchar(50) DEFAULT NULL,
  `Grund` varchar(100) DEFAULT NULL,
  `Information` varchar(100) DEFAULT NULL,
  `Geburtstag` date DEFAULT NULL,
  `QR-Code` int(11) DEFAULT NULL,
  `patient_image` text,
  `herkunft` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- Exportiere Daten aus Tabelle ps_cagebot.patients: ~4 rows (ungefähr)
DELETE FROM `patients`;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` (`id`, `Vorname`, `Nachname`, `Grund`, `Information`, `Geburtstag`, `QR-Code`, `patient_image`, `herkunft`) VALUES
	(1, 'Max', 'Mustermann', 'Lungenentzuendung', 'Bettlaegrig', '1960-08-17', 1, 'patient01.png', 'https://cdn-blog.adafruit.com/uploads/2017/02/facesofopensource.png'),
	(2, 'Petra', 'Petrovski', 'Bluthochdruck', NULL, '1991-08-15', 2, 'patient02.png', 'https://blog.adafruit.com/2017/06/28/faces-of-open-source-by-peter-adams-peteradamsphoto-facesopensource-adafruit/'),
	(5, 'Franz', 'Glagenberg', 'Verdacht auf Leukaemie', 'Privatversichert', '1970-11-16', 5, 'patient05.png', 'https://cdn-blog.adafruit.com/uploads/2017/02/facesofopensource.png'),
	(12, 'Maria', 'Mustermann', 'Schienenbeinfraktur', NULL, '1965-08-07', 12, 'patient12.png', 'https://cdn-blog.adafruit.com/uploads/2017/02/facesofopensource.png');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle ps_cagebot.patients_allergy
CREATE TABLE IF NOT EXISTS `patients_allergy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ingredients_id` int(10) unsigned NOT NULL,
  `patients_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle ps_cagebot.patients_allergy: ~4 rows (ungefähr)
DELETE FROM `patients_allergy`;
/*!40000 ALTER TABLE `patients_allergy` DISABLE KEYS */;
INSERT INTO `patients_allergy` (`id`, `ingredients_id`, `patients_id`) VALUES
	(1, 1, 1),
	(2, 10, 1),
	(3, 15, 12),
	(4, 19, 12);
/*!40000 ALTER TABLE `patients_allergy` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
