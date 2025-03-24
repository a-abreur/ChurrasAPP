from rich import print

def calcular_quantidades(adultos, criancas):
    fator_adulto = 1.0  # Cada adulto consome 100%
    fator_crianca = 0.6  # Cada criança consome 60%
    
    total_pessoas = (adultos * fator_adulto) + (criancas * fator_crianca)
    
    itens = {
        "Carne (kg)": round(total_pessoas * 0.4, 2),  # 400g por pessoa
        "Arroz (kg)": round(total_pessoas * 0.2, 2), #200g por pessoa
        "Farofa (Kg)": round(total_pessoas * 0.05, 2), #50g por pessoa
        "Pao de Alho": round(total_pessoas * 1.5),  # 1.5 unidades por pessoa
        "Refrigerante (L)": round(total_pessoas * 0.6, 2),  # 600ml por pessoa
        "Cerveja (L)": round(total_pessoas * 1.2, 2),  # 1.2L por pessoa
        "Carvão (kg)": round((adultos + criancas) / 5, 2)  # 5 pessoas = 1kg carvão
    }
    return itens

def exibir_lista(itens, adultos, criancas):
    """
    Exibe a lista de compras no terminal de forma estilizada.
    """
    print("\n" + "=" * 40)
    print("     LISTA DE COMPRAS PARA CHURRASCO")
    print("=" * 40)
    print(f" Adultos: {adultos} | Crianças: {criancas}")
    print("-" * 40)
    
    for item, quantidade in itens.items():
        print(f" {item.ljust(20)}: {quantidade}")
    
    print("=" * 40)

def main():
    """
    Função principal para entrada de dados e exibição da lista.
    """
    try:
        adultos = int(input("Quantidade de adultos: "))
        criancas = int(input("Quantidade de crianças: "))
        
        if adultos < 0 or criancas < 0:
            print("Erro: Quantidades não podem ser negativas.")
            return
        
        itens = calcular_quantidades(adultos, criancas)
        exibir_lista(itens, adultos, criancas)
    except ValueError:
        print("Erro: Insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
