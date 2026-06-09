const receitas = document.getElementById("receitas");

const alimentacao = document.getElementById("alimentacao");
const transporte = document.getElementById("transporte");
const lazer = document.getElementById("lazer");
const investimentos = document.getElementById("investimentos");

const saldo = document.getElementById("saldo");

function atualizarDashboard() {

    const receita = Number(receitas.value);

    const gastoAlimentacao = Number(alimentacao.value);
    const gastoTransporte = Number(transporte.value);
    const gastoLazer = Number(lazer.value);
    const gastoInvestimentos = Number(investimentos.value);

    const totalDespesas =
        gastoAlimentacao +
        gastoTransporte +
        gastoLazer +
        gastoInvestimentos;

    const saldoFinal = receita - totalDespesas;

    saldo.innerText = "R$ " + saldoFinal.toFixed(2);

    expenseChart.data.datasets[0].data = [
        gastoAlimentacao,
        gastoTransporte,
        gastoLazer,
        gastoInvestimentos
    ];

    expenseChart.update();
}

const ctx = document.getElementById("expenseChart");

const expenseChart = new Chart(ctx, {
    type: "doughnut",

    data: {
        labels: [
            "Alimentação",
            "Transporte",
            "Lazer",
            "Investimentos"
        ],

        datasets: [{
            data: [450, 200, 150, 500]
        }]
    }
});

receitas.addEventListener("input", atualizarDashboard);
alimentacao.addEventListener("input", atualizarDashboard);
transporte.addEventListener("input", atualizarDashboard);
lazer.addEventListener("input", atualizarDashboard);
investimentos.addEventListener("input", atualizarDashboard);

atualizarDashboard();