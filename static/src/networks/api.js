import axios from 'axios'

class Api {
  constructor () {
    this.http = axios.create()
  }
}

export default new Api()
