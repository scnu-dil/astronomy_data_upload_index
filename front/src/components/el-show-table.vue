<template> 
    <div class="test" >
      <el-card >
        <el-row>
                <el-col >
                    <div class="grid-content bg-purple-light">
                        <el-table :data="ShowData" style="width: 100%;height: 450px; overflow-y: scroll;" >
                            <el-table-column prop="id" label="Accepted Time" width="136px">
                                <template slot-scope="scope">
                                        <p style='width:100px;white-space:nowrap;
                                        text-overflow:ellipsis;overflow:hidden;'
                                        v-bind:title="scope.row.data_time">
                                        {{ scope.row.data_time}}</p>
                                </template>
                            </el-table-column>
                            <!-- <el-table-column prop="id" label="Element" width="136px" v-for="(Element, index) in ShowData"> -->
                            <el-table-column prop="id" label="Element" width="136px">
                                <template slot-scope="scope">
                                        <p>{{ scope.row.Element }}</p>
                                        <!-- <p>{{ scope.row.Element }}</p> -->
                                </template>
                            </el-table-column>
                            <el-table-column prop="name" label="N_line" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.N_line }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="sex" label="Original [X/H]" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.O_XH }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="hobbies" label="Original [X/Fe]" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.O_XFe }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="adress" label="Original log⁡-e" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.O_loge }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="beizhu" label="Converted [X/H]" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.C_XH }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="beizhu" label="Converted [X/Fe]" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.C_XFe }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="beizhu" label="Converted log⁡-e" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.C_loge }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="beizhu" label="Organization" width="136px">
                                <template slot-scope="scope">
                                    <p style='width:100px;white-space:nowrap;
                                    text-overflow:ellipsis;overflow:hidden;'
                                    v-bind:title="scope.row.Organization">
                                    {{ scope.row.Organization }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="beizhu" label="Authors" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.Authors }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="beizhu" label="tsHash" width="136px">
                                <template slot-scope="scope">
                                    <p style='color:rgb(17, 2, 2);width:100px;white-space:nowrap;
                                    text-overflow:ellipsis;overflow:hidden;'
                                    v-bind:title="scope.row.tshash">
                                    {{ scope.row.tshash }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="beizhu" label="Paper" width="136px">
                                <template slot-scope="scope">
                                    <p>{{ scope.row.Paper }}</p>
                                </template>
                            </el-table-column>
                            <el-table-column prop="beizhu1" label="操作" width="136px">
                              <template slot-scope="scope">
                                <el-button type="primary" @click="getCertificate(scope.row.tshash)">获取证书</el-button>
                                
                              </template>
                            </el-table-column>
                        </el-table>
    
                    </div>
                </el-col>

                <el-button type="primary" name="submit" @click="showDataFresh" round>刷新数据</el-button>
                <!-- <pagination
                :total="total"
                :page.sync="listQuery.page"
                :limit.sync="listQuery.limit"
                @pagination="getList" /> -->
        </el-row>

      </el-card>

      <div>
        <Modal :show="show" :title="title" @hideModal="hideModal" @submit="submit">
              <p style="color:rgb(0, 0, 0);font-size: 20px;">此条恒星元素数据由{{ data_offer }}</p>
              <p style="color:rgb(0, 0, 0);font-size: 20px;">于{{ block_time }}提供</p>
              <!-- title 用 v-bind绑定属性功能 -->
              <p class="information-title"
              style='width:350px;white-space:nowrap;
              text-overflow:ellipsis;overflow:hidden;'  
              v-bind:title="certificate_content.blockHash"
              ref="copyButton" :data-clipboard-text="certificate_content.blockHash">
              <span style="color:rgb(0, 0, 0);font-size: 20px;">hash值为:</span> {{ certificate_content.blockHash }}</p>
              <p style="color:rgb(0, 0, 0);font-size: 20px;">特此证明</p>
        </Modal>
      </div>
    </div>

  </template>
    
    <script type="text/javascript">
    import axios from 'axios';
    import config from '@/config.js';
    import Modal from './alert_windows.vue';
    import Pagination from './Pagination.vue';
    import Clipboard from 'clipboard';

    // document.getElementById("title_unit").title = 111;

    // 截取过长字符串
    function cutString(str, len) { 
      if(str.length*2 <= len) { 
        return str; 
      } 
      var strlen = 0; 
      var s = ""; 
      for(var i = 0;i < str.length; i++) { 
        s = s + str.charAt(i); 
        strlen = strlen + 1; 
        if(strlen >= len){ 
          s = s.substring(0,s.length-2) + "..."; 
          break;
        } 
      } 
      for (var i = str.length-len; i < str.length; i++){
        s = s + str.charAt(i);
      }
      return s; 
    } 

    export default {
      components: {
          Modal,
          Pagination  // 分页组件
      },

       data() {
        var time_temp = new Date();
        return {
          copy_tsHash: '',
          block_time: '',
          data_offer: '',
          ShowData:[{
            Element: '',
            N_line: '',
            O_XH: '',
            O_XFe: '',
            O_loge: '',
            C_XH: '',
            C_XFe: '',
            C_loge: '',
            Organization: '',
            tshash: '',
            Authors: '',
            date_time: '',
            Paper: ''
          }],
          title: '证书信息',
          show: false,
          certificate_content: {},
          total: 30,  // 总条目数
          listQuery: {
            page: 1,  
            limit: 5  // 每页限制条目数
          },
          from_input: '',
          // index: 0,
          current_index: 0,
          temp_showData: [],  // 缓存变量。存储后台传回的数据
        };

      },
      mounted(){  //每次刷新后自动执行一次
          const temp_list = this.ShowData;  
          temp_list.splice(0, temp_list.length)  // 每次刷新清空缓存数据
          axios.get(`${config.HOST}/get`)
            .then((response) => {
                console.log("GET Response")
                this.from_input = response.data.back_data
                this.index = response.data.data_len
                for (var i=0; i<this.index; i++){
                  temp_list.push(this.from_input[i]);
                };
                // const list = this.ShowData;
                // for (var i=0; i<this.index; i++){
                // list.push(this.temp_showData[i]);
                // };
            })
            .catch(error => {
              console.log(error)
            })
          this.initClipboard()
      },           
      methods: {
        initClipboard() {
              const clipboard = new Clipboard(this.$refs.copyButton);
              clipboard.on('success', (e) => {
                console.log('复制成功!')});      
              clipboard.on('error', (e) => {        
                console.log('复制失败，请再次尝试')});
        }, 
        // getList() {
        // // 获取数据
        //   const list = this.ShowData;
        //   this.total = this.index;
        //   var temp_index = this.listQuery.limit;
        //   console.log("getList");
        //   for (var i=0; i<this.index; i++){
        //         list.push(this.temp_showData[i]);
        //       };
        // },

        showDataFresh() {
          // const list = this.ShowData;
          const temp_list = this.ShowData;  
          temp_list.splice(0, temp_list.length)  // 每次刷新清空缓存数据
          axios.get(`${config.HOST}/get`)
            .then((response) => {
              console.log("GET Response")
                this.from_input = response.data.back_data
                this.index = response.data.data_len
                for (var i=0; i<this.index; i++){
                  temp_list.push(this.from_input[i]);
                };
            })
            .catch(error => {
              console.log(error)
            })
            console.log(this.index)
        },
        hideModal() {
          // 取消弹窗回调
          this.show = false
        },

        submit() {
          // 确认弹窗回调
          this.show = false
        },

        getCertificate (hash_data) {  // 传入hash值，返回证书信息
          this.show = true  
          axios.put(`${config.HOST}/get_certificate`, {params: hash_data})
          .then(response => {
            // this.title = response.data.hash_certificate_title
            this.certificate_content = response.data.hash_certificate
            this.block_time = response.data.tshash_time
            this.data_offer = response.data.offer
            this.copy_tsHash = response.data.input_tsHash
          })
          .catch(error => {
            console.log(error)
          })
        },
    
      },
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
      .from_input {
      height: 5em;
      width: 20%;
      border: 1px solid #dcdfe6;
      border-radius: 100px;
      }
    }
    .information-title {
      color: #19d3ea;
      font-size: 18px;
      cursor: pointer;  /*鼠标悬停变小手*/
      width: 100%;
    }
    </style>