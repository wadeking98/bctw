<template>
  <div class="signup">
    <form class="signup-form" v-on:submit.prevent="onSubmit">
    <div class="form-group">
        <label for="FirstName">First Name</label>
        <input type="text" class="form-control" id="FirstName"  placeholder="First Name" v-model="fname">
    </div>

    <div class="form-group">
        <label for="LastName">Last Name</label>
        <input type="text" class="form-control" id="LastName"  placeholder="Last Name" v-model="lname">
    </div>

    <div class="form-group">
        <label for="InputEmail">Email address</label>
        <input type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp" placeholder="Enter email" v-model="email">
        <small v-if="emailErr" id="emailErr">that email already exists</small>
    </div>
    <div class="form-group">
        <label for="InputPassword">Password</label>
        <input type="password" class="form-control" id="InputPassword" v-model="password1">
    </div>
    <div class="form-group">
        <label for="InputPasswordConf">Confirm Password</label>
        <input type="password" class="form-control" id="InputPasswordConf" v-model="password2">
    </div>
    
    <button v-if="checkInput()" type="submit" class="btn btn-primary">Submit</button>
    <button v-else  class="btn btn-secondary">Submit</button>
    
    </form>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Signup',
  components: {
  },
  data: function(){
    return{
      fname:'',
      lname:'',
      password1:'',
      password2:'',
      email:'',
      emailErr:false
    }
  },
  methods:{
    checkInput: function(){
      let emailRegex = new RegExp(/\w+@\w+\.\w+/)
      return this.password1 == this.password2 && this.password1 != '' && emailRegex.test(this.email)
    },
    onSubmit(){      
      axios.post("http://localhost:8000/api/signup/",{
        fname:this.fname,
        lname:this.lname,
        password:this.password1,
        email:this.email
        }).then((response)=>{
          if(response.status==200){
            this.$router.push('dash')
          }
        },(error)=>{
          console.log(error.response)
          if(error.response.status==409){
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
}
#emailErr{
  color: darkred;
}
</style>