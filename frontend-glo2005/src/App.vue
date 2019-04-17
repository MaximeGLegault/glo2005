<template>
    <div id="things">
        <Menubar/>
        <router-view/>
    </div>
</template>

<script>
    import Menubar from "./components/Menubar";

    export default {
        components: {
            'Menubar':
            Menubar
        },
    }
</script>

<style>
    body {
        background-color: #202020;
        padding: 0;
        margin: 0;
        color: lightgrey;
    }
</style>
