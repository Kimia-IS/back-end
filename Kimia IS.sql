CREATE TABLE `lecturer` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `role` int,
  `password` varchar(255),
  `email` varchar(255),
  `nip` int
);

CREATE TABLE `admin` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `role` int,
  `password` varchar(255),
  `email` varchar(255),
  `auth_id` varchar(255)
);

CREATE TABLE `academic` (
  `id` int,
  `course_id` varchar(255),
  `course_name` varchar(255),
  `total_credit` int
);

CREATE TABLE `academic_lecturer` (
  `id` int,
  `id_academic` varchar(255),
  `lecturer_nip` int,
  `credit` int,
  `class` int
);

CREATE TABLE `final_task` (
  `id` int,
  `student_name` varchar(255),
  `student_nim` int,
  `student_type` varchar(255),
  `title` varchar(255),
  `starting_date` datetime,
  `graduation_date` datetime
);

CREATE TABLE `final_task_lecturer` (
  `id` int,
  `id_final_task` int,
  `lecturer_nip` int,
  `lecturer_position` varchar(255)
);

CREATE TABLE `final_task_file` (
  `id` int,
  `id_final_task` int,
  `filepath` varchar(255)
);

CREATE TABLE `research` (
  `id` int,
  `lecturer_nip` int,
  `year` int,
  `title` varchar(255),
  `investor` varchar(255),
  `amount` int,
  `position` varchar(255)
);

CREATE TABLE `research_file` (
  `id` int,
  `id_research` int,
  `filepath` varchar(255)
);

CREATE TABLE `journal` (
  `id` int,
  `title` varchar(255),
  `lecturer_nip` int,
  `name` varchar(255),
  `year` int,
  `journal_id` varchar(255),
  `issue` varchar(255),
  `total_page` int,
  `type` varchar(255),
  `doi` varchar(255),
  `link` varchar(255),
  `filepath` varchar(255)
);

CREATE TABLE `journal_corresponding_author` (
  `id` int,
  `id_journal` int,
  `name` varchar(255)
);

CREATE TABLE `patent` (
  `id` int,
  `lecturer_nip` int,
  `title` varchar(255),
  `status` varchar(255),
  `publisher` varchar(255),
  `year` int,
  `filepath` varchar(255)
);

CREATE TABLE `other_publication` (
  `id` int,
  `lecturer_nip` int,
  `title` varchar(255),
  `date` date,
  `author` varchar(255),
  `publisher` varchar(255),
  `filepath` varchar(255)
);

CREATE TABLE `social_responsibility` (
  `id` int,
  `year` int,
  `title` varchar(255),
  `lecturer_nip` int,
  `investor` varchar(255),
  `amount` int,
  `position` varchar(255)
);

CREATE TABLE `social_responsibility_other_party` (
  `id` int,
  `id_socres` int,
  `name` varchar(255)
);

CREATE TABLE `social_responsibility_file` (
  `id` int,
  `id_socres` int,
  `filepath` varchar(255)
);

CREATE TABLE `achievement` (
  `id` int,
  `lecturer_nip` int,
  `title` varchar(255),
  `issuer` varchar(255),
  `year` int,
  `filepath` varchar(255)
);

CREATE TABLE `organization` (
  `id` int,
  `lecturer_nip` int,
  `name` varchar(255),
  `year` int,
  `role` varchar(255),
  `filepath` varchar(255)
);

CREATE TABLE `work_experience` (
  `id` int,
  `lecturer_nip` int,
  `job_name` varchar(255),
  `job_type` varchar(255),
  `year` int,
  `term` int,
  `filepath` varchar(255)
);

CREATE TABLE `announcement` (
  `id` int,
  `title` varchar(255),
  `author` varchar(255),
  `content` varchar(255),
  `module` int,
  `timestamp` timestamp
);

ALTER TABLE `academic_lecturer` ADD FOREIGN KEY (`id_academic`) REFERENCES `academic` (`id`);

ALTER TABLE `academic_lecturer` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `final_task_lecturer` ADD FOREIGN KEY (`id_final_task`) REFERENCES `final_task` (`id`);

ALTER TABLE `final_task_lecturer` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `final_task_file` ADD FOREIGN KEY (`id_final_task`) REFERENCES `final_task` (`id`);

ALTER TABLE `research` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `research_file` ADD FOREIGN KEY (`id_research`) REFERENCES `research` (`id`);

ALTER TABLE `journal` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `journal_corresponding_author` ADD FOREIGN KEY (`id_journal`) REFERENCES `journal` (`id`);

ALTER TABLE `patent` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `other_publication` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `social_responsibility` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `social_responsibility_other_party` ADD FOREIGN KEY (`id_socres`) REFERENCES `social_responsibility` (`id`);

ALTER TABLE `social_responsibility_file` ADD FOREIGN KEY (`id_socres`) REFERENCES `social_responsibility` (`id`);

ALTER TABLE `achievement` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `organization` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);

ALTER TABLE `work_experience` ADD FOREIGN KEY (`lecturer_nip`) REFERENCES `lecturer` (`nip`);
