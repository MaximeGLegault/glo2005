import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Album from './views/Album.vue'
import Profile from "./views/Profile";
import Signup from "./views/Signup";
import PlaylistView from "./views/PlaylistView";
import Artist from "./views/Artist";
import Search from './views/Search.vue'
import allAlbums from './views/allAlbums'
import allArtists from './views/allArtists'
import allSongs from './views/allSongs'

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
            path: '/artist/:artist_id',
            name: 'artist',
            component: Artist,
        },
        {
            path: '/album/:album_id',
            name: 'album',
            component: Album,
        },
        {
            path: '/songs',
            name: 'allSongs',
            component: allSongs,
        },
        {
            path: '/albums',
            name: 'allAlbums',
            component: allAlbums,
        },
        {
            path: '/artists',
            name: 'allArtists',
            component: allArtists,
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
