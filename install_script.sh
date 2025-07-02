#!/bin/bash

# Script de instalação para OSINT Links Manager
# Compatível com Linux e macOS

echo "=== OSINT Links Manager - Instalação ==="
echo

# Detectar sistema operacional
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    echo "Sistema detectado: Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    echo "Sistema detectado: macOS"
else
    echo "Sistema operacional não suportado: $OSTYPE"
    exit 1
fi

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python 3 não está instalado. Por favor, instale Python 3 primeiro."
    
    if [[ "$OS" == "linux" ]]; then
        echo "No Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip python3-tk"
        echo "No CentOS/RHEL: sudo yum install python3 python3-pip tkinter"
        echo "No Arch: sudo pacman -S python python-pip tk"
    elif [[ "$OS" == "macos" ]]; then
        echo "No macOS: brew install python-tk"
        echo "Ou baixe Python do site oficial: https://www.python.org/downloads/"
    fi
    
    exit 1
fi

echo "Python 3 encontrado: $(python3 --version)"

# Verificar se tkinter está disponível
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "Tkinter não está disponível. Instalando..."
    
    if [[ "$OS" == "linux" ]]; then
        if command -v apt &> /dev/null; then
            sudo apt update && sudo apt install python3-tk
        elif command -v yum &> /dev/null; then
            sudo yum install tkinter
        elif command -v pacman &> /dev/null; then
            sudo pacman -S tk
        else
            echo "Não foi possível instalar tkinter automaticamente."
            echo "Por favor, instale o pacote tkinter para Python 3 manualmente."
            exit 1
        fi
    elif [[ "$OS" == "macos" ]]; then
        if command -v brew &> /dev/null; then
            brew install python-tk
        else
            echo "Homebrew não encontrado. Por favor, instale tkinter manualmente."
            echo "Você pode instalar o Homebrew em: https://brew.sh/"
            exit 1
        fi
    fi
fi

# Criar diretório de instalação
INSTALL_DIR="$HOME/osint-links-manager"
echo "Criando diretório de instalação: $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

# Baixar ou copiar o arquivo principal
if [[ -f "osint_links_manager.py" ]]; then
    echo "Copiando arquivo principal..."
    cp osint_links_manager.py "$INSTALL_DIR/"
else
    echo "Arquivo osint_links_manager.py não encontrado no diretório atual."
    echo "Por favor, certifique-se de que o arquivo está no mesmo diretório que este script."
    exit 1
fi

# Tornar o arquivo executável
chmod +x "$INSTALL_DIR/osint_links_manager.py"

# Criar script de inicialização
echo "Criando script de inicialização..."
cat > "$INSTALL_DIR/run.sh" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 osint_links_manager.py
EOF

chmod +x "$INSTALL_DIR/run.sh"

# Criar link simbólico para execução global (opcional)
if [[ "$OS" == "linux" ]]; then
    DESKTOP_FILE="$HOME/.local/share/applications/osint-links-manager.desktop"
    echo "Criando entrada no menu de aplicações..."
    
    mkdir -p "$HOME/.local/share/applications"
    
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=OSINT Links Manager
Comment=Ferramenta para organizar links de OSINT
Exec=$INSTALL_DIR/run.sh
Icon=applications-internet
Terminal=false
Categories=Network;Security;
EOF
    
    chmod +x "$DESKTOP_FILE"
    echo "Entrada criada no menu: $DESKTOP_FILE"
fi

# Criar alias para terminal
SHELL_RC=""
if [[ -f "$HOME/.bashrc" ]]; then
    SHELL_RC="$HOME/.bashrc"
elif [[ -f "$HOME/.zshrc" ]]; then
    SHELL_RC="$HOME/.zshrc"
fi

if [[ -n "$SHELL_RC" ]]; then
    echo "Adicionando alias ao $SHELL_RC..."
    echo "" >> "$SHELL_RC"
    echo "# OSINT Links Manager" >> "$SHELL_RC"
    echo "alias osint-links='cd $INSTALL_DIR && ./run.sh'" >> "$SHELL_RC"
    echo "Alias 'osint-links' adicionado. Execute 'source $SHELL_RC' ou reinicie o terminal."
fi

echo
echo "=== Instalação Concluída ==="
echo "Diretório de instalação: $INSTALL_DIR"
echo
echo "Para executar a ferramenta:"
echo "1. Execute: $INSTALL_DIR/run.sh"
echo "2. Ou use o alias: osint-links (após reiniciar o terminal)"
if [[ "$OS" == "linux" ]]; then
    echo "3. Ou procure por 'OSINT Links Manager' no menu de aplicações"
fi
echo
echo "Para desinstalar, simplesmente remova o diretório: rm -rf $INSTALL_DIR"
echo