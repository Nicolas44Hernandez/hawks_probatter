<script setup>
import NumberOfPitchesItem from './NumberOfPitchesItem.vue'
import SelectVideoItem from './SelectVideoItem.vue'
import ConfigurationButtonsItem from './ConfigurationButtonsItem.vue'
</script>

<template>  
  <div>
    <ConfigurationButtonsItem @image-setup="handleImageSetup" @load-config="loadConfig" @get-config="getConfig"></ConfigurationButtonsItem>
    <NumberOfPitchesItem  @pitches-changed="handlePitchesQuandityChanged" :pitches=pitches></NumberOfPitchesItem>
    <SelectVideoItem @video-changed="handleVideoSelectionChanged" :videos=videos_list :selected-video=video></SelectVideoItem>
  </div>  
</template>
<script>
import axios from 'axios';
import qs from 'qs';
import config from '@/config.js';

export default {
  data() {
    return {
      pitches: 10,
      video: "",
      videos_list: [],
    };
  },
  mounted() {
    this.getConfig();
  },
  methods: {
    imageSetup() {
      console.log(config.IMAGE_SETUP_URL);
      axios.get(config.IMAGE_SETUP_URL)
        .then(response => {
          console.log('Image Setup response OK');
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
    },
    loadConfig() {
      const data = {
        video: this.video,
        pitches: this.pitches,
      };
      const queryString = qs.stringify(data);
      const url = `${config.CONFIGURATION_URL}?${queryString}`;
      console.log('Loading configuration:');        
      console.log(url);
      axios.post(url)
        .then(response => {          
          console.log("Config loaded");
          console.log(response.data);
          this.pitches = response.data.pitches;
          this.video = response.data.video;
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
    },
    getConfig() {
      console.log('Getting configuration from:');      
      console.log(config.CONFIGURATION_URL);
      axios.get(config.CONFIGURATION_URL)
        .then(response => {
          console.log("Configuration retreieved:");
          this.pitches = response.data.pitches;
          this.video = response.data.video;
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
      console.log('Getting videos list from:');      
      console.log(config.VIDEOS_LIST_URL);
      axios.get(config.VIDEOS_LIST_URL)
        .then(response => {
          console.log("Videos list retreieved:");
          console.log(response.data);
          let videos_list = []
          for (let i = 0; i < response.data.length; i++) {
            videos_list.push(response.data[i].name)
          }
          this.videos_list = videos_list;
          console.log("videos: list");
          console.log(this.videos_list);
          // TODO: load config in IHM elements
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
    },
    handlePitchesQuandityChanged(newVal) {          
      this.pitches = newVal;
      console.log("Pitches selection has changed");  
      console.log(this.pitches);
    },
    handleVideoSelectionChanged(newVal) {          
      this.video = newVal;
      console.log("Video selection has changed");  
      console.log(this.video);
    },
    handleImageSetup() {   
      console.log('Image Setup event handler');       
      console.log(config.IMAGE_SETUP_URL);
      axios.get(config.IMAGE_SETUP_URL)
        .then(response => {
          console.log('Image Setup response OK');
        })
        .catch(error => {
          console.log(error);
          // TODO: Handle errors
        });
    }
  }
}
</script>