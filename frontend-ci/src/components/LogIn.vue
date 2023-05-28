<template>
    <div class="logIn_user">
        <div class="container_logIn_user">
            <h2>Login</h2>
            <form v-on:submit.prevent="processLogInUser">
                <input id="input" type="text" v-model="user.nickName" placeholder="Username">
                <br>
                <input id="input" type="password" v-model="user.password" placeholder="Password">
                <br>
                <button id="button" type="submit">Iniciar Sesion</button>
            </form>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: "LogIn",
    data: function () {
        return {
            user: {
                nickName: "",
                password: ""
            }
        }
    },
    methods: {
        processLogInUser: function () {
            axios.post(
                "http://127.0.0.1:8000/administrador/iniciarsesion",{
                    nickName: this.user.nickName,
                    password: this.user.password
                })
                .then((result) => {
                    let resultado = JSON.parse(result.data);
                    console.log(resultado.message);
                   if (resultado.message == "datos validados") {
                    let dataLogin = {
                        nickName: this.user.nickName,
                    }
                    this.$emit('completedLogIn', dataLogin);
                   }
                })
                .catch((error) => {
                    if (error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                });
        }
    }
}
</script>
<style>
.logIn_user {
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container_logIn_user {
    border: 3px solid #283747;
    border-radius: 10px;
    width: 25%;
    height: 60%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #0275b3;
}

.logIn_user h2 {
    color: #ffffff;
    font-family: Arial, Helvetica, sans-serif;
}

.logIn_user form {
    width: 70%;
}

#input {
    background-color: #ffffff;
}

#button {
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
    font-weight: bold;
}

.logIn_user input {
    height: 40px;
    width: 100%;
    box-sizing: border-box;
    background-color: #a6d9fba9;
    color: rgb(0, 0, 0);
    padding: 10px 20px;
    margin: 5px 0;
    border: 1px solid #283747;
    border-radius: 30px;
}

.logIn_user button {
    width: 100%;
    height: 40px;
    color: #ffffff;
    background: #39c1eed0;
    border: 1px solid #9abada;
    border-radius: 30px;
    padding: 10px 25px;
    margin: 5px 0;
}

.logIn_user button:hover {
    color: #565fd6;
    background: #E5E7E9;
    border: 1px solid #283747;
}
</style>