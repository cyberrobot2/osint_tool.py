
#!/usr/bin/env python3
"""
OSINT Links Manager
Ferramenta para organizar e acessar links de OSINT
Compatível com Linux e macOS
"""

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import json
import os
from urllib.parse import urlparse
import threading

class OSINTLinksManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OSINT Links Manager")
        self.root.geometry("1200x800")
        
        # Lista de links OSINT organizados por categoria
        self.links = {
            "Telegram/Bots": [
                {"name": "BING SIX BOT", "url": "https://t.me/BINGSIXBOT", "desc": "Bot do Telegram para pesquisas"}
            ],
            "Busca Geral": [
                {"name": "SR Watson", "url": "https://srwatson.co/", "desc": "Plataforma de investigação"},
                {"name": "WebMii", "url": "https://webmii.com/", "desc": "Busca de pessoas na web"},
                {"name": "OSINT Industries", "url": "https://www.osint.industries/", "desc": "Plataforma OSINT completa"},
                {"name": "AI OSINT ChatGPT", "url": "https://chatgpt.com/g/g-aZQ1x6vqB-ai-osint", "desc": "IA especializada em OSINT"}
            ],
            "Empresas/CNPJ": [
                {"name": "Busca Prime", "url": "https://buscaprime.com.br/buscar-dados-de-empresas/consulta.php", "desc": "Consulta dados de empresas"},
                {"name": "Hunter Jud", "url": "https://www.hunterjud.com.br/", "desc": "Consulta judicial e empresarial"},
                {"name": "Econodata", "url": "https://www.econodata.com.br/consulta-empresa", "desc": "Dados econômicos de empresas"},
                {"name": "Exato Digital", "url": "https://exato.digital/", "desc": "Consultas empresariais"}
            ],
            "Monitoramento/Vazamentos": [
                {"name": "Sherlocker", "url": "https://live.sherlocker.com.br/", "desc": "Monitoramento em tempo real"},
                {"name": "Have I Been Pwned", "url": "https://haveibeenpwned.com/", "desc": "Verificação de vazamentos de dados"},
                {"name": "Exploit-DB", "url": "https://www.exploit-db.com/", "desc": "Base de dados de exploits"},
                {"name": "DeHashed", "url": "https://dehashed.com/", "desc": "Base de dados de vazamentos"},
                {"name": "Intelligence X", "url": "https://intelx.io/", "desc": "Motor de busca OSINT"}
            ],
            "E-mail/Comunicação": [
                {"name": "Epieos", "url": "https://epieos.com/", "desc": "Investigação de e-mails"},
                {"name": "Dono do Zap", "url": "https://donodozap.com/", "desc": "Identificação de números WhatsApp"},
                {"name": "Consulta Número", "url": "https://consultanumero.abrtelecom.com.br/consultanumero", "desc": "Consulta operadora telefônica"},
                {"name": "MailScrap", "url": "https://mailscrap.com/", "desc": "Extração de e-mails"},
                {"name": "Mailbox Validator", "url": "https://www.mailboxvalidator.com/", "desc": "Validação de e-mails"}
            ],
            "Domínios/IPs": [
                {"name": "Registro.br WHOIS", "url": "https://registro.br/tecnologia/ferramentas/whois/", "desc": "WHOIS brasileiro"},
                {"name": "ICANN Lookup", "url": "https://lookup.icann.org/en", "desc": "Consulta ICANN"},
                {"name": "Archive.org", "url": "http://archive.org/", "desc": "Wayback Machine"},
                {"name": "MaxMind IP", "url": "https://www.maxmind.com/en/locate-my-ip-address", "desc": "Localização de IP"},
                {"name": "Meu IP", "url": "https://www.meuip.com.br/", "desc": "Informações do seu IP"},
                {"name": "IP Location", "url": "https://www.iplocation.net/", "desc": "Localização geográfica de IP"},
                {"name": "DNS Leak", "url": "https://dnsleak.com/results?token=ky923ptcj0phbyok", "desc": "Teste de vazamento DNS"}
            ],
            "Redes Sociais/Pessoas": [
                {"name": "NameCheck", "url": "https://www.namecheck.com/en/", "desc": "Verificação de username"},
                {"name": "NameChk", "url": "https://namechk.com/", "desc": "Disponibilidade de nomes"},
                {"name": "WhatsMyName", "url": "https://whatsmyname.app/", "desc": "Busca de usernames"},
                {"name": "UserSearch", "url": "https://usersearch.org/", "desc": "Busca de usuários"}
            ],
            "Reconhecimento Facial": [
                {"name": "FaceCheck", "url": "https://facecheck.id/pt", "desc": "Reconhecimento facial"},
                {"name": "PimEyes", "url": "https://pimeyes.com/en", "desc": "Busca reversa de faces"},
                {"name": "TinEye", "url": "https://tineye.com/", "desc": "Busca reversa de imagens"},
                {"name": "Image Identify", "url": "https://www.imageidentify.com/", "desc": "Identificação de imagens"},
                {"name": "Image Edited", "url": "https://imageedited.com/", "desc": "Detecção de edições"}
            ],
            "Geolocalização": [
                {"name": "GeoSpy AI", "url": "https://geospy.ai/", "desc": "IA para geolocalização"},
                {"name": "Google Maps", "url": "https://www.google.com.br/maps/", "desc": "Mapas e localização"},
                {"name": "WiGLE", "url": "https://wigle.net/", "desc": "Base de dados WiFi"}
            ],
            "Ferramentas/Recursos": [
                {"name": "OSINT Brazuca", "url": "https://github.com/osintbrazuca/osint-brazuca", "desc": "Recursos OSINT brasileiros"},
                {"name": "Sherlock Project", "url": "https://github.com/sherlock-project/sherlock", "desc": "Busca de usernames"},
                {"name": "NixIntel", "url": "https://nixintel.info/osint/", "desc": "Tutoriais e recursos OSINT"},
                {"name": "Intelligence X Tools", "url": "https://intelx.io/tools", "desc": "Ferramentas OSINT"},
                {"name": "Hunchly", "url": "https://hunch.ly/", "desc": "Ferramenta de investigação"},
                {"name": "Trace Labs", "url": "https://www.tracelabs.org/", "desc": "Competições OSINT"},
                {"name": "Maltego", "url": "https://www.maltego.com/", "desc": "Análise de links"},
                {"name": "Hak5 Shop", "url": "https://shop.hak5.org/", "desc": "Ferramentas de hacking ético"}
            ],
            "Privacidade/Proxy": [
                {"name": "Free Proxy List", "url": "https://free-proxy-list.net/rotating-proxy.html", "desc": "Lista de proxies gratuitos"}
            ],
            "Geradores de Dados": [
                {"name": "Data Fake Generator", "url": "https://datafakegenerator.com/generador.php", "desc": "Gerador de dados falsos"},
                {"name": "Fake Name Generator", "url": "https://www.fakenamegenerator.com", "desc": "Gerador de identidades"},
                {"name": "ElfQrin FakeID", "url": "https://www.elfqrin.com/fakeid.php", "desc": "Gerador de IDs falsos"}
            ]
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="OSINT Links Manager", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Frame esquerdo - Lista de categorias
        left_frame = ttk.LabelFrame(main_frame, text="Categorias", padding="5")
        left_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        
        # Lista de categorias
        self.category_listbox = tk.Listbox(left_frame, width=25)
        self.category_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para categorias
        cat_scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=self.category_listbox.yview)
        cat_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.category_listbox.configure(yscrollcommand=cat_scrollbar.set)
        
        # Frame direito - Links da categoria selecionada
        right_frame = ttk.LabelFrame(main_frame, text="Links OSINT", padding="5")
        right_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        # Treeview para exibir links
        columns = ("Nome", "Descrição", "URL")
        self.links_tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=20)
        
        # Configurar colunas
        self.links_tree.heading("Nome", text="Nome")
        self.links_tree.heading("Descrição", text="Descrição")
        self.links_tree.heading("URL", text="URL")
        
        self.links_tree.column("Nome", width=200)
        self.links_tree.column("Descrição", width=300)
        self.links_tree.column("URL", width=400)
        
        self.links_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para links
        links_scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.links_tree.yview)
        links_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.links_tree.configure(yscrollcommand=links_scrollbar.set)
        
        # Frame inferior - Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))
        
        # Botões
        open_button = ttk.Button(button_frame, text="Abrir Link", command=self.open_selected_link)
        open_button.grid(row=0, column=0, padx=(0, 5))
        
        copy_button = ttk.Button(button_frame, text="Copiar URL", command=self.copy_url)
        copy_button.grid(row=0, column=1, padx=5)
        
        search_button = ttk.Button(button_frame, text="Buscar", command=self.search_links)
        search_button.grid(row=0, column=2, padx=5)
        
        # Campo de busca
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(button_frame, textvariable=self.search_var, width=30)
        search_entry.grid(row=0, column=3, padx=(5, 0))
        search_entry.bind('<Return>', lambda e: self.search_links())
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Pronto")
        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))
        
        # Preencher lista de categorias
        self.populate_categories()
        
        # Bind eventos
        self.category_listbox.bind('<<ListboxSelect>>', self.on_category_select)
        self.links_tree.bind('<Double-1>', self.on_link_double_click)
        
    def populate_categories(self):
        """Preenche a lista de categorias"""
        for category in self.links.keys():
            self.category_listbox.insert(tk.END, category)
            
    def on_category_select(self, event):
        """Evento quando uma categoria é selecionada"""
        selection = event.widget.curselection()
        if selection:
            category = event.widget.get(selection[0])
            self.populate_links(category)
            
    def populate_links(self, category):
        """Preenche a lista de links da categoria selecionada"""
        # Limpar árvore
        for item in self.links_tree.get_children():
            self.links_tree.delete(item)
            
        # Adicionar links da categoria
        if category in self.links:
            for link_data in self.links[category]:
                self.links_tree.insert("", tk.END, values=(
                    link_data["name"],
                    link_data["desc"],
                    link_data["url"]
                ))
                
        self.status_var.set(f"Categoria '{category}' carregada - {len(self.links[category])} links")
        
    def open_selected_link(self):
        """Abre o link selecionado no navegador"""
        selection = self.links_tree.selection()
        if selection:
            item = self.links_tree.item(selection[0])
            url = item['values'][2]
            webbrowser.open(url)
            self.status_var.set(f"Abrindo: {url}")
        else:
            messagebox.showwarning("Aviso", "Selecione um link para abrir")
            
    def on_link_double_click(self, event):
        """Evento de duplo clique em um link"""
        self.open_selected_link()
        
    def copy_url(self):
        """Copia a URL selecionada para a área de transferência"""
        selection = self.links_tree.selection()
        if selection:
            item = self.links_tree.item(selection[0])
            url = item['values'][2]
            self.root.clipboard_clear()
            self.root.clipboard_append(url)
            self.status_var.set(f"URL copiada: {url}")
        else:
            messagebox.showwarning("Aviso", "Selecione um link para copiar")
            
    def search_links(self):
        """Busca links por termo"""
        search_term = self.search_var.get().lower()
        if not search_term:
            messagebox.showinfo("Info", "Digite um termo para buscar")
            return
            
        # Limpar árvore
        for item in self.links_tree.get_children():
            self.links_tree.delete(item)
            
        results_count = 0
        
        # Buscar em todas as categorias
        for category, links in self.links.items():
            for link_data in links:
                if (search_term in link_data["name"].lower() or 
                    search_term in link_data["desc"].lower() or 
                    search_term in link_data["url"].lower()):
                    
                    self.links_tree.insert("", tk.END, values=(
                        f"[{category}] {link_data['name']}",
                        link_data["desc"],
                        link_data["url"]
                    ))
                    results_count += 1
                    
        self.status_var.set(f"Busca por '{search_term}': {results_count} resultados encontrados")
        
    def run(self):
        """Inicia a aplicação"""
        self.root.mainloop()

def main():
    """Função principal"""
    try:
        app = OSINTLinksManager()
        app.run()
    except Exception as e:
        print(f"Erro ao iniciar a aplicação: {e}")

if __name__ == "__main__":
    main()