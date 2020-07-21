<template>
  <div class="signup">
    <vnav/>
    <form class="signup-form" v-on:submit.prevent="onSubmit">
    
    <div class="form-group">
        <label for="InputEmail">Email address</label>
        <input type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp" placeholder="Enter email" v-model="email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
    </div>
    <div class="form-group">
        <label for="InputPassword">Password</label>
        <input type="password" class="form-control" id="InputPassword" v-model="password">
    </div>
    
    
    <button v-if="checkInput()" type="submit" class="btn btn-primary">Submit</button>
    <button v-else  class="btn btn-secondary">Submit</button>
    
    </form>
  </div>
</template>

<script>
// @ is an alias to /src
import vnav from '@/components/vnav.vue'
import axios from 'axios'

export default {
  name: 'Signin',
  components: {
    vnav
  },
  data: function(){
    return{
      password:'',
      email:''
    }
  },
  methods:{
    checkInput: function(){
      let emailRegex = new RegExp(/\w+@\w+\.\w+/)
      return emailRegex.test(this.email)
    },
    onSubmit(){
      alert("test")
      axios.post("http://localhost:8000/api/signin/",{
        password:this.password,
        email:this.email
        })
    }
  }
}
</script>

<style>
.signup-form{
    width: 50%;
    margin: auto;
}
</style>