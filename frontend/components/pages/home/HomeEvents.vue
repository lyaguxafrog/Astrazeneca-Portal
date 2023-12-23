<template>
  <div class="home-events">
    <div class="home-events__title">Мероприятия</div>

    <ItemsSlider :items="events" :desktop-slides-per-view="2.75" #default="{ item }">
      <a href="" target="_blank">
        <img :src="item.img" alt="" />
      </a>
    </ItemsSlider>
  </div>
</template>

<script setup lang="ts">
import ItemsSlider from '~/components/common/ItemsSlider.vue';

const events = [
  {
    id: '1',
    img: '/img/e1.png',
  },
  {
    id: '2',
    img: '/img/e2.png',
  },
  {
    id: '3',
    img: '/img/e1.png',
  },
  {
    id: '4',
    img: '/img/e2.png',
  },
];
</script>

<style scoped lang="scss">
.home-events {
  margin-top: 30px;

  &__title {
    margin-top: 57px;
    margin-bottom: 174px;
    padding-left: 93px;

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 28px;
    font-weight: 900;
    text-transform: uppercase;
  }

  @include md-and-down {
    &__title {
      margin-top: 0;
      margin-bottom: 43px;
      padding-left: 26px;

      font-size: 27px;
      line-height: 28px;
    }
  }
}
</style>
