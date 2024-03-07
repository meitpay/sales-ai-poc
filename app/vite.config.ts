import { defineConfig, loadEnv, UserConfig, ConfigEnv } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig(({ mode }: ConfigEnv): UserConfig => {
  const env = loadEnv(mode, process.cwd());

  const port = parseInt(env.VITE_APP_PORT, 10) || 3000;

  return {
    plugins: [react()],
    server: {
      host: env.VITE_APP_URL || true,
      port: port,
      cors: true,
    },
  };
});
