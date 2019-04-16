<template>
    <playlist v-if="this.album" v-bind:songs="album.songs" v-bind:title="album.title"/>

</template>

<script>
    import Playlist from './Playlist';
    import api from "../lib/api";


    export default {
        name: "Album",
        components: {
            Playlist
        },
        data: () => ({
            album: []
        }),
        async created() {
            let album_id = this.$route.params.album_id ? this.$route.params.album_id : 10000002;
            await api.getAlbum(album_id).then(value => {
                this.album = value;
            });
        }
    }


</script>

<style scoped>

</style>
