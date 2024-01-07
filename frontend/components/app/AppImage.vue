<template>
  <picture>
    <source
      v-if="urlFull && urlFullX2"
      :srcset="`${baseUrl}${urlFull}, ${baseUrl}${urlFullX2} 2x`"
    />
    <img :src="`${baseUrl}${url}`" loading="lazy" />
  </picture>
</template>

<script setup lang="ts">
defineProps<{
  url: string;
  urlFullX2?: string;
  urlFull?: string;
  urlThinX2?: string;
  urlThin?: string;
}>();

const { baseUrl } = useRuntimeConfig().public;
</script>

<style scoped lang="scss">
picture {
  img {
    width: 100%;
    height: 100%;

    object-fit: cover;
  }
}
</style>
