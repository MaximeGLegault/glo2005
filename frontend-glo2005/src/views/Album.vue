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
            await api.getAlbum(10000003).then(value => {
                this.album = value;
            });
        }
    }


</script>

<style scoped>

</style>
