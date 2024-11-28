-- Comando para deletar a tabela conversations, se existir
DROP TABLE IF EXISTS conversations;

-- Comando para deletar a tabela contacts, se existir
DROP TABLE IF EXISTS contacts;

-- Comando para criar a tabela contacts
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    number VARCHAR(20) NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Comando para criar a tabela conversations
CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    type_message VARCHAR(50) NOT NULL,
    date_message TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
