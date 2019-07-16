import re



padrao = re.compile(r'(01)\/\d\d\/\d{4}')  # corresponde a questão "a"

with open('atv02_ex01.txt', 'r', encoding='utf-8') as f:
    leitor = f.read()
    matches = padrao.finditer(leitor)
    for match in matches:
        print(match)