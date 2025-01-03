<style scoped>
.x {
  color: #fed7aa;
}
.x1 {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.x:hover {
  background-color: transparent !important;
}
.left,
.right {
  float: left;
  width: 20%;
}
.add {
  margin-top: auto;
}
#add {
  width: 70px;
  height: 70px;
  padding: 10px 16px;
  border-radius: 35px;
  font-size: 30px;
  text-align: center;
}
#add:hover {
  transform: translate(2px);
  background-color: blue;
  color: white;
}
.main {
  float: left;
  width: 60%;
}
@media screen and (max-width: 800px) {
  .left,
  .main,
  .right {
    width: 100%;
  }
}
h1 {
  color: salmon;
  text-align: center;
  font-family: foglghten;
  font-weight: bold;
  font-size: 40px;
}
p {
  color: darkblue;
  font-family: foglghten;
  font-size: 25px;
}
.center {
  display: flex;
  flex-direction: row;
  gap: 20px;
}
.image {
  align-items: center;
}
.container-fluid {
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;
}
.image {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 500px;
  margin-top: 150px;
}
.intro {
  display: flex;
  flex-direction: column;
  width: 70%;
}
.text {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.row {
  font-size: 20px;
  color: blue;
  height: 100%;
  margin-top: 50px;
}
.main-class {
  display: flex;
  flex-direction: column;
  background-size: cover;
  background-image: url('../../assets/images/dmp_index.png');
  background-repeat: no-repeat;
  min-height: 100vh;
}
.dark {
  display: flex;
  flex-direction: column;
  background-size: cover;
  background-image: url('../../assets/images/section.jpg');
  background-repeat: no-repeat;
  min-height: 100vh;
}
span {
  color: red;
}
.main-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  gap: 30px;
  padding: 20px;
}
.add {
  margin-top: auto;
  width: 200px;
  height: 50px;
}
.add:hover {
  transform: translate(2px);
}
.h2light {
  font-size: 22px;
  color: darkblue;
  font-weight: bold;
  margin-bottom: auto;
}
.h2dark {
  font-size: 22px;
  color: black;
  font-weight: bold;
  margin-bottom: auto;
}
h2,
p,
a {
  font-family: "Courier New", Courier, "Lucida Sans Typewriter", "Lucida Typewriter", monospace;
  font-size: 25px;
  font-style: normal;
  font-variant: normal;
  font-weight: 700;
  line-height: 26.4px;
}
.pie-chart,
.bar-chart,
.chart-3d {
  background-color: aliceblue;
  background-size: cover;
  background-position: center;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}
.com {
  display: flex;
  flex-direction: row;
  gap: 20px;
}
</style>
