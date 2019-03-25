<template>
    <div class="main" v-bind:key="this">
        <search-bar v-on:update="handler($event)"/>
        <search-result v-on:update2="handler2()"
                       v-if="this.results"
                       :key="this.searchTerm"
                       :results="results"
                       :searchTerm="searchTerm"
                       :searchType="searchType"
        />
    </div>
</template>

<script>
    import Cookies from 'js-cookie';
    import api from '@/lib/api';
    import SearchBar from './SearchBar';
    import SearchResult from './SearchResult';

    export default {
        name: 'Search',
        components: {
            SearchResult,
            SearchBar
        },
        methods: {
            handler(event) {
                this.searchTerm = event.searchTerm;
                this.searchType = event.searchType;
            },
            handler2() {
                this.$router.replace({
                    name: 'Search', query: { q: this.searchTerm }
                });
            }
        },
        data() {
            return {
                searchTerm: '',
                searchType: 'global',
                results: []
            };
        },
        async created() {
            this.searchTerm = this.$route.query.q;
            await api.getSearch(this.searchTerm)
                .then((value) => {
                    this.results = value.results;
                });
        },
        async updated() {
            if (this.searchType === 'global') {
                await api.getSearch(this.searchTerm)
                    .then((value) => {
                        this.results = value.results;
                    });
            } else if (this.searchType === 'artists') {
                await api.getSearchByArtist(this.searchTerm)
                    .then((value) => {
                        this.results = value.results;
                    });
            } else if (this.searchType === 'albums') {
                await api.getSearchByAlbum(this.searchTerm)
                    .then((value) => {
                        this.results = value.results;
                    });
            } else if (this.searchType === 'songs') {
                await api.getSearchBySong(this.searchTerm)
                    .then((value) => {
                        this.results = value.results;
                    });
            } else if (this.searchType === 'playlists') {
                    await api.getSearchByPlaylist(this.searchTerm)
                        .then((value) => {
                            this.results = value.results;
                        });
            } else if (this.searchType === 'users') {
                await api.getSearchByUser(this.searchTerm)
                    .then((value) => {
                        this.results = value;
                    });
            }
        },
        beforeCreate() {
            if (Cookies.get('token') === '') {
                this.$router.push('/login');
            }
        }
    };
</script>

<style scoped>

</style>
