import re
from collections import Counter

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

frequencia_portugues = {
    'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99, 'E': 12.57, 'F': 1.02, 'G': 1.30,
    'H': 1.28, 'I': 6.18, 'J': 0.40, 'K': 0.02, 'L': 2.78, 'M': 4.74, 'N': 5.05,
    'O': 10.73, 'P': 2.52, 'Q': 1.20, 'R': 6.53, 'S': 7.81, 'T': 4.34, 'U': 4.63,
    'V': 1.67, 'W': 0.01, 'X': 0.21, 'Y': 0.01, 'Z': 0.47
}

frequencia_ingles = {
    'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70, 'F': 2.23, 'G': 2.02,
    'H': 6.09, 'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75,
    'O': 7.51, 'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06, 'U': 2.76,
    'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97, 'Z': 0.07
}

def limpar_texto(texto):
    return re.sub(r'[^A-Z]', '', texto.upper())

def encontrar_repeticoes(texto):
    trigrams = {}
    for i in range(len(texto) - 2):
        trigram = texto[i:i + 3]
        if trigram in trigrams:
            trigrams[trigram].append(i)
        else:
            trigrams[trigram] = [i]

    distancias = []
    for positions in trigrams.values():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                distancia = positions[i + 1] - positions[i]
                distancias.append(distancia)
    return distancias

def fatores_comuns_top3(distancias):
    if not distancias:
        return [1]

    fatores = []
    for d in distancias:
        for i in range(2, 21):  # testamos tamanhos de chave até 20
            if d % i == 0:
                fatores.append(i)

    contagem = Counter(fatores).most_common(3)
    return [f[0] for f in contagem] if contagem else [1]

def fatiar_texto(texto, tamanho_chave):
    return [texto[i::tamanho_chave] for i in range(tamanho_chave)]

def calcular_frequencia(texto):
    contador = Counter(texto)
    total = sum(contador.values())
    return {letra: (contador.get(letra, 0) / total) * 100 for letra in abc}

def descobrir_chave(fatias, freq_idioma):
    chave = ''
    for fatia in fatias:
        menor_erro = float('inf')
        melhor_deslocamento = 0

        for deslocamento in range(26):
            texto_deslocado = ''.join(abc[(abc.index(c) - deslocamento) % 26] for c in fatia)
            freq_texto = calcular_frequencia(texto_deslocado)

            erro = sum(abs(freq_texto.get(l, 0) - freq_idioma.get(l, 0)) for l in abc)

            if erro < menor_erro:
                menor_erro = erro
                melhor_deslocamento = deslocamento

        chave += abc[melhor_deslocamento]
    return chave

def decifrar_vigenere(texto, chave):
    texto_decodificado = ''
    tamanho_chave = len(chave)
    for i, c in enumerate(texto):
        c_index = abc.index(c)
        k_index = abc.index(chave[i % tamanho_chave])
        letra = abc[(c_index - k_index) % 26]
        texto_decodificado += letra
    return texto_decodificado

def chave_com_melhor_erro(texto, freq_idioma):
    distancias = encontrar_repeticoes(texto)
    candidatos = fatores_comuns_top3(distancias)

    melhor_chave = None
    menor_erro_total = float('inf')

    for tamanho_chave in candidatos:
        fatias = fatiar_texto(texto, tamanho_chave)
        chave = descobrir_chave(fatias, freq_idioma)

        texto_decodificado = decifrar_vigenere(texto, chave)
        freq_texto_dec = calcular_frequencia(texto_decodificado)
        erro_total = sum(abs(freq_texto_dec[l] - freq_idioma[l]) for l in abc)

        if erro_total < menor_erro_total:
            menor_erro_total = erro_total
            melhor_chave = chave

    return melhor_chave

# =========================
# Entrada dos textos cifrados
# =========================

texto_pt = input("Digite o texto cifrado em Português: ").upper()
texto_en = input("Digite o texto cifrado em Inglês: ").upper()

# Limpa os textos
texto_pt_limpo = limpar_texto(texto_pt)
texto_en_limpo = limpar_texto(texto_en)

# Descobre as chaves
chave_pt = chave_com_melhor_erro(texto_pt_limpo, frequencia_portugues)
chave_en = chave_com_melhor_erro(texto_en_limpo, frequencia_ingles)

# Mostra as chaves
print(f"Chave descoberta para o texto em Português: {chave_pt}")
print(f"Chave descoberta para o texto em Inglês: {chave_en}")

# Opcional: decifra os textos para ver a mensagem original
msg_pt = decifrar_vigenere(texto_pt_limpo, chave_pt)
msg_en = decifrar_vigenere(texto_en_limpo, chave_en)

print("\nMensagem decifrada em Português:\n", msg_pt)
print("\nMensagem decifrada em Inglês:\n", msg_en)
