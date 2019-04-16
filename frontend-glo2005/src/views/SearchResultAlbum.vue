<template>
    <div>
        <div class="list-title" >Results for Albums with title {{this.searchQuery}}</div>
    <table class="list">
        <tr class="header">
            <th>Title</th>
            <th>Year</th>
            <th>Genre</th>
            <th>Artist</th>
        </tr>
        <tr class="tableItem" v-for="album of albums" v-bind:key="album">
            <td v-on:click="albumTitleClicked(album.album_id)">{{album.title}}</td>
            <td>{{album.year}}</td>
            <td>{{album.genre_name}}</td>
            <td v-on:click="albumArtistNameClicked(album.artist_id)">{{album.artist_name}}</td>
        </tr>
    </table>
    </div>
</template>


<script>

    export default {
        name: "SearchResultAlbum",
        props: ['results', 'searchTerm'],
        watch: {
            results(newValue) {
                if(newValue){
                    this.init();
                }
                else {
                    this.albums = [];
                }
            }
        },
        data() {
            return {
                albums: [
                    {title: ''},
                    {album_id: 0},
                    {year: 0},
                    {artist_id: 0},
                    {genre_id: 0},
                    {artist_name: ''},
                    {genre_name: ''},
                ]
            };
        },
        methods:{
            init() {
                this.albums = [];
                this.albums.title = '';
                this.albums.album_id = 0;
                this.albums.year = 0;
                this.albums.artist_name = '';
                this.albums.genre_name = '';
                for (var i = 0; i < this.rawResult.length; i++) {
                    this.albums[i] = [];
                    this.albums[i].title = this.rawResult[i]["title"];
                    this.albums[i].album_id = this.rawResult[i]["album_id"];
                    this.albums[i].year = this.rawResult[i]["year"];
                    this.albums[i].genre_name = this.rawResult[i]["genre"];
                    this.albums[i].artist_name = this.rawResult[i]["artist_name"];
                }
            },
            albumTitleClicked(album_id) {
                this.$router.push({ path: `/album/${album_id}` })
            },
            albumArtistNameClicked(artist_id) {
                this.$router.push({ path: `/artist/${artist_id}` })
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

    .loadingSymbolPadding {
        padding-bottom: 27px;
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

    .list-title {
        align-self: center;
        font-size: 45px;
        border: 0px;
        padding-bottom: 30px;
        padding-left: 30px;
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
