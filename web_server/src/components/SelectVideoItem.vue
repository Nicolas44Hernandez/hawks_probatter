<template>
  <div class="item">
    <div>
      <font-awesome-icon icon="fa-solid fa-baseball-bat-ball" class="fa-2xl" />
    </div>     
    <div class="column-left">
      Video to play
    </div>
    <div class="column-right">
      <div>  
        <select id="video-select" v-model="selectedVideo">
          <option v-for="video in videos" :key="video">{{ video }}</option>
        </select>  
        <!-- <p>You selected: {{ selectedVideo }}</p> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedVideo: null,
      videos: ['R Jules', 'R Dylan', 'L Devin', 'L Jovsan']
    }
  }
}
</script>

<style scoped>
.column-left{
  flex-basis: 48%;
  margin-left: 10%; 
  font-size: 20px;
  padding: 8px;
}
.column-right {
  flex-basis: 48%;
  margin-left: 10%; 
}
.item {
  margin-top: 2rem;
  display: flex;
}
.select {
  font-size: 15px;
  padding: 8px;
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
