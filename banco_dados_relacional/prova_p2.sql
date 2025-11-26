CREATE DATABASE techmarica;
USE techmarica;


CREATE TABLE funcionarios (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
area VARCHAR(100) NOT NULL,
ativo BOOLEAN NOT NULL DEFAULT TRUE,
data_admissao DATE NOT NULL DEFAULT (CURRENT_DATE)
);

CREATE TABLE produtos (
id INT AUTO_INCREMENT PRIMARY KEY,
codigo_interno VARCHAR(20) NOT NULL UNIQUE,
nome VARCHAR(100) NOT NULL,
custo_producao DECIMAL(10,2) NOT NULL,
responsavel_tecnico INT NOT NULL,
data_cadastro DATE NOT NULL DEFAULT (CURRENT_DATE),
FOREIGN KEY (responsavel_tecnico) REFERENCES funcionarios(id)
);

CREATE TABLE maquinas (
id INT AUTO_INCREMENT PRIMARY KEY,
codigo VARCHAR(20) NOT NULL UNIQUE,
nome VARCHAR(100) NOT NULL,
setor VARCHAR(100) NOT NULL,
capacidade_hora INT DEFAULT 10
);

CREATE TABLE ordens_producao (
id INT AUTO_INCREMENT PRIMARY KEY,
data_inicio DATETIME NOT NULL DEFAULT NOW(),
data_conclusao DATETIME NULL,
produto_id INT NOT NULL,
maquina_id INT NOT NULL,
autorizado_por INT NOT NULL,
quantidade INT NOT NULL DEFAULT 1,
status VARCHAR(50) NOT NULL DEFAULT 'EM PRODUCAO',
FOREIGN KEY (produto_id) REFERENCES produtos(id),
FOREIGN KEY (maquina_id) REFERENCES maquinas(id),
FOREIGN KEY (autorizado_por) REFERENCES funcionarios(id)
);

INSERT INTO funcionarios (nome, area, ativo, data_admissao) VALUES
('Carlos Silva', 'Eletrônica', TRUE, '2020-03-15'),
('Thiago Santos', 'Produção', TRUE, '2019-07-22'),
('João Pereira', 'Qualidade', TRUE, '2021-01-10'),
('Ana Ribeiro', 'TI', TRUE, '2022-05-18'),
('Paula Costa', 'Eletrônica', FALSE, '2018-11-05'),
('Marcos Oliveira', 'Produção', TRUE, '2023-02-14'),
('Fernanda Lima', 'Engenharia', TRUE, '2020-09-30');

INSERT INTO produtos (codigo_interno, nome, custo_producao, responsavel_tecnico, data_cadastro) VALUES
('P1001', 'Sensor Ultrassônico X1', 45.90, 1, '2022-01-15'),
('P1002', 'Placa Controladora A7', 120.50, 2, '2021-06-20'),
('P1003', 'Módulo Bluetooth M3', 35.00, 1, '2023-03-10'),
('P1004', 'Sensor de Temperatura T5', 18.90, 3, '2022-11-25'),
('P1005', 'Placa Lógica L2', 88.70, 2, '2021-08-18'),
('P1006', 'Sensor de Pressão P9', 52.30, 7, '2023-07-05'),
('P1007', 'Módulo WiFi W4', 41.80, 1, '2024-02-12');

INSERT INTO maquinas (codigo, nome, setor, capacidade_hora) VALUES
('MQ-01', 'Impressora 3D Sigma', 'Prototipagem', 5),
('MQ-02', 'Fresadora CNC F500', 'Corte', 15),
('MQ-03', 'Linha SMT L80', 'Montagem de Placas', 20),
('MQ-04', 'Torno Automático T300', 'Usinagem', 12),
('MQ-05', 'Estação de Solda ES-200', 'Montagem Manual', 8);

INSERT INTO ordens_producao (produto_id, maquina_id, autorizado_por, quantidade, status, data_inicio, data_conclusao) 
VALUES
(1, 3, 1, 50, 'CONCLUIDO', '2025-11-01 08:00:00', '2025-11-01 16:30:00'),
(2, 2, 2, 30, 'CONCLUIDO', '2025-11-05 09:00:00', '2025-11-06 14:00:00'),
(3, 1, 1, 20, 'PAUSADO', '2025-11-10 10:00:00', NULL),
(4, 3, 3, 100, 'CONCLUIDO', '2025-11-12 07:30:00', '2025-11-13 18:00:00'),
(5, 2, 2, 25, 'EM PRODUCAO', '2025-11-20 08:00:00', NULL),
(6, 4, 6, 40, 'EM PRODUCAO', '2025-11-22 09:30:00', NULL),
(7, 5, 7, 60, 'CONCLUIDO', '2025-11-15 11:00:00', '2025-11-16 15:30:00');

SELECT 
    op.id AS ordem_id,
    op.data_inicio,
    op.data_conclusao,
    op.quantidade,
    op.status,
    p.codigo_interno,
    p.nome AS produto,
    p.custo_producao,
    m.codigo AS codigo_maquina,
    m.nome AS maquina,
    m.setor,
    f.nome AS autorizado_por,
    f.area AS area_responsavel,
    op.quantidade * p.custo_producao AS custo_total_ordem
FROM ordens_producao op
INNER JOIN produtos p ON op.produto_id = p.id
INNER JOIN maquinas m ON op.maquina_id = m.id
INNER JOIN funcionarios f ON op.autorizado_por = f.id
ORDER BY op.data_inicio DESC;

SELECT 
    id,
    nome,
    area,
    data_admissao,
    TIMESTAMPDIFF(YEAR, data_admissao, CURDATE()) AS anos_empresa
FROM funcionarios
WHERE ativo = FALSE;

SELECT 
    f.id,
    f.nome AS responsavel_tecnico,
    f.area,
    COUNT(p.id) AS total_produtos,
    AVG(p.custo_producao) AS custo_medio,
    SUM(p.custo_producao) AS custo_total_produtos
FROM funcionarios f
INNER JOIN produtos p ON f.id = p.responsavel_tecnico
WHERE f.ativo = TRUE
GROUP BY f.id, f.nome, f.area
ORDER BY total_produtos DESC;

SELECT 
    codigo_interno,
    nome,
    custo_producao,
    UPPER(LEFT(nome, 1)) AS primeira_letra
FROM produtos
WHERE nome LIKE 'S%'
ORDER BY nome;

SELECT 
    codigo_interno,
    nome,
    custo_producao,
    data_cadastro
FROM produtos
WHERE nome LIKE 'P%' OR nome LIKE 'M%'
ORDER BY nome;

SELECT 
    codigo_interno,
    nome,
    data_cadastro,
    TIMESTAMPDIFF(YEAR, data_cadastro, CURDATE()) AS anos_catalogo,
    TIMESTAMPDIFF(MONTH, data_cadastro, CURDATE()) AS meses_catalogo,
    DATEDIFF(CURDATE(), data_cadastro) AS dias_catalogo,
    CASE 
        WHEN TIMESTAMPDIFF(YEAR, data_cadastro, CURDATE()) < 1 THEN 'Novo'
        WHEN TIMESTAMPDIFF(YEAR, data_cadastro, CURDATE()) BETWEEN 1 AND 2 THEN 'Recente'
        ELSE 'Antigo'
    END AS classificacao
FROM produtos
ORDER BY data_cadastro;

SELECT 
    m.codigo,
    m.nome,
    m.setor,
    COUNT(op.id) AS total_ordens,
    SUM(op.quantidade) AS total_pecas_produzidas
FROM maquinas m
LEFT JOIN ordens_producao op ON m.id = op.maquina_id
GROUP BY m.id, m.codigo, m.nome, m.setor
ORDER BY total_ordens DESC;

SELECT 
    p.codigo_interno,
    p.nome,
    p.custo_producao,
    f.nome AS responsavel
FROM produtos p
LEFT JOIN ordens_producao op ON p.id = op.produto_id
INNER JOIN funcionarios f ON p.responsavel_tecnico = f.id
WHERE op.id IS NULL;

SELECT 
    op.id,
    p.nome AS produto,
    op.data_inicio,
    op.data_conclusao,
    TIMESTAMPDIFF(HOUR, op.data_inicio, op.data_conclusao) AS horas_producao,
    op.quantidade,
    TIMESTAMPDIFF(HOUR, op.data_inicio, op.data_conclusao) / op.quantidade AS horas_por_peca
FROM ordens_producao op
INNER JOIN produtos p ON op.produto_id = p.id
WHERE op.status = 'CONCLUIDO' AND op.data_conclusao IS NOT NULL
ORDER BY horas_producao DESC;

SELECT 
    area,
    COUNT(*) AS total_funcionarios,
    GROUP_CONCAT(nome SEPARATOR ', ') AS funcionarios
FROM funcionarios
WHERE ativo = TRUE
GROUP BY area;

CREATE VIEW vw_painel_producao AS
SELECT 
    op.id AS ordem_id,
    op.status,
    op.quantidade,
    DATE_FORMAT(op.data_inicio, '%d/%m/%Y %H:%i') AS inicio,
    CASE 
        WHEN op.data_conclusao IS NOT NULL 
        THEN DATE_FORMAT(op.data_conclusao, '%d/%m/%Y %H:%i')
        ELSE 'Em andamento'
    END AS conclusao,
    p.codigo_interno AS cod_produto,
    p.nome AS produto,
    p.custo_producao AS custo_unitario,
    p.custo_producao * op.quantidade AS custo_total,
    m.codigo AS cod_maquina,
    m.nome AS maquina,
    m.setor,
    f.nome AS responsavel,
    f.area,
    CASE 
        WHEN op.data_conclusao IS NOT NULL 
        THEN TIMESTAMPDIFF(HOUR, op.data_inicio, op.data_conclusao)
        ELSE TIMESTAMPDIFF(HOUR, op.data_inicio, NOW())
    END AS horas_decorridas
FROM ordens_producao op
INNER JOIN produtos p ON op.produto_id = p.id
INNER JOIN maquinas m ON op.maquina_id = m.id
INNER JOIN funcionarios f ON op.autorizado_por = f.id;

SELECT * FROM vw_painel_producao ORDER BY ordem_id DESC;

SELECT * FROM vw_painel_producao WHERE status = 'EM PRODUCAO';

SELECT * FROM vw_painel_producao WHERE setor = 'Montagem de Placas';

DELIMITER $$

CREATE PROCEDURE sp_nova_ordem_producao(
    IN p_produto_id INT,
    IN p_maquina_id INT,
    IN p_autorizado_por INT,
    IN p_quantidade INT
)
BEGIN
    DECLARE v_ordem_id INT;
    DECLARE v_produto_nome VARCHAR(100);
    DECLARE v_maquina_nome VARCHAR(100);
    DECLARE v_funcionario_nome VARCHAR(100);
    
    IF NOT EXISTS (SELECT 1 FROM produtos WHERE id = p_produto_id) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Erro: Produto não encontrado';
    END IF;
    
    IF NOT EXISTS (SELECT 1 FROM maquinas WHERE id = p_maquina_id) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Erro: Máquina não encontrada';
    END IF;
    
    IF NOT EXISTS (SELECT 1 FROM funcionarios WHERE id = p_autorizado_por AND ativo = TRUE) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Erro: Funcionário não encontrado ou inativo';
    END IF;
    
    INSERT INTO ordens_producao (produto_id, maquina_id, autorizado_por, quantidade, status, data_inicio)
    VALUES (p_produto_id, p_maquina_id, p_autorizado_por, p_quantidade, 'EM PRODUCAO', NOW());
    
    SET v_ordem_id = LAST_INSERT_ID();
    
    SELECT nome INTO v_produto_nome FROM produtos WHERE id = p_produto_id;
    SELECT nome INTO v_maquina_nome FROM maquinas WHERE id = p_maquina_id;
    SELECT nome INTO v_funcionario_nome FROM funcionarios WHERE id = p_autorizado_por;
    
    SELECT 
        v_ordem_id AS ordem_criada,
        v_produto_nome AS produto,
        v_maquina_nome AS maquina,
        v_funcionario_nome AS autorizado_por,
        p_quantidade AS quantidade,
        'EM PRODUCAO' AS status,
        NOW() AS data_inicio,
        'Ordem de produção registrada com sucesso!' AS mensagem;
        
END$$

DELIMITER ;

CALL sp_nova_ordem_producao(1, 3, 2, 75);

CALL sp_nova_ordem_producao(5, 4, 6, 40);

DELIMITER $$

CREATE TRIGGER trg_finalizar_ordem
BEFORE UPDATE ON ordens_producao
FOR EACH ROW
BEGIN
    IF NEW.data_conclusao IS NOT NULL 
       AND OLD.data_conclusao IS NULL 
       AND NEW.status != 'CONCLUIDO' THEN
        SET NEW.status = 'CONCLUIDO';
    END IF;
END$$

DELIMITER ;

UPDATE ordens_producao 
SET data_conclusao = NOW() 
WHERE id = 5;

SELECT id, status, data_inicio, data_conclusao 
FROM ordens_producao 
WHERE id = 5;

UPDATE produtos 
SET custo_producao = custo_producao * 1.10 
WHERE codigo_interno = 'P1003';

UPDATE ordens_producao 
SET status = 'PAUSADO' 
WHERE id = 6;

DELETE FROM ordens_producao WHERE id = 3;

UPDATE funcionarios 
SET ativo = TRUE 
WHERE id = 5;

UPDATE maquinas 
SET setor = 'Montagem Especial' 
WHERE codigo = 'MQ-05';