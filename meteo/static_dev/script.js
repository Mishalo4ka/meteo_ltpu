// Получаем DOM-элементы
const ctx1 = document.getElementById('graph1');
const ctx2 = document.getElementById('graph2');
const ctx3 = document.getElementById('graph3');

// Загружаем данные из JSON-скриптов
const labels = JSON.parse(document.getElementById('labels-data').textContent);
const tempDataArr = JSON.parse(document.getElementById('temp-data').textContent);
const humDataArr = JSON.parse(document.getElementById('hum-data').textContent);
const presDataArr = JSON.parse(document.getElementById('pres-data').textContent);




const tempData = document.getElementById('temp');
const humidityData = document.getElementById('humidity');
const preasureData = document.getElementById('preasure');



// Обновляем карточки с показателями
document.getElementById('temp').textContent = `${latestTemp}°C`;
document.getElementById('humidity').textContent = `${latestHum}%`;
document.getElementById('preasure').textContent = `${latestPres} мм рт. ст.`;

// Создаем графики
const chart1 = createChart(ctx1, labels, presDataArr, false);
const chart2 = createChart(ctx2, labels, tempDataArr, true);
const chart3 = createChart(ctx3, labels, humDataArr, false);


console.log(labels, tempDataArr, humDataArr, presDataArr)

// Функция построения графиков
function createChart(ctx, labels, data, beginAtZero){
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: '',
                data: data,
                borderWidth: function(context) {
                    const width = context.chart.width;
                    return Math.max(1, Math.min(5, width / 300));
                },
                borderColor: '#5686DF',
                pointBackgroundColor: 'white',
                pointRadius: function(context) {
                    const width = context.chart.width;
                    return Math.max(4, Math.min(9, width / 100));
                }
            }]
        },
        options: {
            layout: {
                padding: function(context) {
                    const width = context.chart.width;
                    const padding = Math.round(width / 25);
                    return {
                        top: padding,
                        bottom: padding * 2,
                        left: padding,
                        right: padding
                    };
                }
            },
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    display: false,
                    beginAtZero: beginAtZero
                },
                x: {
                    display: false
                }
            },
            plugins: {
                legend: { display: false },
                title: { display: false },
                datalabels: {
                    display: true,
                    color: '#6B95E2',
                    font: function(context) {
                        const width = context.chart.width;
                        const size = Math.round(width / 25);
                        return {
                            size: size > 24 ? 24 : size,
                            weight: 'bold'
                        };
                    },
                    align: 'bottom',
                    formatter: value => `${value}`,
                    offset: function(context) {
                        const width = context.chart.width;
                        return Math.min(30, Math.round(width / 30));
                    }
                }
            }
        },
        plugins: [ChartDataLabels]
    });
}

setInterval(() => {
    fetch('/latest/')
        .then(response => response.json())
        .then(data => {
            if (data.temperature !== undefined) {
                // Обновить карточки
                tempData.textContent = `${data.temperature}°C`;
                humidityData.textContent = `${data.humidity}%`;
                preasureData.textContent = `${data.pressure} мм рт. ст.`;

                // Добавить новую точку на график
                const timeLabel = data.timestamp;

                // Обновим графики (в конец добавим точку, уберём первую)
                const maxPoints = 12;

                const updateChart = (chart, arr, newValue) => {
                    chart.data.labels.push(timeLabel);
                    arr.push(newValue);

                    if (chart.data.labels.length > maxPoints) {
                        chart.data.labels.shift();
                        arr.shift();
                    }

                    chart.data.datasets[0].data = arr;
                    chart.update();
                };

                updateChart(chart1, presDataArr, data.pressure);
                updateChart(chart2, tempDataArr, data.temperature);
                updateChart(chart3, humDataArr, data.humidity);
            }
        });
}, 5000);  // каждые 5 секунд

