import { fileURLToPath, URL } from 'node:url';

import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import { defineConfig, type Plugin } from 'vite';
import { frameFoot, frameHead, frameTop, inlineIcons } from './site-frame';

const path = (file: string) => fileURLToPath(new URL(file, import.meta.url));

// Writes the shared site frame and the Lucide icons into the site pages' HTML, so the first paint is complete.
const kerfFrame = (): Plugin => ({
  name: 'kerf-frame',
  transformIndexHtml: {
    order: 'pre',
    handler: (html) =>
      inlineIcons(
        html
          .replace('<!--kerf:head-->', frameHead())
          .replace(/<!--kerf:top:(player|design)-->/, (_, page: 'player' | 'design') => frameTop(page))
          .replace('<!--kerf:foot-->', frameFoot()),
      ),
  },
});

// The workbench in apps/preview serves the app; `@/` imports reach the skin in src/.
export default defineConfig({
  root: path('./apps/preview'),
  // Relative URLs, so the build works at a domain root or in a subfolder such as GitHub Pages.
  base: './',
  plugins: [kerfFrame(), tailwindcss(), react()],
  resolve: {
    alias: {
      '@preview': path('./apps/preview/src'),
      '@': path('./src'),
    },
  },
  server: {
    fs: { allow: [path('.')] },
  },
  build: {
    outDir: path('./dist'),
    emptyOutDir: true,
    rolldownOptions: {
      // The workbench shell, and the preview page it frames.
      // The Kerf site (player and design pages), the CLI workbench, and the preview page it frames.
      input: {
        index: path('./apps/preview/index.html'),
        design: path('./apps/preview/design.html'),
        workbench: path('./apps/preview/workbench.html'),
        preview: path('./apps/preview/preview.html'),
      },
    },
  },
});
