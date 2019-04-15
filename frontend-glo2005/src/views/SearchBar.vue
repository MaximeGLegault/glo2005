<template>
    <div class="searchBar">
        <div class="form">
            <input class="searchText" autocomplete="off" @keyup.enter.prevent="toSearch" v-model="searchTerm" id="search" type="text" placeholder="Search...">
            <button class="deep-purple accent-3 waves-effect waves-light btn"><a class="search-button" @click="toSearch">Search</a></button>
        </div>
        <div style="text-align:center" class="errorMessage" v-if="noSearchTerm">
            <b class ="errorMessage">Please correct the following error:</b>
                <p>{{ errors }}</p>
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
                try {
                    await api.getSearch(this.searchType, this.searchTerm).then((response) => {
                        if(response.status === 404){
                            this.errors = response.data["message"];
                            this.results = null;
                            this.$emit('error404', { results: this.results, error: this.error });
                            console.log("this.errors: " + this.errors);
                            console.log("error response message: " + response.data["message"]);
                            console.log("response.status === 404");
                            console.log("response.data : " + response.data);
                        }
                        else {
                            this.results = response;
                            this.errors = null;
                            console.log("response: " + response);
                        }
                    })
                }
                catch(err) { console.error("err.response.data: " + err.response.data) }
                finally
                {
                    if(!this.errors){
                        console.log("results: " + JSON.stringify(this.results));
                        this.$emit('update', { searchTerm: this.searchTerm, searchType: this.searchType, results: this.results });
                        if(this.searchTerm){
                            this.$router.push({ path: `/search/${this.searchType}/${this.searchTerm}` });
                            this.errors = null;
                        }
                        else {
                            this.$router.push({ path: `/Search/` });
                            this.noSearchTerm = true;
                        }
                    }
                    else{
                        this.$emit('update', { searchTerm: this.searchTerm, searchType: this.searchType, results: this.results });
                    }
                }

            },
            changeType(picked) {
                this.searchType = picked
            },
            init(){
                this.searchTerm =  '';
                this.searchType = '';
                this.results = null;
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
