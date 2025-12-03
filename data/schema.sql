CREATE DATABASE IF NOT EXISTS dv_database;
USE dv_database;

CREATE TABLE BotUsers (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    ChatID BIGINT NOT NULL,
    TgName VARCHAR(100),
    Lang VARCHAR(10),
    UserRole ENUM('Regular', 'Agent', 'Admin') DEFAULT 'Regular',
    StartDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Agent (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    AgentName VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(30),
    BankAccount VARCHAR(100),
    ApplicationCount INT DEFAULT 0,
    
    FOREIGN KEY (UserID) REFERENCES BotUsers(UserID)
);

CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    FullName VARCHAR(150),
    Gender VARCHAR(10),
    BirthDate VARCHAR(50),
    BirthCity VARCHAR(100),
    CurrentCity VARCHAR(100),
    PhoneNumber VARCHAR(30),
    Email VARCHAR(120),
    Education VARCHAR(120),
    MaritalStatus VARCHAR(50),
    PhotoPath VARCHAR(255),
    PaymentPath VARCHAR(255),
    PaymentStatus ENUM('Pending', 'Paid', 'Rejected') DEFAULT 'Pending',
    RegisterStatus ENUM('Unsubmitted','Submitted') DEFAULT 'Unsubmitted',
    CreationDate DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (UserID) REFERENCES BotUsers(UserID)
)