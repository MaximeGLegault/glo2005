<template>
    <ul class="list">
        <h3>Search Results for Albums</h3>
        <li class="header">
            <div class="title">
                Title
            </div>
            <div class="artist">
                Year
            </div>
            <div class="album">
                Artist
            </div>
            <div class="genre">
                Genre
            </div>
        </li>
        <album v-for="album of albums" v-bind:key="album.title" v-model="albums" v-bind:artist=album.artist v-bind:genre=album.genre v-bind:year=song.year />
    </ul>
</template>

<script>
    import Album from './Album';
    import api from '@/lib/api';

    export default {
        name: "SearchResultAlbum",
        components: {
            'album': Album
        },
        props: {
            albums: Array
        },
        methods:{

        },
        created(){
            this.albums = api.search_album()
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
