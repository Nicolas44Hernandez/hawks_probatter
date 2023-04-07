<template>
  <div class="item">
    <div class="column">      
        <button class="btn-get-config">
          Get Configuration 
          <font-awesome-icon icon="fa-solid fa-gear" />
        </button>
    </div>  
    <div class="column">      
        <button class="btn-load-config">
          Load Configuration 
          <font-awesome-icon icon="fa-solid fa-bolt" />
        </button>
    </div>            
    <div class="column">      
        <button class="btn-image-setup">
          Videoprojector setup
          <font-awesome-icon icon="fa-solid fa-image" />
        </button>
    </div> 
  </div>
</template>

<style scoped>
.column{
  flex-basis: 50%;
  font-size: 40px;
  padding: 8px;
}
.btn-get-config {
  display: flex;
  align-items: center;
  font-size: 40%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(7, 8, 77);
  color: #eee2e2;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.btn-image-setup {
  display: flex;
  align-items: center;
  font-size: 40%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(7, 8, 77);
  color: #eee2e2;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.btn-load-config {
  display: flex;
  align-items: center;
  font-size: 40%;
  gap: 10px;
  padding: 10px 20px;
  background-color: rgb(7, 8, 77);
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
