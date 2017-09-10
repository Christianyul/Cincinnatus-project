<template>
  <div id="home">
  
    <h1>{{ msg }}</h1>

	<button @click="component = 'info'">Personal info</button>
    <button @click="component = 'contacts'">Contacts</button>
    <button @click="component = 'medic'">Medical information</button>
	
	<component :is="component"></component>
  </div>
</template>

<script>
import Contacts from './Contacts.vue'
import Info from './Info.vue'
import Medic from './Medic-info.vue'

export default {
  name: 'home',
  data () {
    return {
      msg: 'Student info',
      component: 'info'
    }
  },
  components : {
    'info': Info,
    'contacts': Contacts,
    'medic': Medic
  }
}
</script>

<style lang="scss">

</style>