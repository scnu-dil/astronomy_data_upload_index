<template> 
  <div id='input_table_element'>
    <input_table></input_table>
    <show_table></show_table>
  </div>
</template>

<script>
import axios from 'axios';
import config from '@/config.js';
import input_table from './el-input-table.vue'
import show_table from './el-show-table.vue'

export default {
	name: 'input_table_element',
	components: {
    input_table,  // 输入组件
    show_table  // 显示数据组件
	}
};

</script>

<style>
.test {
  .educationExperienceTable {
    .educationExperienceDiv {
      width: 100%;
      overflow: hidden;
      border: 1px solid rgb(231, 227, 227);
      border-radius: 10px;
      .el-input__inner {
        border: none;
      }
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



 