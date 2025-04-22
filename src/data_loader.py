import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados tabulares

# Função para carregar os dados dos arquivos CSV
def load_data(product_path, specs_path):
    products = pd.read_csv(product_path)  # Lê o CSV dos produtos
    specs = pd.read_csv(specs_path)       # Lê o CSV das especificações técnicas
    return products, specs                # Retorna os dois DataFrames

# Função para mesclar os dados dos produtos com suas especificações técnicas
def merge_data(products, specs):
    merged_docs = []  # Lista onde os documentos combinados serão armazenados

    # Itera por cada linha do DataFrame de produtos
    for _, row in products.iterrows():
        name = row['product_name']        # Nome do produto
        code = row['product_code']        # Código do produto
        price = row['price']              # Preço do produto
        availability = row['availability']# Disponibilidade do produto

        # Tenta encontrar uma especificação cuja 'product_group' esteja contida no 'product_name'
        matched_specs = specs[specs['product_group'].apply(lambda g: g.lower() in name.lower())]

        # Se encontrou alguma correspondência, pega as especificações técnicas
        if not matched_specs.empty:
            tech = matched_specs.iloc[0]['technical_details']
        else:
            tech = "Sem especificações técnicas disponíveis."  # Caso contrário, usa uma mensagem padrão

        # Concatena todas as informações em um único texto para cada produto
        doc = (
            f"{name} (código {code}): R$ {price}, disponibilidade: {availability}. "
            f"Especificações: {tech}"
        )
        merged_docs.append(doc)  # Adiciona o documento à lista

    return merged_docs  # Retorna todos os documentos prontos para serem usados como contexto
