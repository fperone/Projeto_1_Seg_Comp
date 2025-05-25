abc = ["A","B","C","D","E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
       "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y","Z"]

acentos = {'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
           'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
           'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
           'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
           'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
           'Ç': 'C'}

def limpar_texto(texto):
    texto_novo = ''
    for c in texto.upper():
        if c.isalpha() or c == ' ':
            if c in acentos:
                texto_novo += acentos[c]
            else:
                texto_novo += c
    return texto_novo

criptograma = input("Digite o criptograma: ").upper()
key = input("Digite a chave: ").upper()

# Verifica se há números
for ele in criptograma:
    if ele.isdigit():
        print("O texto não pode conter números")
        exit()
for ele in key:
    if ele.isdigit():
        print("A chave não pode conter números")
        exit()

# Limpa chave
key = limpar_texto(key).replace(" ", "")  # Retira espaços da chave

mensagem = ""
k = 0  # contador da chave

for e in range(len(criptograma)):
    char = criptograma[e]
    if char == ' ':
        mensagem += ' '
    else:
        n = abc.index(char)
        kn = abc.index(key[k % len(key)])
        msg_letter = ((n - kn) + 26) % 26
        mensagem += abc[msg_letter]
        k += 1  # só avança a chave se processou uma letra

print(mensagem)
