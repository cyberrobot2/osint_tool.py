# OSINT Links Manager

Ferramenta desktop para organizar e acessar rapidamente links de OSINT (Open Source Intelligence).

## 📋 Características

- **Multiplataforma**: Funciona em Linux e macOS
- **Interface Gráfica**: Interface intuitiva desenvolvida em Tkinter
- **Categorização**: Links organizados por categoria (Busca Geral, E-mail, Empresas, etc.)
- **Busca Rápida**: Sistema de busca integrado
- **Acesso Direto**: Abre links diretamente no navegador padrão
- **Cópia de URLs**: Copia URLs para área de transferência

## 🛠️ Instalação

### Pré-requisitos

- Python 3.6 ou superior
- Tkinter (geralmente incluído com Python)

### Linux

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk
```

#### CentOS/RHEL:
```bash
sudo yum install python3 python3-pip tkinter
```

#### Arch Linux:
```bash
sudo pacman -S python python-pip tk
```

### macOS

#### Com Homebrew:
```bash
brew install python-tk
```

#### Ou baixe Python do site oficial:
https://www.python.org/downloads/

### Instalação Automática

1. Baixe os arquivos do projeto
2. Execute o script de instalação:
```bash
chmod +x install.sh
./install.sh
```

### Instalação Manual

1. Baixe o arquivo `osint_links_manager.py`
2. Execute diretamente:
```bash
python3 osint_links_manager.py
```

## 🚀 Como Usar

### Executando a Ferramenta

#### Após instalação automática:
```bash
osint-links
```

#### Ou execute diretamente:
```bash
cd ~/osint-links-manager
./run.sh
```

#### Ou via Python:
```bash
python3 osint_links_manager.py
```

### Interface

1. **Painel Esquerdo**: Lista de categorias
2. **Painel Principal**: Links da categoria selecionada
3. **Botões Inferiores**:
   - **Abrir Link**: Abre o link selecionado no navegador
   - **Copiar URL**: Copia a URL para área de transferência
   - **Buscar**: Realiza busca nos links
4. **Campo de Busca**: Digite termos para encontrar links específicos

### Atalhos

- **Duplo clique** em um link: Abre no navegador
- **Enter** no campo de busca: Executa a busca

## 📂 Categorias de Links

### Busca Geral
- SR Watson - Plataforma de investigação
- WebMii - Busca de pessoas na web
- OSINT Industries - Plataforma OSINT completa
- AI OSINT ChatGPT - IA especializada em OSINT

### Empresas/CNPJ
- Busca Prime - Consulta dados de empresas
- Hunter Jud - Consulta judicial e empresarial
- Econodata - Dados econômicos de empresas
- Exato Digital - Consultas empresariais

### Monitoramento/Vazamentos
- Have I Been Pwned - Verificação de vazamentos
- DeHashed - Base de dados de vazamentos
- Intelligence X - Motor de busca OSINT
- Sherlocker - Monitoramento em tempo real

### E-mail/Comunicação
- Epieos - Investigação de e-mails
- Dono do Zap - Identificação WhatsApp
- MailScrap - Extração de e-mails
- Mailbox Validator - Validação de e-mails

### Domínios/IPs
- Registro.br WHOIS - WHOIS brasileiro
- ICANN Lookup - Consulta ICANN
- MaxMind IP - Localização de IP
- Archive.org - Wayback Machine

### Redes Sociais/Pessoas
- NameCheck - Verificação de username
- WhatsMyName - Busca de usernames
- UserSearch - Busca de usuários

### Reconhecimento Facial
- FaceCheck - Reconhecimento facial
- PimEyes - Busca reversa de faces
- TinEye - Busca reversa de imagens

### Geolocalização
- GeoSpy AI - IA para geolocalização
- Google Maps - Mapas e localização
- WiGLE - Base de dados WiFi

### Ferramentas/Recursos
- OSINT Brazuca - Recursos brasileiros
- Sherlock Project - Busca de usernames
- Maltego - Análise de links
- Hunchly - Ferramenta de investigação

## 🔍 Funcionalidades

### Busca
- Digite qualquer termo no campo de busca
- A busca procura em nomes, descrições e URLs
- Resultados mostram a categoria de origem

### Abertura de Links
- Selecione um link e clique em "Abrir Link"
- Ou dê duplo clique no link
- Abre no navegador padrão do sistema

### Cópia de URLs
- Selecione um link e clique em "Copiar URL"
- A URL é copiada para área de transferência

## 🛡️ Segurança e Privacidade

- A ferramenta apenas organiza links, não coleta dados
- Links abrem no seu navegador padrão
- Nenhuma informação é enviada para servidores externos
- Use as ferramentas OSINT de forma ética e legal

## 🔧 Personalização

Para adicionar novos links, edite o arquivo `osint_links_manager.py` na seção `self.links` e adicione:

```python
"Nova Categoria": [
    {"name": "Nome do Site", "url": "https://exemplo.com", "desc": "Descrição do site"}
]
```

## 📋 Requisitos do Sistema

- **