let saldo = 0;

class Usuario {
    nome;
    senha;

    constructor(nome, senha) {
        this.nome = nome;
        this.senha = senha;
    }
}

class Extrato{
    index;
    tipo;
    valor;

    constructor(index, tipo, valor){
        this.index = index;
        this.tipo = tipo;
        this.valor = valor;
    }
}

let usuarios = [];
let extrato = [];
let contadorExtrato = 1;

function cadastrarUsuario() {
    let usuarioExiste = false;
    let cadastSenha
    let cadastNome = prompt('Qual nome deseja cadastrar?');
    
    let verificacao = usuarios.some(usuario => {
        usuario.nome === cadastNome
        return true
    })

    if (verificacao) {
        usuarioExiste = true;
        console.log('Esse usuário já foi cadastrado!');
        alert('Esse usuário já foi cadastrado!');
    } else if (!usuarioExiste) {
        cadastSenha = Number(prompt('Qual senha deseja cadastrar? 4 dígitos'));
        
        let cadastUsuario = new Usuario(cadastNome, cadastSenha);

        usuarios.push(cadastUsuario);

        console.log('Usuário cadastrado com sucesso!');
        alert('Usuário cadastrado com sucesso!');
    }
}

function login(nomeUsu, senhaUsu) {
    let loginValido = false;

    usuarios.forEach(usuario => {
        if (usuario.nome === nomeUsu && usuario.senha === senhaUsu) {
            loginValido = true;
            console.log('Login validado, seja bem vindo!');
            alert('Login validado, seja bem vindo!');
        }
    })

    if (!loginValido) {
        console.log('Usuário ou senha incorretos!');
        alert('Usuário ou senha incorretos!');
    }

    return loginValido;
}

function depositar(valorAtual, valorDeposito) {
    saldo = valorAtual += valorDeposito;
    console.log('Valor depositado com sucesso, seu saldo atual é: R$' + saldo);
    alert('Valor depositado com sucesso, seu saldo atual é: R$' + saldo);

    let transacao = new Extrato(contadorExtrato, 'depositou', valorDeposito);

    extrato.push(transacao);
    contadorExtrato++
}

function sacar(valorAtual, valorSaque) {
    saldo = valorAtual -= valorSaque;
    console.log('Valor sacado com sucesso, seu saldo atual é: R$' + saldo);
    alert('Valor sacado com sucesso, seu saldo atual é: R$' + saldo);

    let transacao = new Extrato(contadorExtrato, 'sacou', valorSaque);

    extrato.push(transacao);
    contadorExtrato++
}

function exibirExtrato(){
    console.log('Extrato de transações:')

    if(extrato.length === 0){
        console.log('Nenhuma transação foi realizada ainda!');
        alert('Nenhuma transação foi realizada ainda!');
    } else{
        extrato.forEach(transacao => {
            console.log(transacao.index + '° transação: ' + transacao.tipo + ' ' + transacao.valor + ' reais.');
        })
    }

    console.log('Valor final: R$' + saldo);
}

function operacao() {
    let continuar = true;

    while (continuar) {
        let opcao = Number(prompt('Qual operação deseja executar? \n1= Depositar; \n2= Sacar; \n3= Conferir saldo; \n4= Conferir extrato; \n5= Encerrar programa;'));

        switch (opcao) {
            case 1:
                let valorDeposito = Number(prompt('Qual valor você deseja depositar?'));
                if (valorDeposito <= 0) {
                    console.log('Valor inválido, por favor escolha um valor maior que 0.');
                    alert('Valor inválido, por favor escolha um valor maior que 0.');
                } else {
                    depositar(saldo, valorDeposito);
                }
                break;

            case 2:
                let valorSaque = Number(prompt('Qual valor deseja sacar?'));
                if (valorSaque <= 0) {
                    console.log('Valor inválido, por favor escolha um valor maior que 0.');
                    alert('Valor inválido, por favor escolha um valor maior que 0.');
                } else if (valorSaque > saldo) {
                    console.log('Saldo indisponível, valor de saque maior que o saldo.');
                    alert('Saldo indisponível, valor de saque maior que o saldo.');
                } else {
                    sacar(saldo, valorSaque);
                }
                break;

            case 3:
                console.log('Seu saldo atual é: R$' + saldo);
                alert('Seu saldo atual é: R$' + saldo);
                break;

            case 4:
                exibirExtrato()
                break;

            case 5:
                continuar = false;
                console.log('Programa encerrado!');
                alert('Programa encerrado!');
                break;

            default:
                console.log('Opção inválida, por favor escolha outra.');
                alert('Opção inválida, por favor escolha outra.');
                break;
        }
    }
}

let continuar = true;

while (continuar) {
    let opcao = Number(prompt('O que deseja fazer hoje? \n1= Cadastrar usuário; \n2= Fazer login; \n3= Encerrar programa.'))

    switch (opcao) {
        case 1:
            cadastrarUsuario();
            break;

        case 2:
            let nomeUsu = prompt('Qual seu nome?');
            let senhaUsu = Number(prompt('Qual sua senha?'));
            let loginValidado = login(nomeUsu, senhaUsu);
            if (loginValidado) {
                operacao();
            }
            break;

        case 3:
            continuar = false;
            console.log('Programa encerrado!');
            alert('Programa encerrado!');
            break;

        default:
            console.log('Opção inválida, por favor escolha outra.');
            alert('Opção inválida, por favor escolha outra.');
            break;
    }
}