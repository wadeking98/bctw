<template>
  <div class="signup">
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
    
    <small id="loginErr" v-if="loginErr">Incorrect Username or Password</small>
    
    <button v-if="checkInput()" type="submit" class="btn btn-primary">Submit</button>
    <button v-else  class="btn btn-secondary">Submit</button>
    
    </form>
    
    <button v-on:click="checkAuth">test</button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
axios.defaults.withCredentials = true

export default {
  name: 'Signin',
  components: {
  },
  data: function(){
    return{
      password:'',
      email:'',
      loginErr:false
    }
  },
  methods:{
    checkInput: function(){
      let emailRegex = new RegExp(/\w+@\w+\.\w+/)
      return emailRegex.test(this.email)
    },
    checkAuth(){
      axios.get("http://localhost:8000/api/test/")
    },
    onSubmit(){
      alert("test")
      axios.post("http://localhost:8000/api/signin/",{
        password:this.password,
        email:this.email
        }).then((response)=>{
          if(response.status==200){
            this.$router.push('dash')
          }
        },(error)=>{
          console.log(error.response)
          if(error.response.status==401){
            this.emailErr=true
          }
        })
    }
  }
}
</script>

<style>
.signup-form{
    width: 50%;
    margin: auto;
}.loginErr{
  color: darkred;
}
</style>