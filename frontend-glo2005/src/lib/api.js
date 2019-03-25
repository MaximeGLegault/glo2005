import axios from 'axios';
import Cookies from 'js-cookie';

const baseUrl = ' http://127.0.0.1:5000/api/';

export default {
    async loginUser(userEmail, userPassword) {
        axios({
            method: 'post',
            url: `${baseUrl}login`,
            data: { email: userEmail, password: userPassword }
        }).then(value => console.log(value))
            .catch(value => console.log(value));
    },

    getSearch(searchTerm) {
        return axios({
            method: 'get',
            url: `${baseUrl}search`,
            headers: {
                Authorization: Cookies.get('token')
            },
            params: {
                q: searchTerm,
            }
        }).then(value => value.data);
    },

    getSearchBySong(searchTerm) {
        return axios({
            method: 'get',
            url: `${baseUrl}search/songs`,
            headers: {
                Authorization: Cookies.get('token')
            },
            params: {
                q: searchTerm,
            }
        }).then(value => value.data);
    },

    getSearchByArtist(searchTerm) {
        return axios({
            method: 'get',
            url: `${baseUrl}search/artists`,
            headers: {
                Authorization: Cookies.get('token')
            },
            params: {
                q: searchTerm,
            }
        }).then(value => value.data);
    },

    getSearchByPlaylist(searchTerm) {
        return axios({
            method: 'get',
            url: `${baseUrl}search/playlists`,
            headers: {
                Authorization: Cookies.get('token')
            },
            params: {
                q: searchTerm,
            }
        }).then(value => value.data);
    },

    getSearchByAlbum(searchTerm) {
        return axios({
            method: 'get',
            url: `${baseUrl}search/albums`,
            headers: {
                Authorization: Cookies.get('token')
            },
            params: {
                q: searchTerm,
            }
        }).then(value => value.data);
    },

    getSearchByUser(searchTerm) {
        return axios({
            method: 'get',
            url: `${baseUrl}search/users`,
            headers: {
                Authorization: Cookies.get('token')
            },
            params: {
                q: searchTerm
            }
        }).then(value => value.data);
    },
}