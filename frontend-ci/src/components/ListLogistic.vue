<template>
    <div class="listLogistic">
        <h2>Lista Logistica</h2>
        <div class="container_listLogistic">

            <table>
                <tr>
                    <th scope="col">NOMBRE</th>
                    <th scope="col">TIPO DE DOCUMENTO</th>
                    <th scope="col">NUMERO DE DOCUMENTO</th>
                    <th scope="col">CORREO</th>
                    <th scope="col">TELEFONO</th>
                    <th scope="col">CIUDAD</th>
                    <th scope="col">DIRECCION</th>
                    <th scope="col">FECHA DE NACIMIENTO</th>
                    <th scope="col">NICKNAME</th>
                    <th scope="col">CONTRASEÑA</th>
                    <th scope="col">ACCIONES</th>
                </tr>
                <tr v-for="i in lista">
                    <td>{{ i.name + " " + i.lastName }}</td>
                    <td>{{ i.documentType }}</td>
                    <td>{{ i.documentNumber }}</td>
                    <td>{{ i.mailAddress }}</td>
                    <td>{{ i.phone }}</td>
                    <td>{{ i.city }}</td>
                    <td>{{ i.address }}</td>
                    <td>{{ i.birthDate }}</td>
                    <td>{{ i.nickName }}</td>
                    <td>{{ i.password }}</td>
                    <td>
                        <router-link :to="{ name:'formUpdateLogistic', params:{logisticId:i.Logistics_id}}"><button>Actualizar</button></router-link>
                        <button id="button" type="submit" v-on:click="deleteLogistic(i.Logistics_id)">Eliminar</button>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { useRoute } from 'vue-router';
export default {
    name: "listLogistic",
    data: function () {
        return {
            lista: null,
            Logistics_id: "",
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
    },
    mounted: async function () {
        await axios.get("http://127.0.0.1:8000/logistica/listar").then((result) => {
            console.log(result.data);
            this.lista = result.data;
        });
    },
    methods: {
        deleteLogistic(Logistics_id) {
            axios.delete("http://127.0.0.1:8000/logistica/eliminar/" + Logistics_id)
                .then((result) => {
                    let resultado = JSON.parse(result.data);
                    console.log(resultado.message);
                    if (resultado.message == "logistica eliminado") {
                        let logisticaDeleted = "logistica" + Logistics_id + "eliminado" 
                        alert("Eliminación exitosa de logistica", logisticaDeleted);
                        location.reload(this.$router.push({ name: "listLogistic" }));
                      //  this.$router.push({ name: "listCustomer" });
                    }
                });
        },
        loadUpdateLogistic: function (Logistics_id) {
            this.$router.push({ name: "formUpdateProveedor",})
        },
   
    }
}

</script>
<style>
.listLogistic {
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.container_listLogistic {
    border: 3px solid #283747;
    border-radius: 10px;
    width: 70%;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #0275b3;

}

.listLogistic h2 {
    color: #000000;
    font-family: Arial, Helvetica, sans-serif;
    justify-content: center;

}

.listLogistic table {
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    text-size-adjust: space;
}

.listLogistic th {
    border: 1px solid #283747;
    border-radius: 2px;
    color: #ffffff;
    font-family: Arial, Helvetica, sans-serif;
    width: 50%;
    text-align: center;

}

.listLogistic td {
    border: 1px solid #283747;
    border-radius: 2px;
    color: #ffffff;
    font-family: Arial, Helvetica, sans-serif;
    width: 50%;
    text-align: center;

}

.listLogistic input {
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

.listLogistic button {
    width: 100%;
    height: 40px;
    color: #ffffff;
    background: #39c1eed0;
    border: 1px solid #9abada;
    border-radius: 30px;
    padding: 8px 15px;
    margin: 3px 0;

}

.listLogistic button:hover {
    color: #565fd6;
    background: #E5E7E9;
    border: 1px solid #283747;
}
</style>