import { fileURLToPath } from 'node:url'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

const webRoot = fileURLToPath(new URL('./frontend', import.meta.url))

// https://vite.dev/config/
export default defineConfig({
  root: webRoot,
  plugins: [react()],
})
