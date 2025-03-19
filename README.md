# 🎉 BirthAPP

## 📌 Descrição
**BirthAPP** é um aplicativo desenvolvido para automatizar o envio de mensagens de felicitação por e-mail para aniversariantes e colaboradores que estão completando mais um ano na empresa. Ele foi pensado para empresas que desejam manter um ambiente corporativo mais acolhedor e engajado.

---

## 🚀 Tecnologias Utilizadas

- **Python** - Linguagem principal do projeto
- **Pandas** - Manipulação de dados no arquivo Excel
- **OpenPyXL** - Leitura de arquivos Excel
- **SMTP** - Envio de e-mails automáticos
- **Twilio (Futuro)** - Envio de mensagens via WhatsApp
- **Selenium (Futuro)** - Automação de processos

---

## 🛠 Como Rodar o Projeto

### 🔹 1. Pré-requisitos
- Ter o **Python** instalado (versão 3.8 ou superior)
- Criar uma conta no **Gmail** para envio de e-mails
- Ativar a opção de "Acesso a aplicativos menos seguros" no Gmail (ou configurar o OAuth2)

### 🔹 2. Instalar Dependências
Abra o terminal e execute:
```sh
pip install pandas openpyxl smtplib
```

### 🔹 3. Configurar o Arquivo Excel
O arquivo Excel deve conter as seguintes colunas:
| Nome  | Email | Data de Nascimento | Data de Entrada |
|-------|------------|------------------|---------------|
| João  | joao@email.com | 1990-03-18 | 2015-03-18 |
| Maria | maria@email.com | 1985-07-22 | 2012-07-22 |

> **Obs.:** O nome do arquivo Excel deve ser passado como parâmetro ao rodar o script.

### 🔹 4. Executar o Programa
```sh
python birthapp.py dados.xlsx
```


---

## 🚀 Melhorias Futuras
- 🔹 Implementação do envio de mensagens via **WhatsApp** (Twilio)
- 🔹 Interface gráfica para facilitar o uso
- 🔹 Integração com banco de dados para gerenciamento de funcionários
- 🔹 Dashboard para visualização de aniversários e métricas
- 🔹 Aprimoramento da Leitura do Excel: Incluir validações para garantir que o arquivo Excel esteja corretamente formatado antes de iniciar o processo de leitura e envio.
- 🔹 Customização de Mensagens: Permitir que as mensagens enviadas sejam customizadas de acordo com o perfil do colaborador ou departamento.

---

## 📝 Autor
**Arthur Abreu** - Desenvolvedor do BirthAPP

