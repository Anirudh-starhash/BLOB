import { fileURLToPath } from 'node:url'
import { mergeConfig, defineConfig, configDefaults } from 'vitest/config'
import viteConfig from './vite.config'

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      environment: 'jsdom',  // Setting test environment to jsdom
      exclude: [...configDefaults.exclude, 'e2e/**'],  // Exclude e2e tests
      root: fileURLToPath(new URL('./', import.meta.url)),  // Set root for tests
    },
  }),
)
