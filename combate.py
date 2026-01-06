stats_jogador = {
    "nome": "Avatar do Iury",
    "vida": 100,
    "mana": 100,
    "dano_base": 50 #  tabela de ataque fraco
}

stats_inimigo = {
    "nome": "Guardião do Portal",
    "vida": 500, # tabela de inimigos
    "velocidade": 1.0
}

def calcular_ataque(tipo):
    if tipo == "fraco":
        return stats_jogador["dano_base"] * 1.0  # 100% do dano base (50 pontos)
    elif tipo == "forte":
        return stats_jogador["dano_base"] * 1.4  # 40% de bônus
    elif tipo == "habilidade":
        if stats_jogador["mana"] >= 10: # Custo de mana
            stats_jogador["mana"] -= 10
            return stats_jogador["dano_base"] * 1.8  # 80% de bônus (90 pontos)
        else:
            print("Mana insuficiente!")
            return 0

# Simulação de um turno
dano = calcular_ataque("habilidade")
stats_inimigo["vida"] -= dano

print(f"--- Relatório de Combate ---")
print(f"O jogador usou uma Habilidade Especial!")
print(f"Dano causado: {dano}")
print(f"Vida restante do {stats_inimigo['nome']}: {stats_inimigo['vida']}")
print(f"Mana restante do jogador: {stats_jogador['mana']}")
# O 'Mundo' permanece o mesmo (Progresso do Save)
save_do_jogo = {
    "portais_fechados": 10,
    "fama_acumulada": 500,
    "guilda_registrada": True
}

def criar_novo_avatar():
    print("\n--- CRIAÇÃO DE NOVO PERSONAGEM ---")
    nome = input("Digite o nome do seu novo caçador: ")
    # Classes
    classe = input("Escolha a classe (Guerreiro, Mago, Atirador, Ladino, Suporte): ")
    return {"nome": nome, "classe": classe, "vida": 100, "vivo": True}

# Início do Jogo
personagem_atual = criar_novo_avatar()

def verificar_estado(personagem):
    if personagem["vida"] <= 0:
        personagem["vivo"] = False
        print(f"\n[FATAL] O personagem {personagem['nome']} morreu em combate!")
        print(f"O corpo não pode ser recuperado. O portal foi quebrado.")
        return False
    return True

# Simulando uma derrota em combate
print(f"\nExplorando portal de Rank S...")
personagem_atual["vida"] = 0 # Personagem foi derrotado

if not verificar_estado(personagem_atual):
    # Lógica State of Decay: O save continua, mas pede novo personagem
    print(f"Lidando com a perda... Portais fechados no save: {save_do_jogo['portais_fechados']}")
    personagem_atual = criar_novo_avatar()
    print(f"\nNovo começo com {personagem_atual['nome']} da classe {personagem_atual['classe']}.")
  import datetime

# Progresso Global do Save
save_do_jogo = {
    "portais_fechados": 10,
    "memorial_de_herois": []  # Lista para armazenar quem morreu
}

def registrar_morte(personagem):
    # Armazena os dados do herói antes de "apagá-lo"
    registro = {
        "nome": personagem["nome"],
        "classe": personagem["classe"],
        "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    save_do_jogo["memorial_de_herois"].append(registro)

def exibir_memorial():
    print("\n=== MEMORIAL DOS CAÇADORES CAÍDOS ===")
    if not save_do_jogo["memorial_de_herois"]:
        print("Ainda não houve baixas nesta guerra.")
    for heroi in save_do_jogo["memorial_de_herois"]:
        print(f"[*] {heroi['nome']} ({heroi['classe']}) - Tombou em: {heroi['data']}")
    print("=====================================\n")

# Exemplo de uso após uma derrota
heroi_derrotado = {"nome": "Iury I", "classe": "Guerreiro", "vida": 0}

if heroi_derrotado["vida"] <= 0:
    print(f"O portal consumiu {heroi_derrotado['nome']}...")
    registrar_morte(heroi_derrotado)

# Ver o histórico
exibir_memorial()
