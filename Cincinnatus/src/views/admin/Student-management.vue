<template>
  <div id="home">
    
    <h1>{{ msg }}</h1>
    <button><router-link to="/admin/add-student">Add student</router-link> </button>
    <button><router-link to="/admin/edit-student/0">Edit student</router-link> </button>
    <button>Delete student</button>
    
    <h2>List of students...</h2>

  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Students management'
    }
  }
}
</script>

<style lang="scss">

</style>