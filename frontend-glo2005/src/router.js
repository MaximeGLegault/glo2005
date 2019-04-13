import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Album from './views/Album.vue'
import Profile from "./views/Profile";

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/album',
            name: 'album',
            component: Album
        },
        {
            path: '/profile',
            name: 'profile',
            component: Profile
        }
    ]
})
