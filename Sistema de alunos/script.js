class Aluno{
    
    nome;
    idade;
    nota;

    constructor(nome, idade, nota){
        this.nome = nome;
        this.idade = idade;
        this.nota = nota;
    }
}

let alunos = [];

function cadastAluno(nome, idade, nota){
    
    let alunoNovo = new Aluno(nome, idade, nota);
   
    alunos.push(alunoNovo);

    console.log('Aluno incluso com sucesso!');
    alert('Aluno incluso com sucesso!');

    contadorAluno++;
    notas += nota;

}

let continuar = true;
let contadorAluno = 0
let notas = 0

while(continuar){

    let opcao = Number(prompt('O que você deseja fazer? \n1= Cadastrar aluno; \n2= Ordenar alunos por nota; \n3= Ordenar Alunos por idade;' + 
        '\n4= Ordenar por nome; \n5= Obter a média das notas cadastradas; \n6= Obter a quantidade de alunos cadastrados; \n7= Encerrar programa.'
    ))
    
    switch(opcao){
        
        case 1:
            let nome = prompt('Qual nome do aluno?');
            let idade
            let nota 
            
            let alunoExiste = false

            alunos.forEach(aluno => {
                if(aluno.nome === nome){
                    console.log('Esse aluno já foi incluso!');
                    alert('Esse aluno já foi incluso!');
                    alunoExiste = true;
                }
            })

            if(!alunoExiste){
                idade = Number(prompt('Qual idade do aluno?'));
                nota = Number(prompt('Qual a nota do aluno?'));

                cadastAluno(nome, idade, nota);
            }

            break;

        case 2:

            console.log('Alunos ordenador por nota:');
            alert('Alunos ordenados por nota:');

            let ordemPorNota = alunos.sort((a, b) => {
                return a.nota - b.nota;
            })

            console.log(ordemPorNota);

            break;

        case 3:

            console.log('Alunos ordenador por idade:');
            alert('Alunos ordenados por idade:');

            let ordemPorIdade = alunos.sort((a, b) => {
               return a.idade - b.idade;
            })

            console.log(ordemPorIdade);

            break;

        case 4:

            console.log('Alunos ordenador por nome:');
            alert('Alunos ordenados por nome:');

            let ordemPorNome = alunos.sort((a, b) => {
                return a.nome - b.nome
            })

            console.log(ordemPorNome);

            break;

        case 5:
            
            let media

            if(notas === 0 || contadorAluno === 0){
                console.log('Nenhum aluno foi incluso ainda.');
                alert('Nenhum aluno foi incluso ainda.');
            } else{
                media = notas / contadorAluno;
                console.log('A média geral das notas dos alunos foi de: ' + media + ' pontos.');
            }

            break;

        case 6:
            
            if(contadorAluno === 0){
                console.log('Nenhum aluno foi incluso ainda.');
                alert('Nenhum aluno foi incluso ainda.');
            } else{
                console.log('A quantidade de alunos cadastrados foi de: ' + contadorAluno + ' alunos.');
            }

            break;

        case 7:
            
            console.log('Programa encerrado com sucesso!');
            alert('Programa encerrado com sucesso!');

            continuar = false;

            break;

        default:

            console.log('Opção inválida! Por favor escolha outra.');
            alert('Opção inválida! Por favor escolha outra.');

            break;
    }
}