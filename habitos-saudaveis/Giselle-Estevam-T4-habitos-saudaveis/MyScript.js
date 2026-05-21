const resultado = document.querySelector('#resultado')
const altura = document.querySelector('#altura')
const peso = document.querySelector('#peso')
const idade = document.querySelector('#idade')

const calcula_imc = () => {
    if (altura.value >= 0 && peso.value >= 0 && idade.value >= 0) {
        const imc = (peso.value / (altura.value * altura.value)).toFixed(2)
        let classificacao = ''
        let imagem_classificacao = ''

        const idade_em_Numero = parseInt(idade.value)
        // Se a pessoa for idosa
        if (idade_em_Numero > 60) {
            if (imc <= 22) {
                classificacao = 'Baixo peso'
                imagem_classificacao = 'img/classificacao-imc-baixo-peso.png'
            }
            else if (imc < 27){
                classificacao = 'Adequado ou eutrófico'
                imagem_classificacao = 'img/classificacao-imc-peso-normal.png'
            }
            else if (imc >= 27) {
                classificacao = 'Sobrepeso'
                imagem_classificacao = 'img/classificacao-imc-sobrepeso.png'
            }
        }
        // Se a pessoa NÃO for idosa
        else {
            if (imc < 18.5) {
                classificacao = 'Baixo peso'
                imagem_classificacao = 'img/classificacao-imc-baixo-peso.png'
            }
            else if (imc < 25.0) {
                classificacao = 'Peso normal'
                imagem_classificacao = 'img/classificacao-imc-peso-normal.png'
            }
            else if (imc < 30.0) {
                classificacao = 'Excesso de peso'
                imagem_classificacao = 'img/classificacao-imc-sobrepeso.png'
            }
            else if (imc < 35.0) {
                classificacao = 'Obesidade de Classe I'
                imagem_classificacao = 'img/classificacao-imc-obesidade-1.png'
            }
            else if (imc < 40.0) {
                classificacao = 'Obesidade de Classe II'
                imagem_classificacao = 'img/classificacao-imc-obesidade-2.png'
            }
            else {
                classificacao = 'Obesidade de Classe III'
                imagem_classificacao = 'img/classificacao-imc-obesidade-3.png'
            }
        }
        const resultadoDiv = document.createElement('div');
        resultadoDiv.className = 'resultado-container';

        const textoResultado = document.createElement('p');
        textoResultado.innerHTML = `Seu IMC é: ${imc} (${classificacao})`;

        const imagemElement = document.createElement('img');
        imagemElement.src = imagem_classificacao;
        imagemElement.alt = classificacao;

        resultadoDiv.appendChild(textoResultado);
        resultadoDiv.appendChild(imagemElement);

        resultado.innerHTML = '';
        resultado.appendChild(resultadoDiv);
    }
    else {
        resultado.innerHTML = 'Preencha os campos corretamente para que se possa calcular.'
    }
}