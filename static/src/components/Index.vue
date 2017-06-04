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
            {{12 - index}} minutes ago
          </div>
          <div class="chat-message">
            <p>
              {{ele}}
            </p>
          </div>
        </div>

        <!-- Message sent by you -->
        <div class="chat-you"v-if="index % 2 === 1">
          <div class="chat-user">
            <img src="http://7xoxxe.com1.z0.glb.clouddn.com/2017-06-04-022819.jpg">
          </div>
          <div class="chat-date">
            4 minutes ago
          </div>
          <div class="chat-message">
            <p>
              {{ele}}
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
        <input class="input" placeholder="Ask me anything">
        <button class="send-text">发送</button>
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
import api from '../networks/api'

console.log(api)

const recorder = new window.Recorder({
  sampleRate: 44100,
  bitRate: 128
})

export default {
  data () {
    return {
      isShowVoice: false,
      isRecording: false,
      messageList: [
        '你好~我是Moe~',
        '你好，我是John',
        '嘻嘻~',
        '今天的天气怎么样',
        '今天的天气：武汉 34°晴'
      ]
    }
  },
  filters: {
    time (value) {
      console.log(value)
      return value
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
    }
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
