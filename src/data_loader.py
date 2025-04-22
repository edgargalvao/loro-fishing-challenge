import pandas as pd

def load_data(product_path, specs_path):
    products = pd.read_csv(product_path)
    specs = pd.read_csv(specs_path)
    return products, specs

def merge_data(products, specs):
    merged_docs = []

    for _, row in products.iterrows():
        name = row['product_name']
        code = row['product_code']
        price = row['price']
        availability = row['availability']

        # Match por substring entre 'product_group' e 'product_name'
        matched_specs = specs[specs['product_group'].apply(lambda g: g.lower() in name.lower())]

        if not matched_specs.empty:
            tech = matched_specs.iloc[0]['technical_details']
        else:
            tech = "Sem especificações técnicas disponíveis."

        doc = (
            f"{name} (código {code}): R$ {price}, disponibilidade: {availability}. "
            f"Especificações: {tech}"
        )
        merged_docs.append(doc)

    return merged_docs
