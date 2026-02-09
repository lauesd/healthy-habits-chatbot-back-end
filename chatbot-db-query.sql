drop database if exists habit_tracker;
create database habit_tracker;

CREATE TABLE user_profile (
    id INT PRIMARY KEY CHECK (id = 1),
    username VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    intent VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
