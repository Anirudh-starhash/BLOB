<template>
  <div class="chart-container">
    <canvas ref="pieChart"></canvas>
  </div>
</template>

<script>
import { Chart, ArcElement, Tooltip, Legend, PieController } from 'chart.js';

Chart.register(ArcElement, Tooltip, Legend, PieController);

export default {
  name: 'PieChart',
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
      const labels = Object.keys(this.blogInfo); // Blog post titles

      const totalViews = Object.values(this.blogInfo).map(info => info.totalViews); // Total views
      const likePercentages = Object.values(this.blogInfo).map(
        info => ((info.totalLikes / info.totalViews) * 100).toFixed(2)
      ); // Calculate like percentages

      // Define custom colors for each blog post
      const viewColors = [
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD700',
        '#8A2BE2', '#FF6347', '#32CD32', '#FF4500', '#20B2AA',
      ];

      const likeColors = [
        '#FF8C00', '#8A2BE2', '#3CB371', '#DAA520', '#7B68EE',
        '#D2691E', '#FF1493', '#00BFFF', '#32CD32', '#FF4500',
      ];

      const data = {
        labels: labels,
        datasets: [
          {
            label: 'Total Views',
            backgroundColor: viewColors.slice(0, labels.length), // Assign view colors
            data: totalViews,
            borderColor: '#333',
            borderWidth: 1,
            hoverOffset: 25,
          },
          {
            label: 'Like Percentage (%)',
            backgroundColor: likeColors.slice(0, labels.length), // Assign like colors
            data: likePercentages,
            borderColor: '#333',
            borderWidth: 1,
            hoverOffset: 25,
          },
        ],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              boxWidth: 20,
              padding: 15,
            },
          },
          tooltip: {
            callbacks: {
              title: function (tooltipItem) {
                const blogTitle = tooltipItem[0].label;
                return `Blog Post: ${blogTitle}`;
              },
              label: function (tooltipItem) {
                const datasetLabel = tooltipItem.dataset.label || '';
                const value = tooltipItem.raw;
                if (datasetLabel === 'Total Views') {
                  return `${datasetLabel}: ${value} views`;
                } else if (datasetLabel === 'Like Percentage (%)') {
                  return `${datasetLabel}: ${value}% likes`;
                }
                return '';
              },
            },
            backgroundColor: '#333',
            titleColor: '#fff',
            bodyColor: '#fff',
            padding: 10,
          },
        },
        animation: {
          animateRotate: {
            duration: 1500,
            easing: 'easeOutBounce',
          },
          animateScale: {
            duration: 1000,
            easing: 'easeInOutQuad',
          },
        },
      };

      this.chart = new Chart(this.$refs.pieChart, {
        type: 'pie',
        data: data,
        options: options,
      });
    },
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.destroy(); // Clean up the chart instance
    }
  },
};
</script>

<style scoped>
/* Chart Container */
.chart-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  overflow: hidden;
  transform: scale(0.95);
  transition: transform 0.3s ease-in-out;
}

/* Hover Effect for the Chart Container */
.chart-container:hover {
  transform: scale(1); /* Slight zoom on hover */
}

/* Pie Chart CSS Styling */
canvas {
  display: block;
  width: 100%;
  height: auto;
  transition: transform 0.3s ease; /* Animation for scaling */
}

/* Tooltip Styling */
.chartjs-tooltip {
  background-color: #333 !important;
  color: #fff !important;
  border-radius: 5px;
  padding: 10px;
}
</style>
