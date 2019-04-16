<template>
    <div>
        <h2>Results for Songs with title {{this.searchQuery}}</h2>
        <table>
            <tr>
                <th>Title</th>
                <th>Artist</th>
                <th>Album</th>
                <th>Duration</th>
            </tr>
            <tr v-for="song of songs" v-bind:key="song">
                <td>{{song.title}}</td>
                <td>{{song.artist_name}}</td>
                <td>{{song.album_name}}</td>
                <td>{{song.duration}}</td>
            </tr>
        </table>
    </div>
</template>

<script>

    export default {
        name: "SearchResultSong",
        props: ['results', 'searchTerm'],
        watch: {
            results(newValue) {
                if(newValue){
                    this.init();
                }
                else {
                    this.songs = [];
                }
            }
        },
        data() {
            return {
                songs: [
                    {title: ''},
                    {artist_name: ''},
                    {album_name: ''},
                    {duration: 0},

                ]
            };
        },
        methods:{
            init() {
                this.songs = [];
                this.songs.title = '';
                this.songs.artist_name = '';
                this.songs.album_name = '';
                this.songs.duration = 0;
                for (var i = 0; i < this.rawResult.length; i++) {
                    this.songs[i] = [];
                    this.songs[i].title = this.rawResult[i]["title"];
                    this.songs[i].artist_name = this.rawResult[i]["artistName"];
                    this.songs[i].album_name = this.rawResult[i]["album_name"];
                    this.songs[i].duration = this.rawResult[i]["duration"];
                }
            }
        },
        computed: {
            rawResult () {
                return this.results;
            },
            searchQuery () {
                return this.searchTerm;
            }
        },
        created() {
            this.init();
        },
        updated() {
        },
    };


</script>

<style scoped>

    .song {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        flex-wrap: wrap;
        align-items: flex-start;


    }

    .song > * {
        padding: 10px;
        flex-basis: 0;
        flex-grow: 1;
    }

</style>
