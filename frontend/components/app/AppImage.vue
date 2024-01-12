<template>
  <picture>
    <source
      v-if="urlThin && urlThinX2"
      :srcset="`${baseUrl}${urlThin}, ${baseUrl}${urlThinX2} 2x`"
      media="(max-width: 550px)"
    />
    <source
      v-if="urlThinX2"
      :srcset="`${baseUrl}${urlThinX2}`"
      media="(max-width: 992px)"
    />
    <source
      v-if="urlFull && urlFullX2"
      :srcset="`${baseUrl}${urlFull}, ${baseUrl}${urlFullX2} 2x`"
    />
    <img
      loading="lazy"
      onerror="this.style.display = 'none'"
      :class="{responsiveHeight}"
      :src="`${baseUrl}${url}`"
    />
  </picture>
</template>

<script setup lang="ts">
defineProps<{
  url: string;
  urlFullX2?: string;
  urlFull?: string;
  urlThinX2?: string;
  urlThin?: string;
  responsiveHeight?: boolean;
}>();

const { baseUrl } = useRuntimeConfig().public;
</script>

<style scoped lang="scss">
picture {
  img {
    display: block;

    width: 100%;
    height: 100%;

    object-fit: cover;

    &.responsiveHeight {
      height: auto;
    }
  }
}
</style>
