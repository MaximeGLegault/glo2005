<template>
    <playlist v-bind:songs="this.playlist.songs" v-bind:title="this.playlist.title"/>
</template>

<script>
    import api from '../lib/api';
    import Playlist from "./Playlist";

    export default {
        name: "PlaylistView",
        components: {
            Playlist
        },
        data: () => ({
            playlistId: 0,
            playlist: {
                playlist_id: -1,
                title: "",
                songs: []
            },
            songs: []
        }),
        async created() {
            this.playlistId = this.$route.params.playlistId;

            await api.getSongsOfPlaylist(this.playlistId)
                .then(value => this.playlist = value)
                .catch(() => this.playlist.title = 'FAILED TO LOAD')
        }
    }
</script>

<style scoped>

</style>
