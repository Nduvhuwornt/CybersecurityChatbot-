-- ============================================================
-- Cybersecurity Chatbot — MySQL Database Setup Script
-- PROG6221 POE — Programming 2A
-- Run this in MySQL Workbench or the MySQL CLI
-- ============================================================

CREATE DATABASE IF NOT EXISTS cybersecurity_chatbot;
USE cybersecurity_chatbot;

CREATE TABLE IF NOT EXISTS tasks (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    IsCompleted BOOLEAN DEFAULT FALSE,
    ReminderDate DATETIME NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Sample tasks for testing
INSERT INTO tasks (Title, Description, IsCompleted, ReminderDate) VALUES
('Enable Two-Factor Authentication', 'Set up 2FA on Gmail, social media, and banking apps.', FALSE, DATE_ADD(NOW(), INTERVAL 3 DAY)),
('Update all passwords', 'Use a password manager and set strong unique passwords.', FALSE, DATE_ADD(NOW(), INTERVAL 7 DAY)),
('Review privacy settings', 'Audit Facebook, Instagram, and Google account privacy settings.', TRUE, NULL),
('Install antivirus software', 'Download and configure a reputable AV solution.', FALSE, DATE_ADD(NOW(), INTERVAL 1 DAY));

SELECT * FROM tasks;
