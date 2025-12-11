document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('applications-chart').getContext('2d');

    const dates = applicationsData.map(item => {
        // Assuming item[0] is a string like '2023-10-27T00:00:00.000Z' or just '2023-10-27'
        const date = new Date(item[0]);
        return date.toLocaleDateString();
    });
    const counts = applicationsData.map(item => item[1]);

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Applications per Day',
                data: counts,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                tension: 0.1,
                fill: true,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            },
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Daily Application Submissions'
                }
            }
        }
    });
});
