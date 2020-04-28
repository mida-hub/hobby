var xhr = new XMLHttpRequest()
var url = 'http://localhost:8888/'

const handler = () => {
  // コンソールに出力
  console.log(xhr.responseText)
}

// get
// const getRequest = () => {
//   xhr.open('GET', url)
//   xhr.onloadend = handler
//   xhr.send()
// }

// document.addEventListener('DOMContentLoaded', () => {
//   getRequest()
// })

// post
// const postRequest = () => {
//     xhr.open('POST', url)
//     xhr.onloadend = handler
//     xhr.send()
// }

// document.addEventListener('DOMContentLoaded', () => {
//     postRequest()
// })

// post Content-Type
// const postJsonRequest = () => {
//     xhr.open('POST', url)
//     xhr.onloadend = handler
//     xhr.setRequestHeader('Content-Type', 'application/json')
//     xhr.send()
// }
  
// document.addEventListener('DOMContentLoaded', () => {
//     postJsonRequest()
// })

// Cookie
const getCookieRequest = () => {
    xhr.open('GET', url)
    // Cookie 取得を有効にするための設定
    xhr.withCredentials = true
    xhr.onloadend = handler
    xhr.send()
}
  
document.addEventListener('DOMContentLoaded', () => {
    document.cookie = 'hoge=123'
    getCookieRequest()
})