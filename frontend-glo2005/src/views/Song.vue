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

    song {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;

    }
</style>
