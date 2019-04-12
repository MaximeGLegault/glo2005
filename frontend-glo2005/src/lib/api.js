import axios from 'axios';

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
    }
}
