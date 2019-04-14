<template>
    <li class="title">
        <div class="title">
            {{title}}
        </div>
        <div class="year">
            {{year}}
        </div>
        <div class="artist">
            {{artist}}
        </div>
        <div class="genre">
            {{genre}}
        </div>
    </li>
</template>

<script>
    export default {
        name: "SearchResultAlbum",
        props: {
            title: String,
            year: Number,
            artist: String,
            genre: String,
        },
        methods:{

        },
        data() {
            return {
                searchTerm: '',
                picked: 'global',
                results: null
            };
        },
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
