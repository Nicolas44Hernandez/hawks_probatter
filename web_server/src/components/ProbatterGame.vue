<script setup>
import MachineButtonsItem from './MachineButtonsItem.vue'
</script>

<template>  
  <div>
    <MachineButtonsItem @playball="handleRunning" @shutdown="handleShutdown" @reboot="handleReboot" :running=running></MachineButtonsItem>
  </div>  
</template>
<script>
import axios from 'axios';
import qs from 'qs';
import config from '@/config.js';

export default {
  data() {
    return {
      running : false,
    };
  },
  mounted() {
    setInterval(this.getRunningStatus, 1000)
  },
  methods: {
    getRunningStatus(){
      axios.get(config.RUNNING_URL)
        .then(response => {
          this.running = response.data.running;
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
    },
    handleRunning(newVal) { 
      const data = {
        running: newVal,
      };
      const queryString = qs.stringify(data);
      const url = `${config.RUNNING_URL}?${queryString}`;
      axios.post(url)
        .then(response => {          
          console.log(response.data);
          this.running = response.data.running;
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
    },
    handleShutdown(){
      const url = `${config.SHUTDOWN_URL}`;
      axios.get(url)
        .then(response => {          
          console.log(response.data);
          this.running = response.data.running;
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
    },
    handleReboot(){
      const url = `${config.REBOOT_URL}`;
      axios.get(url)
        .then(response => {          
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
    }
  }
}
</script>
