-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 13. Aug 2017 um 20:45
-- Server-Version: 10.1.25-MariaDB
-- PHP-Version: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `ps_cagebot`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `consumption`
--

CREATE TABLE `consumption` (
  `id` int(11) NOT NULL,
  `currentValue` int(11) DEFAULT NULL,
  `min_Value` int(11) DEFAULT NULL COMMENT 'Minimalbestand',
  `max_Value` int(11) DEFAULT NULL,
  `unit` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `consumption`
--

INSERT INTO `consumption` (`id`, `currentValue`, `min_Value`, `max_Value`, `unit`) VALUES
(20001, 100, 20, 250, 'Milliliter'),
(20002, 3, 5, 40, 'Stueck'),
(20003, 100, 50, 365, 'Stueck');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `Vorname` varchar(50) DEFAULT NULL,
  `Nachname` varchar(50) DEFAULT NULL,
  `Berufsbezeichnung` varchar(50) DEFAULT NULL,
  `Geburtstag` date DEFAULT NULL,
  `QR-Code` int(11) DEFAULT NULL,
  `Information` varchar(100) DEFAULT NULL,
  `Angestellt seit` date DEFAULT NULL,
  `E-Mail` varchar(50) DEFAULT NULL,
  `Skype` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `employee`
--

INSERT INTO `employee` (`id`, `Vorname`, `Nachname`, `Berufsbezeichnung`, `Geburtstag`, `QR-Code`, `Information`, `Angestellt seit`, `E-Mail`, `Skype`) VALUES
(10001, 'Simon-J.', 'Wimmer', 'Masterstudent Wirtschaftsinformatik', '1991-12-20', 10001, 'Mitglied Projektseminar WI-Cagebot', '2010-10-10', 'simon-justus.wimmer@student.uni-halle.de', NULL),
(10002, 'Antje', 'Fackler', 'Masterstudent Wirtschaftsinformatik', '1990-01-01', 10002, 'Mitglied Projektseminar WI-Cagebot', '2010-01-01', 'antje.fackler@student.uni-halle.de', NULL),
(10003, 'Gunter', 'Sachse', 'Bachelorstudent Wirtschaftsinformatik', '1990-01-01', 10003, 'Mitglied Projektseminar WI-Cagebot', '2010-01-01', 'gunter.sachse@student.uni-halle.de', NULL),
(10004, 'Carsten', 'Helbig', 'Dipl.-Wirtsch.-Inf. Karsten Helbig', '1990-01-01', 10004, 'Leiter Projektseminar WI-Cagebot', '2000-01-01', 'karsten.helbig@wiwi.uni-halle.de', NULL),
(10005, 'Taieb', 'Mellouli', 'Professor der MLU Halle', '1983-06-21', 10005, 'Lehrstuhlinhaber WI und OR', '2004-01-01', 'mellouli@wiwi.uni-halle.de', '');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `materials`
--

CREATE TABLE `materials` (
  `id` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Typ` varchar(50) DEFAULT NULL,
  `Hersteller` varchar(50) DEFAULT NULL,
  `QR-Code` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `materials`
--

INSERT INTO `materials` (`id`, `Name`, `Typ`, `Hersteller`, `QR-Code`) VALUES
(20001, 'Handcreme Vanille', 'Creme', 'elkos', 20001),
(20002, 'Pflasterstrips', 'Verbandzeug', 'altapharma', 20003),
(20003, 'Vitamin D Tabletten', 'Tabletten', 'Nu U', 20003);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `patients`
--

CREATE TABLE `patients` (
  `id` int(11) NOT NULL,
  `Vorname` varchar(50) DEFAULT NULL,
  `Nachname` varchar(50) DEFAULT NULL,
  `Grund` varchar(100) DEFAULT NULL,
  `Information` varchar(100) DEFAULT NULL,
  `Geburtstag` date DEFAULT NULL,
  `QR-Code` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `patients`
--

INSERT INTO `patients` (`id`, `Vorname`, `Nachname`, `Grund`, `Information`, `Geburtstag`, `QR-Code`) VALUES
(1, 'Max', 'Mustermann', 'Lungenentzuendung', 'Bettlaegrig', '1960-08-17', 1),
(5, 'Franz', 'Glagenberg', 'Verdacht auf Leukaemie', 'Privatversichert', '1970-11-16', 5),
(12, 'Maria', 'Mustermann', 'Schienenbeinfraktur', '-', '1965-08-07', 12);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `consumption`
--
ALTER TABLE `consumption`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `materials`
--
ALTER TABLE `materials`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10006;
--
-- AUTO_INCREMENT für Tabelle `materials`
--
ALTER TABLE `materials`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20004;
--
-- AUTO_INCREMENT für Tabelle `patients`
--
ALTER TABLE `patients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
