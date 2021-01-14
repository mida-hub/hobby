import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import awsmobile from './aws-exports'
import Amplify from 'aws-amplify'
const amplifyConfig = {
    'aws_appsync_graphqlEndpoint': awsmobile.aws_appsync_graphqlEndpoint,
    'aws_appsync_region': awsmobile.aws_appsync_region,
    'aws_appsync_authenticationType': awsmobile.aws_appsync_authenticationType,
    'aws_appsync_apiKey': awsmobile.aws_appsync_apiKey
}
Amplify.configure(amplifyConfig)
Vue.config.productionTip = false
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
