# SPRINT1-PYTHON
## Integrantes
- Carolina Ferraz RM86833
- Estevam Melo RM555124
- Gustavo Morais RM554972
- Leonardo Novaes RM554807
- Miguel Carmo RM557622

# Projeto de Cadastro e Login de Usuários

Este projeto é uma aplicação simples em Python que permite o cadastro e login de usuários, e oferece informações sobre Fórmula E e Fórmula 1 após um login bem-sucedido.

## Detalhes do Projeto

A aplicação possui as seguintes funcionalidades:
- Cadastro de novos usuários.
- Login de usuários cadastrados.
- Menu pós-login com opções de:
  - Curiosidades sobre carros de Fórmula E e Fórmula 1.
  - Informações sobre as últimas corridas de Fórmula E.
  - Informações sobre as próximas corridas de Fórmula E.
  - Listagem dos times de Fórmula E e suas respectivas vitórias.

## Instruções de Uso

1. **Clonar o Repositório**
   ```bash
   git clone <URL do repositório>
   cd <diretório do repositório>
   
2. **Executar Aplicação**
   ```bash
   python <nome_do_arquivo>.py
   
3. **Navegar no Menu Principal**
- Escolha entre cadastrar um novo usuário, fazer login ou sair da aplicação.
- Após o login, navegue pelas opções do menu para obter informações sobre Fórmula E e Fórmula 1.

## Informações Relevantes
- Segurança Simples: A aplicação utiliza listas para armazenar usuários e senhas, o que não é seguro para uso em produção. Em uma aplicação real, considere utilizar um banco de dados e métodos seguros de armazenamento de senhas (como hashing).
- Sistema de Menu: A aplicação utiliza os.system('cls' if os.name == 'nt' else 'clear') para limpar a tela, tornando-a compatível com Windows e Unix-like systems.
