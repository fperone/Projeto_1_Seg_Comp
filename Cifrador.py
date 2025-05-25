abc = ["A","B","C","D","E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y","Z"]
acentos = {'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A','É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E','Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I','Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O','Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U','Ç': 'C'}
def limpar_texto(texto):
  texto_novo = ''.join([c.upper() for c in texto if c.isalpha()])
  for i in texto_novo:
    if i in acentos:
      texto_novo = texto_novo.replace(i, acentos[i])
  return texto_novo
texto, key = input("Digite a mensagem: "), input("Digite a chave: ")
for ele in texto:
  if ele.isdigit():
    print("O texto não pode conter números")
    exit()
for ele in key:
  if ele.isdigit():
    print("A chave não pode conter números")
    exit()
key = limpar_texto(key)
texto = limpar_texto(texto)
criptograma = ""
for e in range(len(texto)):
  n = abc.index(texto[e])
  k = e % len(key)
  kn = abc.index(key[k])
  new_letter = (n + kn) % 26
  criptograma += abc[new_letter]
print(criptograma)
