<template>
  <div class="scatter-plot">
    <canvas ref="scatterChart"></canvas>
  </div>
</template>

<script>
import { Chart, ScatterController, LinearScale, PointElement, Tooltip, Legend } from "chart.js";

Chart.register(ScatterController, LinearScale, PointElement, Tooltip, Legend);

export default {
  name: "ScatterPlotBlog",
  props: {
    blogInfo: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      const labels = Object.keys(this.blogInfo); // Blog titles
      const dataPoints = Object.values(this.blogInfo); // Blog statistics

      const data = {
        datasets: [
          {
            label: "Blog Statistics",
            data: labels.map((label, index) => {
              const info = dataPoints[index];
              return {
                x: info.totalViews, // x-axis is the total views
                y: info.popularityRate, // y-axis is the popularity rate
                label: label, // Blog title
                details: info, // Store additional details for use in tooltips
              };
            }),
            backgroundColor: "#FF5733",
            pointBorderColor: "#36A2EB",
            pointBackgroundColor: "#FFCE56",
            pointBorderWidth: 2,
            pointRadius: 6,
            hoverBackgroundColor: "#FF9F40", // Change color on hover
            hoverBorderWidth: 3,
            hoverBorderColor: "#FF5733",
          },
        ],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
          },
          tooltip: {
            enabled: true,
            callbacks: {
              title: function (tooltipItem) {
                return `Blog: ${tooltipItem[0].raw.label}`; // Show the blog title
              },
              label: function (tooltipItem) {
                const { details } = tooltipItem[0].raw;
                return `Popularity Rate: ${tooltipItem[0].raw.y}%\nTotal Views: ${details.totalViews}`;
              },
            },
          },
        },
        scales: {
          x: {
            type: "linear",
            position: "bottom",
            title: {
              display: true,
              text: "Total Views",
            },
          },
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Popularity Rate (%)",
            },
          },
        },
      };

      new Chart(this.$refs.scatterChart, {
        type: "scatter",
        data: data,
        options: options,
      });
    },
  },
};
</script>

<style scoped>
.scatter-plot {
  background-color: aliceblue;
  background-size: cover;
  background-position: center;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

canvas {
  display: block;
  width: 100%;
  height: auto;
}
</style>
