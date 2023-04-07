import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'


/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'
/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import { faBaseballBall, faBaseballBatBall, faGear, faImage, faBolt, faStopCircle, faPlayCircle } from '@fortawesome/free-solid-svg-icons'
/* add icons to the library */
library.add(faGear)
library.add(faBaseballBall)
library.add(faBaseballBatBall)
library.add(faImage)
library.add(faBolt)
library.add(faStopCircle)
library.add(faPlayCircle)

const app = createApp(App)

app.use(router)
.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
