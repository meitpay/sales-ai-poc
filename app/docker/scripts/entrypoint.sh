#!/bin/zsh

if [[ "${NODE_ENV}" == "production" ]]; then
  npm run preview
else
  npm install
  npm run dev
fi
