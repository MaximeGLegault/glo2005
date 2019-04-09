<template>
    <nav>
        <div id="logoDiv">
            <span id="logo">UBeat</span>
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
        display: flex;
        flex-direction: row;

    }

    #logo {
        font-family: 'Black Ops One', cursive;
        color: #fff;
        margin-left: 2px;
        font-size: 44px;
        font-weight: normal;
    }
</style>
