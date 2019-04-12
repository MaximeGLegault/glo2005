<template>
    <nav>
        <div id="allthings">
            <div id="logoDiv">
                <router-link to="/"><span id="logo">GLO2005</span></router-link>
            </div>
            <div>
                <router-link to="/"><span class="button">Home</span></router-link>
            </div>
            <div>
                <router-link to="/Artists"><span class="button">Artists</span></router-link>
            </div>
            <div>
                <router-link to="/Album"><span class="button">Albums</span></router-link>
            </div>
            <div id="menuSearch" class="menuSmSearch">
                <div class="form">
                    <label for="search"></label><input v-on:keyup.enter.prevent="goSearch" v-model="searchTerm"
                                                       id="search" type="text" placeholder="Search...">
                    <a id="searchBtn" @click="goSearch"><i class="material-icons">search</i></a>
                </div>
            </div>
            <div>
                <router-link to="/Profile"><span class="button">Profile</span></router-link>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: "Menubar"
    }
</script>

<style scoped>
    nav {
        height: 60px;
        background-color: black;
    }

    #allthings {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        justify-content: space-between;
        align-items: stretch;
        align-content: stretch;
        height: 100%;
        text-align: center;
        color: #fff;
        font-weight: normal;
        margin-left: 30px;
        margin-right: 30px;
    }

    #allthings:hover {
        color: #651fff;
        cursor: pointer;
    }

    #logo {
        color: #fff;
        font-size: 44px;
        font-weight: normal;
        display: inline-block;
        height: 100%;
        margin-top: 4px;
    }

    #menuSearch {
        display: flex;
        flex-direction: row;
        height: 100%;
        align-items: center;

    }

    #menuSearch input {
        height: auto;
        margin: 0 4px 0 0;
    }

    .menuSmSearch .form {
        display: flex;
    }

    .menuSmSearch .form input:focus {
        border-bottom: 1px solid #fff;
        -webkit-box-shadow: 0 1px 0 0 #fff;
        -moz-box-shadow: 0 1px 0 0 #fff;
        box-shadow: 0 1px 0 0 #fff;
    }

    .button {
        font-size: 36px;
        height: 100%;
        margin-top: 6px;
        display: inline-block;
    }

    .button:hover {
        color: #651fff;
    }
</style>
