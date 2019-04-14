<template>
    <div class="searchBar">
        <div class="form">
            <input autocomplete="off" @keyup.enter.prevent="toSearch" v-model="searchTerm" id="search" type="text" placeholder="Search...">
            <button class="deep-purple accent-3 waves-effect waves-light btn"><a class="search-button" @click="toSearch">Search</a></button>
        </div>
        <span class="typeButtons">
            <input @click="changeType('global')" type="radio" class="radio" id="global" name="searchType" value="global" v-model="picked" checked><label for="global">All result</label>
      <input @click="changeType('albums')" type="radio" class="radio" id="albums" name="searchType" value="albums" v-model="picked"><label for="albums">Albums</label>
      <input @click="changeType('artists')" type="radio" class="radio" id="artists" name="searchType" value="artists" v-model="picked"><label for="artists">Artists</label>
      <input @click="changeType('songs')" type="radio" class="radio" id="songs" name="searchType" value="songs" v-model="picked"><label for="songs">Songs</label>
      <input @click="changeType('playlists')" type="radio" class="radio" id="playlists" name="searchType" value="playlists" v-model="picked"><label for="playlists">Playlists</label>
      <input @click="changeType('users')" type="radio" class="radio" id="users" name="searchType" value="users" v-model="picked"><label for="users">Users</label>
        </span>
    </div>
</template>

<script>

    import api from '@/lib/api';

    export default {
        name: 'SearchBar',
        props: ['name', 'targetPath'],
        data() {
            return {
                searchTerm: '',
                picked: 'global',
                results: null
            };
        },
        methods: {
            async toSearch() {
                try {
                if (this.picked === 'global') {
                    await api.getSearch(this.searchTerm)
                        .then((value) => {
                            this.results = value.results;
                        });
                } else if (this.picked === 'artists') {
                    await api.getSearchByArtist(this.searchTerm)
                        .then((value) => {
                            this.results = value.results;
                        });
                } else if (this.picked === 'albums') {
                    await api.search_album(this.searchTerm).then(value => this.results = value);
                    console.log("search_album called with search term: " + this.searchTerm + " and search type: " + this.picked + "and the result is: " + JSON.stringify(this.results));
                } else if (this.picked === 'songs') {
                    await api.getSearchBySong(this.searchTerm)
                        .then((value) => {
                            this.results = value.results;
                        });
                } else if (this.picked === 'playlists') {
                    await api.getSearchByPlaylist(this.searchTerm)
                        .then((value) => {
                            this.results = value.results;
                        });
                } else if (this.picked === 'users') {
                    await api.getSearchByUser(this.searchTerm)
                        .then((value) => {
                            this.results = value;
                        });
                }
                }
                catch(err) { throw new Error(`Something failed`); }
                finally
                {
                    this.$emit('update', { searchTerm: this.searchTerm, searchType: this.picked, results: this.results });
                    this.$router.push({ path: `/search/${this.picked}/${this.searchTerm}` });
                }

            },
            created(){
            },
            changeType(picked) {
                this.picked = picked
            }
        },
    };
</script>

<style scoped>
    a:hover{
        color: #42b983;
    }
    a{
        height: 36px;
        color: black;
        cursor: pointer;
    }
    .form{
        height: 36px;
        width: 50%;
        display: flex;
        flex-direction: row;
    }
    .searchBar{
        width: 100%;
        font-size: 1rem;
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
    }
    .typeButtons{
        padding-top: 20px;
    }
    #search{
        width: 90%;
    }

    [type="radio"]:not(:checked)+label, [type="radio"]:checked+label {
        font-size: 1rem;
    }
    [type="radio"]:checked+label:after, [type="radio"].with-gap:checked+label:after {
        background-color: #651fff;
    }

    [type="radio"]:checked+label:after, [type="radio"].with-gap:checked+label:before, [type="radio"].with-gap:checked+label:after {
        border: 2px solid #651fff;
    }

</style>
