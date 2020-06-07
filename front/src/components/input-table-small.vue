<template>
    <el-table-column label="Element" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.Element"
                      placeholder="C1">
            </el-input>
          </div>
        </template>
      </el-table-column>
  </template>
  
  <script>
  export default {
    name: 'hello11',

  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .test {
      .educationExperienceDiv {
        width: 100%;
        overflow: hidden;
        border: 1px solid rgb(231, 227, 227);
        border-radius: 10px;
        .el-input__inner {
          border: none;
        }
      }
    .cardHeader {
      font-weight: bold;
      color: #606266;
      display: block;
      padding-bottom: 10px;
      margin-bottom: 20px;
      border-bottom: 1px solid rgb(211, 211, 211);
    }
    .ShowTable {
      .ShowDiv {
        width: 100%;
        overflow: hidden;
        border: 1px solid rgb(231, 227, 227);
        border-radius: 100px;
      }
    }
  }
  </style>