<template>
  <div id="admin">
    
    <h1>{{ msg }}</h1>
    <button> <router-link to="/admin/students-management">Students management</router-link> </button>
    
    <button> <router-link to="/admin/courses-management">Courses management </router-link> </button>
	<button v-if="rango === 'adm'"> <router-link to="/admin/admin-management">Admins management</router-link> </button>

	<router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'Admin',
  data () {
    return {
      msg: 'ADMIN',
      rango: 'adm'
    }
  }
}
</script>

<style lang="scss">

</style>