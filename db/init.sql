-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 17 Feb 2020 pada 05.50
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
  `total_classes` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `academic`
--

INSERT INTO `academic` (`id`, `course_id`, `course_name`, `total_classes`) VALUES
(1, 'KI1202', 'Kimia Murni', 1),
(2, 'MA9902', 'Matematika Testing', 2),
(3, 'SI2290', 'Sistem Testing', 4),
(4, 'FI3230', 'Fisika Testing', 2),
(5, 'IF3120', 'Basis Data Boongan', 4),
(6, 'II2212', 'Apaan Lagi', 2),
(7, 'KI7782', 'Bingung', 1),
(8, 'TE2200', 'TESTING LAGI', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `academic_lecturer`
--

CREATE TABLE `academic_lecturer` (
  `id` int(11) NOT NULL,
  `course_id` varchar(255) NOT NULL,
  `course_class` int(11) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `lecturer_credit` int(11) NOT NULL,
  `total_credit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `academic_lecturer`
--

INSERT INTO `academic_lecturer` (`id`, `course_id`, `course_class`, `lecturer_nip`, `lecturer_credit`, `total_credit`) VALUES
(1, 'KI1202', 1, '18217050', 3, 0);

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
  `email` varchar(255) NOT NULL,
  `token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`id`, `name`, `role`, `auth_id`, `password`, `email`, `token`) VALUES
(2, 'Vincent', 5, '18217042', 'password', 'siauw@com.com', NULL),
(3, 'Vincent Siauw', 1, '18217022', '$2b$12$Al1bPQ93Uy5nKo94OgNPyeBbhwWUCYdpMq8BUwKyW3NvTbo2G5t5W', 'jamesvincentsiauw@gmail.com', 'asdasdasdasdasfrgrgsdvadv');

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

--
-- Dumping data untuk tabel `final_task`
--

INSERT INTO `final_task` (`id`, `student_name`, `student_nim`, `student_type`, `title`, `starting_date`, `graduation_date`) VALUES
(1, 'vincent', '182170422', 'S1', 'testing', '5 maret', '2 maret'),
(3, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(4, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(5, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(6, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(7, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(8, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(9, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(10, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(11, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(12, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(13, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei'),
(14, 'vincent post', '182174224122', 'S4', 'sdasdasda', '7 Mei', '10 Mei');

-- --------------------------------------------------------

--
-- Struktur dari tabel `final_task_file`
--

CREATE TABLE `final_task_file` (
  `id` int(11) NOT NULL,
  `final_task_id` int(11) NOT NULL,
  `file_path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `final_task_file`
--

INSERT INTO `final_task_file` (`id`, `final_task_id`, `file_path`) VALUES
(1, 1, '/file/path'),
(2, 14, '[\'datas/files/finalTasks/LIST MAHASISWA.pdf\']');

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

--
-- Dumping data untuk tabel `final_task_lecturer`
--

INSERT INTO `final_task_lecturer` (`id`, `final_task_id`, `lecturer_nip`, `lecturer_position`) VALUES
(9, 13, '18217050', 'baru'),
(10, 14, '18217050', 'baru');

-- --------------------------------------------------------

--
-- Struktur dari tabel `journal`
--

CREATE TABLE `journal` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `number` varchar(255) NULL,
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
  `email` varchar(255) NOT NULL,
  `token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `lecturer`
--

INSERT INTO `lecturer` (`id`, `name`, `role`, `nip`, `password`, `email`, `token`) VALUES
(1, 'Alfian Maulana', 1, '18217050', 'password', 'alfian@com.com', NULL),
(3, 'Vincent', 1, '182170400', '$2b$12$LZB/tUJd3LmwzMAJKsV4NuF0pmTJJZ.ExPi4gRQi.J5db2Ygq7gdy', 'jamesvincentsiauw@gmail.com', 'ffgua999a7asuassdajsdasda33354kivytee'),
(4, 'Vincent Siauw', 1, '182170401', '$2b$12$Z7YZHMrnoXf8ogxHVgjOj.pEUP9CXGwAUtUsO2zJPsD6lqA1R1xy.', 'jamesvincentsiauw@gmail.com', NULL),
(5, 'Vincent Siauw', 1, '182170404', '$2b$12$yBpUyAa/3jUNShsvDeHDEOjs6QQyCV9IQf/M1/ijZxZUoLEu7RMg6', 'jamesvincentsiauw@gmail.com', NULL),
(6, 'Vincent Siauw', 1, '182170409', '$2b$12$Kjwn1mYbZFSZ6gvQKi.Ip.qBBy8UlzGoyessFSkMkeSre8l128yyO', 'jamesvincentsiauw@gmail.com', NULL),
(7, 'Vincent Siauw', 1, '182170429', '$2b$12$E.qfNvKjXK0TlXpbAQWga.YmwZ985j5FOGmxEu7i3McoCMZ0V8/66', 'jamesvincentsiauw@gmail.com', NULL),
(8, 'Vincent Siauw', 1, '1821729', '$2b$12$V8/cOWbPNcp8RjM1iJJSr.7R56hoD6rHzjo5caukB03flPQ6gdTii', 'jamesvincentsiauw@gmail.com', NULL),
(9, 'Vincent Siauw', 1, '182171129', '$2b$12$slgVKl8fSCIECdYQFEr6VOAcRr8drwJJKsRCvydtNv.6naHWv5Sl.', 'jamesvincentsiauw@gmail.com', NULL),
(10, 'Vincent Siauw', 1, '182171111129', '$2b$12$0/Ya.AI29AAIA8u3xL61eeeENjB5DUqd/NBEnvbaxOKJwIzonKUWi', 'jamesvincentsiauw@gmail.com', NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `organization`
--

CREATE TABLE `organization` (
  `id` int(11) NOT NULL,
  `lecturer_nip` varchar(255) NOT NULL,
  `organization_name` varchar(255) NOT NULL,
  `position` varchar(255) NOT NULL,
  `year` varchar(5) NOT NULL,
  `filepath` varchar(255) NOT NULL
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
  ADD KEY `final_task_id` (`final_task_id`) USING BTREE,
  ADD KEY `lecturer_nip` (`lecturer_nip`) USING BTREE;

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
-- Indeks untuk tabel `organization`
--
ALTER TABLE `organization`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lecturer_nip` (`lecturer_nip`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `academic_lecturer`
--
ALTER TABLE `academic_lecturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `achievement`
--
ALTER TABLE `achievement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT untuk tabel `final_task_file`
--
ALTER TABLE `final_task_file`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `final_task_lecturer`
--
ALTER TABLE `final_task_lecturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `journal`
--
ALTER TABLE `journal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `lecturer`
--
ALTER TABLE `lecturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `organization`
--
ALTER TABLE `organization`
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

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
