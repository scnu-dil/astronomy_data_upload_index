<template> 
<div class="test">
  <el-card class="educationExperienceTable">
  <span class="cardHeader">天文数据</span>
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
  
  <el-card >
	<el-row>
			<el-col >
				<div class="grid-content bg-purple-light">
					<el-table :data="ShowData" style="width: 100%;height: 450px; overflow-y: scroll;" >
						<el-table-column prop="id" label="序号" width="136px"></el-table-column>
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
						<el-table-column prop="beizhu1" label="操作" width="136px">
							<template slot-scope="scope">
								<el-button type="primary" @click="update(scope.row,scope.$index)">修改</el-button>
							</template>
						</el-table-column>

					</el-table>

				</div>
			</el-col>
			<el-button type="primary" name="submit" @click="showDataFresh" round>刷新数据</el-button>
	</el-row>
  </el-card>
  

  <!-- <textarea type="text" class="from_input" placeholder="结果显示" readonly="readonly">oo</textarea> -->
<!-- <span style="margin-left: 10px">tttt</span> -->
      <!-- const from_input = { -->
        <!-- Element: '1', -->
        <!-- N_line: '2', -->
        <!-- O_XH: '3', -->
        <!-- O_XFe: '4', -->
        <!-- O_loge: '5', -->
        <!-- C_XH: '6', -->
		<!-- C_XFe: '7', -->
		<!-- C_loge: '8', -->
      <!-- }; -->
</div>
</template>

<script>
import axios from 'axios';
import qs from 'qs';

export default {

  data() {
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
      }],
	  ShowData:[{
        Element: '',
        N_line: '',
        O_XH: '',
        O_XFe: '',
        O_loge: '',
        C_XH: '',
		C_XFe: '',
		C_loge: '',
	  }]
    };
  },
  //mounted(){  # 每次刷新后自动执行一次
  //  this.onSubmit()
  //},
  methods: {
    onSubmit (index) {
	  const table = this.educationExperience
	  console.log(table)
	  const path = 'http://172.24.234.84:5000/put';  // 输入数据对应地址
	  const list = this.educationExperience
      axios.post(path,
      {params: {input: table}})
        .then(response => {
		if (response.data.status === 1){
		  this.$notify.success({
			title: '成功',
			message: `数据上传成功`
		  });
		  list.splice(0, list.length);
			list.push({
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
      const list = this.educationExperience;
      list[index].show = 'false';
      list.push({
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
      });
    this.educationExperience = list;
    },
    // 删除教育经历
    deleteEducation(index) {
      const list = this.educationExperience;
      if (index === 0 && list.length === 1) {
        list.splice(index, 1);
        list.push({
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
        });
      } else {
        list.splice(index, 1);
      }
      if (index === list.length) {
        list[index - 1].show = 'true';
      }
//      list = this.educationExperience;
    },
	
    showDataFresh() {
      const list = this.ShowData;
	  list.splice(0, list.length)  // 每次刷新清空缓存数据
	  const path = 'http://172.24.234.84:5000/get';  // 后台链接地址
	  axios.get(path)
        .then(response => {
			this.from_input = response.data.back_data
			this.index = response.data.data_len
		})
        .catch(error => {
          console.log(error)
        })
	  console.log(this.from_input)
	  var i;
	  for (i=0; i<this.index; i++){
		list.push(this.from_input[i]);
	  };
	  
    this.ShowData = list;
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
</style>



