#!/bin/bash
echo "--- Configurando Cyber Duende v7.0 ---"
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install requests
git clone https://github.com/tonibanderitas46-ai/CyberDuende-v7.git
cd CyberDuende-v7
echo "--- Instalación Completa. Iniciando... ---"
python duende.py
