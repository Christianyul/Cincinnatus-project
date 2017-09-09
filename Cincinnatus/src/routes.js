import Admin from './views/Admin.vue'
import Home from './views/Home.vue'
import Login from './views/Login.vue'

export const routes = [
	{path: '/', component: Home},
	{path: '/home', component: Home},
	{path: '/login', component: Login},
	{path: '/admin', component: Admin}
];
