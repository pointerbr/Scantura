#!/usr/bin/env python3
import socket
import argparse
import time

class color:
	Preto = "\033[1;30m"
	Vermelho = "\033[1;31m"
	Verde = "\033[1;32m"
	Amarelo = "\033[1;33m"
	Azul = "\033[1;34m"
	Magenta = "\033[1;35m"
	Cyan = "\033[1;36m"
	Branco_Cinza_Claro = "\033[1;37m"
	Negrito = "\033[1m"

exemplos = f"""
{color.Negrito}
manual
{color.Amarelo}

{color.Branco_Cinza_Claro}
"""
um_pequeno_texto_inicial = f"""
{color.Vermelho}
________________________________________________________________________
Olá, eu soi pointer(criador da ferramenta) eu criei essa ferramenta para ajudar muito em pentest, analise de rede, ajudar muito vocês nisso, então nessa ferramenta ainda será adicionado mais coisas no momento ainda está em desenvolvimento e irei adicionar mais coisas mo futuro a frente.
------------------------------------------------------------------------
{color.Branco_Cinza_Claro}
"""

art = f"""{color.Azul}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠃⠀⠀⠀⡁⠀⠀⠀⠀⠀⠐⠆⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢔⡤⠊⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠁⠀⠀⠘⠁⢀⠀⠀⠀⠀⢈⠓⠂⠠⡄⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠿⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠁⠀⠠⡚⠁⢀⣙⣀⣈⡩⠬⢁⠀⢑⠶⠤⡆⠤⡀⠀⠀⠀⠀⠀⠀⢀⠴⢲⣋⣽⣷⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢠⠀⠀⣶⠃⠗⣡⣶⣮⣿⡿⠿⠿⢿⣿⣷⣶⣤⣤⠤⠴⠦⠬⣤⣤⠄⣉⠉⠝⢲⣿⡷⠻⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠁⡀⡸⠁⣰⣿⡿⠛⠋⣁⡀⠤⠤⢄⡀⠈⠛⢯⣿⣟⣾⣶⣶⣮⣭⣵⣾⣿⣟⠿⠉⢨⠖⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⢠⠳⡧⣻⡿⠋⢀⠒⠉⠀⠀⠀⠀⠀⠀⠉⠢⠀⠀⠙⠛⣻⣿⣿⣿⢿⣿⣿⠟⡱⠖⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢠⣧⠓⣾⣿⠁⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢦⣠⣾⣿⠿⣿⣿⣿⡿⣫⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠂⢃⣸⣿⠇⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⠟⢿⠁⠸⡿⣿⣯⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢘⡄⠘⣿⣿⠀⠸⡀⠀⠀⠀⠀⠀⢀⣀⣴⣾⣿⡿⡟⡋⠐⡇⠀⢸⣿⣿⠃⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠘⢰⣿⡿⡆⠀⣇⠀⣀⣠⣤⣶⣿⢷⢟⠻⠀⠈⠀⠀⠀⡇⠀⣼⣿⣿⠂⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⢀⡴⢯⣾⠟⡏⢀⣠⣿⣿⣿⣟⢟⡋⠅⠘⠉⠀⠀⠀⠀⢀⠀⠁⢠⣿⣟⠃⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⣻⣷⡿⢙⣩⣶⡿⠿⠛⠉⠑⢡⡁⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⣾⣥⣾⢫⡦⠾⠛⠙⠉⠀⠀⢀⣀⠀⠈⠙⠓⠦⠤⠤⠀⠘⠁⢀⡤⣾⡿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠔⣴⣾⣿⣿⢟⢝⠢⠃⢀⣤⢴⣾⣮⣷⣶⢿⣶⡤⣐⡀⠀⣠⣤⢶⣪⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⣦⣾⡿⡛⠵⠺⢈⡠⠶⠿⠥⠥⡭⠉⠉⢱⡛⠻⠿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠭⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⢴⠕⣋⠝⠕⠐⠀⠔⠉⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠉⠁⠁⠁⠁⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣠⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
print(art)
print(um_pequeno_texto_inicial)
print(exemplos)

portas_mais_utilizadasTCP_UDP = [20,21,22,23,25,53,67,68,69,80,110,111,123,135,137,138,139,143,161,162,443,445,500,514,520,631,993,995,1434,1723,1900,3306,3389,4500,5900,8080,49152]

principais_portas_web = [80 , 443 , 8009 , 8180 , 81 , 300 , 591 , 593 , 832 , 981 , 1010 , 1311 , 2082 , 2087 , 2095 , 2096 , 2480 , 3000 , 3128 , 3333 , 4243 , 4567 , 4711 , 4712 , 4993 , 5000 , 5104 , 5108 , 5800 , 6543 , 7000 , 7396 , 7474 , 8000 , 8001 , 8008 , 8014 , 8042 , 8069 , 8080 , 8081 , 8088 , 8090 , 8091 , 8118 , 8123 , 8172 , 8222 , 8243 , 8280 , 8281 , 8333 , 8443 , 8500 , 8834 , 8880 , 8888 , 8983 , 9000 , 9043 , 9060 , 9080 , 9090 , 9091 , 9200 , 9443 , 9800 , 9981 , 12443 , 16080 , 18091 , 18092 , 20720 , 28017]

todas_as_portas_TCP = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,8009,8180,81,300,591,593,832,981,1010,1311,2082,2087,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993]

UDP_ports = [
    53, 67, 68, 69, 123, 137, 138, 161, 162,
    500, 514, 520, 1194, 1812, 1813, 1900,
    3478, 4500, 5060
]

comum_ports = list(range(1, 1025))

all_ports = list(range(1,65536))

port_modes = {
    "all": all_ports,
    "all-tcp": todas_as_portas_TCP,
    "all-udp": UDP_ports,
    "web": principais_portas_web,
    "top": portas_mais_utilizadasTCP_UDP,
    "_": comum_ports
}

Portas_inseguras = {
    20: "FTP-DATA - transferência sem criptografia",
    21: "FTP - credenciais podem trafegar sem criptografia",
    23: "TELNET - comunicação sem criptografia",
    69: "TFTP - sem autenticação nativa",
    110: "POP3 - pode transmitir credenciais sem TLS",
    111: "RPCbind - exposição de serviços RPC",
    137: "NetBIOS Name Service - exposição de informações",
    138: "NetBIOS Datagram - protocolo legado",
    139: "NetBIOS Session - compartilhamento legado",
    143: "IMAP - pode transmitir credenciais sem TLS",
    161: "SNMP - comunidades e informações expostas",
    162: "SNMP Trap - informações de monitoramento",
    389: "LDAP - pode operar sem TLS",
    512: "REXEC - execução remota de comandos",
    513: "RLOGIN - acesso remoto legado",
    514: "RSH/Syslog - serviço legado ou sem proteção",
    515: "LPD - serviço de impressão legado",
    520: "RIP - protocolo de roteamento",
    623: "IPMI - interface de gerenciamento",
    2049: "NFS - compartilhamento de arquivos",

 
    3389: "RDP - acesso remoto",
    5900: "VNC - acesso remoto gráfico",
    5901: "VNC - acesso remoto gráfico",
    5902: "VNC - acesso remoto gráfico",
    10000: "Webmin - painel administrativo",

    
    1433: "Microsoft SQL Server - banco de dados",
    1521: "Oracle Database - banco de dados",
    3306: "MySQL - banco de dados",
    5432: "PostgreSQL - banco de dados",
    6379: "Redis - armazenamento em memória",
    9200: "Elasticsearch - mecanismo de busca",
    27017: "MongoDB - banco de dados",

   
    2375: "Docker API - API sem TLS",
    2376: "Docker API - verificar autenticação e TLS",
    3000: "Aplicação web ou painel administrativo",
    4848: "GlassFish Admin - painel administrativo",
    5000: "Aplicação web ou API",
    8080: "HTTP alternativo ou proxy",
    8089: "Splunk - serviço de gerenciamento",
    8443: "HTTPS alternativo ou painel administrativo",
    8888: "HTTP alternativo ou painel administrativo",
    9090: "Prometheus ou painel administrativo",
    9091: "Serviço de monitoramento",
    11211: "Memcached - serviço de cache",
    15672: "RabbitMQ Management - painel administrativo",
    1883: "MQTT - comunicação sem TLS",
    2379: "etcd - armazenamento de configuração",
    2380: "etcd - comunicação entre membros",
    5672: "RabbitMQ AMQP - mensageria",
    9092: "Kafka - mensageria"
}


arg = argparse.ArgumentParser()

arg.add_argument("--address", dest="ip", type=str,  help="coloque o ip ou dominio determinado", default=None)
arg.add_argument("--address6", dest="ipv6", type=str, help="coloque seu ip do tipo ipv6 ", nargs="+")
arg.add_argument("--port", dest="port", type=str, help="colque a porta determinada", nargs="+", default=None)
arg.add_argument("--options", type=int, choices=range(1, 7), required=True)

args = arg.parse_args()

def port_scanner(ip, port):
	if ip is None:
		print("Coloque o IP")
		return
		
	if args.port is None:
		ports = comum_ports
	elif len(args.port) == 1 and args.port[0] in port_modes:
		ports = port_modes[args.port[0]]

	else:
    try:
    	ports = [int(p) for p in args.port]
    except ValueError:
        arg.error("Informe portas numéricas ou um modo válido.")
        
	try:
		for p in port:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
				sock.settimeout(0.5)
				scanner = sock.connect_ex((ip, p))
				if scanner == 0:
					print(f"[ + ] porta {p} aberta")
	except OSError as erro:
		print(f"erro {erro}")
		
def vulnerability_sca_ip(args.ip, port):
	if ip is None:
		print("Coloque o IP")
		return
		
	if args.port is None:
    ports = comum_ports
	try:
			for v in port:
				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock2:
					sock2.settimeout(0.5)
					scanner = sock2.connect_ex((ip, v))
					if scanner == 0 and v in Portas_inseguras:
						print(f"[ + ]  vulns: {Portas_inseguras[v]}")
	except OSError as erro:
		print(f"erro {erro}")