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
                    v-on:click="showCreationplaylistSection">
                <i id="clickButtonId" class="material-icons">add</i>
            </button>

            <div id="newPlaylist" v-if="showPlaylistCreationSection">
                <div class="input-field col s6">
                    <label for="pl_name"></label><input id="pl_name" type="text" v-model="inputNameEdit"
                                                        placeholder="Playlist's Name">
                </div>

                <a class="btnCreatePlaylist" title="Create new Playlist" @click="addNewPlaylist">
                    <i class="material-icons">done</i>
                </a>
                <a class="btnCreatePlaylist" title="Cancel creating new Playlist" @click="cancelCreatingPlaylist">
                    <i class="material-icons">cancel</i>
                </a>
            </div>
            <a >{{ messageLog }}</a>

            <playlist-list v-if="this.playlists" :playlists="this.playlists"
                           v-on:changeTitle="editTitlePlaylist($event)"
                           v-on:deletePlaylist="deletePlaylist($event)"/>
        </div>
    </div>
</template>

<script>
    import api from "../lib/api";
    import PlaylistList from "./PlaylistList";
    // import { mapMutations } from 'vuex'

    export default {
        name: "Profile",
        components: {PlaylistList},
        data: () => ({
            playlists: [],
            currentlySelectedPlaylist: {},
            showPlaylistCreationSection: false,
            showEditButton: false,
            inputNameEdit: '',
            messageLog: "",

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
            async deletePlaylist(playlistId) {
                await api.deletePlaylist(playlistId)
                    .then(() => this.playlists = this.playlists.filter((value,) => {
                        return value.playlist_id !== playlistId
                    }));
            },
            async addNewPlaylist() {
                if (!this.inputNameEdit) {
                    this.messageLog = "Please put a name!"
                } else {
                    await api.addPlaylist(this.inputNameEdit)
                        .then(value => {
                            this.playlists.push({playlist_id: value.playlist_id, title: this.inputNameEdit});
                            this.inputNameEdit = "";
                            this.messageLog = "";
                            this.showPlaylistCreationSection = false;
                        });
                }
            },
            showCreationplaylistSection() {
                this.showPlaylistCreationSection = true;
            },
            cancelCreatingPlaylist() {
                this.showPlaylistCreationSection = false;
                this.messageLog = ""
            },
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

    #newPlaylist {
        display: flex;
        justify-content: center;
        margin: 0;
    }

    .input-field {
        margin: 0;
    }

    .btnCreatePlaylist {
        color: white;
        cursor: pointer;
    }

    .btnCreatePlaylist:hover {
        color: #651fff;
    }

</style>
