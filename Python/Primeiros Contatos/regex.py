# regex.py
import re

musica = '''
For a while there, it was rough
But lately, I've been doin' better
Than the last four cold Decembers
I recall
And I see my family every month
I found a girl my parents love
She'll come and stay the weekend
And I'll work late on a weekday
And I'll hang out with my friends
And I'm still young

Oh, I know I've got a good thing, yeah
And I know I've got it all
And I know I'm where I'm s'posed to be
Yeah, I know it's what I want

So please don't take
These beautiful things that I've got
Please don't take
These beautiful things that I've got
Please don't take
These beautiful things that I've got
Oh-oh-oh

And I know I'm not a perfect man
But I'm tryna be a better person
For the one I love at home
She said, "I've been on the edge
And you know that I've been hurt
And you know that I'm afraid
That you'll walk right out the door
Like you did the time before"
But I'm still young

Oh, I know I've got a good thing, yeah
And I know I've got it all
And I know I'm where I'm s'posed to be
Yeah, I know it's what I want

So please don't take
These beautiful things that I've got
Please don't take
These beautiful things that I've got
Please don't take
These beautiful things that I've got
Oh-oh-oh

Oh, I know I've got a good thing, yeah
And I know I've got it all
And I know I'm where I'm s'posed to be
Yeah, I know it's what I want

So please don't take
These beautiful things that I've got
Please don't take
These beautiful things that I've got
Please don't take
These beautiful things that I've got
Oh-oh-oh
'''


# 1- Contar quantas vezes o caracter "a" aparece em todo o texto da música
# Encontra todas as ocorrências de 'a' e conta o tamanho da lista resultante
contagem_a = len(re.findall(r"a", musica))

print(f"O caractere 'a' (minúsculo) aparece {contagem_a} vezes.")

# 2- Contar quantas vezes a palavra tempo aparece na música
palavra = "things"
contagem_plv = len(re.findall(
    rf"\b{re.escape(palavra)}\b", musica, re.IGNORECASE))
print(f"A palavra '{palavra}' aparece {contagem_plv} vez(es).")

# 3- Extrair as palavras seguidas por apóstrofo
regex_captura = r"(\w+)'"
matches_captura = re.findall(regex_captura, musica)
print(f"As palavras que vem depois do apóstrofo são: {matches_captura}")

# 4- Extrair qualquer palavra cujo antecessor seja a palavra "beautiful" e o sucessor seja a palavra "that" em um texto.
regex_plv = r"\bbeautiful\b\s+(\w+)\s+\bthat\b"
palavras_encontradas = re.findall(regex_plv, musica, re.IGNORECASE)
print(
    f"As palavras encontradas entre 'beautiful' e 'that' são: {palavras_encontradas}")

# 5- Retornar as palavras com apóstrofo, mas somente os caracteres na palavra que são anteriores ao caractere apóstrofo
regex_aps = r"(\w+)'"
palavras_aps = re.findall(regex_aps, musica)
print(f"As palavras que vêm antes do caracter apóstrofo são: {palavras_aps}")

# 6- Retornar as palavras com apóstrofo, mas somente os caracteres na palavra que são posteriores ao caractere apóstrofo

regex_daps = r"'(\w+)"
palavras_daps = re.findall(regex_daps, musica)
print(f"As palavras que vêm depois do apóstrofo são: {palavras_daps}")
