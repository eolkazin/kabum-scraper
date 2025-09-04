from playwright.sync_api import sync_playwright
import pandas as pd
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.kabum.com.br/")

    time.sleep(5)  # espera a página carregar

    # Nomes dos produtos
    nomes_locator = page.locator("h3 span")

    # Preços dos produtos
    precos_locator = page.locator("span.sc-57f0fd6e-2.hjJfoh.priceCard")

    total = nomes_locator.count()
    print(f"Quantidade de produtos: {total}")

    nomes = []
    precos = []

    for i in range(total):
        nomes.append(nomes_locator.nth(i).inner_text())
        precos.append(precos_locator.nth(i).inner_text())

    # Criar DataFrame
    df = pd.DataFrame({
        "Nome": nomes,
        "Preço": precos
    })

    # Salvar em Excel
    df.to_excel("produtos_kabum.xlsx", index=False)
    print("Planilha gerada: produtos_kabum.xlsx")

    browser.close()
