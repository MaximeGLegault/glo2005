<template>
    <div id="master">
        Welcome to our site!
    </div>
</template>

<script>
    import Cookies from 'js-cookie'

    export default {
        name: "Profile",
        beforeMount() {
            if (Cookies.get('token') === undefined) {
                this.$router.push('/login');
            }
        }
    }
</script>

<style scoped>
    #master{
        text-align: center;
        font-size: 4em;
        color: #fff;
    }
</style>
