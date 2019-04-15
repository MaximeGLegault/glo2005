<template>
    <div class="main" v-bind:key="this">
        <h1>
            Search
        </h1>
        <search-bar class="searchBar" v-bind:targetPath="path" v-bind:name="typeOfSearch" v-on:update="handler($event)"/>
        <search-result-album v-bind:results.sync="results" v-model="results" v-if="searchType==='albums' && searchTerm"/>
        <search-result-artist v-if="searchType==='artists' && searchTerm"/>
        <search-result-song v-if="searchType==='songs' && searchTerm"/>
        <search-result-playlist v-if="searchType==='playlists' && searchTerm"/>
        <search-result-user v-if="searchType==='users' && searchTerm"/>
    </div>
</template>

<script>
    import Cookies from 'js-cookie';
    import SearchBar from './SearchBar';
    /*import SearchResult from './SearchResult';*/
    import SearchResultAlbum from "./SearchResultAlbum";
    import SearchResultArtist from "./SearchResultArtist";
    import SearchResultSong from "./SearchResultSong";
    import SearchResultUser from "./SearchResultUser";
    import SearchResultPlaylist from "./SearchResultPlaylist";

    export default {
        name: 'search',
        components: {
            /*'search-result': SearchResult,*/
            'search-result-album': SearchResultAlbum,
            'search-result-artist': SearchResultArtist,
            'search-result-song': SearchResultSong,
            'search-result-user': SearchResultUser,
            'search-result-playlist': SearchResultPlaylist,
            'search-bar': SearchBar,
        },
        methods: {
            handler(event) {
                this.searchTerm = event.searchTerm;
                this.searchType = event.searchType;
                this.results = event.results;
                console.log("results dans search: " + JSON.stringify(this.results));
            },
            init() {
                this.path = this.$route.path;
                this.typeOfSearch = this.$route.name
            },
        },
        data() {
            return {
                searchTerm: '',
                searchType: 'global',
                path: '',
                typeOfSearch: '',
                results: [],
            };
        },
        updated() {
        },
        created() {
            this.init();
        },
        beforeCreate() {
            if (Cookies.get('token') === '') {
                this.$router.push('/login');
            }
        }
    };
</script>

<style scoped>
    h1 {
        color: #d1d1d1;
        text-align: center;
        padding-bottom: 70px;
        padding-top: 20px;
    }
    .searchBar{
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
    }

</style>
