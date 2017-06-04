<template>
  <q-layout>
    <div slot="header" class="toolbar">
      <q-toolbar-title :padding="0">
        Talk with Moe
      </q-toolbar-title>
    </div>
    <div class="chat-container">
      <template v-for="(ele, index) in messageList">
        <div class="chat-other" v-if="index % 2 === 0">
          <div class="chat-user">
            <img src="~assets/bot-header.jpeg">
          </div>
          <div class="chat-date">
            {{ele.time | time}}
          </div>
          <div class="chat-message">
            <p>
              {{ele.text}}
              <template v-if="ele.url">
                <br>
                <a :href="ele.url" style="color: #ffffff;text-decoration: underline;" target="_blank">点此查看</a>
              </template>
            </p>
          </div>
        </div>

        <!-- Message sent by you -->
        <div class="chat-you"v-if="index % 2 === 1">
          <div class="chat-user">
            <img src="http://7xoxxe.com1.z0.glb.clouddn.com/2017-06-04-022819.jpg">
          </div>
          <div class="chat-date">
            {{ele.time | time}}
          </div>
          <div class="chat-message">
            <p>
              {{ele.text}}
            </p>
          </div>
        </div>
      </template>
    </div>
    <div class="input-message">
      <template v-if="!isShowVoice">
        <div class="switch-ovice" @click="isShowVoice = true">
          <i class="iconfont icon-voice1"></i>
        </div>
        <input @keyup.enter="addMessage" class="input" placeholder="Ask me anything" v-model="message">
        <button class="send-text" @click="addMessage">发送</button>
      </template>
      <template v-if="isShowVoice">
        <div class="switch-ovice" @click="isShowVoice = false">
          <i class="iconfont icon-jianpan"></i>
        </div>
        <button class="send-voice" @click="recordVoice">说话</button>
      </template>
    </div>
    <div class="cancel-button-container" v-if="isRecording">
      <button class="primary circular" @click="endRecord">
        结束
      </button>
    </div>
  </q-layout>
</template>

<script>
import { Loading, Toast } from 'quasar'
import axios from 'axios'
import moment from 'moment'

moment.locale('zh-cn')

const recorder = new window.Recorder({
  sampleRate: 44100,
  bitRate: 128
})

export default {
  data () {
    return {
      isShowVoice: false,
      isRecording: false,
      message: '',
      messageList: [
        {
          text: '你好~我是Moe~',
          time: Date.now()
        }
      ]
    }
  },
  filters: {
    time (value) {
      return moment(value).fromNow()
    }
  },
  methods: {
    recordVoice () {
      recorder.start()
      Loading.show({
        message: '请说话',
        spinner: 'bars'
      })
      this.$nextTick(() => {
        this.isRecording = true
      })
    },
    endRecord () {
      recorder.stop()
      this.isRecording = false
      Loading.hide()
      this.uploadRecord()
    },
    uploadRecord () {
      Toast.create.info('正在开发中')
      recorder.getBlob(blob => {
        console.log(blob)
      })
    },
    addMessage () {
      const url = '/openapi/api'
      const key = '34a937c951c84cb3aaa855e54fda653e'
      this.messageList.push({
        text: this.message,
        time: Date.now()
      })
      this.$nextTick(() => {
        this.message = ''
      })
      axios.post(url, {
        key,
        info: this.message
      })
      .then(res => res.data)
      .then(data => {
        this.messageList.push({
          text: data.text,
          time: Date.now(),
          url: data.url || ''
        })
        this.$nextTick(() => {
          const content = document.querySelector('.layout-content')
          content.scrollTop = 9999999
        })
      })
      .catch(e => {
        Toast.create.negative('出错了，请稍后重试')
      })
      this.$nextTick(() => {
        const content = document.querySelector('.layout-content')
        content.scrollTop = 9999999
      })
    }
  },
  mounted () {
    setInterval(() => {
      this.messageList.forEach((data) => {
        data.time += 1
      })
    }, 5000)
  }
}
</script>


<style>
html,
body {
  background-color: #f5f5f5;
}

body {
  overflow: hidden;
}

.layout-content::before {
  content: '';
  background: url('~assets/bg3.jpeg') no-repeat no-repeat center;
  background-size: cover;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0.35;
}

.layout-header {
  position: fixed;
  width: 100%;
}
.layout-content {
  margin-top: 50px;
  margin-bottom: 50px;
  overflow: scroll !important;
}
.chat-container {
  padding: 0px 10px;
  margin-bottom: 10px;
  z-index: 3;
}
.input-message {
  position: fixed;
  bottom: -4px;
  width: 100%;
  background-color: #336891;
  height: 50px;
  background-color: white;
  border-top: 1px solid #e1e1e1;
  display: flex;
  align-items: center;
  padding: 0 10px;
}
.input {
  flex: 1;
  margin-right: 5px;
  /*color: #ffffff;*/
}
.chat-you,
.chat-other {
  min-width: 94vw;
}

.chat-you .chat-date, .chat-other .chat-date {
  color: #181818;
}

.height-patch {
  height: 50px;
  width: 100%;
}
.switch-ovice {
  width: 30px;
  height: 30px;
  margin: 0 10px 0 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.switch-ovice i {
  font-size: 36px;
  font-weight: 100;
  color: #625959;
}
.send-text {
  height: 33px !important;
  min-height: 0px !important;
  color: #625959;
  width: 60px;
  border: 1px solid #625959;
}
.send-voice {
  flex: 1;
  height: 33px !important;
  min-height: 0px !important;
  border: 1px solid #625959;
  color: #625959;
}
.cancel-button-container {
  z-index: 999;
  position: fixed;
  bottom: 72px;
  left: 50%;
  transform: translate(-50%, 0)
}
</style>
