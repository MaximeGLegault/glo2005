<template>
    <div id="app">
        <div id="nav">
            <router-link to="/">Home</router-link>
            |
            <router-link to="/about">About</router-link>
            |
            <router-link to="/login">Login</router-link>
        </div>
        <router-view/>
    </div>
</template>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #828179;
    }

    #nav {
        padding: 30px;
    }

    #nav a {
        font-weight: bold;
        color: #828179;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    }

    body {
        background-color: #202020;
        color: #fff;
        padding: 0;
        margin: 0;
    }

    .main {
        margin-top: 60px;
        margin-bottom: 100px;
    }
</style>
