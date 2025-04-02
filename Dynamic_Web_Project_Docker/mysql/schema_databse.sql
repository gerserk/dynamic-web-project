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
