<template>
    <div class="signUp_user">
        <div class="container_createCustomer">
            <h2>Actualizar Cliente</h2>
            <form v-on:submit.prevent="proccessUpdateCustomer">
                <input type="text" v-model="user.name" placeholder="Name">
                <br>
                <input type="text" v-model="user.lastName" placeholder="Last Name">
                <br>
                <input type="text" v-model="user.documentType" placeholder="Document Type">
                <br>
                <input type="number" v-model="user.documentNumber" placeholder="Document Number">
                <br>
                <input type="email" v-model="user.mailAddress" placeholder="Mail Address">
                <br>
                <input type="number" v-model="user.phone" placeholder="Phone Number">
                <br>
                <input type="text" v-model="user.city" placeholder="City">
                <br>
                <input type="text" v-model="user.address" placeholder="Address">
                <br>
                <input type="date" v-model="user.birthDate" placeholder="BirthDate">
                <br>
                <input type="text" v-model="user.nickName" placeholder="nickName">
                <br>
                <input type="password" v-model="user.password" placeholder="Password">
                <br>
                <button type="submit">Registrarse</button>
            </form>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: "UpdateLogistic",
    data: function () {
        return {
            user: {
                name: "",
                lastName: "",
                documentType: "",
                documentNumber: "",
                mailAddress: "",
                phone: "",
                city: "",
                address: "",
                birthDate: "",
                nickName: "",
                password: ""
                }
            }
    },
    methods: {
        proccessUpdateCustomer: function () {
            axios.put(
                "http://127.0.0.1:8000/cliente/actualizar/" + this.$route.params.customerId, {
                    name: this.user.name,
                    lastName: this.user.lastName,
                    documentType: this.user.documentType,
                    documentNumber: this.user.documentNumber,
                    mailAddress: this.user.mailAddress,
                    phone: this.user.phone,
                    city: this.user.city,
                    address: this.user.address,
                    birthDate: this.user.birthDate,
                    nickName: this.user.nickName,
                    password: this.user.password
                }
            )
                .then((result) => {
                    let resultado = JSON.parse(result.data);
                    console.log(resultado.message);
                   if (resultado.message == "datos actualizados") {
                    let updateCustomer = this.user.name 
                    alert("Actualización exitosa del cliente", updateCustomer);
                    location.reload(this.$router.push({ name: "formUpdateCustomer" }));
                    //this.$emit('createdCustomer', createCustomer);
                   }
                })
                .catch((error) => {
                    console.log(error)

                    alert("ERROR: Fallo en la actualización.");
                });
        }
    }
}
</script>
<style>
.signUp_user {
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container_createCustomer {
    border: 3px solid #283747;
    border-radius: 10px;
    width: 25%;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #0275b3;

}

.signUp_user h2 {
    color: #ffffff;
    font-family: Arial, Helvetica, sans-serif;

}

.signUp_user form {

    width: 70%;

}

.signUp_user input {
    height: 20px;
    width: 100%;
    box-sizing: border-box;
    background-color: #ffffff;
    color: rgb(0, 0, 0);
    padding: 10px 20px;
    margin: 5px 0;
    border: 1px solid #283747;
    border-radius: 30px;

}

.signUp_user button {
    width: 100%;
    height: 40px;
    color: #ffffff;
    background: #39c1eed0;
    border: 1px solid #9abada;
    border-radius: 30px;
    padding: 10px 25px;
    margin: 5px 0;

}

.signUp_user button:hover {
    color: #565fd6;
    background: #E5E7E9;
    border: 1px solid #283747;
}
</style>