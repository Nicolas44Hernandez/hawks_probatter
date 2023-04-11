<template>
   <div>
    <br><br><br><br>
    <h1>{{ appName }}</h1>
    <h2>v{{ appVersion }}</h2>
    <p>Designed and developed by {{ developer }}</p>
  </div>
</template>
<script>
export default {
  data() {
    return {
      appName: 'Hawks Probatter',
      appVersion: '1.0.0',
      developer: 'Nicolas Hernandez',
    }
  },
}
</script>

