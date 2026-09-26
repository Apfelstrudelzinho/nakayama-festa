# ============================================================================
# PROJECT:     Nakayama Festa - A Piracy Megathread
# Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
# Description: Compiles markdown documentation into structured JSON database.
# Version:     0.1 (09.2026)
# ============================================================================

import os
import re
import json
import glob
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
PUBLIC_DATA_DIR = os.path.join(DOCS_DIR, "public", "data")
THEME_DATA_DIR = os.path.join(DOCS_DIR, ".vitepress", "theme", "data")

os.makedirs(PUBLIC_DATA_DIR, exist_ok=True)
os.makedirs(THEME_DATA_DIR, exist_ok=True)

CATEGORY_META = {
    "uso-geral": {
        "name": "Uso Geral",
        "icon": "🧭",
        "img": "/img/lain_cables.png",
        "desc": "Buscadores especializados, VPNs sem logs, DNS seguro, navegadores e comunidades.",
        "path": "/uso-geral",
        "color": "#00f076"
    },
    "filmes-series-tv": {
        "name": "Filmes, Séries & TV",
        "icon": "🎦",
        "img": "/img/lain_tvs.png",
        "desc": "Streaming de filmes, séries, transmissões de esportes ao vivo, IPTV, downloads em DDL e torrents.",
        "path": "/filmes-series-tv",
        "color": "#ff3b69"
    },
    "jogos-emulacoes": {
        "name": "Jogos & Emulações",
        "icon": "🎮",
        "img": "/img/lain_bear_suit.png",
        "desc": "Repacks seguros para PC, DDL, patches, emuladores de consoles antigos e modernos e ROMs.",
        "path": "/jogos-emulacoes",
        "color": "#9d4edd"
    },
    "otaku": {
        "name": "Anime & Mangá",
        "icon": "⛩️",
        "img": "/img/lain_resting.png",
        "desc": "Streaming e download de animes, leitores de mangá, light novels e trilhas sonoras.",
        "path": "/otaku",
        "color": "#ff4d6d"
    },
    "livros": {
        "name": "Livros & Quadrinhos",
        "icon": "📚",
        "img": "/img/lain_crow.png",
        "desc": "Bibliotecas digitais, e-books em EPUB/PDF, artigos científicos e HQs traduzidas.",
        "path": "/livros",
        "color": "#f77f00"
    },
    "educacional": {
        "name": "Cursos & Educação",
        "icon": "🧠",
        "img": "/img/lain_school.png",
        "desc": "Plataformas de cursos universitários gratuitos, tutoriais de programação e videoaulas.",
        "path": "/educacional",
        "color": "#2ec4b6"
    },
    "musica": {
        "name": "Música & Áudio",
        "icon": "🎹",
        "img": "/img/lain_music.png",
        "desc": "Streaming de música, downloads FLAC/MP3, ripping de plataformas e audiobooks.",
        "path": "/musica",
        "color": "#1db954"
    },
    "utilitarios": {
        "name": "Utilitários",
        "icon": "🧰",
        "img": "/img/lain_glitch.png",
        "desc": "Softwares, ferramentas web, extensões para navegadores, adblockers e downloaders de mídia.",
        "path": "/utilitarios",
        "color": "#38bdf8"
    },
    "trackers-warez": {
        "name": "Trackers & Warez",
        "icon": "🌊",
        "img": "/img/lain_finger.png",
        "desc": "Trackers BitTorrent públicos e privados, clientes seguros, fóruns e cena warez.",
        "path": "/trackers-warez",
        "color": "#00d2ff"
    },
    "inteligencia-artificial": {
        "name": "Inteligência Artificial",
        "icon": "🤖",
        "img": "/img/lain_server.jpg",
        "desc": "Modelos LLMs locais, geradores de imagem, ferramentas de IA e prompts livres.",
        "path": "/inteligencia-artificial",
        "color": "#8338ec"
    },
    "linux-mac-mobile": {
        "name": "Linux, Mac & Mobile",
        "icon": "🐧",
        "img": "/img/lain_monitors.png",
        "desc": "Programas e ferramentas para Linux, macOS e APKs/lojas para Android e iOS.",
        "path": "/linux-mac-mobile",
        "color": "#06d6a0"
    },
    "adulto": {
        "name": "Adulto (+18)",
        "icon": "🔞",
        "img": "/img/lain_red_matrix.png",
        "desc": "Conteúdo adulto, doujinshi, mangás hentai e plataformas sem censura.",
        "path": "/adulto",
        "color": "#ff3355"
    }
}

CATEGORY_MAP = {
    "filmes-tv": "filmes-series-tv",
    "esportes": "filmes-series-tv",
    "linux-macos": "linux-mac-mobile",
    "mobile": "linux-mac-mobile",
    "jogos": "jogos-emulacoes",
    "emuladores-roms": "jogos-emulacoes",
    "softwares": "utilitarios",
    "ferramentas": "utilitarios",
    "social-media-tools": "utilitarios",
    "trackers": "trackers-warez",
    "warez": "trackers-warez",
    "uso-geral": "uso-geral",
    "privacidade": "uso-geral",
    "sites-geral": "uso-geral"
}

EXCLUDE_DOMAINS = {
    'urlvoid.com', 'virustotal.com', 'reddit.com', 't.me', 
    'github.com/piratarialink', 'twitter.com', 'x.com', 'discord.gg', 'discord.com'
}

def clean_url(url: str) -> str:
    return url.strip().rstrip(').,;')

def detect_tags(name: str, desc: str, section: str) -> list:
    combined = f"{name} {desc} {section}".lower()
    tags = []
    
    if any(k in combined for k in ['ddl', 'download direto', 'mega', 'gdrive', '1fichier', 'mediafire']):
        tags.append('DDL')
    if any(k in combined for k in ['torrent', 'magnet', 'tracker', 'p2p', 'seedbox']):
        tags.append('Torrent')
    if any(k in combined for k in ['streaming', 'assistir online', 'player', 'transmissão', 'ao vivo', 'iptv']):
        tags.append('Streaming')
    if any(k in combined for k in ['manga', 'mangá', 'leitor', 'scan', 'webtoon', 'hq']):
        tags.append('Mangá')
    if any(k in combined for k in ['repack', 'fitgirl', 'dodi', 'pré-instalado', 'pre-installed']):
        tags.append('Repack')
    if any(k in combined for k in ['rom', 'iso', 'emulador', 'bios']):
        tags.append('ROMs')
    if any(k in combined for k in ['curso', 'aula', 'livro', 'pdf', 'epub', 'acadêmico']):
        tags.append('Educativo')
    if any(k in combined for k in ['sem anúncio', 'no ads', 'sem ads', 'limpo']):
        tags.append('Sem Anúncios')
    if any(k in combined for k in ['open source', 'código aberto', 'github.com', 'gitlab.com']):
        tags.append('Open Source')
    if any(k in combined for k in ['1080p', '4k', 'hd', 'qualidade']):
        tags.append('1080p')
        
    return tags[:3]

def parse_markdown_files():
    items = []
    seen_urls = set()
    
    src_dir = os.path.join(BASE_DIR, "backup", "sources_markdown")
    if not os.path.exists(src_dir):
        src_dir = os.path.join(BASE_DIR, "sources", "markdown_backup")
    if not os.path.exists(src_dir):
        src_dir = DOCS_DIR
        
    md_files = glob.glob(os.path.join(src_dir, "*.md"))
    
    for md_file in sorted(md_files):
        basename = os.path.basename(md_file)
        if basename in ['index.md', 'inicio.md', 'publicacoes.md', 'sites-inseguros.md', 'FONTES_INACESSIVEIS.md', 'PROJETO_MEGATHREAD.md', 'README.md', 'README2.md', 'guias.md', 'sobre.md']:
            continue
        raw_cat = basename.replace('.md', '')
        mapped_cat = CATEGORY_MAP.get(raw_cat, raw_cat)
        
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        current_section = ''
        i = 0
        while i < len(lines):
            line = lines[i]
            
            if line.startswith('## '):
                current_section = line.strip('# \t\r\n')
                i += 1
                continue
                
            m_h3 = re.search(r'###\s+(🌟\s*)?\[([^\]]+)\]\((https?://[^\)]+)\)', line)
            if m_h3:
                star = bool(m_h3.group(1))
                name = m_h3.group(2).strip().replace('🌟', '').strip()
                url = clean_url(m_h3.group(3))
                domain = urlparse(url).netloc.lower().replace('www.', '')
                
                desc_parts = []
                i += 1
                while i < len(lines) and lines[i].strip().startswith('-'):
                    bullet = lines[i].strip('- \t\r\n')
                    if not any(ex in bullet for ex in ['Resultados de segurança', 'urlvoid.com', 'virustotal.com']):
                        desc_parts.append(bullet)
                    i += 1
                    
                desc = ' '.join(desc_parts[:2]).strip()
                if url not in seen_urls and domain and not any(ed in domain for ed in EXCLUDE_DOMAINS):
                    seen_urls.add(url)
                    tags = detect_tags(name, desc, current_section)
                    items.append({
                        'id': f"item-{len(items)+1}",
                        'name': name,
                        'url': url,
                        'domain': domain,
                        'category': mapped_cat,
                        'section': current_section,
                        'lang': 'PT-BR',
                        'desc': desc if desc else f'Recurso listado na seção {current_section or mapped_cat}.',
                        'warning': '',
                        'tags': tags,
                        'recommended': star
                    })
                continue
                
            m_tag = re.search(r'-\s*(?:\[(PT-BR|EN|GLOBAL|ES|RU|RAW)\])?\s*\[([^\]]+)\]\((https?://[^\)]+)\)\s*(?:—|-|:|\s{2,})\s*(.*)', line)
            if m_tag:
                tag = m_tag.group(1) or 'GLOBAL'
                name = m_tag.group(2).strip().replace('🌟', '').strip()
                url = clean_url(m_tag.group(3))
                domain = urlparse(url).netloc.lower().replace('www.', '')
                desc = m_tag.group(4).strip()
                
                warning = ''
                if i + 1 < len(lines) and lines[i+1].strip().startswith('>'):
                    warning = lines[i+1].strip('> \t\r\n')
                    i += 1
                    
                if url not in seen_urls and domain and not any(ed in domain for ed in EXCLUDE_DOMAINS):
                    seen_urls.add(url)
                    tags = detect_tags(name, desc, current_section)
                    items.append({
                        'id': f"item-{len(items)+1}",
                        'name': name,
                        'url': url,
                        'domain': domain,
                        'category': mapped_cat,
                        'section': current_section,
                        'lang': tag,
                        'desc': desc if desc else f'Recurso curado em {current_section or mapped_cat}.',
                        'warning': warning,
                        'tags': tags,
                        'recommended': '🌟' in line or 'recomendado' in desc.lower()
                    })
                i += 1
                continue
                
            m_bullet = re.search(r'-\s+\[([^\]]+)\]\((https?://[^\)]+)\)(?:\s*(?:—|-|:)\s*(.*))?', line)
            if m_bullet:
                name = m_bullet.group(1).strip().replace('🌟', '').strip()
                url = clean_url(m_bullet.group(2))
                domain = urlparse(url).netloc.lower().replace('www.', '')
                desc = (m_bullet.group(3) or '').strip()
                
                if url not in seen_urls and domain and not any(ed in domain for ed in EXCLUDE_DOMAINS) and 'Resultados de segurança' not in name:
                    seen_urls.add(url)
                    is_pt = any(w in desc.lower() for w in ['dublado', 'legendado', 'em português', 'pt-br', 'nacional', 'brasileiro'])
                    tags = detect_tags(name, desc, current_section)
                    items.append({
                        'id': f"item-{len(items)+1}",
                        'name': name,
                        'url': url,
                        'domain': domain,
                        'category': mapped_cat,
                        'section': current_section,
                        'lang': 'PT-BR' if is_pt else 'GLOBAL',
                        'desc': desc if desc else f'Disponível na categoria {current_section or mapped_cat}.',
                        'warning': '',
                        'tags': tags,
                        'recommended': False
                    })
            i += 1
            
    database = {
        "categories": CATEGORY_META,
        "total": len(items),
        "items": items
    }
    
    out_public = os.path.join(PUBLIC_DATA_DIR, "links.json")
    out_theme = os.path.join(THEME_DATA_DIR, "links.json")
    
    with open(out_public, 'w', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=2)
        
    with open(out_theme, 'w', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=2)
        
    print(f"Compiled database with {len(items)} items across {len(CATEGORY_META)} categories.")

if __name__ == "__main__":
    parse_markdown_files()
