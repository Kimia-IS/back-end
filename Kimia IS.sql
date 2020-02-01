-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 01 Feb 2020 pada 16.49
-- Versi server: 10.3.16-MariaDB
-- Versi PHP: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kimia_is`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `academic`
--

CREATE TABLE `academic` (
  `id` int(11) NOT NULL,
  `course_id` varchar(255) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `total_credit` int(11) NOT NULL,
  `total_classes` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `academic_lecturer`
--

CREATE TABLE `academic_lecturer` (
  `id` int(11) NOT NULL,
  `course_id` varchar(255) NOT NULL,
  `course_class` int(11) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `lecturer_credit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `achievement`
--

CREATE TABLE `achievement` (
  `id` int(11) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `issuer` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `role` int(11) NOT NULL,
  `auth_id` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `announcement`
--

CREATE TABLE `announcement` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` varchar(50000) NOT NULL,
  `author` varchar(255) NOT NULL,
  `module` int(11) NOT NULL,
  `created_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `experience`
--

CREATE TABLE `experience` (
  `id` int(11) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `job_name` varchar(255) NOT NULL,
  `job_type` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `term` int(11) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `final_task`
--

CREATE TABLE `final_task` (
  `id` int(11) NOT NULL,
  `student_name` varchar(255) NOT NULL,
  `student_nim` varchar(255) NOT NULL,
  `student_type` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `starting_date` varchar(255) NOT NULL,
  `graduation_date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `final_task_file`
--

CREATE TABLE `final_task_file` (
  `id` int(11) NOT NULL,
  `final_task_id` int(11) NOT NULL,
  `file_path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `final_task_lecturer`
--

CREATE TABLE `final_task_lecturer` (
  `id` int(11) NOT NULL,
  `final_task_id` int(11) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `lecturer_position` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `journal`
--

CREATE TABLE `journal` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `issue` varchar(255) NOT NULL,
  `total_page` int(11) NOT NULL,
  `type` varchar(255) NOT NULL,
  `doi` varchar(255) NOT NULL,
  `link` varchar(255) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `lecturer`
--

CREATE TABLE `lecturer` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `role` int(11) NOT NULL,
  `nip` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `other_publication`
--

CREATE TABLE `other_publication` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `publisher` varchar(255) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `patent`
--

CREATE TABLE `patent` (
  `id` int(11) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `publisher` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `research`
--

CREATE TABLE `research` (
  `id` int(11) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `title` varchar(255) NOT NULL,
  `investor` varchar(255) NOT NULL,
  `amount` varchar(255) NOT NULL,
  `position` varchar(255) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `research_file`
--

CREATE TABLE `research_file` (
  `id` int(11) NOT NULL,
  `research_id` int(11) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `social_responsibility`
--

CREATE TABLE `social_responsibility` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `investor` varchar(255) NOT NULL,
  `amount` varchar(255) NOT NULL,
  `filepath` varchar(255) NOT NULL,
  `other_parties` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `social_responsibility_file`
--

CREATE TABLE `social_responsibility_file` (
  `id` int(11) NOT NULL,
  `socres_id` int(255) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `social_responsibility_other_parties`
--

CREATE TABLE `social_responsibility_other_parties` (
  `id` int(11) NOT NULL,
  `socres_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `academic`
--
ALTER TABLE `academic`
  ADD PRIMARY KEY (`id`,`course_id`) USING BTREE,
  ADD UNIQUE KEY `course_id` (`course_id`);

--
-- Indeks untuk tabel `academic_lecturer`
--
ALTER TABLE `academic_lecturer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`course_id`),
  ADD KEY `lecturer_nip` (`lecturer_nip`);

--
-- Indeks untuk tabel `achievement`
--
ALTER TABLE `achievement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lecturer_nip` (`lecturer_nip`);

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `announcement`
--
ALTER TABLE `announcement`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `experience`
--
ALTER TABLE `experience`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lecturer_nip` (`lecturer_nip`);

--
-- Indeks untuk tabel `final_task`
--
ALTER TABLE `final_task`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`);

--
-- Indeks untuk tabel `final_task_file`
--
ALTER TABLE `final_task_file`
  ADD PRIMARY KEY (`id`),
  ADD KEY `final_task_id` (`final_task_id`);

--
-- Indeks untuk tabel `final_task_lecturer`
--
ALTER TABLE `final_task_lecturer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `lecturer_nip` (`lecturer_nip`),
  ADD KEY `final_task_id` (`final_task_id`);

--
-- Indeks untuk tabel `journal`
--
ALTER TABLE `journal`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `journal_ibfk_1` (`lecturer_nip`);

--
-- Indeks untuk tabel `lecturer`
--
ALTER TABLE `lecturer`
  ADD PRIMARY KEY (`id`,`nip`) USING BTREE,
  ADD KEY `nip` (`nip`);

--
-- Indeks untuk tabel `other_publication`
--
ALTER TABLE `other_publication`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `lecturer_nip` (`lecturer_nip`);

--
-- Indeks untuk tabel `patent`
--
ALTER TABLE `patent`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `lecturer_nip` (`lecturer_nip`);

--
-- Indeks untuk tabel `research`
--
ALTER TABLE `research`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `lecturer_nip` (`lecturer_nip`);

--
-- Indeks untuk tabel `research_file`
--
ALTER TABLE `research_file`
  ADD PRIMARY KEY (`id`),
  ADD KEY `research_id` (`research_id`);

--
-- Indeks untuk tabel `social_responsibility`
--
ALTER TABLE `social_responsibility`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lecturer_nip` (`lecturer_nip`);

--
-- Indeks untuk tabel `social_responsibility_file`
--
ALTER TABLE `social_responsibility_file`
  ADD PRIMARY KEY (`id`),
  ADD KEY `socres_id` (`socres_id`);

--
-- Indeks untuk tabel `social_responsibility_other_parties`
--
ALTER TABLE `social_responsibility_other_parties`
  ADD PRIMARY KEY (`id`),
  ADD KEY `socres_id` (`socres_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `academic`
--
ALTER TABLE `academic`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `academic_lecturer`
--
ALTER TABLE `academic_lecturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `achievement`
--
ALTER TABLE `achievement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `announcement`
--
ALTER TABLE `announcement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `experience`
--
ALTER TABLE `experience`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `final_task`
--
ALTER TABLE `final_task`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `final_task_file`
--
ALTER TABLE `final_task_file`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `final_task_lecturer`
--
ALTER TABLE `final_task_lecturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `journal`
--
ALTER TABLE `journal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `lecturer`
--
ALTER TABLE `lecturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `other_publication`
--
ALTER TABLE `other_publication`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `patent`
--
ALTER TABLE `patent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `research`
--
ALTER TABLE `research`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `research_file`
--
ALTER TABLE `research_file`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `social_responsibility`
--
ALTER TABLE `social_responsibility`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `social_responsibility_file`
--
ALTER TABLE `social_responsibility_file`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `social_responsibility_other_parties`
--
ALTER TABLE `social_responsibility_other_parties`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `academic_lecturer`
--
ALTER TABLE `academic_lecturer`
  ADD CONSTRAINT `academic_lecturer_ibfk_1` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `id` FOREIGN KEY (`course_id`) REFERENCES `academic` (`course_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `achievement`
--
ALTER TABLE `achievement`
  ADD CONSTRAINT `achievement_ibfk_1` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `experience`
--
ALTER TABLE `experience`
  ADD CONSTRAINT `experience_ibfk_1` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `final_task_file`
--
ALTER TABLE `final_task_file`
  ADD CONSTRAINT `final_task_file_ibfk_1` FOREIGN KEY (`final_task_id`) REFERENCES `final_task` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `final_task_lecturer`
--
ALTER TABLE `final_task_lecturer`
  ADD CONSTRAINT `final_task_lecturer_ibfk_1` FOREIGN KEY (`final_task_id`) REFERENCES `final_task` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `final_task_lecturer_ibfk_2` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `journal`
--
ALTER TABLE `journal`
  ADD CONSTRAINT `journal_ibfk_1` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `other_publication`
--
ALTER TABLE `other_publication`
  ADD CONSTRAINT `other_publication_ibfk_1` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `patent`
--
ALTER TABLE `patent`
  ADD CONSTRAINT `patent_ibfk_1` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `research`
--
ALTER TABLE `research`
  ADD CONSTRAINT `research_ibfk_1` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `research_file`
--
ALTER TABLE `research_file`
  ADD CONSTRAINT `research_file_ibfk_1` FOREIGN KEY (`research_id`) REFERENCES `research` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `social_responsibility`
--
ALTER TABLE `social_responsibility`
  ADD CONSTRAINT `social_responsibility_ibfk_1` FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `social_responsibility_file`
--
ALTER TABLE `social_responsibility_file`
  ADD CONSTRAINT `social_responsibility_file_ibfk_1` FOREIGN KEY (`socres_id`) REFERENCES `social_responsibility` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `social_responsibility_other_parties`
--
ALTER TABLE `social_responsibility_other_parties`
  ADD CONSTRAINT `social_responsibility_other_parties_ibfk_1` FOREIGN KEY (`socres_id`) REFERENCES `social_responsibility` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
