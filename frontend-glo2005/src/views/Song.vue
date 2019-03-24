<template>
    <li class="song">
        <div class="title">
            {{title}}
        </div>
        <div class="artist">
            {{artist}}
        </div>
        <div class="album">
            {{album}}
        </div>
        <div class="genre">
            {{genre}}
        </div>
        <div class="duration">
            {{duration}}
        </div>
        <div class="year">
            {{year}}
        </div>
    </li>
</template>

<script>
    export default {
        name: "Song",
        props: {
            title: String,
            artist: String,
            album: String,
            genre: String,
            duration: Number,
            year: Number,
        },
        methods:{

        }
    };
</script>

<style scoped>

    .song {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        flex-wrap: wrap;
        align-items: flex-start;


    }

    .song > * {
        padding: 10px;
        flex-basis: 0;
        flex-grow: 1;
    }

    /*.title{*/
        /*flex-grow: 1;*/
    /*}*/

    /*.artist{*/
        /*flex-grow: 1;*/

    /*}*/

    /*.album{*/
        /*flex-grow: 1;*/

    /*}*/
    /*.genre{*/
        /*flex-grow: 1;*/

    /*}*/
    /*.duration{*/
        /*flex-grow: 1;*/

    /*}*/
    /*.year{*/
        /*flex-grow: 1;*/

    /*}*/

</style>
