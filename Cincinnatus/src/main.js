import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Admin from './views/Admin.vue'
import Home from './views/Home.vue'
import Login from './views/Login.vue'

Vue.use(VueRouter);

const routes = [
	{path: '/', component: Home},
	{path: '/home', component: Home},
	{path: '/login', component: Login},
	{path: '/admin', component: Admin}
];

const router = new VueRouter({
	routes,
	mode: 'history'
});

Vue.component('admin', Admin);
Vue.component('login', Login);
Vue.component('home', Home);
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
