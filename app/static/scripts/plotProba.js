const toPercent = function(data) {
  return data.map(e => Math.round(e * 10000) / 100);
};

const plotProba = function(data, id) {
  data = toPercent(data);
  const ctx = document.getElementById(id).getContext("2d");
  const color =
    id === "team_1_proba" ? "rgba(52, 152, 219,1.0)" : "rgba(231, 76, 60,1.0)";
  const chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: [...Array(20).keys()],
      datasets: [
        {
          label: "Probability",
          backgroundColor: color,
          borderColor: "rgba(255, 255, 255,1.0)",
          data: data
        }
      ]
    },
    options: {
      scales: {
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Percentage"
            }
          }
        ],
        xAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Number of goals"
            }
          }
        ]
      }
    }
  });
};
