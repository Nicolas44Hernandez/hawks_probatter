<template>
  <div class="item">
    <div class="column-left">      
      <button @click="onClickPlayBall" :disabled="running" class="btn-play-ball">
        Play ball 
        <font-awesome-icon icon="fa-solid fa-circle-play" class="fa-2xl" />
      </button>
    </div>   
    <div class="column-center">  
      <button @click="onClickStopGame" :disabled="!running" class="btn-stop">
        Stop game
        <font-awesome-icon icon="fa-solid fa-circle-stop" class="fa-2xl" />
      </button>            
    </div>          
    <div class="column-right">    
      <button @click="onClickTurnOff" class="btn-off">
        Turn Off 
        <font-awesome-icon icon="fa-solid fa-power-off" class="fa-2xl" />
      </button>          
    </div> 
  </div>
</template>
<script>
export default {
  props: {
    running: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    onClickPlayBall() {
      this.$emit('playball', true);
    },
    onClickStopGame() {
      this.$emit('playball',false);
    },
    onClickTurnOff() {
      console.log("TurnOff");
    }
  }
}
</script>

<style scoped>

.column-left{
  flex-basis: 100%;
  font-size: 40px;
  padding: 8px;
}
.column-center{
  margin-left: 2%;
  margin-right: 2%;
  flex-basis: 100%;
  font-size: 40px;
  padding: 8px;
}
.column-right{
  flex-basis: 100%;
  font-size: 40px;
  padding: 8px;
}
.btn-play-ball {
  display: flex;
  align-items: center;
  font-size: 50%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(17, 136, 53);
  color: #eee2e2;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.btn-stop {
  display: flex;
  align-items: center;
  font-size: 45%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(112, 29, 29);
  color: #eee2e2;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.btn-off {
  display: flex;
  align-items: center;
  font-size: 50%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(8, 8, 8);
  color: #eee2e2;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.item {
  margin-top: 2rem;
  display: flex;
}
</style>
