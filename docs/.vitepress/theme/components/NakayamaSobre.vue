<script setup>
// ============================================================================
// PROJECT:     Nakayama Festa - A Piracy Megathread
// Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
// Description: About page showcasing the manifesto, community sources, and rules.
// Version:     0.1 (09.2026)
// ============================================================================

import './nakayama-shared.css'

const sourcesList = [
  {
    category: "Comunidades e Megathreads Globais",
    items: [
      { name: "FMHY (FreeMediaHeckYeah)", url: "https://fmhy.net/", desc: "O maior acervo de mídia e ferramentas gratuitas da internet mundial." },
      { name: "r/Piracy Megathread", url: "https://www.reddit.com/r/Piracy/wiki/megathread", desc: "A compilação oficial da maior comunidade sobre pirataria do Reddit." },
      { name: "r/FREEMEDIAHECKYEAH Wiki", url: "https://www.reddit.com/r/FREEMEDIAHECKYEAH/wiki/index/", desc: "A base de conhecimento e índice dinâmico do FMHY." },
      { name: "Privateers Club Wiki", url: "https://github.com/privateersclub/wiki", desc: "Índice e documentação colaborativa sobre preservação digital." },
      { name: "MediaSavvy", url: "https://github.com/MediaSavvy/MediaSavvy", desc: "Guia prático sobre streaming, consumo de mídia e ferramentas digitais." },
      { name: "Piracy Vercel / GitLab", url: "https://gitlab.com/piracy/piracy", desc: "Repositório de links e guias da comunidade internacional." },
      { name: "dbzer0 Piracy Wiki", url: "https://wiki.dbzer0.com/piracy", desc: "Guia de recursos e descentralização hospedado na rede federada." },
      { name: "Rentry Megathread", url: "https://rentry.co/megathread", desc: "Megathread colaborativa mantida em Markdown no Rentry." },
      { name: "Mega-Rentry", url: "https://rentry.co/Mega-Rentry", desc: "Catálogo extenso de links de streaming, DDL e utilitários." },
      { name: "Sajay Prakash Megathread", url: "https://github.com/sajayprakash/megathread", desc: "Megathread open-source voltada para desenvolvedores e entusiastas de mídia." }
    ]
  },
  {
    category: "Jogos, Emulação e Preservação",
    items: [
      { name: "r/ROMs Megathread", url: "https://r-roms.github.io/", desc: "O maior índice de preservação de ROMs, ISOs e jogos retrô do mundo." },
      { name: "Pirated Games Megathread (r/PiratedGames)", url: "https://rentry.org/pgames", desc: "Referência mundial para segurança, downloads e repacks de jogos para PC." },
      { name: "Champagne Piracy Wiki", url: "https://github.com/champagnewiki/champagne-wiki", desc: "Wiki focada em gaming, segurança e ativadores." },
      { name: "Ripped.guide", url: "https://github.com/rippedpiracy/docs", desc: "Guia estruturado de fontes de áudio, jogos, emulação e cena warez." }
    ]
  },
  {
    category: "Anime, Mangá e Cultura Asiática (Otaku)",
    items: [
      { name: "Wotaku Wiki", url: "https://wotaku.wiki/", desc: "A wiki mais detalhada sobre cultura otaku, fansubs, scanlations e J-Music." },
      { name: "The Index (theindex.moe)", url: "https://theindex.moe/", desc: "Diretório minimalista e curado focado em anime, light novels e visual novels." },
      { name: "The Wiki Moe", url: "https://thewiki.moe/", desc: "Guias avançados de reprodução de mídia (mpv, encoders e qualidade de vídeo)." },
      { name: "Everything Moe", url: "https://everythingmoe.com/", desc: "Tabela comparativa e agregador de plataformas de streaming e leitura." },
      { name: "DuckWeeb", url: "https://rentry.co/duckweeb", desc: "Guia concentrado em recursos e ferramentas para a comunidade weeb." }
    ]
  },
  {
    category: "Livros, Cursos e Recursos Acadêmicos",
    items: [
      { name: "Library Genesis (LibGen Help)", url: "https://www.libgen.help/", desc: "Guia e espelhos para busca de artigos científicos e livros acadêmicos." },
      { name: "Course Piracy Index", url: "https://github.com/ItIsMeCall911/Course-Piracy-Index", desc: "Índice especializado em plataformas de cursos online e videoaulas gratuitas." }
    ]
  },
  {
    category: "Repositórios e Curadorias Especializadas",
    items: [
      { name: "Awesome Piracy (Igglybuff)", url: "https://github.com/Igglybuff/awesome-piracy", desc: "A lista clássica de recursos que serviu de fundação para a documentação moderna." },
      { name: "Awesome Piracy (Shakil Shahadat)", url: "https://github.com/Shakil-Shahadat/awesome-piracy", desc: "Lista de referências curadas sobre segurança, privacidade e pirataria ética." },
      { name: "Awesome GTK", url: "https://github.com/valpackett/awesome-gtk", desc: "Coletânea de softwares, bibliotecas e utilitários para Linux e interfaces GTK." },
      { name: "Indian Piracy Index", url: "https://github.com/anymeofu/Indian-Piracy-Index", desc: "Índice internacional de recursos com ênfase em conteúdo asiático e alternativo." },
      { name: "Ori5000 Guide", url: "https://github.com/Ori5000/ori5000.github.io", desc: "Guia prático de ativação, utilitários e ripping de áudio." },
      { name: "FilterStalker", url: "https://rentry.co/FilterStalker", desc: "Guias e filtros para bloqueadores de anúncios e burladores de encurtadores." },
      { name: "DuckLink", url: "https://rentry.co/ducklink", desc: "Compilação independente de ferramentas e sites úteis." },
      { name: "Software Pirates Megathread", url: "https://rentry.co/SoftwarePirates-Megathread", desc: "Relação curada de softwares para produtividade, design e edição." },
      { name: "WikiWiki Rentry", url: "https://rentry.co/wikiwiki", desc: "Compilado de listas e links para download direto." },
      { name: "Cool Stuff I Found On The Internet", url: "https://rentry.co/cool-stuff-i-found-on-the-internet", desc: "Recursos e utilitários da web aberta." },
      { name: "Watch Free Movies and Series", url: "https://watchfreemoviesandseries.com/", desc: "Agregador de fontes de streaming para cinema e televisão." },
      { name: "Vidpop List", url: "https://list.vidpop.xyz/", desc: "Curadoria de indexadores de vídeo e reprodutores web." },
      { name: "CryptPad & Comunidade Aberta", url: "https://cryptpad.fr/", desc: "Notas e planilhas colaborativas mantidas por entusiastas da preservação." },
      { name: "Pirataria BR Comunitária", url: "https://pirataria.link/", desc: "Catálogo comunitário de links e fontes em português." }
    ]
  }
]
</script>

<template>
  <div class="theindex-root theindex-subpage">
    <!-- Navbar -->
    <header class="theindex-navbar">
      <div class="nav-container">
        <div class="nav-left">
          <a href="/" class="nav-brand">
            <span class="brand-icon">🏴‍☠️</span>
            <span class="brand-title">Megathread</span>
          </a>

          <nav class="nav-links">
            <a href="/" class="nav-link">Bibliotecas</a>
            <a href="/guias" class="nav-link">Guias</a>
            <a href="/privacidade" class="nav-link">Privacidade</a>
            <a href="/sobre" class="nav-link active">Sobre</a>
          </nav>
        </div>

        <div class="nav-right">
          <a
            href="https://github.com/Apfelstrudelzinho/nakayama-festa"
            target="_blank"
            rel="noopener noreferrer"
            class="nav-github-btn"
          >
            <svg viewBox="0 0 16 16" width="15" height="15" fill="currentColor">
              <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
            </svg>
            GitHub
          </a>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="theindex-main">
      <!-- Breadcrumb -->
      <div class="breadcrumb-bar" style="margin-bottom: 1.5rem;">
        <a href="/" class="back-link">
          <svg viewBox="0 0 448 512" width="13" height="13" fill="currentColor">
            <path d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z"/>
          </svg>
          Voltar ao Início
        </a>
      </div>

      <!-- Hero Header -->
      <section class="about-hero">
        <span class="hero-badge">INICIATIVA COMUNITÁRIA & OPEN SOURCE</span>
        <h1 class="about-title">Sobre a <span class="highlight-title">Megathread</span></h1>
        <p class="about-subtitle">
          Um índice unificado, aberto e ético dedicado a organizar e facilitar o acesso ao conhecimento, entretenimento e ferramentas livres na internet.
        </p>
      </section>

      <!-- Pillars Section -->
      <section class="pillars-grid">
        <div class="pillar-card">
          <div class="pillar-icon">🏛️</div>
          <h3 class="pillar-title">Preservação Digital</h3>
          <p class="pillar-text">
            A web perde milhares de páginas, jogos retrô e documentos anualmente. Agregamos acervos dedicados a preservar o patrimônio cultural digital.
          </p>
        </div>

        <div class="pillar-card">
          <div class="pillar-icon">🇧🇷</div>
          <h3 class="pillar-title">Foco no Brasil & Lusofonia</h3>
          <p class="pillar-text">
            Curadoria adaptada para falantes de português, destacando fontes com legendas, dublagens em PT-BR e mirrors de alta velocidade para a América Latina.
          </p>
        </div>

        <div class="pillar-card">
          <div class="pillar-icon">🛡️</div>
          <h3 class="pillar-title">Segurança & Ética</h3>
          <p class="pillar-text">
            Filtramos ativamente sites com malwares, mineradores ou golpes. Recomendamos as melhores práticas de OpSec, bloqueio de anúncios e VPNs no-logs.
          </p>
        </div>

        <div class="pillar-card">
          <div class="pillar-icon">✨</div>
          <h3 class="pillar-title">100% Livre & Sem Anúncios</h3>
          <p class="pillar-text">
            Sem fins lucrativos, sem rastreadores e sem anúncios. Nosso código-fonte e base de dados são abertos para inspeção no GitHub.
          </p>
        </div>
      </section>

      <!-- 35 Sources Section -->
      <section class="sources-section">
        <div class="section-header">
          <h2 class="section-title">
            Compilação Baseada em <span class="highlight-title">35+ Fontes Globais</span>
          </h2>
          <span class="section-hint">Índices, comunidades e repositórios cruzados e organizados</span>
        </div>

        <div class="sources-categories-wrap">
          <div v-for="cat in sourcesList" :key="cat.category" class="source-cat-block">
            <h3 class="source-cat-title">{{ cat.category }}</h3>
            <div class="source-items-grid">
              <a
                v-for="src in cat.items"
                :key="src.name"
                :href="src.url"
                target="_blank"
                rel="noopener noreferrer"
                class="source-card"
              >
                <div class="source-card-header">
                  <span class="source-name">{{ src.name }}</span>
                  <span class="source-link-icon">↗</span>
                </div>
                <p class="source-desc">{{ src.desc }}</p>
              </a>
            </div>
          </div>
        </div>
      </section>

      <!-- Legal Disclaimer -->
      <section class="disclaimer-card">
        <div class="disclaimer-header">
          <span class="disclaimer-icon">⚖️</span>
          <h3 class="disclaimer-title">Isenção de Responsabilidade Legal (Disclaimer)</h3>
        </div>
        <p class="disclaimer-text">
          A <strong>Megathread</strong> opera estritamente como um <strong>catálogo de hiperlinks público e informativo</strong>. Nenhum arquivo de áudio, vídeo, software ou material protegido está hospedado nos servidores deste projeto. Todos os links direcionam para domínios públicos de terceiros administrados de forma independente. O cumprimento das legislações vigentes em sua jurisdição é de responsabilidade individual de cada usuário.
        </p>
      </section>

      <!-- How to Contribute -->
      <section class="contribute-card">
        <h3 class="contribute-title">🤝 Como Contribuir</h3>
        <p class="contribute-text">
          A Megathread é construída coletivamente. Se encontrou um link offline, uma nova ferramenta indispensável ou deseja sugerir melhorias de tradução, seu feedback é fundamental.
        </p>
        <div class="contribute-actions">
          <a
            href="https://github.com/Apfelstrudelzinho/nakayama-festa/issues"
            target="_blank"
            rel="noopener noreferrer"
            class="btn-contribute"
          >
            Abrir uma Issue no GitHub
          </a>
          <a
            href="https://github.com/Apfelstrudelzinho/nakayama-festa/pulls"
            target="_blank"
            rel="noopener noreferrer"
            class="btn-contribute secondary"
          >
            Enviar um Pull Request
          </a>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="theindex-footer">
      <div class="footer-inner">
        <p><strong>Megathread</strong> — Compilação colaborativa de fontes abertas da internet brasileira.</p>
        <p>Inspirado no TheIndex.moe & EverythingMoe • Licenciado sob CC0 1.0 Universal (Domínio Público) • 100% de código aberto</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
@import './nakayama-shared.css';

.about-hero {
  text-align: center;
  padding: 3rem 1rem 2rem;
  margin-bottom: 2rem;
  background: radial-gradient(circle at 50% 0%, rgba(0, 240, 118, 0.08) 0%, rgba(0, 210, 255, 0.03) 45%, transparent 70%);
}

.hero-badge {
  display: inline-block;
  background-color: var(--bg-2);
  border: 1px solid rgba(0, 240, 118, 0.35);
  color: var(--accent-color);
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 0.25rem 0.75rem;
  border-radius: 999px;
  margin-bottom: 1rem;
  box-shadow: 0 0 10px rgba(0, 240, 118, 0.15);
}

.about-title {
  font-family: var(--font-mono);
  font-size: 2.5rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 0.75rem;
  letter-spacing: -0.02em;
  text-shadow: 0 0 14px rgba(0, 240, 118, 0.25);
}

.about-subtitle {
  font-size: 1.05rem;
  color: #94a3b8;
  max-width: 650px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Pillars */
.pillars-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.25rem;
  margin-bottom: 3.5rem;
}

.pillar-card {
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-radius: 8px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.pillar-card:hover {
  border-color: var(--accent-color);
  box-shadow: 0 0 12px rgba(0, 240, 118, 0.12);
}

.pillar-icon {
  font-size: 2rem;
  margin-bottom: 0.75rem;
}

.pillar-title {
  font-family: var(--font-mono);
  font-size: 1.1rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 0.5rem;
}

.pillar-text {
  font-size: 0.85rem;
  color: #94a3b8;
  line-height: 1.5;
  margin: 0;
}

/* Sources */
.sources-section {
  margin-bottom: 3.5rem;
}

.source-cat-block {
  margin-bottom: 2rem;
}

.source-cat-title {
  font-family: var(--font-mono);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--accent-color);
  text-shadow: 0 0 8px var(--accent-glow);
  margin-bottom: 1rem;
  padding-bottom: 0.35rem;
  border-bottom: 1px solid var(--bg-3);
}

.source-items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  gap: 0.85rem;
}

.source-card {
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-radius: 6px;
  padding: 1rem;
  text-decoration: none;
  color: inherit;
  transition: all 0.15s ease;
  display: flex;
  flex-direction: column;
}

.source-card:hover {
  background-color: var(--bg-3);
  border-color: var(--accent-color);
  box-shadow: 0 0 10px rgba(0, 240, 118, 0.15);
  transform: translateY(-2px);
}

.source-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.4rem;
}

.source-name {
  font-family: var(--font-mono);
  font-weight: 700;
  color: #fff;
  font-size: 0.95rem;
}

.source-link-icon {
  color: #666;
  font-size: 0.9rem;
}

.source-desc {
  font-size: 0.8rem;
  color: #888;
  margin: 0;
  line-height: 1.4;
}

/* Disclaimer */
.disclaimer-card {
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-left: 4px solid #ffbe0b;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 2.5rem;
}

.disclaimer-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.disclaimer-icon {
  font-size: 1.3rem;
}

.disclaimer-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #fff;
  margin: 0;
}

.disclaimer-text {
  font-size: 0.85rem;
  color: #aaa;
  line-height: 1.6;
  margin: 0;
}

/* Contribute */
.contribute-card {
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-radius: 8px;
  padding: 1.75rem;
  text-align: center;
}

.contribute-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #fff;
  margin: 0 0 0.5rem;
}

.contribute-text {
  font-size: 0.9rem;
  color: #999;
  max-width: 600px;
  margin: 0 auto 1.25rem;
  line-height: 1.5;
}

.contribute-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-contribute {
  background-color: var(--accent-color);
  color: #fff;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.88rem;
  padding: 0.5rem 1.25rem;
  border-radius: 6px;
  transition: all 0.15s ease;
}

.btn-contribute:hover {
  filter: brightness(1.1);
  box-shadow: 0 0 10px var(--accent-glow);
}

.btn-contribute.secondary {
  background-color: var(--bg-3);
  border: 1px solid var(--bg-5);
  color: #ddd;
}

.btn-contribute.secondary:hover {
  background-color: var(--bg-4);
  color: #fff;
}
</style>
