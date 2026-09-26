// ============================================================================
// PROJECT:     Nakayama Festa - A Piracy Megathread
// Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
// Description: VitePress project configuration and theme settings.
// Version:     0.1 (09.2026)
// ============================================================================

import { OramaPlugin } from "@orama/plugin-vitepress";

export default {
  head: [
    [
      "link",
      {
        rel: "icon",
        media: "(prefers-color-scheme: light)",
        href: "/favicon.ico",
      },
    ],
    [
      "link",
      {
        rel: "icon",
        media: "(prefers-color-scheme: dark)",
        href: "/favicon-dark.ico",
      },
    ],
    ["meta", { name: "theme-color", content: "#050508" }],
    ["meta", { property: "og:type", content: "website" }],
    ["meta", { property: "og:locale", content: "pt_BR" }],
    ["meta", { property: "og:site_name", content: "Nakayama Festa — A Piracy Megathread" }],
    ["meta", { property: "og:title", content: "Nakayama Festa — A Piracy Megathread" }],
    ["meta", { property: "og:description", content: "O portal definitivo de recursos, ferramentas livres, preservação digital e privacidade da internet em português." }],
    ["meta", { property: "og:image", content: "/img/lain_cyberia.png" }],
    ["meta", { name: "twitter:card", content: "summary_large_image" }],
    ["meta", { name: "twitter:title", content: "Nakayama Festa — A Piracy Megathread" }],
    ["meta", { name: "twitter:description", content: "O portal definitivo de recursos, ferramentas livres, preservação digital e privacidade da internet em português." }],
    ["meta", { name: "twitter:image", content: "/img/lain_cyberia.png" }],
  ],
  vite: {
    plugins: [OramaPlugin()],
    server: {
      host: '0.0.0.0',
      port: 5173,
      allowedHosts: true
    }
  },
  base: "/",
  lang: "pt-BR",
  title: "Nakayama Festa — A Piracy Megathread",
  description:
    "O portal definitivo de recursos digitais, softwares livres, guias, mídia e privacidade da internet em português.",
  ignoreDeadLinks: true,
  cleanUrls: true,
  lastUpdated: true,
  externalLinkIcon: true,
  themeConfig: {
    domain: "pirataria.megathread.com.br",
    lastUpdatedText: "Última atualização em",
    logo: "/logo.svg",
    siteTitle: "Megathread",
    nav: [
      {
        text: "Guias",
        link: "guias",
      },
      {
        text: "Privacidade",
        link: "privacidade",
      },
      {
        text: "Sobre",
        link: "sobre",
      },
    ],
    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/Apfelstrudelzinho/nakayama-festa",
      },
    ],
    sidebar: [
      {
        text: "Tópicos Principais",
        collapsible: true,
        items: [
          { text: "🧭 Uso Geral", link: "uso-geral" },
          { text: "🎦 Filmes, Séries & TV", link: "filmes-series-tv" },
          { text: "🎮 Jogos & Emulações", link: "jogos-emulacoes" },
          { text: "⛩️ Anime & Mangá", link: "otaku" },
          { text: "📚 Livros & Quadrinhos", link: "livros" },
          { text: "🧠 Cursos & Educação", link: "educacional" },
          { text: "🎹 Música & Áudio", link: "musica" },
          { text: "🧰 Utilitários", link: "utilitarios" },
          { text: "🌊 Trackers & Warez", link: "trackers-warez" },
          { text: "🤖 Inteligência Artificial", link: "inteligencia-artificial" },
          { text: "🐧 Linux, Mac & Mobile", link: "linux-mac-mobile" },
          { text: "🔞 Adulto (+18)", link: "adulto" },
        ],
      },
      {
        text: "Portais & Guias",
        collapsible: true,
        items: [
          { text: "🗺️ Guias & Tutoriais", link: "guias" },
          { text: "🔒 Privacidade & Segurança", link: "privacidade" },
          { text: "📖 Sobre & Fontes", link: "sobre" },
        ],
      },
    ],
    editLink: {
      pattern:
        "https://github.com/Apfelstrudelzinho/nakayama-festa/edit/main/docs/:path",
      text: "Edite essa página no GitHub",
    },
    docFooter: {
      prev: false,
      next: false,
    },
    footer: {
      message: "Megathread — O maior índice de recursos em português",
    },
    markdown: {
      attrs: false,
      theme: "material-palenight",
      lineNumbers: true,
    },
    returnToTopLabel: "Voltar para o topo",
    sidebarMenuLabel: "Menu",
  },
  sitemap: {
    hostname: "https://pirataria.megathread.com.br",
  },
};
