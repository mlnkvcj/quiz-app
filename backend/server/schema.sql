DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS questions;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  highscore INTEGER
);

CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT UNIQUE NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    answer TEXT NOT NULL
);

INSERT INTO questions (question, option1, option2, option3, option4, answer) 
VALUES 
('Ko je napisao roman "Ana Karenjina"?', 'Fjodor Dostojevski', 'Leo Tolstoj', 'Dostojevski', 'Ivan Sergejevič Turgenjev', 'Leo Tolstoj'),
('Ko je napisao dramu "Hamlet"?', 'Vilijam Šekspir', 'Džejn Ostin', 'Fridrih Niče', 'Fjodor Dostojevski', 'Vilijam Šekspir'),
('Koji je glavni grad Italije?', 'Milano', 'Rim', 'Napulj', 'Firenca', 'Rim'),
('Ko je napisao knjigu "Rat i mir"?', 'Fjodor Dostojevski', 'Mihail Bulgakov', 'Anton Pavlovič Čehov', 'Lev Tolstoj', 'Lev Tolstoj'),
('Ko je naslikao Mona Lizu?', 'Leonardo da Vinči', 'Mikelanđelo', 'Pablo Pikaso', 'Vincent van Gog', 'Leonardo da Vinči'),
('Koja je najduža reka u svetu?', 'Nil', 'Amazon', 'Jangce', 'Misisipi', 'Nil'),
('Koji je najveći kontinent na svetu?', 'Evropa', 'Afrika', 'Azija', 'Australija', 'Azija'),
('Ko je osnovao kompaniju "Microsoft"?', 'Bill Gates', 'Steve Jobs', 'Mark Zuckerberg', 'Elon Musk', 'Bill Gates'),
('Ko je prvi čovek koji je kročio na Mesec?', 'Neil Armstrong', 'Buzz Aldrin', 'Yuri Gagarin', 'John Glenn', 'Neil Armstrong'),
('Ko je napisao "Ana Frank: Dnevnik mlade devojke"?', 'Ana Frank', 'Majkl Endru', 'J. K. Rouling', 'Dan Braun', 'Ana Frank'),
('Ko je autor knjige "Zločin i kazna"?', 'Fjodor Dostojevski', 'Mark Tven', 'Tolkin', 'Džordž Orvel', 'Fjodor Dostojevski'),
('Ko je prvi pronasao Ameriku?', 'Kolumbo', 'Vasko da Gama', 'Ferdinand Magelan', 'Ameriko Vespuči', 'Kolumbo'),
('Ko je napisao knjigu "Sto godina samoće"?', 'Gabrijel Garsija Markes', 'Pablo Neruda', 'Mario Vargas Ljosa', 'Julio Cortázar', 'Gabrijel Garsija Markes'),
('Koji je glavni grad Francuske?', 'Berlin', 'Pariz', 'London', 'Rim', 'Pariz'),
('Ko je napisao "Drakulu"?', 'Bram Stoker', 'Stephen King', 'Edgar Alan Po', 'Maks Fraj', 'Bram Stoker'),
('Ko je naslikao "Gerniku"?', 'Pablo Pikaso', 'Salvador Dalí', 'Vincent van Gog', 'Mikelanđelo', 'Pablo Pikaso'),
('Ko je bio prvi predsednik SAD-a?', 'Džordž Vašington', 'Tomas Džeferson', 'Abraham Linkoln', 'Džon Adams', 'Džordž Vašington'),
('Ko je napisao "Romeo i Julija"?', 'Vilijam Šekspir', 'Fjodor Dostojevski', 'Dostojevski', 'Herman Hese', 'Vilijam Šekspir'),
('Ko je osnivač kompanije "Apple"?', 'Steve Jobs', 'Bill Gates', 'Elon Musk', 'Mark Zuckerberg', 'Steve Jobs'),
('Ko je napisao knjigu "Harry Potter"?', 'J. K. Rowling', 'Stephen King', 'Dan Brown', 'J. R. R. Tolkien', 'J. K. Rowling');