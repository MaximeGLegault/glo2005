<template>
    <div>
        <h1>Results for artists with name containing: {{this.searchQuery}}</h1>
        <table class="list">
        <tr class="header">
            <th>Name</th>
            <th>Years active</th>
        </tr>
        <tr class="tableItem" v-for="artist of artists" v-bind:key="artist">
            <td v-on:click="artistNameClicked(artist.artist_id)">{{artist.artist_name}}</td>
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
            },
            artistNameClicked(artist_id) {
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

    .loading {
        margin-left:auto;
        margin-right:auto;
        border: 16px solid #f3f3f3; /* Light grey */
        border-top: 16px solid #3498db; /* Blue */
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 2s linear infinite;
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
