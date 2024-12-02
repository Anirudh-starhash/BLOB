<template>
    <div v-bind:class="['abc',{dark:isDarkMode},{ 'dark-background': isDarkMode }]">
      <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <div class="main">
        <h1>Edit Profile Page
        </h1>
        <p>{{message}}</p>
        <div class="row">
          <form method="post" @submit.prevent="editProfile">
            <div class="mb-7">
              <label for="exampleInputlastname1" class="form-label"><p class="x">Name</p></label>
              <input type="text" class="form-control" id="exampleInputlastname1" aria-describedby="emailHelp" required v-model="name">
            </div>
            <div class="mb-7">
              <label for="exampleInputEmail1" class="form-label"><p class="x">Email address</p></label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" required v-model="email">
            </div>
            <div v-if="email_error">Email not properly Formatted</div>
            <button  type="submit" class="btn btn-primary">Edit</button>
          </form> 
        </div>
        <div class="buttons">
          <div>
            <a @click="cancel">
              <button :class="['btn', isDarkMode ? 'btn-dark' : 'btn-outline-primary', 'p-3', 'lh-1']">Cancel</button>
            </a>
          </div>
        </div>
      </div>
     
  
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import { useRouter } from 'vue-router';
  export default {
   name:'register_page',
   data(){
    return {
      message:'Welcome to Edit Profile Page',
      email:"",
      email_error:"",
      isDarkMode: false,
      password:"",
      name:"",
      type:"",
      confirm_password:"",
      profile_pic:"",
      id:""
    }
   },
   setup(){
    const router=useRouter()
    return {router}
   },
    methods: {
      toggleDarkMode() {
        this.isDarkMode = !this.isDarkMode;
      },
      async onFileChanges1(event){
          const file = event.target.files[0];
            if (file) {
              this.profile_pic = file.name;
            } else {
              this.profile_pic = this.profile_pic
            }
            // Assuming fileInput is the input element
        },
        cancel(){
            this.$router.push({name:'profile_page',params:{id:this.id}})
        },
      async editProfile(){
        try{
          let info = JSON.parse(localStorage.getItem("info")) || {};

          // Update only the name and email keys
          info.name = this.name;
          info.email = this.email;
          localStorage.setItem("info",JSON.stringify(info));
          const response=await axios.post("https://blob-backend.onrender.com/api/edit_profile",
            JSON.stringify({
              id:this.id,
              name:this.name,
              email:this.email,
              profile_pic:this.profile_pic
            }),{
              headers:{
                'Content-Type':'application/json'
              }
            }
          );

          if(response.status===200){
            alert('updated successfully!')

            this.$router.push({path:`/profile_page/${this.id}`})
          }
        }catch(error){
          console.log(error);
        }
      }
    },
    async mounted(){
        const access_token=localStorage.getItem("access_token")
        if(!access_token){
            alert('You have to login first!')
            this.$router.push("/login_page")
        }
        else{
            this.id=JSON.parse(localStorage.getItem("info")).id
            try{
                const r=await axios.post("https://blob-backend.onrender.com/api/user_check_permission",null,
                {
                    headers:{
                    Authorization:`Bearer ${access_token}`
                    }
                }
                );
                if(r.status===200){
                    const response=await axios.get(`https://blob-backend.onrender.com/api/getProfile/${this.id}`)
                    this.profile_pic=response.data.profile_details["profile_pic"]
                    this.name=response.data.profile_details["name"]
                    this.email=response.data.profile_details["email"]
                }
            }
            catch(error){
                console.log(error)
            }
        }
    }
  }
  </script>
  
  <style scoped>
  .abc {
    --bg-color:aliceblue;
    --text-color: black;
    --link-color: blue;
    --input-bg-color: white;
    --input-text-color: black;
    --button-bg-color: white;
    --button-text-color: black;
    --shadow-color:whitesmoke;
  }
  .dark {
    --bg-color: #2c2c2c;
    --text-color:  #6bb5ff;
    --link-color: black;
    --input-bg-color: whitesmoke;
    --input-text-color: black;
    --button-bg-color: #555;
    --button-text-color: #ffffff;
    --shadow-color:gainsboro;
  }
  
  
  
  .left, .right {
    float: left;
    width: 20%; /* The width is 20%, by default */
  }
  
  .main {
    float: left;
    width: 60%; /* The width is 60%, by default */
  }
  
  /* Use a media query to add a breakpoint at 800px: */
  @media screen and (max-width: 800px) {
    .left, .main, .right {
      width: 100%; /* The width is 100%, when the viewport is 800px or smaller */
    }
  }
  
  .dark .c{
    color:black;
  }
  .x3{
    font-size:15px;
  }
  .abc {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    min-width: 100%;
    background-image: url("../../assets/images/dmp_index.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-color: var(--bg-color);
    color: var(--text-color);
  }
  
  
  .x:hover {
    transform: translate(2px);
  }
  
  .x {
    height: 40px;
  }
  
  .main {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 20px;
  }
  
  .row {
    box-sizing: border-box;
    box-shadow: 0 0 15px var(--shadow-color);
    width: 700px;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: var(--bg-color);
    border-radius: 50px;
    cursor: pointer;
    font-size: 15px;
    padding: 40px;
  }
  
  .dark  {
    background-color: black;
    background-image: url("../../assets/images/section.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    width:100%;
  
  }
  .dark h1{
    color: white;
  }
  
  
  .buttons {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 40px;
  }
  
  form {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    gap: 40px;
    width: 500px;
  }
  
  p {
    color: var(--link-color);
  }
  
  p, a {
    font-size: 24px;
  }
  
  .x,.c {
    font-size: 18px;
    color: var(--text-color);
  }
  
  .password-container .input-group {
    display: flex;
  }
  
  .password-container .input-group .input-group-text {
    cursor: pointer;
    background-color: var(--input-bg-color);
    color: var(--input-text-color);
  }
  h1,p{
    color :white;
  }
  </style>
  