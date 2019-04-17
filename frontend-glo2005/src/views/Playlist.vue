<template>
    <ul class="list">

        <div class="list-title">{{title}}</div>
        <li class="header">
            <div class="title">
                Song
            </div>
            <div class="artist">
                Artist
            </div>
            <div class="album">
                Album
            </div>
            <div class="genre">
                Genre
            </div>
            <div class="duration">
                Duration
            </div>
        </li>
        <SongItem v-for="song of songs" v-bind:key="song.song_id" v-model="songs" :song="song"/>
    </ul>
</template>

<script>
    import SongItem from './Song';

    export default {
        name: "Playlist",
        components: {
            SongItem
        },
        props: {
            title: String,
            songs: Array
        },
        methods: {
        },
        created() {
        }
    };


</script>

<style scoped>

    .list {
        border: 5px solid #4f4f4f;
        border-radius: 8px;
        margin: 30px 30px 30px 30px;
        padding: 40px;
        width: 90%;
        background-image: linear-gradient(#404040, #202020);
        display: flex;
        flex-direction: column;
    }

    .list > * {
        border-bottom: 1px solid white;
    }

    .list-title {
        font-size: 45px;
        border: 0px;
        padding-bottom: 30px;
    }

    .header {
        font-size: 25px;
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        flex-wrap: wrap;
        align-items: flex-start;
    }

    .header > * {
        padding: 10px;
        flex-basis: 0;
        flex-grow: 1;
    }

</style>
