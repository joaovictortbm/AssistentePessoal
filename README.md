# Assistente Pessoal - Chatbot Empresarial com IA

Este projeto é uma simulação de um assistente inteligente para donos de empresa, que responde perguntas baseadas em dados empresariais fictícios armazenados em um banco de dados SQLite. O objetivo é demonstrar como um chatbot pode integrar consultas SQL e análises em Python para auxiliar em decisões empresariais.

---

## Arquitetura do Projeto

O assistente é construído utilizando um **agente LangChain** que combina múltiplas **tools** para entregar respostas precisas e contextualizadas:

- **SQLDatabaseToolkit:** permite que o agente consulte diretamente a base de dados SQLite com comandos SQL, extraindo dados operacionais como vendas, clientes e produtos.
- **Python REPL:** possibilita a execução de código Python para realizar cálculos, estatísticas e transformações avançadas sobre os dados extraídos.
- **Modelo de linguagem GPT-4o-mini:** gera respostas naturais, interpreta perguntas e decide qual tool utilizar para atender à solicitação do usuário.

Essa combinação permite que o agente funcione de forma inteligente, alternando entre busca direta nos dados e análises complexas, mantendo contexto da conversa para melhor experiência.

---

## Base de Dados Utilizada

Este projeto usa a base de dados **Northwind** em formato SQLite, que é uma base de dados fictícia muito conhecida para aprendizado e testes em ambientes empresariais.

- Nome: Northwind
- Link para download: [https://github.com/jpwhite3/northwind-SQLite3](https://github.com/jpwhite3/northwind-SQLite3)

---

## Funcionalidades

- Responde perguntas sobre vendas, clientes, produtos e receitas da empresa com base em dados fictícios.
- Consulta dados diretamente do banco SQL (SQLite).
- Realiza cálculos e análises usando ambiente Python REPL integrado.
- Mantém contexto da conversa para respostas mais naturais.
- Interface web simples e interativa com Streamlit.
- Persistência do histórico de mensagens na sessão.

---

## Tecnologias utilizadas

- Python 3.10+
- [LangChain](https://github.com/hwchase17/langchain)
- [OpenAI GPT (gpt-4o-mini)](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
- SQLite (base de dados Northwind — base fictícia para simulação)
- dotenv para gerenciamento seguro de variáveis de ambiente
