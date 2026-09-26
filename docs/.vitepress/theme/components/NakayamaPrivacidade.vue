<script setup>
// ============================================================================
// PROJECT:     Nakayama Festa - A Piracy Megathread
// Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
// Description: Curated digital privacy, anonymity, and security tools portal.
// Version:     0.1 (09.2026)
// ============================================================================

import { ref, computed, onMounted, onUnmounted } from 'vue'

const privacyTools = [
  // VPNs
  {
    name: "Mullvad VPN",
    url: "https://mullvad.net/",
    domain: "mullvad.net",
    category: "VPN",
    tags: ["Sem Logs", "WireGuard", "Anônimo", "P2P"],
    desc: "A VPN mais recomendada para privacidade máxima. Não exige e-mail ou dados pessoais para criar conta (apenas um número de 16 dígitos). Auditada e comprovada em apreensões policiais sem retenção de logs.",
    recommended: true
  },
  {
    name: "IVPN",
    url: "https://www.ivpn.net/",
    domain: "ivpn.net",
    category: "VPN",
    tags: ["Sem Logs", "Open Source", "WireGuard", "Multi-hop"],
    desc: "Serviço de VPN transparente com clientes 100% de código aberto, auditorias regulares e política estrita de não retenção de registros de atividade.",
    recommended: true
  },
  {
    name: "Proton VPN",
    url: "https://protonvpn.com/",
    domain: "protonvpn.com",
    category: "VPN",
    tags: ["Suíça", "Plano Grátis", "Sem Logs", "Secure Core"],
    desc: "Sediada na Suíça sob fortes leis de privacidade. Possui plano gratuito ilimitado sem anúncios e código aberto auditado.",
    recommended: true
  },
  {
    name: "AirVPN",
    url: "https://airvpn.org/",
    domain: "airvpn.org",
    category: "VPN",
    tags: ["Port Forwarding", "Ativistas", "P2P", "OpenVPN"],
    desc: "Operada por ativistas dos direitos digitais. Excelente para quem precisa de encaminhamento de portas (port forwarding) e seeding de torrents.",
    recommended: false
  },
  
  // DNS Resolvers
  {
    name: "NextDNS",
    url: "https://nextdns.io/",
    domain: "nextdns.io",
    category: "DNS",
    tags: ["DoH", "Bloqueio de Ads", "Customizável", "Seguro"],
    desc: "Funciona como um Pi-hole na nuvem. Permite bloquear anúncios, rastreadores e sites maliciosos diretamente na camada DNS com DoH/DoT.",
    recommended: true
  },
  {
    name: "Quad9",
    url: "https://quad9.net/",
    domain: "quad9.net",
    category: "DNS",
    tags: ["9.9.9.9", "Sem Fins Lucrativos", "Segurança", "Suíça"],
    desc: "Servidor de DNS seguro sem fins lucrativos sediado na Suíça que bloqueia domínios de phishing e malware automaticamente sem registrar seu IP.",
    recommended: true
  },
  {
    name: "AdGuard DNS",
    url: "https://adguard-dns.io/",
    domain: "adguard-dns.io",
    category: "DNS",
    tags: ["Adblock", "Filtros", "DoH", "Fácil Configuração"],
    desc: "Servidor DNS público focado em eliminar anúncios invasivos e rastreadores em todos os aplicativos do sistema.",
    recommended: false
  },

  // Browsers
  {
    name: "LibreWolf",
    url: "https://librewolf.net/",
    domain: "librewolf.net",
    category: "Navegadores",
    tags: ["Firefox Fork", "Sem Telemetria", "Anti-Fingerprint", "uBlock Integrado"],
    desc: "Versão customizada e endurecida do Firefox focada em privacidade, com telemetria desativada, proteção contra fingerprinting e uBlock Origin pré-instalado.",
    recommended: true
  },
  {
    name: "Cromite",
    url: "https://github.com/uazo/cromite",
    domain: "github.com/uazo/cromite",
    category: "Navegadores",
    tags: ["Chromium", "Android", "Windows", "Adblock Nativo"],
    desc: "Sucessor do Bromite para Android e PC. Navegador baseado em Chromium sem rastreamento do Google e com bloqueador de anúncios nativo.",
    recommended: true
  },
  {
    name: "Mullvad Browser",
    url: "https://mullvad.net/en/browser",
    domain: "mullvad.net",
    category: "Navegadores",
    tags: ["Tor Project", "Anti-Rastreamento", "Privativo"],
    desc: "Desenvolvido em parceria com o Projeto Tor para oferecer as mesmas proteções avançadas contra fingerprinting do Tor Browser, mas para navegação normal na web.",
    recommended: true
  },

  // Blockers & Extensions
  {
    name: "uBlock Origin",
    url: "https://ublockorigin.com/",
    domain: "ublockorigin.com",
    category: "Bloqueadores",
    tags: ["Essencial", "Open Source", "CPU Leve", "Anti-Malware"],
    desc: "O bloqueador de anúncios e elementos nocivos mais eficiente, ético e leve do mundo. Não vende anúncios 'aceitáveis' e protege contra scripts perigosos.",
    recommended: true
  },
  {
    name: "Pi-hole",
    url: "https://pi-hole.net/",
    domain: "pi-hole.net",
    category: "Bloqueadores",
    tags: ["Rede Inteira", "Raspberry Pi", "DNS Sinkhole"],
    desc: "Bloqueador de anúncios para toda a sua rede local (Smart TVs, celulares, consoles), interceptando requisições antes mesmo de chegarem aos aparelhos.",
    recommended: false
  },

  // Password Managers
  {
    name: "Bitwarden",
    url: "https://bitwarden.com/",
    domain: "bitwarden.com",
    category: "Senhas",
    tags: ["Open Source", "Criptografia E2E", "Multiplataforma"],
    desc: "Gerenciador de senhas de código aberto com criptografia de ponta a ponta zero-knowledge. Excelente aplicativo para celular e extensão de navegador.",
    recommended: true
  },
  {
    name: "KeePassXC",
    url: "https://keepassxc.org/",
    domain: "keepassxc.org",
    category: "Senhas",
    tags: ["100% Offline", "Sem Nuvem", "Controle Total"],
    desc: "Para quem não quer suas senhas armazenadas na nuvem de terceiros. Seu cofre é um arquivo local criptografado sob seu controle absoluto.",
    recommended: true
  },

  // Encryption
  {
    name: "VeraCrypt",
    url: "https://www.veracrypt.fr/",
    domain: "veracrypt.fr",
    category: "Criptografia",
    tags: ["Disco Inteiro", "Containers", "Open Source"],
    desc: "Ferramenta robusta para criar discos virtuais criptografados ou criptografar partições inteiras de sistema com algoritmos militares.",
    recommended: true
  },
  {
    name: "Cryptomator",
    url: "https://cryptomator.org/",
    domain: "cryptomator.org",
    category: "Criptografia",
    tags: ["Nuvem Criptografada", "Google Drive", "OneDrive"],
    desc: "Criptografa seus arquivos localmente antes de enviá-los para serviços de nuvem como Google Drive, Dropbox ou OneDrive.",
    recommended: true
  }
]

const searchQuery = ref('')
const selectedCategory = ref('todos')
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

const categoriesList = ['todos', 'VPN', 'DNS', 'Navegadores', 'Bloqueadores', 'Senhas', 'Criptografia']

const filteredTools = computed(() => {
  const q = searchQuery.value.toLowerCase().trim()
  return privacyTools.filter(t => {
    if (selectedCategory.value !== 'todos' && t.category !== selectedCategory.value) {
      return false
    }
    if (q) {
      return t.name.toLowerCase().includes(q) || 
             t.desc.toLowerCase().includes(q) || 
             t.tags.some(tag => tag.toLowerCase().includes(q))
    }
    return true
  })
})
</script>

<template>
  <div class="theindex-root theindex-subpage">
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
            <a href="/privacidade" class="nav-link active">Privacidade</a>
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
            Privacidade, <span class="highlight-title">Segurança & Anonimato</span>
          </h2>
          <span class="section-hint">Ferramentas essenciais para proteção dos seus dados na web</span>
        </div>

        <!-- Law Box Callout (TheIndex style) -->
        <div class="law-callout-box">
          <div class="callout-header">
            <span class="callout-icon">⚖️</span>
            <strong>Panorama Legal no Brasil: Artigo 184 do Código Penal</strong>
          </div>
          <p class="callout-text">
            No Brasil, o consumo ou download de conteúdo sem intuito de lucro direto ou indireto é tipificado de forma distinta da distribuição comercial. Ainda assim, o uso de <strong>VPNs sem retenção de registros (no-logs)</strong> e de <strong>DNS criptografados (DoH)</strong> é a melhor salvaguarda para impedir a espionagem e a interceptação de pacotes por provedores de internet (ISPs).
          </p>
        </div>

        <!-- Search Bar -->
        <div class="theindex-search-row">
          <div class="search-field-wrap">
            <svg class="search-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
              <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
            </svg>
            <input
              ref="searchInputRef"
              v-model="searchQuery"
              type="text"
              placeholder="Pesquisar ferramentas por nome (ex: mullvad, nextdns, librewolf)... (Pressione /)"
              class="theindex-search-input"
            />
            <button v-if="searchQuery" @click="searchQuery = ''" class="search-clear-x">×</button>
            <span class="search-key-hint">/</span>
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
            {{ cat === 'todos' ? 'Todas as Ferramentas' : cat }}
          </button>
        </div>

        <!-- Cards Grid -->
        <div class="theindex-cards-grid">
          <div
            v-for="tool in filteredTools"
            :key="tool.name"
            class="theindex-item-card"
          >
            <div class="item-card-inner">
              <div class="item-header-row">
                <span class="online-ping-dot" title="Serviço ativo"></span>
                <span v-if="tool.recommended" class="item-star-icon" title="Recomendado">★</span>
                
                <img
                  :src="`https://www.google.com/s2/favicons?domain=${tool.domain}&sz=32`"
                  :alt="tool.name"
                  class="item-favicon"
                  loading="lazy"
                />

                <a :href="tool.url" target="_blank" rel="noopener noreferrer" class="item-title-link">
                  {{ tool.name }}
                </a>

                <div class="item-actions">
                  <a :href="tool.url" target="_blank" rel="noopener noreferrer" class="item-action-icon" title="Visitar site oficial">
                    ↗
                  </a>
                </div>
              </div>

              <span class="item-domain-text">{{ tool.domain }}</span>

              <p class="item-description-text">
                {{ tool.desc }}
              </p>

              <!-- Tags -->
              <div class="item-badges-list">
                <span class="theindex-badge badge-category">
                  {{ tool.category }}
                </span>
                <span v-for="tag in tool.tags" :key="tag" class="theindex-badge badge-tag">
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
        <p><strong>Megathread</strong> — Guia de Privacidade e Segurança Digital.</p>
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
