<template>
  <div id="home">
    <h1>{{ msg }}</h1>
    <button> <router-link to="/admin/add-admin">Add adm</router-link> </button>
    <button>Delete adm</button>
    
    <h2>List of adm...</h2>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Owner management'
    }
  }
}
</script>

<style lang="scss">

</style>