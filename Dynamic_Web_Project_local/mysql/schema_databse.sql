USE rubrica;

CREATE TABLE lista_contatti (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cognome VARCHAR(100) NOT NULL,
    indirizzo VARCHAR(255),
    telefono VARCHAR(20),
    anni INT,
    PRIMARY KEY (id)
);

-- INSERT INTO lista_contatti (nome, cognome, indirizzo, telefono, anni)
-- VALUES 
--     ("Francesco", "Gaggini", "Corso Italia 67, Torino", "3359876543", 28);