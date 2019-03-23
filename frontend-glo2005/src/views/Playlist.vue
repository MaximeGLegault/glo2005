<template>
    <ul>
        <song v-for="song of songs" v-bind:key="song.title" title="song.title" artist="song.artist" album="song.album" genre="song.genre" duration="song.duration" year="song.year"/>
    </ul>
</template>

<script>
    import Song from './Song';
    export default {
        name: "Playlist",
        props: {
            songs: Array
        },
        methods:{

        }
    };



</script>

<style scoped>

</style>
