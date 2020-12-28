<template>
  <v-content>
    <v-container fluid>
      <v-row>
        <v-col>
        </v-col>
        <v-col cols="8">
          <vue-dropzone
            ref="myVueDropzone"
            id="dropzone"
            method="PUT"
            :options="dropzoneOptions"
            @vdropzone-sending="sending"
            @vdropzone-processing="processing"
            @vdropzone-file-added="fileAdded"
          ></vue-dropzone>
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
    },
    methods: {
      sending(file, xhr) {
        const _send = xhr.send;
        xhr.send = function() {
          // Fileオブジェクトを送信するようにする
          _send.call(xhr, file);
        };
      },
      fileAdded(file) {
        // ↓↓↓ここはprocessingから移植↓↓↓
        // Fileオブジェクトに署名付きURLのプロパティを追加
        file.uploadUrl = "https://httpbin.org/put";
        // 実際はこんな感じになると思います
        // file.uploadUrl = await axios.get('/api/signed_url')
        // ↑↑↑ここはprocessingから移植↑↑↑
      },
      processing(file) {
        // Fileオブジェクトに退避しておいた署名付きURLでファイル送信先を上書き
        this.$refs.myVueDropzone.dropzone.options.url = file.uploadUrl;
      }
    }
  };
</script>

