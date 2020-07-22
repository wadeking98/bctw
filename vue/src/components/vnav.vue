<template>
  <div class="vnav">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <router-link class="navbar-brand" to="/">Tashis</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
        <li class="nav-item active">
            <router-link class="nav-link" to="/signin">Login</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to="/signup">Signup</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to="/about">About</router-link>
        </li>

        <li class="nav-item">
            <router-link class="nav-link" to="/dash">Dashboard</router-link>
        </li>
        
        <li class="nav-item logout">
          <a class="nav-link" v-on:click="logout" href="#">Logout</a>
        </li>
        </ul>
    </div>
    </nav>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'vnav',
  props: {
  },
  data: function(){
    return {

    }
  },
  methods:{
    logout(){
      axios.post("http://localhost:8000/api/logout/")
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.logout{
  position: absolute;
  right: 2em;
}
</style>
