<script setup>
// ============================================================================
// PROJECT:     Nakayama Festa - A Piracy Megathread
// Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
// Description: Main portal view displaying library categories and global export.
// Version:     0.1 (09.2026)
// ============================================================================

import { ref, computed, onMounted, onUnmounted } from 'vue'
import rawData from '../data/links.json'
import './nakayama-shared.css'

const categories = rawData.categories
const allItems = rawData.items

const searchQuery = ref('')
const searchInputRef = ref(null)

function handleKeydown(e) {
  if (e.key === '/' && document.activeElement !== searchInputRef.value) {
    e.preventDefault()
    searchInputRef.value?.focus()
  } else if (e.key === 'Escape') {
    if (searchQuery.value) {
      searchQuery.value = ''
    }
    searchInputRef.value?.blur()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})

const categoryCounts = computed(() => {
  const counts = {}
  for (const item of allItems) {
    counts[item.category] = (counts[item.category] || 0) + 1
  }
  return counts
})

const filteredCategories = computed(() => {
  const q = searchQuery.value.toLowerCase().trim()
  if (!q) return categories

  const res = {}
  for (const [key, meta] of Object.entries(categories)) {
    const matchName = meta.name.toLowerCase().includes(q)
    const matchDesc = meta.desc.toLowerCase().includes(q)
    if (matchName || matchDesc) {
      res[key] = meta
    }
  }
  return res
})

function exportAllBookmarks() {
  const timestamp = Math.floor(Date.now() / 1000)
  let html = `<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file. -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks - Nakayama Festa Megathread</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><H3 ADD_DATE="${timestamp}" LAST_MODIFIED="${timestamp}">Nakayama Festa — A Piracy Megathread</H3>
    <DL><p>
`
  for (const [catKey, catMeta] of Object.entries(categories)) {
    const catItems = allItems.filter(i => i.category === catKey)
    if (catItems.length === 0) continue

    html += `        <DT><H3 ADD_DATE="${timestamp}" LAST_MODIFIED="${timestamp}">${catMeta.name}</H3>\n`
    html += `        <DL><p>\n`
    for (const item of catItems) {
      const desc = item.desc ? ` - ${item.desc.replace(/"/g, '&quot;')}` : ''
      html += `            <DT><A HREF="${item.url}" ADD_DATE="${timestamp}">${item.name}${desc}</A>\n`
    }
    html += `        </DL><p>\n`
  }

  html += `    </DL><p>
</DL><p>`

  const blob = new Blob([html], { type: 'text/html;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'nakayama-festa-megathread-bookmarks.html'
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
}
</script>

<template>
  <div class="theindex-root">
    <header class="theindex-navbar">
      <div class="nav-container">
        <div class="nav-left">
          <a href="/" class="nav-brand">
            <span class="brand-icon">🏴‍☠️</span>
            <span class="brand-title">Megathread</span>
          </a>

          <nav class="nav-links">
            <a href="#libraries-section" class="nav-link active">Bibliotecas</a>
            <a href="/guias" class="nav-link">Guias</a>
            <a href="/privacidade" class="nav-link">Privacidade</a>
            <a href="/sobre" class="nav-link">Sobre</a>
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

    <!-- MAIN BODY -->
    <main class="theindex-main">
      <!-- HERO BANNER -->
      <section class="hero-banner">
        <div class="hero-badge">🇧🇷 DIRETÓRIO ABERTO E VERIFICADO</div>
        <h1 class="hero-title">
          🏴‍☠️ <span class="highlight-title">Megathread</span>
        </h1>
        <p class="hero-subtitle">
          Compilação completa de recursos digitais, softwares, filmes, animes, jogos e guias de segurança selecionados da internet brasileira.
        </p>

        <!-- Search Bar -->
        <div class="hero-search-wrap">
          <div class="search-field-wrap">
            <svg class="search-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
              <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
            </svg>
            <input
              ref="searchInputRef"
              v-model="searchQuery"
              type="text"
              placeholder="Filtrar bibliotecas temáticas... (Pressione / para focar)"
              class="theindex-search-input"
            />
            <button
              v-if="searchQuery"
              @click="searchQuery = ''"
              class="search-clear-x"
            >
              ×
            </button>
            <span class="search-key-hint">/</span>
          </div>
        </div>

        <!-- STATS BADGES -->
        <div class="stats-pills-row">
          <div class="stat-pill">
            <span class="stat-number">{{ Object.keys(categories).length }}</span>
            <span class="stat-label">Bibliotecas</span>
          </div>
          <div class="stat-pill">
            <span class="stat-number">{{ allItems.length }}</span>
            <span class="stat-label">Recursos Verificados</span>
          </div>
          <div class="stat-pill">
            <span class="stat-number">100%</span>
            <span class="stat-label">Livre de Malwares</span>
          </div>
          <div class="stat-pill">
            <span class="stat-number">35+</span>
            <span class="stat-label">Fontes Compiladas</span>
          </div>
        </div>
      </section>

      <!-- LIBRARIES SECTION -->
      <section id="libraries-section" class="section-container">
        <div class="section-header">
          <h2 class="section-title">
            <span class="highlight-title">Bibliotecas</span>
          </h2>
          <div class="section-actions">
            <button
              @click="exportAllBookmarks"
              class="btn-export-all"
              title="Baixar todo o acervo compilado de links para importar no navegador"
            >
              📥 Exportar Favoritos
            </button>
            <span class="section-hint">Clique em uma biblioteca para ver seus recursos</span>
          </div>
        </div>

        <div class="libraries-grid">
          <a
            v-for="(meta, catKey) in filteredCategories"
            :key="catKey"
            :href="meta.path"
            class="library-card"
            :style="{ '--card-accent': meta.color }"
          >
            <div class="lib-thumb-wrapper">
              <img
                :src="meta.img"
                :alt="meta.name"
                class="lib-thumb"
                loading="lazy"
              />
            </div>

            <div class="lib-content">
              <div class="lib-header">
                <h3 class="lib-title">{{ meta.icon }} {{ meta.name }}</h3>
                <span class="lib-badge">{{ categoryCounts[catKey] || 0 }}</span>
              </div>
              <p class="lib-desc">{{ meta.desc }}</p>
              <div class="lib-footer-action">
                <span class="lib-action-text">
                  Explorar biblioteca <span class="lib-action-arrow">→</span>
                </span>
              </div>
            </div>
          </a>
        </div>

        <div v-if="Object.keys(filteredCategories).length === 0" class="no-libraries-found">
          <p>Nenhuma biblioteca encontrada para "<strong>{{ searchQuery }}</strong>"</p>
          <button @click="searchQuery = ''" class="btn-clear-search">Limpar Busca</button>
        </div>
      </section>
    </main>

    <!-- FOOTER -->
    <footer class="theindex-footer">
      <div class="footer-inner">
        <p><strong>Megathread</strong> — Compilação colaborativa de fontes abertas da internet brasileira.</p>
        <p>Inspirado no TheIndex.moe & EverythingMoe • Licenciado sob CC0 1.0 (Domínio Público) • 100% de código aberto</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
@import './nakayama-shared.css';

/* HERO SECTION */
.hero-banner {
  position: relative;
  text-align: center;
  padding: 3rem 1rem 2.25rem;
  margin-bottom: 2rem;
  background: linear-gradient(180deg, rgba(16, 20, 30, 0.5) 0%, transparent 100%);
  border-radius: 12px;
  overflow: hidden;
}

.hero-badge,
.hero-title,
.hero-subtitle,
.hero-search-wrap,
.stats-pills-row {
  position: relative;
  z-index: 1;
}

.hero-badge {
  display: inline-block;
  background-color: var(--bg-2);
  border: 1px solid var(--bg-4);
  color: var(--accent-cyan);
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 0.25rem 0.75rem;
  border-radius: 999px;
  margin-bottom: 1rem;
}

.hero-title {
  font-family: var(--font-mono);
  font-size: 2.8rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 0.75rem;
  letter-spacing: -0.03em;
  text-shadow: 0 0 10px rgba(0, 240, 118, 0.3);
}

.hero-subtitle {
  font-size: 1.05rem;
  color: #94a3b8;
  max-width: 680px;
  margin: 0 auto 1.5rem;
  line-height: 1.6;
}

.hero-search-wrap {
  max-width: 620px;
  margin: 0 auto 1.75rem;
}

.hero-search-wrap .search-field-wrap {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
}

.search-key-hint {
  font-family: var(--font-mono);
  background-color: var(--bg-3);
  border: 1px solid var(--bg-5);
  color: var(--accent-color);
  font-size: 0.75rem;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  margin-left: 0.5rem;
}

.stats-pills-row {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.stat-pill {
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.stat-pill:hover {
  border-color: var(--accent-color);
  box-shadow: 0 0 10px rgba(0, 240, 118, 0.15);
}

.stat-number {
  color: var(--accent-color);
  font-family: var(--font-mono);
  font-weight: 800;
  font-size: 1rem;
  text-shadow: 0 0 8px var(--accent-glow);
}

.stat-label {
  color: #64748b;
  font-family: var(--font-mono);
  font-size: 0.78rem;
}

/* LIBRARIES GRID */
.libraries-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 0.95rem;
}

.library-card {
  display: flex;
  flex-direction: row;
  height: 112px;
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-right: 4px solid var(--card-accent, var(--bg-4));
  border-radius: 8px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  transition: all 0.2s ease-in-out;
}

.library-card:hover {
  background-color: var(--bg-3);
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.6), 0 0 12px rgba(0, 240, 118, 0.1);
  border-right-color: var(--card-accent, var(--accent-color));
}

.lib-thumb-wrapper {
  width: 105px;
  min-width: 105px;
  max-width: 105px;
  height: 100%;
  background-color: #06090e;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  flex-shrink: 0;
}

.lib-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.library-card:hover .lib-thumb {
  transform: scale(1.05);
}

.lib-content {
  padding: 0.75rem 0.95rem;
  height: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  min-width: 0;
  overflow: hidden;
}

.lib-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
  min-width: 0;
}

.lib-title {
  font-family: var(--font-mono);
  font-size: 0.96rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0;
  letter-spacing: -0.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  min-width: 0;
  flex-grow: 1;
}

.lib-badge {
  background-color: rgba(16, 20, 30, 0.8);
  border: 1px solid var(--card-accent, var(--bg-4));
  color: var(--card-accent, var(--accent-color));
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  flex-shrink: 0;
  transition: all 0.2s ease;
}

.library-card:hover .lib-badge {
  background-color: var(--card-accent, var(--accent-color));
  color: #06090e;
  box-shadow: 0 0 10px var(--card-accent, var(--accent-glow));
}

.lib-desc {
  font-size: 0.8rem;
  color: #94a3b8;
  margin: 0;
  line-height: 1.35;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.lib-footer-action {
  margin-top: auto;
}

.lib-action-text {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--accent-cyan);
  transition: color 0.2s ease, text-shadow 0.2s ease;
}

.lib-action-arrow {
  display: inline-block;
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.library-card:hover .lib-action-text {
  color: var(--card-accent, var(--accent-color));
  text-shadow: 0 0 8px rgba(0, 240, 118, 0.2);
}

.library-card:hover .lib-action-arrow {
  transform: translateX(4px);
}

.no-libraries-found {
  text-align: center;
  padding: 3rem;
  color: #64748b;
  font-family: var(--font-mono);
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-radius: 8px;
}

.btn-clear-search {
  background-color: var(--accent-color);
  color: #06090e;
  border: none;
  padding: 0.4rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  margin-top: 0.5rem;
  font-family: var(--font-mono);
  font-weight: 700;
  box-shadow: 0 0 8px var(--accent-glow);
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.1rem;
  }
  .libraries-grid {
    grid-template-columns: 1fr;
  }
}
</style>
