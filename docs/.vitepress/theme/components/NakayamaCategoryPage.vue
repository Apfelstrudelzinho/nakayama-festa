<script setup>
// ============================================================================
// PROJECT:     Nakayama Festa - A Piracy Megathread
// Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
// Description: Dynamic category view with grid/table display, filtering and search.
// Version:     0.1 (09.2026)
// ============================================================================

import { ref, computed, onMounted, onUnmounted } from 'vue'
import rawData from '../data/links.json'
import './nakayama-shared.css'

const props = defineProps({
  category: {
    type: String,
    required: true
  }
})

const categories = rawData.categories
const allItems = rawData.items

const currentCategory = computed(() => {
  return categories[props.category] || {
    name: props.category,
    icon: '📁',
    img: '/img/teasip.gif',
    desc: 'Recursos selecionados e verificados.',
    path: `/${props.category}`,
    color: '#0d6efd'
  }
})

const categoryItems = computed(() => {
  return allItems.filter(item => item.category === props.category)
})

const availableSections = computed(() => {
  const s = new Set()
  for (const item of categoryItems.value) {
    if (item.section) {
      s.add(item.section)
    }
  }
  return Array.from(s)
})

const searchQuery = ref('')
const selectedSection = ref('todas')
const activeTag = ref('todos')
const sortBy = ref('recommended')
const activeView = ref('grid')
const copiedId = ref(null)
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

const filteredItems = computed(() => {
  const q = searchQuery.value.toLowerCase().trim()

  let list = categoryItems.value.filter(item => {
    if (selectedSection.value !== 'todas' && item.section !== selectedSection.value) {
      return false
    }

    if (activeTag.value === 'PT-BR' && item.lang !== 'PT-BR') return false
    if (activeTag.value === 'recommended' && !item.recommended) return false
    if (['DDL', 'Torrent', 'Streaming', 'Sem Anúncios', 'Repack', 'ROMs', 'Educativo', 'Open Source', '1080p'].includes(activeTag.value)) {
      const matchTag = item.tags?.includes(activeTag.value) ||
                       item.desc?.toLowerCase().includes(activeTag.value.toLowerCase()) ||
                       item.section?.toLowerCase().includes(activeTag.value.toLowerCase())
      if (!matchTag) return false
    }

    if (q) {
      const matchName = item.name.toLowerCase().includes(q)
      const matchDesc = item.desc.toLowerCase().includes(q)
      const matchDomain = item.domain.toLowerCase().includes(q)
      const matchTags = item.tags?.some(t => t.toLowerCase().includes(q))
      const matchSection = item.section?.toLowerCase().includes(q)
      return matchName || matchDesc || matchDomain || matchTags || matchSection
    }

    return true
  })

  if (sortBy.value === 'asc') {
    list.sort((a, b) => a.name.localeCompare(b.name))
  } else if (sortBy.value === 'desc') {
    list.sort((a, b) => b.name.localeCompare(a.name))
  } else if (sortBy.value === 'recommended') {
    list.sort((a, b) => (b.recommended === true ? 1 : 0) - (a.recommended === true ? 1 : 0))
  }

  return list
})

function copyLink(item) {
  if (navigator?.clipboard) {
    navigator.clipboard.writeText(item.url)
    copiedId.value = item.id
    setTimeout(() => {
      copiedId.value = null
    }, 2000)
  }
}

function reportBrokenLink(item) {
  const repo = 'Apfelstrudelzinho/nakayama-festa'
  const title = encodeURIComponent(`[Link Quebrado] ${item.name}`)
  const body = encodeURIComponent(
`### Relato de Link Quebrado

- **Nome:** ${item.name}
- **URL:** ${item.url}
- **Categoria:** ${currentCategory.value.name} (${props.category})
- **Seção:** ${item.section || 'N/A'}
- **Data do Relato:** ${new Date().toISOString().split('T')[0]}

**Descrição do problema:**
<!-- Descreva se o link está fora do ar, mudou de domínio ou apresenta erro -->`
  )
  window.open(`https://github.com/${repo}/issues/new?title=${title}&body=${body}`, '_blank', 'noopener,noreferrer')
}

function exportCategoryBookmarks() {
  const timestamp = Math.floor(Date.now() / 1000)
  let html = `<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file. -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks - ${currentCategory.value.name} - Nakayama Festa Megathread</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><H3 ADD_DATE="${timestamp}" LAST_MODIFIED="${timestamp}">${currentCategory.value.name} — Nakayama Festa</H3>
    <DL><p>
`
  for (const item of filteredItems.value) {
    const desc = item.desc ? ` - ${item.desc.replace(/"/g, '&quot;')}` : ''
    html += `        <DT><A HREF="${item.url}" ADD_DATE="${timestamp}">${item.name}${desc}</A>\n`
  }
  html += `    </DL><p>
</DL><p>`

  const blob = new Blob([html], { type: 'text/html;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `nakayama-${props.category}-bookmarks.html`
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
}

function handleFaviconError(e) {
  e.target.style.display = 'none'
  const fallback = e.target.nextElementSibling
  if (fallback) fallback.style.display = 'flex'
}
</script>

<template>
  <div class="theindex-root theindex-subpage" :style="{ '--category-accent': currentCategory.color }">
    <!-- 1. TheIndex NAVBAR -->
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
      <!-- Breadcrumb & Back Link -->
      <div class="breadcrumb-bar">
        <a href="/" class="back-link">
          <svg viewBox="0 0 448 512" width="13" height="13" fill="currentColor">
            <path d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z"/>
          </svg>
          Todas as Bibliotecas
        </a>
      </div>

      <!-- CATEGORY BANNER (TheIndex Signature Banner) -->
      <section class="category-banner-card" :style="{ '--banner-accent': currentCategory.color }">
        <div class="banner-avatar-wrap">
          <img :src="currentCategory.img" :alt="currentCategory.name" class="banner-avatar" />
        </div>
        <div class="banner-content">
          <div class="banner-header">
            <h1 class="banner-title">
              <span class="banner-icon">{{ currentCategory.icon }}</span>
              {{ currentCategory.name }}
            </h1>
            <span class="banner-count-badge">{{ categoryItems.length }} recursos</span>
          </div>
          <p class="banner-desc">{{ currentCategory.desc }}</p>
        </div>
      </section>

      <!-- SECTION SECTIONS CHIPS (If category has multiple sections) -->
      <section v-if="availableSections.length > 1" class="section-pills-bar">
        <span class="section-pills-label">Seções:</span>
        <button
          @click="selectedSection = 'todas'"
          :class="['section-chip', { active: selectedSection === 'todas' }]"
        >
          Todas ({{ categoryItems.length }})
        </button>
        <button
          v-for="sec in availableSections"
          :key="sec"
          @click="selectedSection = selectedSection === sec ? 'todas' : sec"
          :class="['section-chip', { active: selectedSection === sec }]"
        >
          {{ sec }}
        </button>
      </section>

      <!-- CONTROLS & SEARCH BAR -->
      <section class="category-controls-card">
        <div class="controls-top-row">
          <!-- Instant Search -->
          <div class="search-field-wrap">
            <svg class="search-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
              <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
            </svg>
            <input
              ref="searchInputRef"
              v-model="searchQuery"
              type="text"
              :placeholder="`Pesquisar em ${currentCategory.name}... (Pressione /)`"
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

          <!-- Sort & Mode Controls -->
          <div class="controls-actions">
            <select v-model="sortBy" class="theindex-select" aria-label="Ordenar">
              <option value="recommended">⭐ Recomendados Primeiro</option>
              <option value="asc">A-Z (Alfabética)</option>
              <option value="desc">Z-A</option>
            </select>

            <button
              @click="exportCategoryBookmarks"
              class="theindex-view-btn"
              title="Baixar lista filtrada como arquivo de favoritos HTML"
            >
              📥 Exportar
            </button>

            <button
              @click="activeView = activeView === 'grid' ? 'table' : 'grid'"
              class="theindex-view-btn"
              :title="activeView === 'grid' ? 'Mudar para modo tabela' : 'Mudar para modo cards'"
            >
              <svg v-if="activeView === 'grid'" viewBox="0 0 512 512" width="14" height="14" fill="currentColor">
                <path d="M0 96C0 60.7 28.7 32 64 32l384 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96zM64 96l0 64 384 0 0-64L64 96zm384 128l-384 0 0 64 384 0 0-64zm0 128l-384 0 0 64c0 17.7 14.3 32 32 32l320 0c17.7 0 32-14.3 32-32l0-64z"/>
              </svg>
              <svg v-else viewBox="0 0 448 512" width="14" height="14" fill="currentColor">
                <path d="M128 136c0-22.1-17.9-40-40-40L40 96C17.9 96 0 113.9 0 136l0 48c0 22.1 17.9 40 40 40l48 0c22.1 0 40-17.9 40-40l0-48zm0 192c0-22.1-17.9-40-40-40l-48 0c-22.1 0-40 17.9-40 40l0 48c0 22.1 17.9 40 40 40l48 0c22.1 0 40-17.9 40-40l0-48zm320-192c0-22.1-17.9-40-40-40l-48 0c-22.1 0-40 17.9-40 40l0 48c0 22.1 17.9 40 40 40l48 0c22.1 0 40-17.9 40-40l0-48zm0 192c0-22.1-17.9-40-40-40l-48 0c-22.1 0-40 17.9-40 40l0 48c0 22.1 17.9 40 40 40l48 0c22.1 0 40-17.9 40-40l0-48z"/>
              </svg>
              {{ activeView === 'grid' ? 'Tabela' : 'Cards' }}
            </button>
          </div>
        </div>

        <!-- Filter Tags Chips -->
        <div class="theindex-tags-bar">
          <button
            @click="activeTag = 'todos'"
            :class="['tag-chip', { active: activeTag === 'todos' }]"
          >
            Todos
          </button>
          <button
            @click="activeTag = activeTag === 'recommended' ? 'todos' : 'recommended'"
            :class="['tag-chip', { active: activeTag === 'recommended' }]"
          >
            ⭐ Recomendados
          </button>
          <button
            @click="activeTag = activeTag === 'PT-BR' ? 'todos' : 'PT-BR'"
            :class="['tag-chip', { active: activeTag === 'PT-BR' }]"
          >
            🇧🇷 PT-BR
          </button>
          <button
            @click="activeTag = activeTag === 'DDL' ? 'todos' : 'DDL'"
            :class="['tag-chip', { active: activeTag === 'DDL' }]"
          >
            📥 DDL
          </button>
          <button
            @click="activeTag = activeTag === 'Torrent' ? 'todos' : 'Torrent'"
            :class="['tag-chip', { active: activeTag === 'Torrent' }]"
          >
            🧲 Torrent
          </button>
          <button
            @click="activeTag = activeTag === 'Streaming' ? 'todos' : 'Streaming'"
            :class="['tag-chip', { active: activeTag === 'Streaming' }]"
          >
            📺 Streaming
          </button>
          <button
            @click="activeTag = activeTag === 'Sem Anúncios' ? 'todos' : 'Sem Anúncios'"
            :class="['tag-chip', { active: activeTag === 'Sem Anúncios' }]"
          >
            🛡️ Sem Ads
          </button>
        </div>

        <!-- Counter info -->
        <div class="results-info-row">
          <span>Mostrando <strong>{{ filteredItems.length }}</strong> de {{ categoryItems.length }} recursos</span>
          <span v-if="searchQuery" class="search-active-pill">Busca: "{{ searchQuery }}"</span>
          <span v-if="selectedSection !== 'todas'" class="search-active-pill">Seção: {{ selectedSection }}</span>
        </div>
      </section>

      <!-- ITEMS: CARDS GRID VIEW -->
      <section v-if="activeView === 'grid'" class="theindex-cards-grid">
        <div
          v-for="item in filteredItems"
          :key="item.id"
          class="theindex-item-card"
          :style="{ '--hover-accent': currentCategory.color }"
        >
          <div class="item-card-inner">
            <!-- Header Row -->
            <div class="item-header-row">
              <span class="online-ping-dot" title="Recurso ativo e verificado"></span>

              <img
                :src="`https://icons.duckduckgo.com/ip3/${item.domain}.ico`"
                :alt="item.name"
                class="item-favicon"
                loading="lazy"
                @error="handleFaviconError"
              />
              <span class="item-favicon-fallback" style="display: none;">🌐</span>

              <span v-if="item.recommended" class="item-star-icon" title="Item Recomendado">⭐</span>

              <a
                :href="item.url"
                target="_blank"
                rel="noopener noreferrer"
                class="item-title-link"
                :title="`Visitar ${item.name}`"
              >
                {{ item.name }}
              </a>

              <div class="item-actions">
                <button
                  @click="copyLink(item)"
                  class="item-action-icon"
                  :title="copiedId === item.id ? 'Copiado!' : 'Copiar link direto'"
                >
                  <span v-if="copiedId === item.id" style="color: #20c997; font-weight: bold;">✓</span>
                  <svg v-else viewBox="0 0 448 512" width="11" height="11" fill="currentColor">
                    <path d="M280 64l40 0c35.3 0 64 28.7 64 64l0 256c0 35.3-28.7 64-64 64L120 448c-35.3 0-64-28.7-64-64l0-256c0-35.3 28.7-64 64-64l40 0 0-48c0-8.8 7.2-16 16-16l88 0c8.8 0 16 7.2 16 16l0 48zM120 128c-8.8 0-16 7.2-16 16l0 256c0 8.8 7.2 16 16 16l200 0c8.8 0 16-7.2 16-16l0-256c0-8.8-7.2-16-16-16l-200 0z"/>
                  </svg>
                </button>

                <button
                  @click="reportBrokenLink(item)"
                  class="item-action-icon report-broken-btn"
                  title="Reportar link quebrado"
                >
                  <svg viewBox="0 0 512 512" width="11" height="11" fill="currentColor">
                    <path d="M256 32c14.2 0 27.3 7.5 34.5 19.8l216 368c7.3 12.4 7.3 27.7 .2 40.1S486.3 480 472 480L40 480c-14.3 0-27.4-7.7-34.7-20.1s-7.1-27.8 .2-40.1l216-368C228.7 39.5 241.8 32 256 32zm0 128c-13.3 0-24 10.7-24 24l0 112c0 13.3 10.7 24 24 24s24-10.7 24-24l0-112c0-13.3-10.7-24-24-24zm32 224a32 32 0 1 0 -64 0 32 32 0 1 0 64 0z"/>
                  </svg>
                </button>

                <a
                  :href="item.url"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="item-action-icon"
                  title="Abrir em nova aba"
                >
                  <svg viewBox="0 0 512 512" width="11" height="11" fill="currentColor">
                    <path d="M320 0c-17.7 0-32 14.3-32 32s14.3 32 32 32l82.7 0L201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L448 109.3l0 82.7c0 17.7 14.3 32 32 32s32-14.3 32-32l0-160c0-17.7-14.3-32-32-32L320 0zM80 32C35.8 32 0 67.8 0 112L0 432c0 44.2 35.8 80 80 80l320 0c44.2 0 80-35.8 80-80l0-112c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 112c0 8.8-7.2 16-16 16L80 448c-8.8 0-16-7.2-16-16l0-320c0-8.8 7.2-16 16-16l112 0c17.7 0 32-14.3 32-32s-14.3-32-32-32L80 32z"/>
                  </svg>
                </a>
              </div>
            </div>

            <!-- Domain -->
            <div class="item-domain-text">{{ item.domain }}</div>

            <!-- Description -->
            <p class="item-description-text">{{ item.desc }}</p>

            <!-- Badges -->
            <div class="item-badges-list">
              <span v-if="item.section" class="theindex-badge badge-category">
                {{ item.section }}
              </span>
              <span v-if="item.lang === 'PT-BR'" class="theindex-badge badge-lang">
                🇧🇷 PT-BR
              </span>
              <span v-for="tag in item.tags" :key="tag" class="theindex-badge badge-tag">
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </section>

      <!-- ITEMS: TABLE VIEW (EverythingMoe style) -->
      <section v-else class="theindex-table-card">
        <table class="everythingmoe-table">
          <thead>
            <tr>
              <th style="width: 35%;">Nome do Recurso</th>
              <th style="width: 25%;">Seção</th>
              <th style="width: 20%;">Tags & Recursos</th>
              <th style="width: 10%;">Idioma</th>
              <th style="width: 10%; text-align: right;">Acessar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in filteredItems" :key="item.id">
              <td>
                <div class="table-name-cell">
                  <span class="online-ping-dot"></span>
                  <img
                    :src="`https://icons.duckduckgo.com/ip3/${item.domain}.ico`"
                    :alt="item.name"
                    class="item-favicon"
                    loading="lazy"
                    @error="handleFaviconError"
                  />
                  <a :href="item.url" target="_blank" rel="noopener noreferrer" class="table-item-link">
                    {{ item.name }}
                  </a>
                  <span v-if="item.recommended" class="item-star-icon">⭐</span>
                </div>
                <div class="table-desc-sub">{{ item.domain }} — {{ item.desc }}</div>
              </td>
              <td>
                <span class="theindex-badge badge-category">{{ item.section || currentCategory.name }}</span>
              </td>
              <td>
                <div class="table-tags-wrap">
                  <span v-for="t in item.tags" :key="t" class="theindex-badge badge-tag">{{ t }}</span>
                </div>
              </td>
              <td>
                <span class="theindex-badge badge-lang">{{ item.lang }}</span>
              </td>
              <td style="text-align: right; white-space: nowrap;">
                <div style="display: inline-flex; gap: 0.35rem; align-items: center;">
                  <button
                    @click="reportBrokenLink(item)"
                    class="item-action-icon report-broken-btn"
                    title="Reportar link quebrado"
                  >
                    ⚠️
                  </button>
                  <a
                    :href="item.url"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="table-open-btn"
                  >
                    Abrir ↗
                  </a>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </section>

      <!-- Empty Results -->
      <div v-if="filteredItems.length === 0" class="no-results-box">
        <p class="no-results-emoji">🔍</p>
        <h3 class="no-results-title">Nenhum recurso encontrado</h3>
        <p class="no-results-desc">Tente alterar os termos da busca ou desmarcar os filtros selecionados.</p>
        <button @click="searchQuery = ''; activeTag = 'todos'; selectedSection = 'todas'" class="btn-reset-filters">
          Limpar Filtros
        </button>
      </div>
    </main>

    <!-- FOOTER -->
    <footer class="theindex-footer">
      <div class="footer-inner">
        <p><strong>Megathread</strong> — Uma compilação colaborativa de fontes abertas da internet.</p>
        <p>Inspirado no TheIndex.moe & EverythingMoe • Licenciado sob CC0 1.0 (Domínio Público) • 100% de código aberto</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
@import './nakayama-shared.css';

.category-banner-card {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-left: 6px solid var(--banner-accent, var(--accent-color));
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
}

.banner-avatar-wrap {
  width: 90px;
  height: 90px;
  min-width: 90px;
  background-color: #0c0c0c;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--bg-4);
}

.banner-avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.banner-content {
  flex-grow: 1;
}

.banner-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 0.4rem;
}

.banner-title {
  font-family: var(--font-mono);
  font-size: 1.6rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  letter-spacing: -0.02em;
  text-shadow: 0 0 10px rgba(0, 240, 118, 0.25);
}

.banner-icon {
  font-size: 1.7rem;
}

.banner-count-badge {
  background-color: var(--bg-3);
  border: 1px solid var(--bg-4);
  color: var(--accent-color);
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  box-shadow: 0 0 8px rgba(0, 240, 118, 0.15);
}

.banner-desc {
  font-size: 0.95rem;
  color: #94a3b8;
  margin: 0;
  line-height: 1.5;
}

/* Section Pills */
.section-pills-bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 1.25rem;
  padding: 0.6rem 0.8rem;
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-radius: 6px;
}

.section-pills-label {
  font-size: 0.82rem;
  color: #777;
  font-weight: 600;
  text-transform: uppercase;
}

.section-chip {
  background-color: var(--bg-3);
  border: 1px solid var(--bg-4);
  color: #bbb;
  font-size: 0.8rem;
  padding: 0.25rem 0.65rem;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.15s ease;
}

.section-chip:hover {
  background-color: var(--bg-4);
  color: #fff;
}

.section-chip.active {
  background-color: var(--accent-color);
  border-color: var(--accent-color);
  color: #fff;
  font-weight: 600;
}

/* Controls Card */
.category-controls-card {
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-radius: 8px;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
}

.controls-top-row {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}

.controls-top-row .search-field-wrap {
  flex-grow: 1;
  min-width: 260px;
}

.controls-actions {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.theindex-select {
  background-color: var(--bg-3);
  border: 1px solid var(--bg-4);
  color: #fff;
  font-size: 0.85rem;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  outline: none;
  cursor: pointer;
}

.theindex-view-btn {
  background-color: var(--bg-3);
  border: 1px solid var(--bg-4);
  color: #fff;
  font-size: 0.85rem;
  padding: 0.5rem 0.85rem;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  cursor: pointer;
}

.theindex-view-btn:hover {
  background-color: var(--bg-4);
}

.results-info-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.82rem;
  color: #888;
  margin-top: 0.75rem;
  border-top: 1px solid var(--bg-3);
  padding-top: 0.75rem;
}

.search-active-pill {
  background-color: var(--bg-3);
  color: #fff;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

/* Hover Accent for cards */
.theindex-item-card:hover {
  border-right-color: var(--hover-accent, var(--accent-color));
}

/* Table View */
.theindex-table-card {
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-radius: 8px;
  overflow-x: auto;
}

.everythingmoe-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.88rem;
}

.everythingmoe-table th {
  background-color: var(--bg-3);
  color: #aaa;
  font-weight: 600;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--bg-4);
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.everythingmoe-table td {
  padding: 0.85rem 1rem;
  border-bottom: 1px solid var(--bg-3);
  vertical-align: middle;
}

.everythingmoe-table tr:hover {
  background-color: var(--bg-3);
}

.table-name-cell {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
}

.table-item-link {
  color: #ffffff;
  text-decoration: none;
}

.table-item-link:hover {
  color: var(--accent-color);
}

.table-desc-sub {
  font-size: 0.75rem;
  color: #777;
  margin-top: 0.2rem;
}

.table-tags-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
}

.table-open-btn {
  background-color: var(--bg-4);
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.8rem;
  padding: 0.3rem 0.65rem;
  border-radius: 4px;
  transition: all 0.15s ease;
}

.table-open-btn:hover {
  background-color: var(--accent-color);
  color: #fff;
}

.badge-lang {
  background-color: #1a3a2a;
  color: #52b788;
  border: 1px solid #2a5a3a;
}

/* Empty State */
.no-results-box {
  text-align: center;
  padding: 4rem 1rem;
  background-color: var(--bg-2);
  border: 1px solid var(--bg-3);
  border-radius: 8px;
}

.no-results-emoji {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.no-results-title {
  color: #fff;
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.no-results-desc {
  color: #888;
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
}

.btn-reset-filters {
  background-color: var(--accent-color);
  color: #fff;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}

@media (max-width: 768px) {
  .category-banner-card {
    flex-direction: column;
    text-align: center;
    padding: 1.25rem;
  }
  .banner-header {
    justify-content: center;
  }
  .controls-top-row {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>
