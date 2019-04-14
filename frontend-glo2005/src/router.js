import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Album from './views/Album.vue'
import Profile from "./views/Profile";
import Signup from "./views/Signup";
import PlaylistView from "./views/PlaylistView";

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
        },
        {
            path: '/signup',
            name: 'signup',
            component: Signup
        },
        {
            path: '/playlist/:playlistId',
            name: 'playlist',
            component: PlaylistView
        }
    ]
})
