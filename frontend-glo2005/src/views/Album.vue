<template>
    <playlist v-if="this.album" v-bind:songs="album.songs" v-bind:title="album.title" v-bind:year="album.year"/>
</template>

<script>
    import Playlist from './Playlist';
    import api from "../lib/api";


    export default {
        name: "Album",
        components: {
            Playlist
        },
        data: () => ({

            album: null
        }),



        async created() {
            let album_id = this.$route.params.album_id ? this.$route.params.album_id : 10000000;
            await api.getAlbum(album_id).then(value => {
                this.album = value;
            });
        }
    }


</script>

<style scoped>

</style>

<!--Hard coded album-->
<!--{album_id: 1,
                title: 'If Purpose Each',
                songs: [{
                    song_id: 1,
                    artist_name: "Participant Development",
                    genre_name: "Grunge",
                    title: "Reality Live Full Arm",
                    duration: 197,
                    album_name: "If Purpose Each",
                    year: 2016
                },
                    {
                        song_id: 1,
                        artist_name: "Participant Development",
                        genre_name: "Grunge",
                        title: "Half Study Sex Determine Door",
                        duration: 197,
                        album_name: "If Purpose Each",
                        year: 2016
                    },
                    {
                        song_id: 2,
                        artist_name: "Participant Development",
                        genre_name: "Grunge",
                        title: "Color Cancer",
                        duration: 197,
                        album_name: "If Purpose Each",
                        year: 2016
                    },
                    {
                        song_id: 3,
                        artist_name: "Participant Development",
                        genre_name: "Grunge",
                        title: "Single Exactly Almost Official",
                        duration: 197,
                        album_name: "If Purpose Each",
                        year: 2016
                    },
                    {
                        song_id: 4,
                        artist_name: "Participant Development",
                        genre_name: "Grunge",
                        title: "Question Nothing Task Must Different View Score",
                        duration: 197,
                        album_name: "If Purpose Each",
                        year: 2016
                    },
                    {
                        song_id: 5,
                        artist_name: "Participant Development",
                        genre_name: "Grunge",
                        title: "Again Later Then",
                        duration: 197,
                        album_name: "If Purpose Each",
                        year: 2016
                    },
                ]
            }-->