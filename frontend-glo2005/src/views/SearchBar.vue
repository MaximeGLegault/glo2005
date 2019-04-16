<template>
    <div class="searchBar">
        <div class="form">
            <input class="searchText" autocomplete="off" @keyup.enter.prevent="toSearch" v-model="searchTerm" id="search" type="text" placeholder="Search...">
            <button class="deep-purple accent-3 waves-effect waves-light btn"><a class="search-button" @click="toSearch">Search</a></button>
        </div>
        <div style="text-align:center" class="errorMessage" v-if="noSearchTerm">
            <b class ="errorMessage">Please correct the following error:</b>
                <p>The search is empty</p>
        </div>
        <div style="text-align:center" class="errorMessage" v-if="errors">
            <b class ="errorMessage">Album not found</b>
        </div>
        <span class="typeButtons">
            <input @click="changeType('global')" type="radio" class="radio" id="global" name="searchType" value="global" v-model="searchType" checked><label for="global">All result</label>
      <input @click="changeType('albums')" type="radio" class="radio" id="albums" name="searchType" value="albums" v-model="searchType"><label for="albums">Albums</label>
      <input @click="changeType('artists')" type="radio" class="radio" id="artists" name="searchType" value="artists" v-model="searchType"><label for="artists">Artists</label>
      <input @click="changeType('songs')" type="radio" class="radio" id="songs" name="searchType" value="songs" v-model="searchType"><label for="songs">Songs</label>
      <input @click="changeType('playlists')" type="radio" class="radio" id="playlists" name="searchType" value="playlists" v-model="searchType"><label for="playlists">Playlists</label>
      <input @click="changeType('users')" type="radio" class="radio" id="users" name="searchType" value="users" v-model="searchType"><label for="users">Users</label>
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
                noSearchTerm: false,
                errors: '',
                searchTerm: '',
                searchType: 'global',
                results: null
            };
        },
        methods: {
            async toSearch() {
                if(this.searchTerm){
                    try {
                        await api.getSearch(this.searchType, this.searchTerm).then(value => this.results = value)
                    }
                    catch(err) { console.error("err " + err) }
                    finally {
                        if(this.results["message"]){
                            console.log("pas bon")
                            this.results = null;
                            this.errors = "Album not found";
                            this.$emit('update', { searchTerm: this.searchTerm, searchType: this.searchType, results: this.results });
                        }
                        else{
                            this.$emit('update', { searchTerm: this.searchTerm, searchType: this.searchType, results: this.results });
                            console.log("results dans searchBar: " + JSON.stringify(this.results));
                            this.noSearchTerm = false;
                            this.errors = null;
                            console.log("bon")
                        }
                    }
                }
                else{
                    this.noSearchTerm = true;
                    this.results = null;
                }
            },
            changeType(picked) {
                this.searchType = picked
            },
            init(){
                this.searchTerm =  '';
                this.searchType = '';
                this.results = null;
                this.errors = null;
                this.noSearchTerm = false;
            },
        },
        updated() {
        },
        created(){
            this.init();
        },
    };
</script>

<style scoped>
    a:hover{
        color: white;
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
    .searchText{
        color: #d1d1d1;
    }
    .search-button {
        position:relative;
        align-self: end;
    }
    .typeButtons{
        padding-top: 20px;
    }
    .errorMessage{
        color: #d1d1d1;
        align-content: center;
        position: relative;
        padding-top: 20px;
        padding-bottom: 20px;
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
