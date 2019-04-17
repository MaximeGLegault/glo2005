<template>
    <li class="song">
        <div class="title">
            {{song.title}}
        </div>
        <div class="artist clickable" @click="albumArtistNameClicked(song.artist_id)">
            {{song.artist_name}}
        </div>
        <div class="album clickable" @click="albumTitleClicked(song.album_id)">
            {{song.album_name}}
        </div>
        <div class="genre">
            {{song.genre_name}}
        </div>
        <div class="duration">
            {{duration}}
        </div>
    </li>
</template>

<script>
    export default {
        name: "SongItem",
        props: {
            song: {
                required: true,
                type: Object,
            },
        },
        methods:{
            albumTitleClicked(album_id) {
                this.$router.push({path: `/album/${album_id}`})
            },
            albumArtistNameClicked(artist_id) {
                this.$router.push({path: `/artist/${artist_id}`})
            },

        },
        computed: {
            duration() {
                let minutes = Math.floor(this.song.duration  / 60);
                let seconds = this.song.duration - minutes * 60;

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

    .clickable {
        color: white;
        cursor: pointer;
    }

    .clickable:hover {
        color: #651fff;
    }

</style>
