import axios from 'axios';
import Cookies from 'js-cookie';

const baseUrl = ' http://127.0.0.1:5000/api/';

export default {
    async loginUser(userEmail, userPassword) {
        return axios({
            method: 'post',
            url: `${baseUrl}login`,
            data: {email: userEmail, password: userPassword}
        }).then(value => console.log(value))
            .catch(value => console.log(value));
    },

    async getAlbum(album_id) {
        return axios({
            method: 'get',
            url: `${baseUrl}albums/${album_id}`
        }).then(value => value.data)
            .catch(value => console.log(value));
    },

    async getSearch(search_term, search_type)
    {
        return axios({
            method: 'get',
            url: `${baseUrl}search/${search_type}/${search_term}`
        }).then(value => value.data)
            .catch(value => console.log(value.data));
    },

    async search_album(album_title){
        return axios({
          method: 'get',
          url: `${baseUrl}search/albums/${album_title}`
        }).then(value => value.data)
            .catch(value => console.log(value + "search_album rejected"));
    },

    async getSearchBySong(searchTerm) {
        return axios({
            method: 'get',
            url: `${baseUrl}search/${searchTerm}`,
            headers: {
                Authorization: Cookies.get('token')
            },
            params: {
                q: searchTerm,
            }
        }).then(value => value.data);
    },

    async getSearchByArtist(searchTerm) {
        return axios({
            method: 'get',
            url: `${baseUrl}search/${searchTerm}`,
            headers: {
                Authorization: Cookies.get('token')
            },
            params: {
                q: searchTerm,
            }
        }).then(value => value.data);
    },

    async getSearchByPlaylist(searchTerm) {
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

    async getSearchByAlbum(searchTerm) {
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

    async getSearchByUser(searchTerm) {
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
