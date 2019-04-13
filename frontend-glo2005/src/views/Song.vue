<template>
    <li class="song">
        <div class="title">
            {{Song.title}}
        </div>
        <div class="artist">
            {{Song.artist_name}}
        </div>
        <div class="album">
            {{Song.album_name}}
        </div>
        <div class="genre">
            {{Song.genre_name}}
        </div>
        <div class="duration">
            {{duration}}
        </div>
        <div class="year">
            {{Song.year}}
        </div>
    </li>
</template>

<script>
    export default {
        name: "SongItem",
        props: {
            Song: {
                required: true,
                type: Object,
            },
        },
        methods:{

        },
        computed: {
            duration() {
                let minutes = Math.floor(this.Song.duration  / 60);
                let seconds = this.Song.duration - minutes * 60;

                let minutes_string = minutes < 10 ? "0" + minutes.toString() : minutes.toString();
                let seconds_string = seconds < 10 ? "0" + seconds.toString() : seconds.toString();

                return minutes_string+":"+seconds_string;
            }
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
