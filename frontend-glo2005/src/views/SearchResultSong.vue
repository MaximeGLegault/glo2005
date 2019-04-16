<template>
    <div>
        <h2>Results for Songs with title {{this.searchQuery}}</h2>
        <table class="list">
            <tr class="header">
                <th>Title</th>
                <th>Artist</th>
                <th>Album</th>
                <th>Duration</th>
            </tr>
            <tr class="tableItem" v-for="song of songs" v-bind:key="song">
                <td>{{song.title}}</td>
                <td v-on:click="artistNameClicked(song.artist_id)">{{song.artist_name}}</td>
                <td v-on:click="albumNameClicked(song.album_id)">{{song.album_name}}</td>
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
                    {album_id: 0},
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
                    this.songs[i].album_id = this.rawResult[i]["album_id"];
                    this.songs[i].title = this.rawResult[i]["title"];
                    this.songs[i].artist_name = this.rawResult[i]["artist_name"];
                    this.songs[i].album_name = this.rawResult[i]["album_name"];
                    this.songs[i].duration = this.rawResult[i]["duration"];
                }
            },
            artistNameClicked(artist_id) {
                this.$router.push({ path: `/artist/${artist_id}` })
            },
            albumNameClicked(album_id) {
                this.$router.push({ path: `/album/${album_id}` })
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

    h1 {
        text-align: center;
        font-size: 2em;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .list {
        margin-left:auto;
        margin-right:auto;
        margin-top:auto;
        border:           5px solid #4f4f4f;
        border-radius:    8px;
        padding: 40px;
        width: 90%;
        background-image: linear-gradient(#404040, #202020);
        display: flex;
        flex-direction: column;
    }

    .list > * {
        border-bottom: 1px solid white;

    }

    .header {
        font-size: 30px;
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

    .tableItem {
        font-size: 20px;
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        flex-wrap: wrap;
        align-items: flex-start;
        cursor: pointer;
    }

    .tableItem > * {
        padding: 10px;
        flex-basis: 0;
        flex-grow: 1;
    }

</style>
