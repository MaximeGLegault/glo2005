<template>
    <div>
    <h2>Results for Albums with title {{this.searchQuery}}</h2>
    <table>
        <tr>
            <th>Title</th>
            <th>Year</th>
            <th>Genre</th>
            <th>Artist</th>
        </tr>
        <tr v-for="album of albums" v-bind:key="album">
            <td>{{album.title}}</td>
            <td>{{album.year}}</td>
            <td>{{album.genre_name}}</td>
            <td>{{album.artist_name}}</td>
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
                    // console.log("newValue");
                    // console.log(newValue);
                    // this.albums = [];
                    // for (var i = 1; i < newValue.length; i++) {
                    //     this.albums[this.title].push(this.rawResult["title"]);
                    //     this.albums[this.year].push(this.rawResult["year"]);
                    //     this.albums[this.genre_name].push(this.rawResult["genre"]);
                    //     this.albums[this.artist_name].push(this.rawResult["artist_name"]);
                    // }
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
                this.albums.year = 0;
                this.albums.artist_name = '';
                this.albums.genre_name = '';
                for (var i = 0; i < this.rawResult.length; i++) {
                    this.albums[i] = [];
                    this.albums[i].title = this.rawResult[i]["title"];
                    this.albums[i].year = this.rawResult[i]["year"];
                    this.albums[i].genre_name = this.rawResult[i]["genre"];
                    this.albums[i].artist_name = this.rawResult[i]["artist_name"];
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

    /*.title{*/
    /*flex-grow: 1;*/
    /*}*/

    /*.artist{*/
    /*flex-grow: 1;*/

    /*}*/

    /*.album{*/
    /*flex-grow: 1;*/

    /*}*/
    /*.genre{*/
    /*flex-grow: 1;*/

    /*}*/
    /*.duration{*/
    /*flex-grow: 1;*/

    /*}*/
    /*.year{*/
    /*flex-grow: 1;*/

    /*}*/

</style>
