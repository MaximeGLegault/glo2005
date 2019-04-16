import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import login from './views/login.vue'
import Album from './views/Album.vue'
import Search from './views/Search.vue'

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: login
        },
        {
            path: '/Album',
            name: 'album',
            component: Album
        },
        {
            path: '/search/albums/:title',
            name: 'searchByAlbum',
            component: Search
        },
        {
            path: '/search',
            name: 'search',
            component: Search
        },
        {
            path: '/search/artists/:artist_name',
            name: 'searchByArtists',
            component: Search
        },
        {
            path: '/search/songs/:id',
            name: 'searchBySong',
            component: Search
        },
        {
            path: '/search',
            name: 'search',
            component: Search
        }
        ]
})