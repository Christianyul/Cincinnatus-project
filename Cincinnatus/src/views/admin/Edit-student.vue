<template>
  <div id="home">
    
    <h1>{{ msg }} id:  {{ $route.params.id}}</h1>

  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Edit student'
    }
  }
}
</script>

<style lang="scss">

</style>