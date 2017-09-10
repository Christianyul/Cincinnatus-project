<template>
  <div id="home">
    
    <h1>{{ msg }}</h1>
    <button><router-link to="/admin/add-course">Add course</router-link></button>
    <button><router-link to="/admin/edit-course/0">Edit course</router-link> </button>
    <button>Delete course</button>
    
    <h2>List of courses...</h2>

  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Courses management'
    }
  }
}
</script>

<style lang="scss">

</style>