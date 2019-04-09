<template>
    <nav>
        <div id="allthings">
            <div id="logoDiv">
                <router-link to="/"><span id="logo">UBeat</span></router-link>
            </div>
            <div>
                <span class="button">Home</span>
            </div>
            <div>
                <span class="button">Artist</span>
            </div>
            <div>
                <span class="button">Album</span>
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
        font-family: 'Black Ops One', cursive;
        color: #fff;
        font-weight: normal;
        margin-left: 30px;
        margin-right: 30px;
    }

    #logo {
        font-family: 'Black Ops One', cursive;
        color: #fff;
        font-size: 44px;
        font-weight: normal;
        display: inline-block;
        height: 100%;
        margin-top: 4px;
    }

    .button {
        font-size: 36px;
        height: 100%;
        margin-top: 6px;
        display: inline-block;
    }
</style>
