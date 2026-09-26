// ============================================================================
// PROJECT:     Nakayama Festa - A Piracy Megathread
// Author:      Christian Stadler (Apfelstrudel / Apfelstrudelzinho)
// Description: Custom VitePress theme setup and global component registration.
// Version:     0.1 (09.2026)
// ============================================================================

import DefaultTheme from "vitepress/theme";
import MyLayout from './MyLayout.vue';
import NakayamaApp from './components/NakayamaApp.vue';
import NakayamaGuias from './components/NakayamaGuias.vue';
import NakayamaPrivacidade from './components/NakayamaPrivacidade.vue';
import NakayamaCategoryPage from './components/NakayamaCategoryPage.vue';
import NakayamaSobre from './components/NakayamaSobre.vue';
import "./custom.css";
import "./components/nakayama-shared.css";

export default {
  extends: DefaultTheme,
  Layout: MyLayout,
  enhanceApp({ app }) {
    app.component('NakayamaApp', NakayamaApp);
    app.component('NakayamaGuias', NakayamaGuias);
    app.component('NakayamaPrivacidade', NakayamaPrivacidade);
    app.component('NakayamaCategoryPage', NakayamaCategoryPage);
    app.component('NakayamaSobre', NakayamaSobre);

    // Backward compatibility aliases
    app.component('TheIndexApp', NakayamaApp);
    app.component('TheIndexGuias', NakayamaGuias);
    app.component('TheIndexPrivacidade', NakayamaPrivacidade);
    app.component('TheIndexCategoryPage', NakayamaCategoryPage);
    app.component('TheIndexSobre', NakayamaSobre);
  }
};
