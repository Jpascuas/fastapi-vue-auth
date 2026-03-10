<script setup>
import { ref, onMounted } from 'vue'
import { login, getUser } from './services/api'

const email = ref('')
const password = ref('')
const user = ref(null)
const error = ref('')

async function doLogin() {

  error.value = ''

  try {

    const data = await login(email.value, password.value)

    if(data.token){
      localStorage.setItem("token", data.token)
      user.value = await getUser()
    }else{
      error.value = "Invalid credentials"
    }

  } catch(e){
    error.value = "Server error"
  }
}

async function logout(){
  localStorage.removeItem("token")
  user.value = null
}

onMounted(async () => {

  const token = localStorage.getItem("token")

  if(token){
    try{
      user.value = await getUser()
    }catch(e){
      logout()
    }
  }

})
</script>

<template>

<div class="container">

  <div v-if="!user" class="card">

    <h2>Vehicle Insurance Platform</h2>

    <p class="subtitle">Login</p>

    <input v-model="email" placeholder="Email" />

    <input v-model="password" type="password" placeholder="Password" />

    <button @click="doLogin">Login</button>

    <p v-if="error" class="error">{{ error }}</p>

  </div>

  <div v-if="user" class="card">

    <h2>Dashboard</h2>

    <div class="user-info">
      <p><strong>ID:</strong> {{ user.id }}</p>
      <p><strong>Name:</strong> {{ user.name }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
    </div>

    <button class="logout" @click="logout">Logout</button>

  </div>

</div>

</template>

<style>

body{
  margin:0;
  font-family: Arial, Helvetica, sans-serif;
  background:#f4f6f9;
}

.container{
  display:flex;
  justify-content:center;
  align-items:center;
  height:100vh;
}

.card{
  background:white;
  padding:40px;
  border-radius:10px;
  width:320px;
  box-shadow:0 10px 25px rgba(0,0,0,0.1);
  text-align:center;
}

.subtitle{
  color:#666;
  margin-bottom:20px;
}

input{
  width:100%;
  padding:10px;
  margin-bottom:12px;
  border:1px solid #ddd;
  border-radius:5px;
}

button{
  width:100%;
  padding:10px;
  background:#3b82f6;
  border:none;
  color:white;
  border-radius:5px;
  cursor:pointer;
}

button:hover{
  background:#2563eb;
}

.logout{
  background:#ef4444;
}

.logout:hover{
  background:#dc2626;
}

.error{
  color:red;
  margin-top:10px;
}

.user-info{
  text-align:left;
  margin-bottom:20px;
}

</style>