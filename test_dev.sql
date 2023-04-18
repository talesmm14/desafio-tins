-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.7.5-MariaDB-1:10.7.5+maria~ubu2004 - mariadb.org binary distribution
-- OS do Servidor:               debian-linux-gnu
-- HeidiSQL Versão:              12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para teste_dev
CREATE DATABASE IF NOT EXISTS `teste_dev` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `teste_dev`;

-- Copiando estrutura para tabela teste_dev.tbl_cliente
CREATE TABLE IF NOT EXISTS `tbl_cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `CPF` int(11) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela teste_dev.tbl_cliente: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela teste_dev.tbl_cliente_endereco
CREATE TABLE IF NOT EXISTS `tbl_cliente_endereco` (
  `id` int(11) NOT NULL,
  `cod_cliente` int(11) DEFAULT NULL,
  `cod_endereco` int(11) DEFAULT NULL,
  `default` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_tbl_cliente_endereco_tbl_cliente` (`cod_cliente`),
  KEY `FK_tbl_cliente_endereco_tbl_endereco` (`cod_endereco`),
  CONSTRAINT `FK_tbl_cliente_endereco_tbl_cliente` FOREIGN KEY (`cod_cliente`) REFERENCES `tbl_cliente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_tbl_cliente_endereco_tbl_endereco` FOREIGN KEY (`cod_endereco`) REFERENCES `tbl_endereco` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela teste_dev.tbl_cliente_endereco: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela teste_dev.tbl_endereco
CREATE TABLE IF NOT EXISTS `tbl_endereco` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `CEP` varchar(250) NOT NULL,
  `logradouro` varchar(250) NOT NULL,
  `bairro` varchar(250) NOT NULL,
  `localidade` varchar(250) NOT NULL,
  `numero` varchar(50) NOT NULL,
  `titulo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela teste_dev.tbl_endereco: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela teste_dev.tbl_pedido
CREATE TABLE IF NOT EXISTS `tbl_pedido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` int(11) DEFAULT NULL,
  `data` datetime DEFAULT NULL,
  `cod_cliente` int(11) NOT NULL,
  `email_enviado` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__tbl_cliente` (`cod_cliente`),
  CONSTRAINT `FK__tbl_cliente` FOREIGN KEY (`cod_cliente`) REFERENCES `tbl_cliente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela teste_dev.tbl_pedido: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela teste_dev.tbl_pedido_produto
CREATE TABLE IF NOT EXISTS `tbl_pedido_produto` (
  `id` int(11) NOT NULL,
  `cod_pedido` int(11) NOT NULL,
  `cod_produto` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__tbl_pedido` (`cod_pedido`),
  KEY `FK__tbl_produto` (`cod_produto`),
  CONSTRAINT `FK__tbl_pedido` FOREIGN KEY (`cod_pedido`) REFERENCES `tbl_pedido` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK__tbl_produto` FOREIGN KEY (`cod_produto`) REFERENCES `tbl_produto` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela teste_dev.tbl_pedido_produto: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela teste_dev.tbl_produto
CREATE TABLE IF NOT EXISTS `tbl_produto` (
  `id` int(11) NOT NULL,
  `descricao` int(11) NOT NULL,
  `valor` decimal(6,2) NOT NULL,
  `codigo` int(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela teste_dev.tbl_produto: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;