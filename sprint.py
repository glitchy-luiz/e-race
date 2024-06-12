import os

lives = []

def exibir_nome_prog():
    '''Exibe o nome'''
    print('Bem Vindo ao E-race Live')

def exibir_opcoes():
    '''mostra as opções de açoes'''
    print('1. Cadastrar lives')
    print('2. Listar lives')
    print('3. Alternar estado da live')
    print('4. Sair\n')

def finalizar_app():
    '''Termina o app'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    '''Retorna para o menu das opções'''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    '''Mostra que não tem opção com tal comando'''
    print('opção invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''mostra o subtitulo da ação'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastar_nova_live():
    '''Essa função é responsavel por cadastrar uma nova live
    
    Inputs:
    - nome da live
    - categoria

    Output:
    - adiciona uma nova live a lista de lives

    '''
    exibir_subtitulo('Cadastro de novas lives')
    nome_da_live = input('Digite o nome da live que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria da live {nome_da_live}: ')
    dados_da_live = {'nome':nome_da_live,
                            'categoria':categoria,
                            'ativo':False}
    lives.append(dados_da_live)
    print(f'A live {nome_da_live} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_lives():
    '''Essa funcão pega todas as lives cadastrados na lista e mostra na tela'''
    exibir_subtitulo('Listando as lives')

    for live in lives:
        nome_live = live['nome']
        categoria = live['categoria']
        ativo = 'ativado' if live['ativo'] else 'desativado'
        print(f'- {nome_live.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_live():
    '''Altera a live para ativo ou inativo
    
    input:
    - nome de uma live cadastrada

    output:
    - altera o estado dele (ativo e inativo)
    
    '''
    exibir_subtitulo('Alterando estado da live')
    nome_live = input('Digite o nome da live que deseja alterar o estado: ')
    live_encontrado = False

    for live in lives:
        if nome_live == live['nome']:
            live_encontrado = True
            live['ativo'] = not live['ativo']
            mensagem = f'O restaurante {nome_live} foi ativado com sucesso' if live['ativo'] else f'A live {nome_live} foi desativado com sucesso'
            print(mensagem)

    if not live_encontrado:
        print('A live não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Exibi as opções disponivel para otras funções
    
    input:
    - numero da ação

    output:
    - ativa a função correspondente ao número

    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastar_nova_live()
        elif opcao_escolhida == 2:
            listar_lives()
        elif opcao_escolhida == 3:
            alternar_estado_live()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: opcao_invalida()

   


def main():
    '''exibe o nome, opções e escolhas do app'''
    os.system('cls')
    exibir_nome_prog()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

