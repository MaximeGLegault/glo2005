<template>
    <div id="player_section">

        <img id="thumbnail"
             :src="this.currentlyPlayingTrack.artworkUrl100"/>


        <controller ref="progressController"
                    :audioCurrentTime="audioCurrentTime"
                    :audioDuration="audioDuration"/>


        <div id="controls">

            <div id="text_info">
                <a style="padding-left: 100px">{{songName}}</a>
                <a style="padding-left: 100px">{{artistName}}</a>
            </div>

            <div id="currentTimeLabel">{{ currentTimeLength }}</div>

            <div id="buttons">
                <div id="left_buttons">
                    <a class=" btn deep-purple accent-3 btn-floating"
                       v-on:click="playPreviousTrack">
                        <i class="material-icons md-48">skip_previous</i>
                    </a>
                </div>
                <div id="middle_button">

                    <a class=" btn deep-purple accent-3 btn-floating"
                       v-on:click="playPressed"
                       v-if="!isPlaying">
                        <i style="font-size: 40px" class="material-icons md-48">play_arrow</i>
                    </a>

                    <a class=" btn deep-purple accent-3 btn-floating"
                       v-on:click="playPressed"
                       v-if="this.isPlaying">
                        <i style="font-size: 40px" class="material-icons md-48">pause</i>
                    </a>
                </div>
                <div id="right_buttons">
                    <a class=" btn deep-purple accent-3 btn-floating"
                       v-on:click="playNextTrack">
                        <i class="material-icons md-48">skip_next</i>
                    </a>
                </div>
            </div>

            <div id="totalTimeLabel">{{ durationLength }}</div>

            <div id="playlist_button"></div>

        </div>

        <audio ref="audio"></audio>

    </div>
</template>

<script>
    import {mapActions} from 'vuex';
    import util from '@/lib/util';
    import Controller from './Player-Controller';


    export default {
        name: 'player',
        components: {
            Controller
        },
        data: () => ({
            audioDuration: 0,
            audioCurrentTime: 0,
            isPlaying: false,
            indexOfPlayingTrack: 0,
            currentlyPlayingTrack: {}
        }),
        computed: {
            audio() {
                return this.$refs.audio;
            },
            playlist() {
                return this.$store.state.currentlyPlayingPlaylist.tracks;
            },
            track() {
                return this.$store.state.currentlyPlayingTrack;
            },
            durationLength() {
                return util.getLength(this.audioDuration, 'seconds');
            },
            currentTimeLength() {
                return util.getLength(this.audioCurrentTime, 'seconds');
            },
            songName() {
                return this.track.trackName;
            },
            artistName() {
                return this.track.artistName;
            }
        },
        methods: {
            ...mapActions([
                'addTrackAsCurrentlyPlayingTrack'
            ]),
            newPlayRequested() {
                if (this.track.previewUrl) {
                    this.audio.pause();
                    this.indexOfPlayingTrack = this.playlist.findIndex(
                        el => el.trackId === this.track.trackId);
                    this.currentlyPlayingTrack = this.track;
                    this.audio.src = this.track.previewUrl;
                    this.audio.play();
                    this.isPlaying = true;
                }
            },
            playPressed() {
                if (this.isPlaying) {
                    this.audio.pause();
                    this.isPlaying = false;
                } else if (this.track.previewUrl) {
                    this.audio.play();
                    this.isPlaying = true;
                } else {
                    this.newPlayRequested();
                }
            },
            onDurationChange() {
                if (this.audio.duration !== 1) {
                    this.audioDuration = this.audio.duration;
                }
            },
            onTimeUpdate() {
                this.audioCurrentTime = this.audio.currentTime;
            },
            playNextTrack() {
                if (this.indexOfPlayingTrack >= (this.playlist.length - 1)) {
                    this.indexOfPlayingTrack = 0;
                } else {
                    this.indexOfPlayingTrack += 1;
                }
                this.addTrackAsCurrentlyPlayingTrack(this.playlist[this.indexOfPlayingTrack]);
                this.newPlayRequested();
            },
            playPreviousTrack() {
                if (this.indexOfPlayingTrack === 0) {
                    this.indexOfPlayingTrack = this.playlist.length - 1;
                } else {
                    this.indexOfPlayingTrack -= 1;
                }
                this.addTrackAsCurrentlyPlayingTrack(this.playlist[this.indexOfPlayingTrack]);
                this.newPlayRequested();
            },
            onEnded() {
                this.playNextTrack();
            },
            initAudio() {
                this.audio.addEventListener('durationchange', this.onDurationChange);
                this.audio.addEventListener('timeupdate', this.onTimeUpdate);
                this.audio.addEventListener('ended', this.onEnded);
            }
        },
        mounted() {
            this.initAudio();
            this.$root.$on('newPlayRequested', this.newPlayRequested);
        },
    };
</script>

<style scoped>
    #player_section {
        background-color: #1e1e1e;
        position: fixed;
        width: 100%;
        height: 100px;
        bottom: 0;
        left: 0;
        display: flex;
        flex-flow: column nowrap;
    }

    #thumbnail {
        position: fixed;
        bottom: 0;
        left: 0;
    }

    #controls {
        display: flex;
        flex-flow: row nowrap;
        height: 100%;
    }

    #buttons {
        flex: 2;
        height: auto;
        align-items: center;
        justify-content: center;
    }

    #currentTimeLabel {
        flex-basis: content;
    }

    #playlist_button {
        flex: 1;
    }

    #text_info {
        margin-left: 10px;
        flex: 1;
        display: flex;
        flex-flow: column nowrap;
    }

    #buttons {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    #totalTimeLabel {
        flex-basis: content;
    }


</style>
