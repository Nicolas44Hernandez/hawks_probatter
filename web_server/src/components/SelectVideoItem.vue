<template>
  <div class="item">
    <div>
      <font-awesome-icon icon="fa-solid fa-baseball-bat-ball" class="fa-xl" />
    </div>     
    <div class="column-left">
      Video to play
    </div>
    <div class="column-right">
      <div>  
        <select id="video-select" v-model="videoSelection" class="select">
          <option v-for="video in videos" :key="video">{{ video }}</option>
        </select>  
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    selectedVideo: {
      type: String,
      required: true,
    },
    videos: {
      type: Array,
      required: true,
      validator: function(value) {
        // Check if each item in the array is a string
        return value.every(item => typeof item === 'string')
      }
    }
  },
  mounted() {
    this.videoSelection = this.selectedVideo;
  },
  data() {
    return {
      videoSelection: 'R Jules',
    }
  },
  watch: {
    videoSelection(newVal) {
      this.$emit('video-changed', newVal);
    },
    selectedVideo(newVal) {
      this.videoSelection = newVal;
    }
  }  
}
</script>

<style scoped>
.column-left{
  flex-basis: 100%;
  margin-left: 10%; 
  font-size: 100%;
  padding: 1%;
}
.column-right {
  flex-basis: 50%;
  margin-left: 1%; 
}
.item {
  margin-top: 2rem;
  display: flex;
}
.select {
  font-size: 100%;
  padding: 2%;
}
i {
  display: flex;
  place-items: center;
  place-content: center;
  width: 32px;
  height: 32px; 
  color: var(--color-text);
}
</style>
