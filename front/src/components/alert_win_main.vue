<template> 
  
    <div id='test_'>
    <!-- <el-button  type="primary" name="submit" @click="onSubmit" round>弹窗</el-button> -->
      <Modal :show="show" :title="title" @hideModal="hideModal" @submit="submit">
        <p>这里放弹窗的内容</p>
      </Modal>  
    </div>
  
  </template>
  
  <script>
  import Modal from './alert_windows.vue'
  export default {
      name: 'test_',
      data() {
        return {
          title: 'hash表内容',
          show: false,
        }
      },
      components: {
          Modal
      },
      methods: {
          hideModal() {
              // 取消弹窗回调
              this.show = false
          },
  
          submit() {
              // 确认弹窗回调
              this.show = false
          },
              
          onSubmit () {
              this.show = true
          },
      }
  }
  </script>
  
  