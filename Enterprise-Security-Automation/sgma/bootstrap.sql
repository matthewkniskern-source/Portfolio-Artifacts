-- Run as local MySQL administrator. Fresh dedicated schema only.
CREATE DATABASE IF NOT EXISTS sgma CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
-- MySQL 8.0.18+ generates a password and displays it once. Store it privately.
CREATE USER 'sgma_app'@'localhost' IDENTIFIED BY RANDOM PASSWORD;
GRANT SELECT, INSERT ON sgma.* TO 'sgma_app'@'localhost';
-- No UPDATE, DELETE, ALTER, DROP, GRANT or global rights for the runtime account.
-- Use a separate administrator session for initial schema setup; never run the web app as root.
