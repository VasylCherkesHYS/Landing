import { resolve } from 'path';

export default {
  build: {
    outDir: '../distributor/static/ada',
    assetsDir: 'assets',
    manifest: true,
    emptyOutDir: true,
    rollupOptions: {
      input: resolve(__dirname, 'main.js'),
    },
  },
};
