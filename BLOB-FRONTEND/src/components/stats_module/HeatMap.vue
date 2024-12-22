<template>
  <div class="chart-container">
    <canvas ref="heatmapChart"></canvas>
  </div>
</template>

<script>
import { Chart, Tooltip, Legend, CategoryScale, LinearScale, PointElement } from 'chart.js';

Chart.register(Tooltip, Legend, CategoryScale, LinearScale, PointElement);

export default {
  name: 'HeatmapChart',
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
      if (this.chart) {
        this.chart.destroy(); // Destroy previous chart instance
      }

      // Prepare data for heatmap:
      // Using Blog Post titles and their total views and popularity rates
      const labels = Object.keys(this.blogInfo); // Blog post names
      const totalViews = Object.values(this.blogInfo).map(info => info.totalViews); // Total views
      const popularityRates = Object.values(this.blogInfo).map(info => info.popularityRate); // Popularity rates

      // Combine the two data arrays (totalViews and popularityRates) for heatmap
      const heatmapData = [
        ...labels.map((label, index) => ({
          x: index + 1, // Use 1-based index for blog post names
          y: totalViews[index],
          label: `${label} Total Views`,
        })),
        ...labels.map((label, index) => ({
          x: index + 1, // Use 1-based index for blog post names
          y: popularityRates[index],
          label: `${label} Popularity Rate`,
        })),
      ];

      const data = {
        datasets: [
          {
            label: 'Heatmap Data',
            data: heatmapData,
            backgroundColor: (context) => {
              if (!context.raw) {
                return 'rgba(0,0,0,0.1)';
              }

              const value = context.raw.y; // y-value (either total views or popularity rate)
              const red = Math.min(255, value * 2);
              const green = Math.min(255, 255 - value * 2);
              const blue = Math.min(255, value * 1.5);
              return `rgba(${red}, ${green}, ${blue}, 0.7)`; // Return RGBA color
            },
            borderWidth: 1,
            pointRadius: 10,
          },
        ],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            type: 'category', // Use category scale to display Blog post titles as labels
            labels: labels, // Set x-axis labels to be the blog post names
            title: {
              display: true,
              text: 'Blog Posts',
            },
          },
          y: {
            type: 'linear',
            position: 'left',
            title: {
              display: true,
              text: 'Values (Views / Popularity Rate)',
            },
          },
        },
        plugins: {
          legend: {
            display: false,
          },
          tooltip: {
            callbacks: {
              title: function (tooltipItem) {
                const postIndex = tooltipItem[0].raw.x - 1; // Get the index based on x value (1-based)
                return `Blog Post: ${labels[postIndex]}`; // Format the blog post title
              },
              label: function (tooltipItem) {
                return `Value: ${tooltipItem.raw.y}`; // Show the y-value (either total views or popularity rate)
              },
            },
          },
        },
      };

      this.chart = new Chart(this.$refs.heatmapChart, {
        type: 'scatter', // Scatter chart type to simulate heatmap
        data: data,
        options: options,
      });
    },
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.destroy(); // Clean up chart instance
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
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

canvas {
  display: block;
  width: 100%;
  height: auto;
}
</style>
