create db 
CREATE TABLE user_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    intent VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
