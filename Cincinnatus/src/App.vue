<template>
  <div id="app">

  
    <div id="content">

      <div id="slidebar"> 
        <img  id="logo" src="./img/logo.png" alt="">
        
        <ul>
          <li> <router-link to='/home'> Home </router-link> </li>
          <li> <router-link to='/login'> Login </router-link> </li>
          <li> <router-link to='/admin'> Admin </router-link> </li>
        </ul>
      </div>

      <div id="views">
        <router-view> </router-view>
      </div>

    </div>
    
    
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
  color: #2c3e50;
}

#slidebar {
  display: flex;
  flex-direction: column;
  width: 15%;
  height: 98%;
  position: absolute;
  color: white;
  background-color: #222222;

}

#content {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
}

#views {
  margin-left: 16%;
  width: 84%;
}
#logo {
  display: flex;
  margin-left: 0%;
  width: 100%;
  height: 10%;
}

h1, h2 {
  font-weight: normal;
}

#slidebar ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-top: 15px;
}

a {
  color: #42b983;
}
.router-link-active{
  color: gray;
}

</style>
