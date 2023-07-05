<template>
  <div class="item">
    <button @click="onClickGetConfig" class="btn-get-config">
      Get config 
      <font-awesome-icon icon="fa-solid fa-gear" />
    </button>
    <button @click="onClickLoadConfig" class="btn-load-config">
      Load config 
      <font-awesome-icon icon="fa-solid fa-bolt" />
    </button>
    <button @click="onClickImageSetup" class="btn-image-setup">
      Image setup
      <font-awesome-icon icon="fa-solid fa-image" />
    </button>
  </div>
</template>

<script>
export default {  
  methods: {
    onClickImageSetup() {
      this.$emit('image-setup');
    },
    onClickLoadConfig() {
      this.$emit('load-config');
    },
    onClickGetConfig() {
      this.$emit('get-config');
    }
  }
}
</script>

<style scoped>
.column{
  align-items: center;
  flex-basis: 100%;
  font-size: 30px;
  padding: 8px;
  margin: 0px;
}
.btn-get-config {
  display: flex;
  align-items: center;
  font-size: 75%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(7, 8, 77);
  color: #eee2e2;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 2%;
}
.btn-image-setup {
  display: flex;
  align-items: center;
  font-size: 75%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(7, 8, 77);
  color: #eee2e2;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 2%;
}
.btn-load-config {
  display: flex;
  align-items: center;
  font-size: 75%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(7, 8, 77);
  color: #eee2e2;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 2%;
}

.item {
  margin-top: 5%;
  /* margin: 0px; */
  display: flex;
}
</style>
