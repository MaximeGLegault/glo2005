<template>
    <li class="title">
        <h3>Search result album</h3>
        <div class="title">
            {{title}}
        </div>
        <div class="year">
            {{year}}
        </div>
        <div class="artist">
            {{artist_name}}
        </div>
        <div class="genre">
            {{genre_name}}
        </div>
    </li>
</template>

<script>

    export default {
        name: "SearchResultAlbum",
        props: ['results'],
        watch: {
            results(newValue) {
                if(newValue){
                    this.title = newValue["title"];
                    this.year = newValue["year"];
                    this.genre_name = newValue["genre"];
                    this.artist_name = newValue["artist_name"];
                }
                else {
                    this.title = null;
                    this.year = null;
                    this.genre_name = null;
                    this.artist_name = null;
                }
            }
        },
        data() {
            return {
                rawArtistResult: null,
                rawGenreResult: null,
                title: '',
                year: 0,
                artist_id: 0,
                genre_id: 0,
                artist_name: '',
                genre_name: ''
            };
        },
        methods:{
            init() {
                this.title = this.rawResult["title"];
                this.year = this.rawResult["year"];
                this.genre_name = this.rawResult["genre"];
                this.artist_name = this.rawResult["artist_name"];
            }
        },
        computed: {
            rawResult () {
                return this.results;
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
