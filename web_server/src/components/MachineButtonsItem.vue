<template>
  <div class="item">
    <div class="column-left">      
        <button class="btn-play-ball">
          Play ball 
          <font-awesome-icon icon="fa-solid fa-circle-play" class="fa-2xl" />
        </button>
    </div>            
    <div class="column-right">      
        <button class="btn-stop">
          Stop 
          <font-awesome-icon icon="fa-solid fa-circle-stop" class="fa-2xl" />
        </button>
    </div> 
  </div>
</template>

<style scoped>

.column-left{
  margin-left: 15%;
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
  font-size: 50%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(112, 29, 29);
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
