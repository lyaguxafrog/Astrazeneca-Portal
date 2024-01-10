<template>
  <div class="search-page">
    <DefaultSearch />
    <BgEllipse size="244" color="#00C2FF" class="search-page__first-ellipse" />
    <BgEllipse size="132" color="#FF4DF8" class="search-page__second-ellipse" />
    <BgEllipse size="132" color="#0085FF" class="search-page__third-ellipse" />
    <BgEllipse size="247" color="#904DFF" class="search-page__forth-ellipse" />
  </div>
</template>

<script setup lang="ts">
import DefaultSearch from '~/components/layout/DefaultSearch.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';

useHead({
  title: 'Поиск',
});
</script>

<style scoped lang="scss">
.search-page {
  position: relative;

  &__first-ellipse {
    top: 90px;
    left: -150px;
  }
  &__second-ellipse {
    top: 300px;
    left: -30px;
  }
  &__third-ellipse {
    top: 260px;
    right: -30px;
  }
  &__forth-ellipse {
    top: 470px;
    right: -150px;
  }
}
</style>
