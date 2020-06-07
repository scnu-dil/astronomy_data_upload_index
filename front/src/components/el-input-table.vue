<template> 
<div class="test">
  <el-card class="educationExperienceTable">
    <!-- <span class="cardHeader" style="display:block;color:blue;font-weight:bold;text-align:center;font-size:35px" >基于区块链的恒星元素丰度数据智能共享平台</span> -->
  <span class="cardHeader" style="display:block;color:blue;font-weight:bold;text-align:center;font-size:35px">基于区块链的恒星元素丰度数据智能共享平台</span>
    <el-table :data="educationExperience"
              stripe
              border>
      <el-table-column label="Element" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.Element"
                      placeholder="C1">
            </el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="N_line" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.N_line"
                      placeholder="N/A">
            </el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Original [X/H]" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.O_XH"
                      placeholder="-0.49">
            </el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Original [X/Fe]" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.O_XFe"
                      placeholder="1.57">
            </el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Original log⁡-e" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.O_loge"
                      placeholder="7.9">
            </el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Converted [X/H]" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.C_XH"
                      placeholder="-0.53">
            </el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Converted [X/Fe]" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.C_XFe"
                      placeholder="1.58">
            </el-input>
          </div>
        </template>
      </el-table-column>  
      <el-table-column label="Converted log⁡-e" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.C_loge"
                      placeholder="7.9">
            </el-input>
          </div>
        </template>
      </el-table-column>
	  <el-table-column label="Organization" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.Organization"
                      placeholder="华师大">
            </el-input>
          </div>
        </template>
      </el-table-column>
	  <el-table-column label="Authors" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.Authors"
                      placeholder="作者">
            </el-input>
          </div>
        </template>
      </el-table-column>
	  <el-table-column label="Paper" width="136px">
        <template slot-scope="scope">
          <div class="educationExperienceDiv">
            <el-input v-model="scope.row.Paper"
                      placeholder="数据出处">
            </el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="操作"
                        width="136px">
        <template slot-scope="scope">
            <el-button type="success"
                        size="mini"
                        icon="el-icon-circle-plus-outline"
                        v-if="scope.row.show === 'true'"
                        plain
                        @click="pushNewEducation(scope.$index)">
            </el-button>
            <el-button type="danger"
                        size="mini"
                        icon="el-icon-delete"
                        plain
                        @click="deleteEducation(scope.$index)">
            </el-button>

        </template>
		</el-table-column>
    </el-table>
	<el-button type="primary" name="submit" @click="onSubmit" round>导入</el-button>
  </el-card>

</div>
</template>

<script>
import axios from 'axios';
import config from '@/config.js';

export default {

   data() {
	var time_temp = new Date();
    return {
      // 教育经历
      educationExperience: [{
        // 元素
        Element: '',
        // N_line
        N_line: '',
        // O_XH
        O_XH: '',
        // O_XFe
        O_XFe: '',
        // O_loge
        O_loge: '',
        // C_XH
        C_XH: '',
		// C_XFe
		C_XFe: '',
		// C_loge
		C_loge: '',
		// 是否显示新增按钮
        show: 'true',
		// 单位机构
		Organization: '',
		Authors: '',
		date_time: time_temp.getFullYear()+ '-' +time_temp.getMonth()+ '-' +time_temp.getDate(),
		Paper: ''
      }],
    };
	
  },
  //mounted(){  # 每次刷新后自动执行一次
  //  this.onSubmit()
  //},

  methods: {
	
    onSubmit (index) {
	  var time = new Date();
	  const table = this.educationExperience
	  console.log(table)
	  const list = this.educationExperience
      axios.post(`${config.HOST}/put`,
      {params: table})
        .then(response => {
		if (response.data.status === 1){
		  this.$notify.success({
			title: '成功',
			message: `数据上传成功`
		  });
		  list.splice(0, list.length);
			list.push({
				Element: '',
				N_line: '',
				O_XH: '',
				O_XFe: '',
				O_loge: '',
				C_XH: '',
				C_XFe: '',
				C_loge: '',
				show: 'true',
				Organization: '',
				Authors: '',
				date_time: time.getFullYear()+ '-' +time.getMonth()+ '-' +time.getDate(),
			    Paper: ''
			  });
		}
		else{
		  this.$notify.error({
			title: '错误',
			message: `请确认数据输入格式（非空）`
		  });
		}

		})
        .catch(error => {
          console.log(error)
        })
	},

    // 添加新的教育经历
    pushNewEducation(index) {
      var time = new Date();
      const list = this.educationExperience;
      list[index].show = 'false';
	  var d=new Date();
      list.push({
        Element: '',
        N_line: '',
        O_XH: '',
        O_XFe: '',
        O_loge: '',
        C_XH: '',
		C_XFe: '',
		C_loge: '',
        show: 'true',
		Organization: '',
		Authors: '',
		date_time: time.getFullYear()+ '-' +time.getMonth()+ '-' +time.getDate(),
        Paper: ''
	  });
    this.educationExperience = list;
    },
    // 删除教育经历
    deleteEducation(index) {
      const list = this.educationExperience;
      if (index === 0 && list.length === 1) {
        list.splice(index, 1)
        list.push({
			Element: '',
			N_line: '',
			O_XH: '',
			O_XFe: '',
			O_loge: '',
			C_XH: '',
			C_XFe: '',
			C_loge: '',
			show: 'true',
			Organization: '',
			date_time: time.getFullYear()+ '-' +time.getMonth()+ '-' +time.getDate(),
			Paper: ''
		});
      } else {
        list.splice(index, 1);
      }
      if (index === list.length) {
        list[index - 1].show = 'true';
      }
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
}
</style>



