<template>
  <div id="app" class="app">
    <div class="header">
      <h1>LOGIN INVENTARIO G4</h1>
      <nav>
        <button v-if="!is_auth" v-on:click="loadLogIn"> Iniciar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadSignUp"> Registrarse </button>
        <button v-if="!is_auth" v-on:click="loadForgotPass"> Recordar Contraseña</button>
        <button v-if="is_auth" v-on:click="loadHome"> Inicio </button>
        <button v-if="is_auth" v-on:click="logOut"> Cerrar Sesión </button>
       
      </nav>
    </div>

    <div class="main-component">
      <router-view v-on:completedLogIn="completedLogIn" 
      v-on:completedSignUp="completedSignUp"
      v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <div class="footer">
      <h2>Ciclo 3 </h2>
    </div>
  </div>
</template>
<script>
export default
  {
    name: 'App',
    data: function () {
      return {
        is_auth: false
      }
    },
    components: {
    },
    methods: {
      verifyAuth: function () {
        this.is_auth = localStorage.getItem("isAuth") || false;
        if (this.is_auth == false)
          this.$router.push({ name: "logIn" });
        else
          this.$router.push({ name: "home" });
      },
      loadLogIn: function () {
        this.$router.push({ name: "logIn" })
      },
      loadSignUp: function () {
        this.$router.push({ name: "signUp" })
      },
      loadForgotPass: function () {
        this.$router.push({ name: "forgotPass" })
      },
      completedLogIn: function (data) {
        localStorage.setItem("isAuth", true);
        localStorage.setItem("username", data.nickName);
        alert("Autenticación Exitosa");
        this.verifyAuth();
      },
      completedSignUp: function (data) {
        alert("Registro Exitoso");
        this.completedLogIn(data);
      },
      loadHome: function () {
        this.$router.push({ name: "home" });
      },
      logOut: function () {
        localStorage.clear();
        alert("Sesión Cerrada");
        this.verifyAuth();
      },
    },
    created: function () {
      this.verifyAuth()
    }
  }
</script>
<style>
body {
  margin: 0 0 0 0;
}

.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #0275b3;
  color: #E5E7E9;
  display: flex;
  justify-content: space-between;
  align-items: center;

}

.header h1 {
  font-family: Arial, Helvetica, sans-serif;
  width: 20%;
  text-align: center;
}

.header nav {
  height: 100%;
  width: 20%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}

.header nav button {

  color: #ffffff;
  background: #39c1eed0;
  border: 1px solid #9abada;
  border-radius: 30px;
  padding: 10px 20px;

}

.header nav button:hover {

  color: #565fd6;
  background: #E5E7E9;
  border: 1px solid #E5E7E9;
}

.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #FDFEFE;

}

.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #0275b3;
  color: #E5E7E9;
}

.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: Arial, Helvetica, sans-serif;
}
</style>