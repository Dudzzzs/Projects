function calculadora(num1, num2, operacao){
    
    let resultado = 0

    switch(operacao){
        case 1:
            resultado = num1 + num2
            break;

        case 2:
            resultado = num1 - num2
            break;

        case 3: 
            resultado = num1 * num2
            break;

        case 4:
            resultado = num1 / num2
            break;

        case 5:
            resultado = num1 ** num2
            break;
    }

    return resultado

}

let numero1 = Number(prompt('Escolha o primeiro número: '));
let numero2 = Number(prompt('Escolha o segundo número:'));

let loop = true

while(loop){
let operacao = Number(prompt('Qual operação deseja executar com esses números? \n1= Soma; \n2= Subtração; \n3= Multiplicação' + 
    '\n4= Divisão; \n5= Exponenciação;'))

    switch(operacao){
        case 1:
            console.log(numero1 + ' + ' + numero2 + ' = ' + calculadora(numero1, numero2, operacao));
            loop = false;
            break;

        case 2:
            console.log(numero1 + ' - ' + numero2 + ' = ' + calculadora(numero1, numero2, operacao));
            loop = false;
            break;

        case 3: 
            console.log(numero1 + ' x ' + numero2 + ' = ' + calculadora(numero1, numero2, operacao));
            loop = false;
            break;

        case 4:
            console.log(numero1 + ' / ' + numero2 + ' = ' + calculadora(numero1, numero2, operacao));
            loop = false;
            break;

        case 5:
            console.log(numero1 + ' elevado a ' + numero2 + ' = ' + calculadora(numero1, numero2, operacao));
            loop = false;
            break;

        default:
            alert('Escolha outra opção!')
            break;
    }

}
