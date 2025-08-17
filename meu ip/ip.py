# -*- coding: utf-8 -*-
#
# Importa as bibliotecas necess\u00E1rias para a automa\u00E7\u00E3o web
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def run_twitch_viewer_bot():
    """
    Fun\u00E7\u00E3o que monitora o n\u00FAmero de espectadores em um canal da Twitch.
    """
    # Define a URL do canal que voc\u00EA deseja monitorar
    STREAM_URL = "https://www.twitch.tv/paidefamiliarj24"

    # --- Configura\u00E7\u00F5es do Chrome para rodar em modo headless ---
    # O modo headless permite que o bot execute sem abrir uma janela do navegador.
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = None
    try:
        # --- Inicializa o driver do Chrome ---
        driver = uc.Chrome(options=options)
        
        print("Acessando o canal da Twitch...")
        driver.get(STREAM_URL)
        
        # Espera um pouco para a p\u00E1gina carregar completamente
        time.sleep(15)
        
        print(f"Monitorando o canal: {driver.title}")

        # Vari\u00E1vel para armazenar a contagem de espectadores anterior
        last_viewer_count = None
        
        # --- Loop principal para verificar os espectadores ---
        while True:
            try:
                # O seletor CSS foi atualizado com base no novo c\u00F3digo da Twitch
                viewer_element = driver.find_element(By.CSS_SELECTOR, "strong[data-a-target='animated-channel-viewers-count']")
                current_viewer_count = viewer_element.text
                
                # Compara a contagem atual com a contagem anterior
                if current_viewer_count != last_viewer_count:
                    print(f"[{time.strftime('%H:%M:%S')}] N\u00FAmero de espectadores: {current_viewer_count}")
                    last_viewer_count = current_viewer_count # Atualiza a contagem anterior
                
            except NoSuchElementException:
                # Caso o elemento n\u00E3o seja encontrado (por exemplo, se o canal estiver offline)
                if last_viewer_count is not None:
                    print(f"[{time.strftime('%H:%M:%S')}] N\u00E3o foi poss\u00EDvel encontrar o contador de espectadores. O canal pode ter ficado offline.")
                    last_viewer_count = None
            
            # Pausa o bot por 30 segundos
            time.sleep(5)
            
    except Exception as e:
        # --- Lida com poss\u00EDveis erros gerais ---
        print(f"Ocorreu um erro: {e}")

    finally:
        # --- Garante que o driver seja fechado ---
        if driver:
            print("Driver do navegador fechado.")
            driver.quit()

# --- Executa a fun\u00E7\u00E3o principal do bot ---
if __name__ == "__main__":
    run_twitch_viewer_bot()

