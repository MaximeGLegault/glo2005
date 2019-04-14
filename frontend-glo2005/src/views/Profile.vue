<template>
    <div id="master">
        Welcome to our site, {{this.$store.state.user.username}}!
        <div id="playlistName">
            <ul>
                <li>
                    <a class="listPlName" v-on:click="$emit('clickedCurrentlyPlaying')">Currently playing</a>
                </li>
            </ul>
            <hr/>
            <button id="addbutton"
                    class="btn-floating waves-effect waves-light deep-purple accent-3"
                    v-on:click="addNewPlaylist">
                <i id="clickButtonId" class="material-icons">add</i>
            </button>
            <ul id="ulOfPlaylist" v-for="playlist in this.playlists" v-bind:key="playlist.playlist_id">
                <li>
                    <router-link class="listPlName"
                                 :to="{name: 'playlist', params: {playlistId: playlist.playlist_id}}">
                        <a
                                v-bind:id="playlist.id"
                                v-on:click="$emit('changePlaylist', playlist.id)">
                            {{playlist.title}}
                        </a>
                    </router-link>
                    <a id="deleteBtn" title="Delete playlist" @click="deletePlaylist"><i class="material-icons">delete</i></a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import api from "../lib/api";
    // import { mapMutations } from 'vuex'

    export default {
        name: "Profile",
        data: () => ({
            playlists: []
        }),
        async beforeMount() {
            await api.getTokenInfo()
                .then(value => {
                    this.$store.commit('saveUsername', value.username)
                })
                .catch(value => {
                    console.log(value);
                    this.$router.push('/Login');
                });
            await api.getProfile().then(value => this.playlists = value)
        },
        computed: {
            username() {
                return this.$store.state.user.username
            },
        },
        methods: {
            deletePlaylist(playlistId) {
                api.deletePlaylist(playlistId)
                    .then()
            }
        }
    }
</script>

<style scoped>
    #master {
        text-align: center;
        font-size: 2em;
    }

    ul {
        margin-bottom: 0;
    }

    #playlistName {
        border-right: solid 5px #111;
        padding: 10px 10px;
        width: 100%;
        min-width: 150px;
        min-height: 100vh;
        background-color: #191919;
        font-size: 1.5em;
    }

    .listPlName {
        color: white;
        cursor: pointer;
    }

    .listPlName:hover {
        color: #651fff;
    }

    #addbutton {
        display: inline;
        margin-bottom: 5px;
    }

    #deleteBtn {
        color: white;
        cursor: pointer;
    }

    #deleteBtn:hover {
        color: #651fff;
    }

    @media only screen and (min-device-width: 320px) and (max-device-width: 480px)
    and (orientation: portrait) {
        #playlistName {
            font-size: 2em;
        }

        #playlistName ul {
            padding-left: 0;
        }

        #addbuttonSm i {
            font-size: 3em;

        }

        #addbutton {
            display: none;
        }
    }

    @media screen and (max-width: 798px) {
        #playlistName ul {
            padding-left: 5px;
        }

        #addbutton {
            margin-bottom: 10px;
        }
    }

</style>
