<script setup>
// ============================================================================
// PROJECT:     Nakayama Festa - A Piracy Megathread
// Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
// Description: Guides and tutorials directory page with search and category filter.
// Version:     0.1 (09.2026)
// ============================================================================

import { ref, computed } from 'vue'

const guidesList = [
  {
    id: "autobrr",
    title: "Aumente seu ratio com Autobrr",
    url: "/guias/autobrr",
    category: "Torrents",
    icon: "⚡",
    tags: ["Torrents", "Automação", "IRC", "Trackers"],
    desc: "Aprenda a utilizar o Autobrr para monitorar e baixar automaticamente novos torrents anunciados no IRC, maximizando seu upload e ratio em trackers privados."
  },
  {
    id: "burlando-mega",
    title: "Burlando o limite de download do Mega",
    url: "/guias/burlando-limite-mega",
    category: "Download",
    icon: "📦",
    tags: ["DDL", "Mega", "Proxy", "Bypass"],
    desc: "Técnicas e ferramentas simples para contornar a cota de transferência imposta pelo Mega, utilizando proxies e gerenciadores de download."
  },
  {
    id: "ativacao-windows-office",
    title: "Download e Ativação do Windows e Office",
    url: "/guias/ativacao-office-win",
    category: "Softwares",
    icon: "🪟",
    tags: ["Windows", "Office", "MAS", "Open Source"],
    desc: "Guia prático e 100% seguro utilizando o Microsoft Activation Scripts (MAS), a ferramenta de código aberto mais recomendada pela comunidade."
  },
  {
    id: "dns-windows-android",
    title: "Como configurar DNS no Windows e Android",
    url: "/guias/dns",
    category: "Segurança",
    icon: "🔒",
    tags: ["DNS", "Privacidade", "Desbloqueio", "DoH"],
    desc: "Passo a passo para trocar seu DNS por alternativas seguras e criptografadas (como Cloudflare, NextDNS ou AdGuard), contornando bloqueios de operadoras."
  },
  {
    id: "guia-stremio",
    title: "Guia completo de como usar o Stremio",
    url: "/guias/guia-stremio",
    category: "Streaming",
    icon: "🎬",
    tags: ["Streaming", "Stremio", "Torrentio", "Debrid"],
    desc: "Aprenda a configurar o Stremio com os melhores complementos (add-ons) da comunidade para assistir a filmes e séries com legendas e máxima qualidade."
  },
  {
    id: "plugins-qbittorrent",
    title: "Instalar plugins de pesquisa no qBitTorrent",
    url: "/guias/guia-plugins-qbittorrent",
    category: "Torrents",
    icon: "🧲",
    tags: ["qBitTorrent", "Busca", "Plugins", "Trackers"],
    desc: "Transforme o qBitTorrent em um motor de busca unificado para encontrar arquivos em dezenas de trackers sem precisar abrir o navegador."
  },
  {
    id: "sonarr-radarr-plex",
    title: "Streaming Doméstico Automatizado (Sonarr, Radarr e Plex)",
    url: "/guias/sonarr-radarr-plex",
    category: "Streaming",
    icon: "🍿",
    tags: ["Arr Stack", "Plex", "Automação", "Home Server"],
    desc: "Guia definitivo para montar sua própria 'Netflix caseira', automatizando o download, organização e reprodução de filmes e séries na sua TV."
  },
  {
    id: "jellyfin-arr",
    title: "Jellyfin e Família Arr via Docker Compose",
    url: "/guias/jellyfin-arr",
    category: "Streaming",
    icon: "🐳",
    tags: ["Docker", "Jellyfin", "Linux", "Open Source"],
    desc: "Suba seu servidor multimídia 100% livre e de código aberto usando contêineres Docker de forma rápida e reprodutível."
  },
  {
    id: "oracle-vps",
    title: "Criando uma VPS gratuita com 24GB de RAM na Oracle",
    url: "/guias/oracle",
    category: "Servidores",
    icon: "☁️",
    tags: ["VPS", "Oracle Cloud", "Free Tier", "Servidor"],
    desc: "Como solicitar e configurar uma instância ARM de 4 núcleos e 24GB de RAM vitalícia e totalmente gratuita no Oracle Cloud Always Free."
  },
  {
    id: "virustotal",
    title: "Como verificar um arquivo no VirusTotal corretamente",
    url: "/guias/virustotal",
    category: "Segurança",
    icon: "🛡️",
    tags: ["Segurança", "Falso Positivo", "Malware", "Análise"],
    desc: "Entenda o que são falsos positivos comuns em cracks e ativadores, e como analisar relatórios de antivírus com inteligência."
  },
  {
    id: "antivirus",
    title: "Os piores e 'menos piores' antivírus",
    url: "/guias/antivirus",
    category: "Segurança",
    icon: "☣️",
    tags: ["Antivírus", "Windows Defender", "Segurança"],
    desc: "Uma análise realista sobre a indústria de antivírus e por que o Windows Defender bem configurado costuma ser a melhor opção para a maioria."
  },
  {
    id: "archive-org-bypass",
    title: "Burlar restrição de download do Archive.org",
    url: "/guias/como-burlar-restricao-de-download-archive-org",
    category: "Download",
    icon: "📚",
    tags: ["Archive.org", "Livros", "PDF", "EPUB"],
    desc: "Como baixar livros protegidos pelo sistema de empréstimo de 1 hora do Internet Archive em formatos legíveis PDF ou EPUB."
  },
  {
    id: "cgnat-portas",
    title: "Como abrir portas no roteador em rede CGNAT",
    url: "/guias/cgnat-portas",
    category: "Servidores",
    icon: "🌐",
    tags: ["Redes", "CGNAT", "Portas", "Roteador"],
    desc: "Soluções práticas para quem quer hospedar servidores ou melhorar a conectividade P2P mesmo estando preso atrás do CGNAT da operadora."
  },
  {
    id: "guia-xdcc",
    title: "Como baixar arquivos de bots IRC/XDCC",
    url: "/guias/guia-xdcc",
    category: "Download",
    icon: "💬",
    tags: ["IRC", "XDCC", "Fservers", "Animes"],
    desc: "Descubra a camada clássica de downloads diretos de alta velocidade via IRC, amplamente utilizada por grupos de fansub de anime."
  },
  {
    id: "guia-fitgirl",
    title: "Guia completo de instalação de repacks FitGirl",
    url: "/guias/guia-fitgirl",
    category: "Jogos",
    icon: "🎮",
    tags: ["FitGirl", "Repacks", "Jogos", "Instalação"],
    desc: "Como baixar, verificar a integridade dos binários e instalar jogos altamente compactados sem erros de memória ou corrupção."
  },
  {
    id: "hakuneko-kcc",
    title: "Converter Mangás para Kindle com HakuNeko e KCC",
    url: "/guias/guia-hakuneko",
    category: "Download",
    icon: "📖",
    tags: ["Kindle", "Mangás", "HakuNeko", "KCC"],
    desc: "Fluxo passo a passo para baixar capítulos inteiros de mangás e otimizar para leitura perfeita no e-reader da Amazon."
  },
  {
    id: "twitch-ads",
    title: "Como bloquear anúncios na Twitch",
    url: "/guias/twitch",
    category: "Download",
    icon: "🟣",
    tags: ["Twitch", "Adblock", "Scripts", "Extensões"],
    desc: "Extensões e scripts atualizados para contornar os anúncios server-side inseridos nas transmissões da Twitch."
  },
  {
    id: "ratio-melhor",
    title: "Um guia simples para um ratio melhor",
    url: "/guias/ratio-melhor",
    category: "Torrents",
    icon: "📈",
    tags: ["Trackers Privados", "Ratio", "Seed", "Dicas"],
    desc: "Boas práticas, configuração de clientes e estratégias de 'freeleech' para nunca mais ter a conta banida por ratio baixo."
  },
  {
    id: "quero-privacidade",
    title: "Guia de Privacidade para Paranoicos",
    url: "/guias/quero-privacidade",
    category: "Segurança",
    icon: "🕵️",
    tags: ["Privacidade", "Anonimato", "OpSec", "Linux"],
    desc: "Passos avançados para minimizar seu rastro digital, desde sistemas operacionais isolados até ferramentas de comunicação segura."
  },
  {
    id: "lancamentos-predbs",
    title: "Verificando lançamentos de jogos usando PreDBs",
    url: "/guias/lancamentos-predbs",
    category: "Jogos",
    icon: "🕹️",
    tags: ["PreDB", "Scene", "Warez", "Verificação"],
    desc: "Aprenda a consultar bases de dados pré-distribuição para checar se um jogo ou atualização já foi oficialmente lançado pela Scene."
  },
  {
    id: "formas-consumo-filmes",
    title: "Diferentes maneiras de consumir filmes e séries",
    url: "/guias/guia-murilouco",
    category: "Streaming",
    icon: "📺",
    tags: ["Streaming", "IPTV", "Qualidade", "Análise"],
    desc: "Panorama comparativo detalhado sobre sites de streaming gratuitos, IPTVs, Debrid, DDL e torrents, analisando prós e contras de cada método."
  }
]

const searchQuery = ref('')
const selectedCategory = ref('todos')

const categoriesList = ['todos', 'Torrents', 'Streaming', 'Download', 'Segurança', 'Softwares', 'Jogos', 'Servidores']

const filteredGuides = computed(() => {
  const q = searchQuery.value.toLowerCase().trim()
  return guidesList.filter(g => {
    if (selectedCategory.value !== 'todos' && g.category !== selectedCategory.value) {
      return false
    }
    if (q) {
      return g.title.toLowerCase().includes(q) || 
             g.desc.toLowerCase().includes(q) || 
             g.tags.some(t => t.toLowerCase().includes(q))
    }
    return true
  })
})
</script>

<template>
  <div class="theindex-root theindex-subpage">
    <!-- Navbar TheIndex -->
    <header class="theindex-navbar">
      <div class="nav-container">
        <div class="nav-left">
          <a href="/" class="nav-brand">
            <span class="brand-icon">🏴‍☠️</span>
            <span class="brand-title">Megathread</span>
          </a>
          <nav class="nav-links">
            <a href="/" class="nav-link">Bibliotecas</a>
            <a href="/guias" class="nav-link active">Guias</a>
            <a href="/privacidade" class="nav-link">Privacidade</a>
            <a href="/sobre" class="nav-link">Sobre</a>
          </nav>
        </div>
        <div class="nav-right">
          <a href="https://github.com/Apfelstrudelzinho/nakayama-festa" target="_blank" class="nav-github-btn">
            GitHub
          </a>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="theindex-main">
      <section class="section-container">
        <div class="section-header">
          <h2 class="section-title">
            Coleção de <span class="highlight-title">Guias e Tutoriais</span>
          </h2>
          <span class="section-hint">{{ filteredGuides.length }} tutoriais práticos verificados</span>
        </div>

        <!-- Law Box Callout (TheIndex style matching Privacidade) -->
        <div class="law-callout-box">
          <div class="callout-header">
            <span class="callout-icon">💡</span>
            <strong>Guias e Tutoriais Recomendados pela Comunidade</strong>
          </div>
          <p class="callout-text">
            Tutoriais passo a passo sobre automação de torrents, streaming doméstico (Stremio, Jellyfin, Plex), bloqueio de anúncios e ativação de sistemas. Todos os métodos foram testados e utilizam ferramentas de código aberto e seguras.
          </p>
        </div>

        <!-- Search Bar -->
        <div class="theindex-search-row">
          <div class="search-field-wrap">
            <svg class="search-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
              <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
            </svg>
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Pesquisar guias por título, ferramenta (ex: stremio, autobrr, dns, vps)..."
              class="theindex-search-input"
            />
            <button v-if="searchQuery" @click="searchQuery = ''" class="search-clear-x">×</button>
          </div>
        </div>

        <!-- Filter Tags -->
        <div class="theindex-tags-bar">
          <button
            v-for="cat in categoriesList"
            :key="cat"
            @click="selectedCategory = cat"
            :class="['tag-chip', { active: selectedCategory === cat }]"
          >
            {{ cat === 'todos' ? 'Todos os Guias' : cat }}
          </button>
        </div>

        <!-- Cards Grid (Exact same layout & classes as Privacidade) -->
        <div class="theindex-cards-grid">
          <div
            v-for="guide in filteredGuides"
            :key="guide.id"
            class="theindex-item-card"
          >
            <div class="item-card-inner">
              <div class="item-header-row">
                <span class="online-ping-dot" title="Tutorial verificado"></span>
                <span style="font-size: 1.15rem; margin-right: 0.15rem;">{{ guide.icon }}</span>
                <a :href="guide.url" class="item-title-link">
                  {{ guide.title }}
                </a>
                <div class="item-actions">
                  <a :href="guide.url" class="item-action-icon" title="Ler guia completo">
                    ➔
                  </a>
                </div>
              </div>

              <span class="item-domain-text">{{ guide.category }}</span>

              <p class="item-description-text">
                {{ guide.desc }}
              </p>

              <!-- Tags -->
              <div class="item-badges-list">
                <span class="theindex-badge badge-category">
                  {{ guide.category }}
                </span>
                <span v-for="tag in guide.tags" :key="tag" class="theindex-badge badge-tag">
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="theindex-footer">
      <div class="footer-inner">
        <p><strong>Megathread</strong> — Guias e Tutoriais práticos em Português.</p>
        <p>Inspirado no TheIndex.moe & EverythingMoe • Sem fins lucrativos • 100% de código aberto</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
@import './nakayama-shared.css';

.law-callout-box {
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-left: 4px solid var(--accent-color);
  border-radius: 6px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 0 15px rgba(0, 240, 118, 0.08);
}

.callout-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #fff;
  font-family: var(--font-mono);
  font-size: 0.95rem;
  margin-bottom: 0.4rem;
}

.callout-text {
  color: #94a3b8;
  font-size: 0.85rem;
  line-height: 1.55;
  margin: 0;
}
</style>
