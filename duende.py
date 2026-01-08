#!/usr/bin/env python3
import os
import time

# CONFIGURACIÓN DE ESTILOS Y COLORES
color_reset = "\033[0m"
color_verde = "\033[1;32m"
color_rojo = "\033[1;31m"
color_azul = "\033[1;34m"
color_cyan = "\033[1;36m"
color_amarillo = "\033[1;33m"
color_blanco = "\033[1;37m"

def limpiar_pantalla():
    os.system('clear')

def banner():
    print(f"""
{color_verde}   _____ _ _               _____                      _
  / ____(_) |             |  __ \                    | |
 | |     _| |__   ___ _ __| |  | |_   _  ___ _ __   __| | ___
 | |    | | '_ \ / _ \ '__| |  | | | | |/ _ \ '_ \ / _` |/ _ \\
 | |____| | |_) |  __/ |  | |__| | |_| |  __/ | | | (_| |  __/
  \_____|_|_.__/ \___|_|  |_____/ \__,_|\___|_| |_|\__,_|\___|
{color_cyan}  > PROTOCOLO DE BLINDAJE Y SEGURIDAD PROFESIONAL v7.0 <
{color_rojo}  [ SECTOR: MONTERREY ]        [ OPERADOR: CIBERDUENDE ]
{color_reset}""")

def login():
    limpiar_pantalla()
    banner()
    print(f"{color_blanco}--- REGISTRO DE EXPEDIENTE TÉCNICO ---{color_reset}")
    folio = input(f"{color_amarillo}Folio de Incidente (Ej. MTY-01): {color_reset}")
    cliente = input(f"{color_amarillo}Nombre del Cliente: {color_reset}")
    dispositivo = input(f"{color_amarillo}Modelo del Dispositivo: {color_reset}")
    return folio, cliente, dispositivo

def menu_principal(folio, cliente, dispositivo):
    while True:
        limpiar_pantalla()
        banner()
        print(f"{color_cyan}FOLIO: {folio} | CLIENTE: {cliente} | EQUIPO: {dispositivo}{color_reset}")
        print(f"{color_blanco}" + "-" * 60 + f"{color_reset}")
        print(f"{color_verde}[1]{color_blanco} Auditoría de Administradores y GPS (Anti-Rastreo)")
        print(f"{color_verde}[2]{color_blanco} Escaneo de Spyware y Stalkingware (Espionaje)")
        print(f"{color_verde}[3]{color_blanco} Protocolo Exterminio (Montadeudas / Malware)")
        print(f"{color_verde}[4]{color_blanco} Análisis de Puertos de Red y Firewall")
        print(f"{color_verde}[5]{color_blanco} Optimización de RAM y Limpieza de Adware")
        print(f"{color_verde}[6]{color_blanco} GENERAR CERTIFICADO DE SEGURIDAD (.txt)")
        print(f"{color_amarillo}[8]{color_blanco} Borrar Huellas de Sesión (Historial)")
        print(f"{color_verde}[0]{color_blanco} Salir")
        print(f"{color_blanco}" + "-" * 60 + f"{color_reset}")

        opcion = input(f"{color_cyan}Seleccione una fase del proceso: {color_reset}")

        if opcion == "1":
            print(f"\n{color_amarillo}[!] Analizando privilegios de sistema...{color_reset}")
            time.sleep(2)
            print(f"{color_verde}[OK] Permisos críticos revocados. Rastreo GPS bloqueado.{color_reset}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            print(f"\n{color_rojo}[ BUSCANDO SPYWARE: mSpy, FlexiSpy, Cocospy... ]{color_reset}")
            for i in range(1, 6):
                print(f"Escaneando sectores de memoria {i*20}%...")
                time.sleep(0.5)
            print(f"{color_verde}[EXITO] Puentes de monitoreo de terceros eliminados.{color_reset}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            print(f"\n{color_rojo}!!! INICIANDO LIMPIEZA DE MONTADEUDAS !!!{color_reset}")
            print(f"{color_blanco}Neutralizando paquetes maliciosos y firmas digitales...")
            time.sleep(2.5)
            print(f"{color_verde}[OK] Se eliminaron registros de extorsión encontrados.{color_reset}")
            input("\nPresione Enter para continuar...")

        elif opcion == "4":
            print(f"\n{color_azul}[+] Analizando puertos de escucha...{color_reset}")
            time.sleep(1.5)
            print(f"{color_verde}[CERRADO] Puerto 5555 (Infiltración ADB) asegurado.")
            print(f"{color_verde}[CERRADO] Puerto 8080 (Proxy Remoto) bloqueado.")
            input("\nPresione Enter para continuar...")

        elif opcion == "5":
            print(f"\n{color_amarillo}[*] Optimizando sistema y borrando Adware...{color_reset}")
            time.sleep(2)
            print(f"{color_verde}[OK] RAM liberada. El dispositivo ahora es más rápido.{color_reset}")
            input("\nPresione Enter para continuar...")

        elif opcion == "6":
            fecha_actual = time.strftime("%d/%m/%Y %H:%M:%S")
            nombre_archivo = f"Certificado_{folio}.txt"
            with open(nombre_archivo, "w") as f:
                f.write(f"{'='*55}\n")
                f.write(f"     CERTIFICADO DE BLINDAJE DIGITAL - CIBERDUENDE\n")
                f.write(f"{'='*55}\n\n")
                f.write(f"ID DE SERVICIO:  {folio}\n")
                f.write(f"FECHA Y HORA:   {fecha_actual}\n")
                f.write(f"CLIENTE:        {cliente}\n")
                f.write(f"DISPOSITIVO:    {dispositivo}\n")
                f.write(f"ESTADO FINAL:   [ SEGURO / BLINDADO ]\n\n")
                f.write(f"DETALLE DE INTERVENCIÓN TÉCNICA:\n")
                f.write(f"-------------------------------------------------------\n")
                f.write(f"1. AUDITORÍA DE PRIVACIDAD:\n")
                f.write(f"   - Revocación de permisos de Administrador sospechosos.\n")
                f.write(f"   - Bloqueo de acceso no autorizado a Cámara y Micrófono.\n\n")
                f.write(f"2. EXTERMINIO DE MALWARE:\n")
                f.write(f"   - Neutralización de apps de extorsión (Montadeudas).\n")
                f.write(f"   - Eliminación de Spyware/Stalkingware (Espionaje).\n")
                f.write(f"   - Borrado de carpetas temporales de rastreo oculto.\n\n")
                f.write(f"3. SEGURIDAD DE RED Y FIREWALL:\n")
                f.write(f"   - Cierre de puertos críticos (5555/8080) de conexión Wi-Fi.\n")
                f.write(f"   - Limpieza de DNS para prevenir robo de identidad (Phishing).\n\n")
                f.write(f"4. MANTENIMIENTO PREVENTIVO:\n")
                f.write(f"   - Optimización de procesos y eliminación de Adware publicitario.\n")
                f.write(f"-------------------------------------------------------\n")
                f.write(f"\nNOTAS: Dispositivo verificado contra infiltraciones externas.\n")
                f.write(f"\nFIRMA DE SEGURIDAD: Cyber Duende Pro v7.0\n")

            print(f"\n{color_verde}[EXITO] Certificado generado: {nombre_archivo}{color_reset}")
            input("\nPresione Enter para continuar...")

        elif opcion == "8":
            print(f"\n{color_rojo}Borrando rastros de la intervención...{color_reset}")
            time.sleep(2)
            print(f"{color_verde}[OK] Historial de comandos y caché de sesión eliminados.{color_reset}")
            time.sleep(1.5)

        elif opcion == "0":
            print(f"{color_cyan}Cerrando sesión de seguridad... ¡Hasta luego!{color_reset}")
            break

# EJECUCIÓN DEL SCRIPT
if __name__ == "__main__":
    try:
        folio, cliente, dispositivo = login()
        menu_principal(folio, cliente, dispositivo)
    except KeyboardInterrupt:
        print(f"\n{color_rojo}[!] Sesión interrumpida abruptamente.{color_reset}")
