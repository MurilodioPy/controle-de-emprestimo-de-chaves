
CREATE TABLE chaves (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  situacao VARCHAR(255) NOT NULL,
  status VARCHAR(255) DEFAULT 'disponivel'
);

CREATE TABLE servidores (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  cpf VARCHAR(255) UNIQUE NOT NULL,
  contato VARCHAR(255),
  nascimento TIMESTAMP,
  status VARCHAR(255) DEFAULT 'ativo'
);

CREATE TABLE emprestimos (
  id SERIAL PRIMARY KEY,
  datahora_emprestimo TIMESTAMP DEFAULT NOW(),
  datahora_devolucao TIMESTAMP,
  status VARCHAR(255) DEFAULT 'pendente',
  chave_id INTEGER REFERENCES chaves(id),
  servidor_retirou_id INTEGER REFERENCES servidores(id),
  servidor_devolveu_id INTEGER REFERENCES servidores(id)
);
