<template>
    <div id="contentLogin">
        <h1>Login</h1>
        <p class="center">You have no account?
            <router-link to="/signUp">Sign up</router-link>
            now!
        </p>
        <div id="inputDiv">
            <div class="input-field col s6">
                <input id="userUsername" type="text" v-model="user_username">
                <label for="userUsername">Username</label>
            </div>
            <div class="input-field col s6">
                <input id="userPass" type="password" v-model="user_password">
                <label for="userPass">Password</label>
            </div>
            <button id="btnLogin" v-on:click="login" class="deep-purple accent-3 waves-effect waves-light btn">Login
            </button>
            <p class="errorMessage">{{messageErr}}</p>
            <p class="loginMessage">{{messageLog}}</p>
        </div>
    </div>
</template>


<script>
    import api from '@/lib/api';
    import Cookies from 'js-cookie'

    export default {
        name: 'Login',

        data: () => ({
            user_username: '',
            user_password: '',
            messageErr: '',
            messageLog: ''
        }),

        methods: {
            async login() {
                await api.loginUser(this.user_username, this.user_password)
                    .then((value) => {
                        this.$store.state.user = {name: value.username};
                        this.messageErr = '';
                        this.messageLog = 'You\'re now log in';
                        Cookies.set('token', value.token);
                        window.location = '/Profile';
                    }).catch(() => {
                        this.messageErr = 'user not found, check your username and password';
                        this.messageLog = '';
                        this.$store.state.user = '';
                    });
            }
        }
    }
</script>

<!--<script>-->
<!--// import util from '@/lib/util';-->
<!--// import {mapActions} from 'vuex';-->
<!--// import api from '@/lib/api';-->


<!--// export default {-->
<!--// data: () => ({-->
<!--//     user_email: '',-->
<!--//     user_password: '',-->
<!--//     messageErr: '',-->
<!--//     messageLog: ''-->
<!--// }),-->
// methods: {
//     ...mapActions([]),
//     async login() {
//         await api.loginUser(this.user_email, this.user_password)
//             .then((value) => {
//                 this.$store.state.user = value.data.name;
//                 this.messageErr = '';
//                 this.messageLog = 'You\'re now log in';
//                 Cookies.set('token', value.data.token);
//                 window.location = '/';
//             }).catch(() => {
//                 this.messageErr = 'user not found, check your username and password';
//                 this.messageLog = '';
//                 this.$store.state.user = '';
//             });
<!--//     }-->
<!--// }-->
<!--// };-->
<!--</script>-->

<style scoped>
    #contentLogin {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    h1 {
        align-self: center;
    }

    #inputDiv {
        width: 40%;
        align-self: center;
    }

    .btn:focus, .btn:hover {
        color: white;
    }

    .errorMessage {
        margin-top: 25px;
        color: red;
        font-size: 1em;
    }

    .loginMessage {
        margin-top: 25px;
        color: greenyellow;
        font-size: 1em;
    }

    .center {
        align-self: center;
    }

    a {
        color: #651fff;
        font-size: 1.2em;
    }

    @media only screen and (min-device-width: 320px) and (max-device-width: 480px)
    and (orientation: portrait) {
        h1 {
            margin-top: 100px;
        }

        p {
            font-size: 2.5em;
        }

        input[type=text]:not(.browser-default) {
            font-size: 2em;
            height: 4rem;
        }

        .input-field label {
            font-size: 2em;
        }

        input[type=password]:not(.browser-default) {
            font-size: 2em;
            height: 4rem;
        }

        #btnLogin {
            font-size: 2em;
        }

        .btn {
            height: 50px;
            margin-top: 20px;
        }

        .input-field label:not(.label-icon).active {
            transform: translateY(-25px) scale(0.8);
        }
    }
</style>
