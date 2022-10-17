def cript () : #função para criptografar
    criptografar = input('\nInsira a mensagem a ser CRIPTOGRAFADA:')
    mensagem = ''

    listaChr=[]
    for i in criptografar: #Cria uma lista com os algarimos inceridos na variavel 'criptografar'
        listaChr.append(chr(ord(i)))
        mensagem = mensagem + str(ord(i)*14).zfill(6)

    print('\nA mensagem criptografada é:' ,mensagem)

def descript () : #função para descriptografar
    descriptografar = input('\nInsira a mensagem a ser DESCRIPTOGRAFADA:')
    mensagem = ''#Mensagem vazia 
    
    listaD = list() #Variavel que recebe uma lista
    for i in range(0, len(descriptografar), 6): #cria um array iniciando em 0 e indo até o sexto augaritimo de descriptografar
        listaD.append(descriptografar[i:i+6]) #insere dentro de listaD todos os números inseridos em descriptografar de 6 em 6 ['0123456', '0123456', '0123456'....]
    print ('listaD',listaD)
    listaI = list()
    for i in range(0, len(listaD)):
        result = ''
        for j in listaD[i]:
            result = result + j
        listaI.insert(i, chr(int(int(result)/14)))
    print ('listaI', listaI)
    for i in listaI:
        mensagem = mensagem + i
    
    print('\nA mensagem descriptografada é:' , mensagem)

while True:
    print('\nBem vindo ao SIC (Sistema de Interativo de Criptografia)!!!')
    print('Você deseja:')       
    print('\n1-Criptografar')
    print('\n2-Descriptografar')

    menu = input('\nInsira a opção desejada (1 ou 2):')
    if menu == '1':
        cript()
    # Se menu = 1 então será chamada a função crit ()
    elif menu == '2':
        descript()
    # Se menu = 2 então será chamada a função descript ()
    else:
        print('\nValor inválido!')
    # Se menu =! 1 ou 2 então pedirá para informar se quer que o programa reinicie ou não, voltando para o inicio do menu ou encerrando o programa
    if input('\nDeseja reiniciar (S/N)?') not in ('S', 's'):
        break # Se digitar qualquer coisa diferente de S ou s o programa sai do loop