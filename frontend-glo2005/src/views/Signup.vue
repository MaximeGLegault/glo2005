<template>
    <div id = "contentSignUp">
        <h1>Sign Up</h1>
        <div id="inputDiv">
            <div class="input-field col s6">
                <input id="userName" type="text" v-model="user_name">
                <label for="userName">Username</label>
            </div>
            <div class="input-field col s6">
                <input id="userEmail" type="text" v-model="user_email">
                <label for="userEmail">Email</label>
            </div>
            <div class="input-field col s6">
                <input id="userPass" type="password" v-model="user_password">
                <label for="userPass">Password</label>
            </div>
            <button id="btnLogin" v-on:click="signup" class="deep-purple accent-3 waves-effect waves-light btn">Sign Up</button>
            <p class="errorMessage">{{messageErr}}</p>
            <p class="loginMessage">{{messageLog}}</p>
        </div>
    </div>
</template>

<script>
    import api from '../lib/api';
    import Cookies from "js-cookie";

    export default {
        data: () => ({
            user_name: '',
            user_email: '',
            user_password: '',
            messageErr: '',
            messageLog: ''
        }),
        methods: {
            async signup() {
                await api.signUp(this.user_name, this.user_email, this.user_password)
                    .then(value => {
                        this.$store.state.user = {name: value.username};
                        Cookies.set('token', value.token);
                        this.messageErr = '';
                        this.messageLog = 'You\'re now registered!';
                        this.$router.push('/Profile');
                    }).catch((error) => {
                        if (error.response.status === 400) {
                            this.messageErr = error.response.data.message;
                        } else {
                            this.messageErr = 'This user already exists';
                        }
                        this.messageLog = '';
                    });
            }
        }
    };
</script>

<style scoped>
    #contentSignUp{
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    h1{
        align-self: center;
    }
    #userName{
        width: 97%;
    }

    #inputDiv{
        width: 40%;
        align-self: center;
    }
    .btn:focus, .btn:hover{
        color: white;
    }
    .errorMessage{
        margin-top: 25px;
        color: red;
        font-size: 1em;
    }
    .loginMessage{
        margin-top: 25px;
        color: greenyellow;
        font-size: 1em;
    }
    @media only screen and (min-device-width : 320px) and (max-device-width : 480px)
    and (orientation: portrait){
        h1{
            margin-top: 100px;
        }
        p{
            font-size: 2.5em;
        }
        input[type=text]:not(.browser-default){
            font-size: 2em;
            height: 4rem;
        }
        .input-field label{
            font-size: 2em;
        }
        input[type=password]:not(.browser-default){
            font-size: 2em;
            height: 4rem;

        }
        #btnLogin{
            font-size: 2em;
        }
        .btn{
            height: 50px;
            margin-top: 20px;
        }
        .input-field label:not(.label-icon).active{
            transform: translateY(-25px) scale(0.8);
        }
    }
</style>
