# --- Importe a biblioteca 'requests' para fazer requisições HTTP ---
# Se você ainda não tem, instale-a com o comando:
# pip install requests
import requests

def obter_ip_publico():
    """
    Função que consulta um serviço online para obter o IP público.
    """
    try:
        # --- Fazendo uma requisição GET para a API do ipify.org ---
        # Este serviço retorna apenas o seu IP público em texto simples.
        response = requests.get('https://api.ipify.org')

        # --- Verificando se a requisição foi bem-sucedida ---
        if response.status_code == 200:
            # O IP está no corpo da resposta
            ip_publico = response.text
            print(f"O seu endereço IP público é: {ip_publico}")
            return ip_publico
        else:
            print(f"Não foi possível obter o IP. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # --- Lidando com erros de conexão (ex: sem internet) ---
        print(f"Erro de conexão: {e}")
        return None

# --- Chamando a função para executar o bot ---
if __name__ == "__main__":
    obter_ip_publico()

