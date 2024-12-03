-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 14, 2022 at 12:54 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `repertoire`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `nom` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `prenom` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `birthday` date NOT NULL,
  `adresse` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `profession` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `numero_fixe` varchar(10) COLLATE utf8_unicode_ci NOT NULL DEFAULT '1111111111',
  `numero_portable` varchar(10) COLLATE utf8_unicode_ci NOT NULL DEFAULT '1111111111',
  `mail` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`nom`, `prenom`, `birthday`, `adresse`, `profession`, `numero_fixe`, `numero_portable`, `mail`) VALUES
('Conact test', 'A supprimer', '2022-10-04', 'qsfqsfqsf', 'sdgsdgsdg', '1111111111', '0000000000', 'QFqfqzsf@gmqisl.com'),
('Randriantsoa', 'Jean', '2011-07-23', 'Tivernon', 'Collegien', '0458456458', '0458126458', 'Mail@mail.com'),
('Randriantsoa', 'Nathan', '2011-07-23', 'Tivernon', 'Collegien', '0123654789', '0645321564', 'test@gmail.com'),
('Fellouh', 'Corentin', '2005-12-11', 'Asherès-le-Marché', 'Lycéen', '0123456789', '0776826145', 'CorentinMail@mail.com'),
('Randriantsoa', 'Nathan', '2005-01-25', 'Tivernon', 'Lycéen ', '0123456789', '0776928387', 'MonMail@gmail.com'),
('Fellouh', 'Lilian', '2002-11-07', 'Ashères-le-Marché', 'Classe Prepa', '0126548920', '0778956412', 'L.Fellouh@mail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`numero_portable`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
