<template>
    <div class="main">
        <h1>{{ artist.artist_name }}</h1>
        <ul v-for="album in this.albums" v-bind:key="album.album_id">
            <li>
                <router-link :to="{name: 'album', params: {album_id: album.album_id}}">
                <span>{{ album.title }}</span>
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
    import api from '../lib/api';

    export default {
        name: 'Artist',
        components: {},
        data() {
            return {
                artist: {},
                albums: []
            };
        },
        async created() {
            let artist_id = this.$route.params.artist_id ? this.$route.params.artist_id : 10000002;
            await api.getArtist(artist_id)
                .then((value) => {
                    this.artist = value;
                    this.albums = value.albums
                });
        }
    }
    ;
</script>

<style scoped>
    .main {
        text-align: center;
    }
</style>
