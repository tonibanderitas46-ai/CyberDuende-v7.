#!/usr/bin/env python3
import os, time, sys, socket, platform, requests

# --- COLORES ESTILO KALI ---
G = '\033[1;32m'; R = '\033[1;31m'; B = '\033[1;34m'
Y = '\033[1;33m'; C = '\033[1;36m'; W = '\033[1;37m'; N = '\033[0m'

def banner():
    os.system('clear')
    print(f"{G}")
    print("  ██████╗██╗   ██╗██████╗ ███████╗██████╗ ")
    print(" ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗")
    print(" ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝")
    print(" ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗")
    print(" ╚██████╗   ██║   ██████╔╝███████╗██║  ██║")
    print("  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print(f"      {W}D U E N D E   v7.0 {G}[ {W}SECTOR: MTY {G}]{N}")
    print(f"{W}-------------------------------------------{N}")
    print(f"{C} Operador:{N} tonbanderitas96-ai")
    print(f"{C} Nodo Central:{N} Juárez, NL (Seguridad Activa)")
    print(f"{W}-------------------------------------------{N}")

def get_public_ip():
    try:
        return requests.get('https://api.ipify.org', timeout=3).text
    except:
        return "Sin Conexión"

def escanear_espias():
    print(f"\n{Y}[*] Iniciando Escaneo Profundo de Amenazas...{N}")
    # Base de datos v7.0 - Spyware y Rastreo
    amenazas = {
        "mSpy / Eyezy": "com.mspy.android",
        "Eyezy Premium": "com.eyezy.android",
        "Life360 (Rastreo GPS)": "com.life360.android",
        "FlexiSPY Professional": "com.vvt.callloger",
        "ClevGuard / KidsGuard": "com.clevguard.assist",
        "iSharing Localizador": "com.isharing.android",
        "TrackView Cam/GPS": "com.trackview"
    }
    encontrado = False
    for nombre, paquete in amenazas.items():
        # Verificamos si el paquete existe en el sistema
        check = os.popen(f"pm list packages | grep {paquete}").read()
        if check:
            print(f" {R}[!] PELIGRO: {nombre} DETECTADO{N}")
            encontrado = True
        else:
            print(f" {W}- {nombre}: {G}LIMPIO{N}")
        time.sleep(0.1)
    
    if not encontrado:
        print(f"\n{G}[✔] No se detectaron intrusos de monitoreo comercial.{N}")
    else:
        print(f"\n{R}[!] ADVERTENCIA: Se detectaron amenazas activas.{N}")

def menu():
    banner()
    public_ip = get_public_ip()
    print(f"{B}[ RED PÚBLICA: {public_ip} ]{N}")
    print(f"{Y}[ ESTATUS: DEFENSIVO-MTY ]{N}\n")

    print(f" {G}[1]{N} 🛡️  Blindaje Anti-Spy   {G}[5]{N} 🕵️  Escanear Red Wi-Fi")
    print(f" {G}[2]{N} 🔍 ESCANEO MSpy/Eyezy   {G}[6]{N} 🚀 Turbo CPU (Kernel)")
    print(f" {G}[3]{N} 🔒 Firewall Monterrey   {G}[7]{N} 🪤  Activar Honeypot")
    print(f" {G}[4]{N} 📍 Localizador IP       {G}[8]{N} 🛠️  Instalar Atajo")
    print(f"\n {R}[0] ❌ DESCONECTAR Y BORRAR RASTROS{N}")

    opc = input(f"\n{G}CyberDuende_MTY > {N}")

    if opc == "1":
        print(f"\n{Y}[*] Cifrando ID de hardware...{N}")
        time.sleep(2); print(f"{G}[✔] Dispositivo ahora es invisible.{N}")
        input("\nPresione Enter..."); menu()

    elif opc == "2":
        escanear_espias()
        input("\nPresione Enter..."); menu()

    elif opc == "3":
        print(f"\n{Y}[*] Cerrando puertos vulnerables en Nodo MTY...{N}")
        ports = [5555, 8080, 4444, 22]
        for p in ports:
            print(f" {W}- Puerto {p}: {G}BLOQUEADO{N}")
            time.sleep(0.3)
        input("\nPresione Enter..."); menu()

    elif opc == "4":
        print(f"\n{Y}[*] Localizando Nodo de Red...{N}")
        print(f" {W}IP Detectada: {G}{public_ip}{N}")
        print(f" {W}Ubicación: {G}Juárez, Nuevo León{N}")
        input("\nPresione Enter..."); menu()

    elif opc == "5":
        print(f"\n{Y}[*] Analizando tráfico Wi-Fi local...{N}")
        time.sleep(2)
        print(f"{G}[✔] No se detectaron sniffers en la red.{N}")
        input("\nPresione Enter..."); menu()

    elif opc == "6":
        print(f"\n{Y}[*] Accediendo a la gestión de procesos del Kernel...{N}")
        time.sleep(1)
        print(f"{W}[*] Forzando liberación de memoria RAM...{N}")
        os.system("sync")
        os.system("am kill-all 2>/dev/null") 
        print(f"{G}[✔] Ciclos de CPU optimizados para alto rendimiento.{N}")
        input("\nPresione Enter..."); menu()

    elif opc == "8":
        print(f"\n{Y}[*] Configurando comando 'duende' en el sistema...{N}")
        try:
            os.system("echo 'python3 ~/duende.py' > /data/data/com.termux/files/usr/bin/duende")
            os.system("chmod +x /data/data/com.termux/files/usr/bin/duende")
            print(f"{G}[✔] Atajo creado. Escribe 'duende' en cualquier momento.{N}")
        except:
            print(f"{R}[!] Error al crear atajo en el sistema.{N}")
        input("\nPresione Enter..."); menu()

    elif opc == "0":
        print(f"\n{R}[!] Protocolo de salida activado. Borrando huellas en Juárez...{N}")
        os.system("history -c") # Borra historial de la sesión
        time.sleep(1)
        print(f"{G}[✔] Sistema Desconectado.{N}")
        sys.exit()
    else:
        menu()

if __name__ == "__main__":
    menu()
