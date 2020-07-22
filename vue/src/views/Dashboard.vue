<template>
  <div class="Dashboard">
    
    <b-nav class="menu navbar navbar-expand-lg navbar-dark bg-dark" vertical>
        <router-link v-for="item in dash_items" v-bind:key="item.name" class="nav-link" v-bind:to="item.path">{{ item.name }}</router-link>

    
    </b-nav>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Dashboard',
  components: {
  },
  data: function(){
      return{
          dash_items:[
              {"name":"Projects", "path":"/#"},
              {"name":"Observations", "path":"/#"},
              {"name":"Search", "path":"/#"},
              {"name":"Profile", "path":"/#"}

          ]
      }
  }
}
</script>
<style>
.menu{
    position: fixed;
    left: 0em;
    width: 10em;
    height: 100%;
}.nav-link{
    color: white;
}
</style>
