<template>
    <playlist v-bind:songs="album.songs" v-bind:title="album.album"/>

</template>

<script>
    import {getAlbums} from '../albums.js'
    import Playlist from './Playlist';


    export default {
        name: "Album",
        components: {
            Playlist
        },
        data: () => ({
            album: []
        }),
        created(){
            // debugger;
            const albums = getAlbums();
            this.album = albums[0];
        }

    }


</script>

<style scoped>

</style>
