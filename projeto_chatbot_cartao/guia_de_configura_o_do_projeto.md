# Guia de Configuração do Projeto

Siga os passos abaixo para criar e executar o ambiente do seu projeto:

## 1. Estrutura Inicial de Pastas e Arquivos

1. **Crie a pasta do projeto** no local de sua preferência.
2. **Adicione os arquivos de dados:** Mova os arquivos `perguntas.csv` e `respostas.json` para dentro desta pasta.
3. **Abra o VS Code:** Abra o programa e selecione a pasta do projeto recém-criada (`File > Open Folder`).
4. **Crie os arquivos principais:**
   - `app.py`
   - `requirements.txt`

---

## 2. Configuração das Dependências

No arquivo `requirements.txt`, adicione as seguintes bibliotecas:

```text
streamlit
pandas
scikit-learn
```

---

## 3. Criação e Ativação do Ambiente Virtual

1. **Abra o terminal** no VS Code (`Ctrl` + `` ` ``).
2. **Crie o ambiente virtual:**
   ```bash
   python -m venv venv
   ```
3. **Ative o ambiente virtual:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   > **Nota:** Após a ativação, o identificador `(venv)` deverá aparecer no início da linha de comando do terminal.

   *(Caso ocorra algum erro de permissão ao ativar a política de execução, execute o comando abaixo antes do script de ativação:)*
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

---

## 4. Instalação de Pacotes

Com o ambiente virtual ativado, instale as bibliotecas contidas no arquivo `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

---

## 5. Execução do Aplicativo

Para testar e rodar a aplicação com o Streamlit, execute:

```bash
python -m streamlit run app.py
```

> O Streamlit abrirá automaticamente a aplicação no seu navegador padrão, geralmente acessível pelo endereço `http://localhost:8501`.