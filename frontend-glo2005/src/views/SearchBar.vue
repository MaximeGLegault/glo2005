<template>
    <div class="searchBar">
        <div class="form">
            <input autocomplete="off" @keyup.enter.prevent="toSearch" v-model="search" id="search" type="text" placeholder="Search...">
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

    export default {
        name: 'SearchBar',
        data() {
            return {
                search: '',
                picked: 'global',
            };
        },
        methods: {
            toSearch() {
                this.$router.push({
                    name: 'search', query: {q: this.search, type: this.picked}
                });
            },
            created() {
                this.search = this.$route.query.q;
            },
            changeType(picked) {
                this.picked = picked
            }
        }
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
