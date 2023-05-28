import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import LogIn from './components/LogIn.vue';
import SignUp from './components/SignUp.vue';
import ForgotPass from './components/ForgotPass.vue';
import Home from './components/Home.vue';
import CreateCustomer from './components/FormCreateCustomer.vue';
import ListCustomer from './components/ListCustomer.vue';
import UpdateCustomer from './components/FormUpdateCustomer.vue';
import CreateProveedor from './components/FormCreateProveedor.vue';
import UpdateProveedor from './components/FormUpdateProveedor.vue';
import ListProveedor from './components/ListProveedor.vue';
import CreateLogistic from './components/FormCreateLogistic';
import ListLogistic from './components/ListLogistic.vue';
import UpdateLogistic from './components/FormUpdateLogistic';
const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path: '/user/logIn',
  name: "logIn",
  component: LogIn
},
{
  path: '/user/signUp',
  name: "signUp",
  component: SignUp
},
{
  path: '/user/forgotPass',
  name: "forgotPass",
  component: ForgotPass
},
{
  path: '/user/home',
  name: "home",
  component: Home
},
{
  path: '/user/formCreateCustomer',
  name: "formCreateCustomer",
  component: CreateCustomer
},
{
  path: '/user/listCustomer',
  name: "listCustomer",
  component: ListCustomer
},
{
  path: '/user/formUpdateCustomer/:customerId',
  name: "formUpdateCustomer",
  props: true,
  component: UpdateCustomer
},
{
  path: '/user/formCreateProveedor',
  name: "formCreateProveedor",
  component: CreateProveedor
},
{
  path: '/user/listProveedor',
  name: "listProveedor",
  component: ListProveedor
},
{
  path: '/user/formUpdateProveedor/:proveedorId',
  name: "formUpdateProveedor",
  props: true,
  component: UpdateProveedor
},
{
  path: '/user/formCreateLogistic',
  name: "formCreateLogistic",
  component: CreateLogistic
},
{
  path: '/user/listLogistic',
  name: "listLogistic",
  component: ListLogistic
},
{
  path: '/user/formUpdateLogistic/:logisticId',
  name: "formUpdateLogistic",
  props: true,
  component: UpdateLogistic
},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;