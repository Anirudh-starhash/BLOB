<template>
  <div class="chart-container">
    <canvas ref="barChart"></canvas>
  </div>
</template>

<script>
import { Chart, BarElement, CategoryScale, LinearScale, Tooltip, Legend, BarController } from 'chart.js';

Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend, BarController); // Register BarController

export default {
  name: 'BarChart',
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
      // Create labels dynamically based on post categories
      const labels = Object.keys(this.blogInfo).map((_, index) => `Category ${index + 1}`);

      const totalViews = Object.values(this.blogInfo).map(info => info.totalViews); // Total views
      const popularityRates = Object.values(this.blogInfo).map(info => info.popularityRate); // Popularity rates

      const data = {
        labels: labels, // Use Category 1, Category 2, ...
        datasets: [
          {
            label: 'Total Views',
            backgroundColor: '#36A2EB',
            data: totalViews,
            borderColor: '#1E74FF',
            borderWidth: 1,
          },
          {
            label: 'Popularity Rate (%)',
            backgroundColor: '#FF6384',
            data: popularityRates,
            borderColor: '#FF3366',
            borderWidth: 1,
          },
        ],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Views / Popularity (%)',
            },
          },
        },
        plugins: {
          tooltip: {
            callbacks: {
              title: function (tooltipItem) {
                const categoryLabel = tooltipItem[0].label; // Get Category label (e.g., Category 1)
                return `Blog Category: ${categoryLabel}`;
              },
              label: function (tooltipItem) {
                const datasetLabel = tooltipItem.dataset.label || '';
                const blogDetails = tooltipItem.raw;
                if (datasetLabel === 'Total Views') {
                  return `${datasetLabel}: ${blogDetails} views`;
                } else if (datasetLabel === 'Popularity Rate (%)') {
                  return `${datasetLabel}: ${blogDetails}%`;
                }
                return '';
              },
            },
          },
        },
      };

      new Chart(this.$refs.barChart, {
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
