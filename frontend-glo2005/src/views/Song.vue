<template>
    <li class="song">
        <div class="title">
            {{song.title}}
        </div>
        <div class="artist">
            {{song.artist_name}}
        </div>
        <div class="album">
            {{song.album_name}}
        </div>
        <div class="genre">
            {{song.genre_name}}
        </div>
        <div class="duration">
            {{duration}}
        </div>
        <div class="year">
            {{song.year}}
        </div>
        <div class="like">
            <img src="../assets/empty_heart.png" v-if="liked == false" v-on:click="liked=!liked; like();">
            <img src="../assets/full_heart.png" v-if="liked == true" v-on:click="liked=!liked; unlike()">
            <!--image-->
        </div>
        <div class="options">
            <vue-multiselect class="dropdown" v-model="playlists" :options="options" :multiple="true" @input="addtoplaylist" @tag="newplaylist" :searchable="true" :show-labels="false" :close-on-select="false" :clear-on-select="false" taggable="true" tag-position="top" placeholder="Add to playlist"></vue-multiselect>
        </div>
    </li>
</template>

<script>
    import Multiselect from 'vue-multiselect';
    import api from "../lib/api";

    export default {
        name: "SongItem",
        components: {
            'vue-multiselect': Multiselect,
        },
        props: {
            song: {
                required: true,
                type: Object,
            },
        },
        data: () => ({
            liked: false,
            options: ['Test', 'test2','test3','Playlist testing different words','test5','test6',],
            playlists: [],
            playlistsadded: [],

        }),
        methods:{
            addtoplaylist() {
                //Verify if this.playlists has elements that are not in this.playlistsadded.
                //If yes, then send request to api to add song
                // api.addSongToPlaylist(,this.song.song_id);
            },
            newplaylist(newPlaylist){
                debugger;
                this.playlists.push(newPlaylist);
                this.options.push(newPlaylist);
                //Create the playlist with api call
                // api.createplaylist(,[this.song.song_id]);

            },
            like(){
                api.like(this.song.song_id);
            },
            unlike(){
                api.unlike(this.song.song_id);
            }

        },
        computed: {
            duration() {
                let minutes = Math.floor(this.song.duration  / 60);
                let seconds = this.song.duration - minutes * 60;

                let minutes_string = minutes < 10 ? "0" + minutes.toString() : minutes.toString();
                let seconds_string = seconds < 10 ? "0" + seconds.toString() : seconds.toString();

                return minutes_string+":"+seconds_string;
            },
        },
        async created() {
            await api.getUserPlaylists().then(value => {
                this.options = value;
            });
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

    .like {

        padding: 10px;
        flex-basis: 20px;
        flex-grow: 0.1;
    }

    .like > img {
        height: 20px;
        width: 20px;
    }

    .options {
        padding: 10px;
        flex-basis: 175px;
        flex-grow: 0.1;
    }

</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
