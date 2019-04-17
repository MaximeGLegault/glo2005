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

        <div class="year" v-if="year">
            {{year}}
        </div>
        <div class="like">
            <a class="clickable" title="favorite" v-if="liked === false" v-on:click="liked=!liked; like();">
                <i class="material-icons">favorite_border</i>
            </a>
            <a class="clickable" title="favorited" v-if="liked === true" v-on:click="liked=!liked; unlike()">
                <i class="material-icons">favorite</i>
            </a>

        </div>
        <div class="options">
            <vue-multiselect class="dropdown" v-model="playlists" :options="options" :multiple="true"
                             @input="addtoplaylist" @tag="newplaylist" :searchable="true" :show-labels="false"
                             :close-on-select="false" :clear-on-select="false" taggable="true" tag-position="top"
                             placeholder="Add to playlist"></vue-multiselect>
        </div>
        <div class="play">
            <a class="clickable" title="play" v-if="playing === false" v-on:click="playing=!playing; play();">
                <i class="material-icons">play_circle_outline</i>
            </a>
            <a class="clickable" title="playing" v-if="playing === true" v-on:click="playing=!playing; stop();">
                <i class="material-icons">play_circle_outline</i>
            </a>
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
            year: Number,
            options: Array,
            playlist_objects: Array,
        },

        data: () => ({
            liked: false,
            playing: false,
            lastemittor: false,
            playlists: [],
            playlistsadded: [],
        }),
        methods: {

            addtoplaylist() {
                var playliststoadd = this.find_playlists_to_add();
                for (var k = 0; k < playliststoadd.length; k++) {
                    var id = this.find_id_from_title(playliststoadd[k]);
                    api.addSongToPlaylist(this.song.song_id, id);
                    this.playlistsadded.push(playliststoadd[k]);
                }


            },
            async newplaylist(newPlaylist) {
                this.playlists.push(newPlaylist);
                this.options.push(newPlaylist);

                await api.addPlaylist(newPlaylist).then(value => {
                    var playlist_id = value.playlist_id;
                    api.addSongToPlaylist(this.song.song_id, playlist_id);
                    this.playlistsadded.push(newPlaylist);
                    this.playlist_objects.push({
                        playlist_id: playlist_id,
                        title: newPlaylist
                    })
                });


            },
            like() {
                api.like(this.song.song_id);
            },
            unlike() {
                api.unlike(this.song.song_id);
            },
            play() {
                api.add_to_history(this.song.song_id);
                this.lastemittor = true;
                this.$root.$emit('play');
            },
            stop() {
                this.$root.$emit('stop');
            },

            find_playlists_to_add() {
                var playliststoadd = [];
                for (var i = 0; i < this.playlists.length; i++) {
                    var found = false;
                    for (var j = 0; j < this.playlistsadded; j++) {
                        if (this.playlists[i] == this.playlistsadded[j]) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        playliststoadd.push(this.playlists[i]);
                    }
                }
                return playliststoadd;
            },

            find_id_from_title(playlist) {
                for (var i = 0; i < this.playlist_objects.length; i++) {
                    if (this.playlist_objects[i].title == playlist) {
                        return this.playlist_objects[i].playlist_id;
                    }
                }
                return null;
            },


            albumTitleClicked(album_id) {
                this.$router.push({path: `/album/${album_id}`})
            },
            albumArtistNameClicked(artist_id) {
                this.$router.push({path: `/artist/${artist_id}`})
            },

        },
        computed: {
            duration() {
                let minutes = Math.floor(this.song.duration / 60);
                let seconds = this.song.duration - minutes * 60;

                let minutes_string = minutes < 10 ? "0" + minutes.toString() : minutes.toString();
                let seconds_string = seconds < 10 ? "0" + seconds.toString() : seconds.toString();

                return minutes_string + ":" + seconds_string;
            },
        },
        mounted() {
            this.$nextTick(() => {
                this.$root.$on('play', () => {
                    if (this.playing && !this.lastemittor) {
                        this.playing = false;

                    }
                    this.lastemittor = false;
                });
                this.$root.$on('stop', () => {
                    this.playing = false;
                });
            });
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

    .play {

        padding: 10px;
        flex-basis: 20px;
        flex-grow: 0.1;
    }

    .play > img {
        height: 20px;
        width: 20px;
    }

    .clickable {
        color: white;
        cursor: pointer;
    }

    .clickable:hover {
        color: #651fff;

    }

</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
