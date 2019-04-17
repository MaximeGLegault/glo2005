<template>
    <div>
        <h1>Songs</h1>
        <div class="loadingSymbolPadding">
            <div class="loading" v-if="loading"></div>
        </div>
        <table class="list">
            <tr class="header">
                <th>Title</th>
                <th>Artist</th>
                <th>Album</th>
                <th>Duration</th>
            </tr>
            <tr v-for="song in songs" :key="song.song_id">
                <song-item v-model="songs" :song="song"/>
            </tr>
        </table>
    </div>
</template>


<script>
    import api from "../lib/api";
    import SongItem from "./Song";

    export default {
        name: "allSongs",
        components: {SongItem},
        data() {
            return {
                loading: false,
                songs: [
                    {song_id: 0},
                    {title: ''},
                    {artist_name: ''},
                    {album_name: ''},
                    {duration: 0},

                ]
            };
        },
        methods: {
            artistNameClicked(artist_id) {
                this.$router.push({path: `/artist/${artist_id}`})
            },
            albumNameClicked(album_id) {
                this.$router.push({path: `/album/${album_id}`})
            },
            async init() {
                this.songs = [];
                this.songs.song_id = 0;
                this.songs.title = '';
                this.songs.artist_name = '';
                this.songs.album_name = '';
                this.songs.duration = 0;
                await api.getAllSongs().then(value => this.songs = value).catch(value => console.log(value));
                console.log(this.songs);
                this.loading = false;
            }
        },
        created() {
            this.loading = true;
            this.init();
        },
        updated() {
        },
    };


</script>

<style scoped>
    h1 {
        text-align: center;
        font-size: 2em;
    }

    .loading {
        margin-left: auto;
        margin-right: auto;
        border: 16px solid #f3f3f3; /* Light grey */
        border-top: 16px solid #3498db; /* Blue */
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 2s linear infinite;
    }

    @keyframes spin {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }

    .loadingSymbolPadding {
        padding-bottom: 27px;
    }

    .list {
        margin-left: auto;
        margin-right: auto;
        margin-top: auto;
        border: 5px solid #4f4f4f;
        border-radius: 8px;
        padding: 40px;
        width: 90%;
        background-image: linear-gradient(#404040, #202020);
        display: flex;
        flex-direction: column;
    }

    .list > * {
        border-bottom: 1px solid white;

    }

    .header {
        font-size: 30px;
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        flex-wrap: wrap;
        align-items: flex-start;
    }

    .header > * {
        padding: 10px;
        flex-basis: 0;
        flex-grow: 1;
    }

    .tableItem > * {
        padding: 10px;
        flex-basis: 0;
        flex-grow: 1;
    }

</style>
