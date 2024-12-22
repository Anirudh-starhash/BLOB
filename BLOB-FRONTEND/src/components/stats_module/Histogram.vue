<template>
  <div class="chart-container">
    <canvas ref="histogramChart"></canvas>
  </div>
</template>

<script>
import { Chart, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js';

Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

export default {
  name: 'HistogramChart',
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
      // Create labels dynamically based on blog post titles
      const labels = Object.keys(this.blogInfo); // Blog post titles

      const totalViews = Object.values(this.blogInfo).map(info => info.totalViews); // Total views for each blog post

      const data = {
        labels: labels, // Labels for each blog post
        datasets: [
          {
            label: 'Total Views',
            backgroundColor: '#FF6384',
            data: totalViews,
            borderColor: '#FF4561',
            borderWidth: 1,
            barThickness: 30, // Adjust thickness of the bars for a histogram effect
          },
        ],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Blog Posts',
            },
          },
          y: {
            beginAtZero: true, // Start from 0
            title: {
              display: true,
              text: 'Total Views',
            },
          },
        },
        plugins: {
          tooltip: {
            callbacks: {
              title: function (tooltipItem) {
                const postTitle = tooltipItem[0].label; // Get blog post title
                return `Post: ${postTitle}`;
              },
              label: function (tooltipItem) {
                const datasetLabel = tooltipItem.dataset.label || '';
                const totalViews = tooltipItem.raw;
                return `${datasetLabel}: ${totalViews} views`;
              },
            },
          },
        },
      };

      new Chart(this.$refs.histogramChart, {
        type: 'bar',
        data: data,
        options: options,
      });
    },
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
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

canvas {
  display: block;
  width: 100%;
  height: auto;
}
</style>
