<template>
  <div class="container shifted">
    <h1 class="h1">
      S3 Uploader
    </h1>
  </div>
</template>

<script>
import Vue from 'vue'
import Amplify, { API,Storage } from 'aws-amplify';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'

Vue.use(ElementUI, { locale })

export default {
  name: 'Home'
}

</script>

<style>
label {
  color: #606266;  
  background-color:white;
  padding: 10px;
}
</style>
