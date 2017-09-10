import Admin from './views/Admin.vue'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import PersonalInfo from './views/student/Personal-info.vue'
import StudentSchedule from './views/student/Student-schedule.vue'
import CourseControl from './views/student/Course-control.vue'
import StudentManagement from './views/admin/Student-management.vue'
import AdmManagement from './views/admin/Adms-management.vue'
import CoursesManagement from './views/admin/Courses-management.vue'
import AddStudent from './views/admin/Add-student.vue'
import AddCourse from './views/admin/Add-course.vue'
import AddAdm from './views/admin/Add-adm.vue'
import EditStudent from './views/admin/Edit-student.vue'
import EditCourse from './views/admin/Edit-course.vue'


export const routes = [
	{path: '/', component: Home},
	{path: '/home', component: Home},
	{path: '/myinfo', component: PersonalInfo},
	{path: '/schedule', component: StudentSchedule},
	{path: '/course', component: CourseControl},
	{path: '/login', component: Login},
	{path: '/admin', component: Admin, children: [
		{path: 'students-management', component: StudentManagement},
		{path: 'admin-management', component: AdmManagement},
		{path: 'courses-management', component: CoursesManagement}
	]},
	{path: '/admin/add-student', component: AddStudent},
	{path: '/admin/add-course', component: AddCourse},
	{path: '/admin/add-admin', component: AddAdm},
	{path: '/admin/edit-student/:id', component: EditStudent},
	{path: '/admin/edit-course/:id', component: EditCourse}

];
