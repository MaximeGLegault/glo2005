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
            {{genre_id}}
        </div>
    </li>
</template>

<script>
    import api from '@/lib/api';

    export default {
        name: "SearchResultAlbum",
        props: ['results'],
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
             async getArtistName(){
                try{
                    console.log("passé à getArtistName: " + this.artist_id);
                    await api.getArtistName(this.artist_id).then(value => this.rawArtistResult = value);
                }
                catch(err) { throw new Error(`Something failed`); }
                finally {
                    this.artist_name = this.rawArtistResult["name"];
                }
            },
            init() {
                this.title = this.rawResult["title"];
                this.year = this.rawResult["year"];
                this.genre_id = this.rawResult["genre_id"];
                this.artist_id = this.rawResult["artist_id"];
                this.getArtistName();
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
            console.log("Search Result updated");
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
