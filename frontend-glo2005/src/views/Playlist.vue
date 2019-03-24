<template>
    <ul class="list">

        <div class="list-title" >{{title}}</div>

        <li class="header">
            <div class="title">
                Title
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
            <div class="year">
                Year
            </div>
        </li>
        <song v-for="song of songs" v-bind:key="song.title" v-model="songs" v-bind:title=song.title v-bind:artist=song.artist v-bind:album=song.album v-bind:genre=song.genre v-bind:duration=song.duration v-bind:year=song.year />
    </ul>
</template>

<script>
    import Song from './Song';
    export default {
        name: "Playlist",
        components: {
            Song
        },
        props: {
            title: String,
            songs: Array
        },
        methods:{

        },
        created(){
        }
    };



</script>

<style scoped>


    .list {

        border:           5px solid #4f4f4f;
        border-radius:    8px;
        margin:           30px 30px 30px 30px;
        padding:          40px;
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
