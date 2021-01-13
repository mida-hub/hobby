<template>
  <div class="container shifted">
    <h1 class="h1">
      S3 Uploader({{this.$route.path}})
    </h1>
    <el-button @click="clickFile" class="el-icon-upload ">
      Upload
      <input type="file" ref="input" @change="upload" id="file" style="display:none;">
    </el-button>
    <el-button @click="refresh" class="el-icon-refresh-right">
      Refresh
    </el-button>
    <el-table 
      :data="s3Data"
      >
      <el-table-column
        prop="key"
        label="File" 
        sortable>
      </el-table-column>
      <el-table-column
        prop='lastModified'
        label="LastModified"
        :formatter="formatDateTime"
        sortable>
      </el-table-column>
      <el-table-column
        prop="size"
        :formatter="formatFilesize"
        label="Size"
        sortable>
      </el-table-column>
      <el-table-column
        label="Action"
      >
        <template slot-scope="scope">
          <el-button
            @click="download(scope.row)">Download</el-button>
        </template>
      </el-table-column>    
    </el-table>
  </div>
</template>

<script>
import Vue from 'vue'
import Amplify, { API,Storage } from 'aws-amplify';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
import moment from "moment-timezone";

Vue.use(ElementUI, { locale })

export default {
  name: 'Upload',
  data () {
    return {
      s3Data: [],
      s3Path: ""
    }
  },
  created () {
    this.s3Path = this.$route.path.slice(1) + '/';
    this.refresh();
  },
  methods: {
    formatFilesize (row, column, cellValue, index) {
      return cellValue.toLocaleString() + 'B';
    },
    formatDateTime (row, column, cellValue, index){
      return moment(cellValue).tz("Asia/Tokyo").format("YYYY-MM-DD HH:mm:ss");
    },
    refresh () {
      Storage.list(this.s3Path)
        .then(result => {
          console.log(JSON.parse(JSON.stringify(result)));
          this.s3Data = JSON.parse(JSON.stringify(result)).filter(
            data => {return data.size !== 0}
          );
        })
        .catch(err => console.log(err));
    },
    upload(e) {
      var files = e.target.files || e.dataTransfer.files;
      console.log(files);
      Storage.put(this.s3Path + files[0].name, files[0])
        .then(result => {
          console.log(result);
          this.$message({
            message: 'file upload succeeded.',
            type: 'success'
          });
          this.refresh();
        })
        .catch(err => {
          console.log(err);
          this.$message.error('Oops, file upload failed.');
        });
    },
    download (row) {
      console.log('key:'+row['key']);
      Storage.get(row['key'], { download: true })
        .then(result => {
          console.log(result);
          const url = URL.createObjectURL(new Blob([result.Body]));
          const link = document.createElement('a');
          link.href = url;
          link.download = row['key'];
          console.log(link);
          link.click();
        })
        .catch(err => console.log(err));
    },
    clickFile () {
       this.$refs.input.click();
    }
  },
  watch: {
    $route (to) {
      this.s3Path = to.path.slice(1) + '/';
      this.refresh();
    }
  }
}

</script>

<style>
label {
  color: #606266;  
  background-color:white;
  padding: 10px;
}
</style>
