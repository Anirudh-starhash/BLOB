<template>
  <div class="chart-container pie-chart-3d">
    <canvas ref="pieChart3D"></canvas>
  </div>
</template>

<script>
import { Chart, ArcElement, Tooltip, Legend, PieController } from "chart.js";

Chart.register(ArcElement, Tooltip, Legend, PieController);

export default {
  name: "PieChart3D",
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

      const totalViews = Object.values(this.blogInfo).map((info) => info.totalViews); // Total views
      const popularityRate = Object.values(this.blogInfo).map((info) =>
        ((info.totalLikes / info.totalViews) * 100).toFixed(2)
      ); // Popularity rate

      const data = {
        labels: labels,
        datasets: [
          {
            label: "Total Views",
            backgroundColor: [
              "#FF5733",
              "#33FF57",
              "#3357FF",
              "#FF33A1",
              "#FFD700",
              "#8A2BE2",
            ],
            data: totalViews,
            borderWidth: 1,
            borderColor: "#333",
            hoverBorderColor: "#000",
            hoverOffset: 20,
          },
          {
            label: "Popularity Rate (%)",
            backgroundColor: [
              "#FF8C00",
              "#8A2BE2",
              "#3CB371",
              "#DAA520",
              "#7B68EE",
              "#D2691E",
            ],
            data: popularityRate,
            borderWidth: 1,
            borderColor: "#333",
            hoverBorderColor: "#000",
            hoverOffset: 20,
          },
        ],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "bottom",
            labels: {
              boxWidth: 20,
              padding: 15,
            },
          },
          tooltip: {
            callbacks: {
              title: function (tooltipItem) {
                return `Blog: ${tooltipItem[0].label}`;
              },
              label: function (tooltipItem) {
                const datasetLabel = tooltipItem.dataset.label || "";
                const value = tooltipItem.raw;
                if (datasetLabel === "Total Views") {
                  return `${datasetLabel}: ${value} views`;
                } else if (datasetLabel === "Popularity Rate (%)") {
                  return `${datasetLabel}: ${value}%`;
                }
                return "";
              },
            },
          },
        },
        animation: {
          animateRotate: true,
          animateScale: true,
          duration: 1500,
          easing: "easeOutBounce",
        },
      };

      this.chart = new Chart(this.$refs.pieChart3D, {
        type: "pie",
        data: data,
        options: options,
      });
    },
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>

<style scoped>
.chart-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Enhanced shadow for 3D effect */
  padding: 20px;
  overflow: hidden;
  transition: transform 0.3s ease-in-out;
}

.chart-container:hover {
  transform: scale(1.05); /* Slight zoom effect on hover */
}

canvas {
  display: block;
  width: 100%;
  height: auto;
  transition: transform 0.3s ease;
}

.pie-chart-3d {
  background-color: #f0f8ff;
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.15);
}
</style>
