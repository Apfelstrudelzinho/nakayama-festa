<script setup>
// ============================================================================
// PROJECT:     Nakayama Festa - A Piracy Megathread
// Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
// Description: Custom VitePress root layout with banner slot and Nakayama guide view.
// Version:     0.1 (09.2026)
// ============================================================================

import DefaultTheme from 'vitepress/theme'
import { useData } from 'vitepress'
import { ref, computed } from 'vue'
import './components/nakayama-shared.css'

const { Layout } = DefaultTheme
const { page } = useData()

const isBannerVisible = ref(true)

function closeBanner() {
  isBannerVisible.value = false
}

// Identify whether the current page is an individual tutorial/guide inside /guias/
const isGuideDetailPage = computed(() => {
  const p = page.value?.relativePath || ''
  return p.startsWith('guias/') && p !== 'guias/index.md'
})
</script>

<template>
  <!-- Guide detail pages inherit the retro-cyberpunk Nakayama theme -->
  <div v-if="isGuideDetailPage" class="theindex-root theindex-subpage nakayama-guide-page">
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

    <main class="theindex-main">
      <div class="breadcrumb-bar">
        <a href="/guias" class="back-link">
          <svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
          </svg>
          Voltar para Guias
        </a>
      </div>

      <article class="guide-content-card">
        <Content class="vp-doc" />
      </article>
    </main>

    <footer class="theindex-footer">
      <div class="footer-inner">
        <p><strong>Megathread</strong> — Guias e Tutoriais práticos em Português.</p>
        <p>Inspirado no TheIndex.moe & EverythingMoe • Licenciado sob CC0 1.0 (Domínio Público) • 100% de código aberto</p>
      </div>
    </footer>
  </div>

  <!-- Standard layout for default pages -->
  <Layout v-else>
    <template #home-features-after>
      <section v-if="isBannerVisible" class="endof10">
        <div class="banner-wrapper">
          <a class="banner-link" href="https://endof10.org/pt-br">
            <svg class="banner-icon" viewBox="0 0 688.235 754">
              <rect width="260.474" height="260.474" x="-36.543" y="129.876" opacity=".4" rx="43.06" style="stroke-width:.920077" transform="rotate(-15.111)"></rect>
              <rect width="260.474" height="260.474" x="407.612" y="96.465" opacity=".4" rx="43.06" style="stroke-width:.920077"></rect>
              <rect width="260.474" height="260.474" x="117.716" y="386.36" opacity=".4" rx="43.06" style="stroke-width:.920077"></rect>
              <rect width="260.474" height="260.474" x="486.185" y="332.836" opacity=".4" rx="43.06" style="stroke-width:.920077" transform="rotate(7.911)"></rect>
            </svg>
            <span class="banner-text">
              Continue usando seu PC após o término do suporte do Windows 10.
              <strong>Visite endof10.org/pt-br</strong>
            </span>
          </a>
        </div>
        <button @click="closeBanner" class="close-banner" aria-label="Fechar Banner" title="Fechar Banner">×</button>
      </section>
    </template>
  </Layout>
</template>
