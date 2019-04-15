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

    async getSearch(search_type, search_term)
    {
        return axios({
            method: 'get',
            url: `${baseUrl}search/${search_type}/${search_term}`
        }).then(value => value.data)
            .catch(function (error) {
                if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx
                    console.log("error.response.data: " + JSON.stringify(error.response.data));
                    console.log("error.response.status: " + error.response.status);
                    console.log("error.response.headers: " + error.response.headers);
                    return error.response;
                } else if (error.request) {
                    // The request was made but no response was received
                    // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                    // http.ClientRequest in node.js
                    console.log("error.request: " + error.request);
                } else {
                    // Something happened in setting up the request that triggered an Error
                    console.log('Error', error.message);
                }
                console.log("error.config: " + error.config);
            });
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
