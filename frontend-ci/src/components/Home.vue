<template>
    <div class="greetings">
        <h1>¡Bienvenido <span> {{username}} </span>!</h1>
        <p>Elige la opción que quieras realizar</p>
    </div>

    <div class="botones">

        <table>
            <th scope="col">ACCIONES CLIENTE</th>
            <th scope="col">ACCIONES PROVEEDOR</th>
            <th scope="col">ACCIONES LOGISTICA</th>
            <th scope="col">ACCIONES VENDEDOR</th>
            <tr>
                <td>
                    <button class="button" v-on:click="loadCreateCustomer"> Crear Cliente</button>
                    <br>
                    <button class="button" v-on:click="loadListCustomer"> Listar Clientes</button>
                    <br>
                </td>
                <td>
                    <button class="button" v-on:click="loadCreateProveedor"> Crear Proveedor</button>
                    <br>
                    <button class="button" v-on:click="loadListProveedor"> Listar Proveedores</button>
                    <br>
                </td>
                <td>
                    <button class="button" v-on:click="loadCreateLogistic"> Crear Logistica</button>
                    <br>
                    <button class="button" v-on:click="loadListLogistic"> Listar Logistica</button>
                    <br>
                </td>
                <td>
                    <button class="button" v-on:click="loadCreateCustomer"> Crear Vendedor</button>
                    <br>
                    <button class="button" v-on:click="loadListCustomer"> Listar Vendedores</button>
                    <br>
                </td>
            </tr>
        </table>
    </div>

</template>
<script>
import App from '@/App.vue';
export default {
    name: "Home",
    data: function () {
        return {
            username: localStorage.getItem("username") || "none"
        };
    },
    methods: {
        loadCreateCustomer: function () {
            this.$router.push({ name: "formCreateCustomer" });
        },
        loadListCustomer: function () {
            this.$router.push({ name: "listCustomer" });
        },
        loadCreateProveedor: function () {
            this.$router.push({ name: "formCreateProveedor" });
        },
        loadListProveedor: function () {
            this.$router.push({ name: "listProveedor" });
        },
        loadCreateLogistic: function () {
            this.$router.push({ name: "formCreateLogistic" });
        },
        loadListLogistic: function () {
            this.$router.push({ name: "listLogistic" });
        },

    },
    components: { App }
}

</script>

<style>
.greetings {
    margin: 0;
    padding: 0%;
    height: 20%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: top;
    align-items: center;
}

.botones {
    margin: 0;
    padding: 0%;
    width: 100%;
    height: 30%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.botones table {
    width: 30%;
    height: 50%;
    flex-direction: column;
    justify-content: center;
    text-size-adjust: space;
}
.botones th {
    border: 1px solid #283747;
    border-radius: 2px;
    color: #000000;
    font-family: Arial, Helvetica, sans-serif;
    width: 10px;
    text-align: center;

}

.botones td {
    border: 1px solid #283747;
    border-radius: 2px;
    color: #000000;
    font-family: Arial, Helvetica, sans-serif;
    width: 2px;
    text-align: center;

}
.greetings h1 {
    font-size: 50px;
    color: #283747;
}

.greetings p {
    font-size: 20px;
    color: #283747;
}

.greetings span {
    color: rgb(20, 123, 220);
    font-weight: bold;
}

.button {
    width: 100px;
    height: 50px;
    color: #ffffff;
    background: #39c1eed0;
    border: 1px solid #9abada;
    border-radius: 30px;
    padding: 10px 25px;
    margin: 5px 0;

}

.button:hover {
    color: #565fd6;
    background: #E5E7E9;
    border: 1px solid #283747;
}
</style>