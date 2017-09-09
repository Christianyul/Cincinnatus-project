<template>
  <div id="app">
    <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <h2>Menu Alpha</h2>
    <ul>
      <li> <router-link to='/home'> Home </router-link> </li>
      <li> <router-link to='/login'> Login </router-link> </li>
      <li> <router-link to='/admin'> Admin </router-link> </li>
    
    </ul>
    <h1> +++==============- Component -==============+++</h1>
    <router-view> </router-view>
    <h1> +++==================- -===================+++</h1>
  </div>
</template>

<script>

export default {
  name: 'app',
  data () {
    return {
      msg: 'Cincinnatus Institute'
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
.router-link-active{
  color: gray;
}
</style>
