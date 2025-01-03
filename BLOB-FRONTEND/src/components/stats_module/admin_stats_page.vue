<template>
  <div class="wrapper">
    <!-- All page content -->
    <div class="content">
      <librarian_header :showSections="false" :showLib="false" :isDarkMode="isDarkMode" @toggleDarkMode="toggleDarkMode" />
  
      <div class="main-content">
        <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">{{ stats_status }}</h2>
        
        <div class="com">
          <PieChart v-if="blogInfo && Object.keys(blogInfo).length" :blogInfo="blogInfo" />
          <HeatMap v-if="blogInfo && Object.keys(blogInfo).length" :blogInfo="blogInfo" />
          <Histogram v-if="blogInfo && Object.keys(blogInfo).length" :blogInfo="blogInfo" />
          <BarChart v-if="blogInfo && Object.keys(blogInfo).length" :blogInfo="blogInfo" />

        </div>
  
        <div class="action-button" @click="getreport">
          <button class="btn btn-primary">Get Report</button>
        </div>
      </div>
    </div>
  
    <!-- Footer -->
    <footer_page />
  </div>
  
  </template>
  
  <script scoped>
  import librarian_header from '../admin_module/admin_header.vue';
  import footer_page from '../other_module/footer_page.vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import PieChart from '../stats_module/PieChart.vue';
  import Histogram from '../stats_module/Histogram.vue';
  import BarChart from '../stats_module/BarChart.vue';
  import HeatMap from '../stats_module/HeatMap.vue';
  
  export default {
    name: "admin_stats_page",
    data() {
      return {
        request_status: 'Currently No Requests Receive',
        stats_status: 'Stats Page is up to date',
        monitor_status: 'No Users to Monitor Currently',
        isDarkMode: false,
        blogInfo: {}, // Initialize as empty
      };
    },
    components: {
      librarian_header,
      footer_page,
      PieChart,
      BarChart,
      Histogram,
      HeatMap
    },
    setup() {
      const router = useRouter();
      return { router };
    },
    methods: {
      toggleDarkMode(isDark) {
        this.isDarkMode = isDark;
      },
      async getreport(){
        try{
          const r=await axios.get("https://blob-backend.onrender.com/api/generate_report");
          if(r.status==200){
            alert(`Report Sent to Mail Check it out`)
          }
        }
        catch(error){
          console.log(error);
        }
      }
    },
    async mounted() {
      const access_token = localStorage.getItem("access_token");
      if (!access_token) {
        alert('You need to login first to come here!');
        this.$router.push("/admin_page");
      } else {
        try {
          const r = await axios.post("https://blob-backend.onrender.com/api/lib_check_permission", null, {
            headers: {
              Authorization: `Bearer ${access_token}`,
            },
          });
          if (r.status === 200) {
            const response = await axios.get("https://blob-backend.onrender.com/api/getAnalysisDetails");
            this.blogInfo = response.data.blogInfo || {}// Populate blogInfo with data
          } else {
            localStorage.clear();
            this.$router.push("/unauthorized");
          }
        } catch (error) {
          console.log(error);
        }
      }
    },
  };
  </script>
  
  <style scoped>
  .main-content {
    display: flex;
    background-size: cover;
    background-image: url('../../assets/images/dmp_index.png');
    background-repeat: no-repeat;
    min-height: 100vh;
  }
  
 
  
  .main-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    gap: 40px;
    padding: 60px;
  }
  
  h2{
    color:white;
    font-weight: bold;
  }
  
  .pie-chart,.bar-chart{
    background-color: aliceblue;
    background-size: cover;
    background-position: center;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  }
  
  .com{
    display: flex;
    flex-direction: row;
    gap:20px;
  }
  </style>
  