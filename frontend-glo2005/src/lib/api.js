import axios from 'axios';
import Cookies from 'js-cookie'

const baseUrl = ' http://127.0.0.1:5000/api/';

export default {
    async loginUser(username, userPassword) {
        return axios({
            method: 'post',
            url: `${baseUrl}login`,
            data: {username: username, password: userPassword}
        }).then(value => value.data)
            .catch(value => console.log(value));
    },

    async signUp(username, email, password) {
        return axios({
            method: 'post',
            url: `${baseUrl}signup`,
            data: {username: username, email: email, password: password}
        }).then(value => value.data)
            .catch(value => {
                console.log(value);
                throw value;
            });
    },

    async getAlbum(album_id) {
        return axios({
            method: 'get',
            url: `${baseUrl}albums/${album_id}`
        }).then(value => value.data)
            .catch(value => console.log(value));
    },

    async getTokenInfo() {
        let token = Cookies.get('token');
        if (token === undefined || token === "") {
            return Promise.reject("no token");
        }
        return axios({
            method: 'get',
            url: `${baseUrl}token`,
            headers: {'Authorization': "Bearer " + token}
        }).then(value => value.data);
    },

    async getProfile() {
        let token = Cookies.get('token');
        return axios({
            method: 'get',
            url: `${baseUrl}profile`,
            headers: {'Authorization': "Bearer " + token}
        }).then(value => value.data);
    },

    async getSongsOfPlaylist(playlist_id) {
        return axios({
            method: 'get',
            url: `${baseUrl}playlists/${playlist_id}`,
        }).then(value => value.data);
    },

    async deletePlaylist(playlist_id) {
        return axios({
            method: 'delete',
            url: `${baseUrl}playlists/${playlist_id}`,
        }).then(value => value.data);
    }
}
