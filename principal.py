from usuarios import Usuarios

def Gera_Arquivo(listaUsuarios):
    with open ('relatorio.txt', mode='w', encoding='latin_1') as arquivo:
        arquivo.buffer.write(bytes('ACME Inc.           Uso do espaço em disco pelos usuários\n', encoding='latin_1'));
        arquivo.buffer.write(bytes('------------------------------------------------------------------------\n', encoding='latin_1'))
        arquivo.buffer.write(bytes('Nr.\t Usuário\t Espaço utilizado\t % do uso\n', encoding='latin_1'));
        for usuario in listaUsuarios:
            arquivo.write(str(usuario))
        arquivo.write('\nEspaço total ocupado: {} MB\n'.format(listaUsuarios[0].espaco_Ocupado));
        arquivo.write('Espaço médio ocupado: {:.2f} MB'.format(listaUsuarios[0].espaco_medio()));


def cria_usuarios(conteudo):
    lista = [];
    for palavra in conteudo:
        lista.append(palavra.split())

    dicionario = dict(lista)
    listaUsuarios = [];

    for chave, valor in dicionario.items():
        listaUsuarios.append(Usuarios(chave, int(valor)));
        
    Gera_Arquivo(listaUsuarios)

try:
    with open('usuarios.txt', mode='r+', encoding='UTF-8') as arquivo:
        conteudo = arquivo.readlines()
                    

except FileNotFoundError:
    print("Arquivo não encontrado")

except PermissionError:
    print("Usuário sem permissão")

finally:
    cria_usuarios(conteudo)
        


    