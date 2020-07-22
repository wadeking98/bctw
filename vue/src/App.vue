<template>
  <div id="app">
    <vnav/>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
import vnav from '@/components/vnav.vue'

export default {
  name: 'App',
  components: {
    vnav
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


</style>
