<template>
  <v-content>
    <v-container fluid>
      <v-row>
        <v-col>
        </v-col>
        <v-col cols="8">
          <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions"></vue-dropzone>
        </v-col>
        <v-col>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'

  export default {
    components: {
      vueDropzone: vue2Dropzone
  },
  data: function () {
    return {
      dropzoneOptions: {
          url: 'https://httpbin.org/post',
          chunking: true,
          chunkSize: 500,
          thumbnailWidth: 150,
          thumbnailHeight: 150,
          maxFilesize: 50,
          maxFiles: 1,
          addRemoveLinks: true,
          headers: { "My-Awesome-Header": "header value" },
          dictDefaultMessage: "<i class='fa fa-cloud-upload'></i>Drop Here. File Upload"
        }
      }
    }
  }
</script>

