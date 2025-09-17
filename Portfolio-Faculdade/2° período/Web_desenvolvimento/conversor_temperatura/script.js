const form = document.getElementById("form");
const inputCelsius = document.getElementById("celsius");
const unidade = document.getElementById("unidade");
const resultado = document.getElementById("resultado");

form.addEventListener("submit", function(event) {
    event.preventDefault(); // impede atualizar a página
    resultado.textContent = "";

    const celsius = parseFloat(inputCelsius.value);
    const escolha = unidade.value;

    if (isNaN(celsius)) {
        resultado.textContent = "Por favor, insira uma temperatura válida.";
        return;
    }

    if (escolha === "f") {
        const fahrenheit = (celsius * 9/5) + 32;
        resultado.textContent = `${celsius} °C = ${fahrenheit.toFixed(2)} °F`;
    } else if (escolha === "k") {
        const kelvin = celsius + 273.15;
        resultado.textContent = `${celsius} °C = ${kelvin.toFixed(2)} K`;
    } else {
        resultado.textContent = "Selecione para qual unidade deseja converter.";
    }
});

form.addEventListener("reset", function() {
    resultado.textContent = "";
});