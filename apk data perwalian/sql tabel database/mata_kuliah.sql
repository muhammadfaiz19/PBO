-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 18, 2024 at 07:58 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perwalian`
--

-- --------------------------------------------------------

--
-- Table structure for table `mata_kuliah`
--

CREATE TABLE `mata_kuliah` (
  `id` int(11) NOT NULL,
  `mahasiswa_id` varchar(50) NOT NULL,
  `nama_mk` enum('Pemrograman Berorientasi Objek','AIK','Arsitektur dan Organisasi Komputer','Sistem Informasi','Kalkulus II','Komunikasi Data','Statistika Dan Probabilitas','Struktur Data dan Algoritma') NOT NULL,
  `sks` enum('1','2','3','4','5','6') NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mata_kuliah`
--

INSERT INTO `mata_kuliah` (`id`, `mahasiswa_id`, `nama_mk`, `sks`, `date`) VALUES
(1, 'Muhammad Faiz', 'Pemrograman Berorientasi Objek', '3', '2024-02-17'),
(2, 'Muhammad Faiz', 'AIK', '2', '2024-02-17'),
(4, 'Muhammad Faiz', 'Arsitektur dan Organisasi Komputer', '2', '2024-02-17'),
(7, 'Nadzwa Nurul Hikmah', 'Pemrograman Berorientasi Objek', '3', '2024-02-17'),
(8, 'Revan Fazry Huda', 'Pemrograman Berorientasi Objek', '3', '2024-02-17'),
(9, 'Nadzwa Nurul Hikmah', 'AIK', '2', '2024-02-17'),
(10, 'Muhammad Faiz', 'Sistem Informasi', '3', '2024-02-17'),
(11, 'Muhammad Faiz', 'Kalkulus II', '2', '2024-02-17'),
(12, 'Muhammad Faiz', 'Komunikasi Data', '2', '2024-02-17'),
(13, 'Muhammad Faiz', 'Statistika Dan Probabilitas', '2', '2024-02-17'),
(14, 'Muhammad Faiz', 'Struktur Data dan Algoritma', '2', '2024-02-17'),
(16, 'Revan Fazry Huda', 'AIK', '2', '2024-02-17');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mata_kuliah`
--
ALTER TABLE `mata_kuliah`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mata_kuliah`
--
ALTER TABLE `mata_kuliah`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
