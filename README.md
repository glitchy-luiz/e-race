<p align="center">
 <h1 align="center">E-Race Live</h1>
 <p align="center">O software de transmissão exclusiva da Formula E</p>
</p>

## Introdução
Este projeto é um protótipo de como funcionará nosso software de streams, mais especificamente este protótipo reflete como o criador da live irá cadastra-lá no nosso software.
> Nota
> Nós utilizamos a biblioteca OS para melhoria visuais

## 1- Funções iniciais:
Ao iniciar o programa, o usuário terá 3 funcionalidades, além de uma função para sair do programa

```md
def exibir_opcoes():
    '''mostra as opções de açoes'''
    print('1. Cadastrar lives')
    print('2. Listar lives')
    print('3. Alternar estado da live')
    print('4. Sair\n')
```

Cada uma das opções é representada por um número que indica qual função terá que ser executada a seguir

```md
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
```

## 2- Funções básicas:
Para melhorar o visual da aplicação, temos no inicio do código algumas funções que chamam outras funções, ou apenas dão um feedback para o usuário

```md
def exibir_nome_prog():
    '''Exibe o nome'''
    print('Bem Vindo ao E-race Live')

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

def main():
    '''exibe o nome, opções e escolhas do app'''
    os.system('cls')
    exibir_nome_prog()
    exibir_opcoes()
    escolher_opcao()
```

> **Note**
>O 'os.system' serve para chamar a biblioteca os e limpar o terminam

## 3- Funções principais:
No inicio do código criamos uma lista vazia com nome de 'lives', para podermos adicionar objetos nela por meio da função de cadastrar live

```md
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

```
Ela pede um nome para a live e uma categoria para ela, e automaticamente implementa ela na lista como 'desativada'


Na função de listar lives, vemos que ela faz exatamente isto
```md
def listar_lives():
    '''Essa funcão pega todas as lives cadastrados na lista e mostra na tela'''
    exibir_subtitulo('Listando as lives')

    for live in lives:
        nome_live = live['nome']
        categoria = live['categoria']
        ativo = 'ativado' if live['ativo'] else 'desativado'
        print(f'- {nome_live.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()
```
Ela roda todos os objetos da lista de lives e mostra ela para o usuário


E a última função, é a de alterar o estado da live para pode ativa-lá
```md
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
```
Ela busca uma live pelo nome dela, caso ela encontre uma live com aquele nome, ela alterará o estado atual dela, mas caso não encontre, ela simplesmente retorna para o usuário que ela não foi encontrada

## 4- Finalização
Assim passamos por cima da principais partes do código do nosso protótipo em que, futuramente, se tornará uma plataforma de lives para ajudar a formula E a expandir seu público e facilitar as transmissões das lives ao vivo das corridas para os espectadores

INTEGRANTES:
- Luiz Fernando Souza RM: 555561
- Bruno Otavio RM:556196
- Guilherme Palhari  RM: 557073​
- Guilherme Flores  RM: 554948​
- Adolfo Kentaro  RM: 556884
