<template>
  <div class="item">
    <div>
      <font-awesome-icon icon="fa-solid fa-baseball" class="fa-2xl" />
    </div>    
    <div class="column-left">
      Number of pitches
    </div>
    <div class="column-right">
      <div>        
        <select id="pitches" v-model="selectedQuantity" class="select">
          <option v-for="n in 21" :key="n" :value="n - 1">{{ n - 1 }}</option>
        </select>
        <!-- <p>You selected: {{ selectedQuantity }}</p> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedQuantity: 1
    };
  }
};
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
