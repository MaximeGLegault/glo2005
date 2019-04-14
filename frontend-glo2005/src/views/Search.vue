<template>
    <div class="main" v-bind:key="this">
        <h1>
            Search
        </h1>
        <search-bar v-bind:targetPath="path" v-bind:name="typeOfSearch" v-on:update="handler($event)"/>
        <search-result-album v-if="searchType==='albums'"/>
    </div>
</template>

<script>
    import Cookies from 'js-cookie';
    import SearchBar from './SearchBar';
    /*import SearchResult from './SearchResult';*/
    import SearchResultAlbum from "./SearchResultAlbum";

    export default {
        name: 'search',
        components: {
            /*'search-result': SearchResult,*/
            'search-result-album': SearchResultAlbum,
            'search-bar': SearchBar,
        },
        methods: {
            handler(event) {
                this.searchTerm = event.searchTerm;
                this.searchType = event.searchType;
                this.results = event.results;
                console.log(event.results);
                console.log(this.results);
            },
            init() {
                this.path = this.$route.path;
                this.typeOfSearch = this.$route.name
            }
        },
        data() {
            return {
                searchTerm: '',
                searchType: 'global',
                results: [],
                path: '',
                typeOfSearch: '',
            };
        },
        watch: {
            $route() {
                this.init();
            }
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
        text-align: center;
        padding-bottom: 70px;
        padding-top: 20px;
    }

</style>
