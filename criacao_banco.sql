-- Criação do banco de dados do Sistema-KUKY
CREATE DATABASE IF NOT EXISTS db_kuky;
USE db_kuky;

-- Tabela de exemplo para cadastrar os usuários/integrantes do sistema
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
