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
            <b class ="errorMessage">{{this.prettySearchType}} not found</b>
        </div>
        <span class="typeButtons">
      <input @click="changeType('albums')" type="radio" class="radio" id="albums" name="searchType" value="albums" v-model="searchType" checked><label for="albums">Albums</label>
      <input @click="changeType('artists')" type="radio" class="radio" id="artists" name="searchType" value="artists" v-model="searchType"><label for="artists">Artists</label>
      <input @click="changeType('songs')" type="radio" class="radio" id="songs" name="searchType" value="songs" v-model="searchType"><label for="songs">Songs</label>
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
                            this.errors = "Result not found";
                            this.$emit('update', { searchTerm: this.searchTerm, searchType: this.searchType, results: this.results});
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
                    this.$emit('update', { searchTerm: this.searchTerm, searchType: this.searchType, results: this.results });
                    this.results = null;
                }
            },
            changeType(picked) {
                this.searchType = picked;
                this.init();
                if(picked === "albums"){
                    this.prettySearchType = "Album";
                }
                else if(picked === "artists"){
                    this.prettySearchType = "Artist";
                }
                else if(picked === "songs"){
                    this.prettySearchType = "Song";
                }
            },
            init(){
                this.searchTerm =  '';
                this.searchType = '';
                this.results = null;
                this.errors = null;
                this.noSearchTerm = false;
                this.prettySearchType = '';
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
