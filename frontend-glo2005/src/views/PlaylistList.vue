<template>
    <div>
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
                <a class="btnPlaylistlist" title="Delete playlist" @click="deletePlaylist(playlist.playlist_id)">
                    <i class="material-icons">delete</i>
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "PlaylistList",
        props: {
            playlists: Array
        },
        methods: {
            deletePlaylist(playlist_id) {
                this.$emit("deletePlaylist", playlist_id)
            }
        }
    }
</script>

<style scoped>
    .btnPlaylistlist {
        color: white;
        cursor: pointer;
    }

    .btnPlaylistlist:hover {
        color: #651fff;
    }

</style>
