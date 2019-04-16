<template>
    <div>
        <h2>Results for Artists with name {{this.searchQuery}}</h2>
        <table>
        <tr>
            <th>Name</th>
            <th>Years active</th>
        </tr>
        <tr v-for="artist of artists" v-bind:key="artist">
            <td>{{artist.artist_name}}</td>
            <td>{{artist.year_active}}</td>
        </tr>
    </table>
    </div>
</template>

<script>

    export default {
        name: "SearchResultArtist",
        props: ['results', 'searchTerm'],
        watch: {
            results(newValue) {
                if(newValue){
                    this.init();
                }
                else {
                    this.artists = [];
                }
            }
        },
        data() {
            return {
                artists: [
                    {artist_name: ''},
                    {year_active: 0}
                ]
            };
        },
        methods:{
            init() {
                this.artists = [];
                this.artists.artist_name = '';
                this.artists.year_active = 0;
                for (var i = 0; i < this.rawResult.length; i++) {
                    this.artists[i] = [];
                    this.artists[i].artist_name = this.rawResult[i]["artist_name"];
                    this.artists[i].year_active = this.rawResult[i]["year_active"];
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
