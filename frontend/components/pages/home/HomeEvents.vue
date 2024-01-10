<template>
  <div v-if="events.data?.length" class="home-events">
    <div class="home-events__title">Мероприятия</div>

    <ItemsSlider :items="events.data" :desktop-slides-per-view="2.75" #default="{ item }">
      <a :href="item.url" target="_blank">
        <AppImage
          :url="item.cover"
          :url-full-x2="item.image_2800px"
          :url-full="item.image_1400px"
          :url-thin-x2="item.image_780px"
          :url-thin="item.image_390px"
        />
      </a>
    </ItemsSlider>
  </div>
</template>

<script setup lang="ts">
import { useEventsStore } from '~/utils/composables/store/events';
import ItemsSlider from '~/components/common/ItemsSlider.vue';

const { getEvents } = useEventsStore();
const { baseUrl } = useRuntimeConfig().public;
const events = await getEvents();

const initialSlide = computed(() => {});
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

  a {
    transition: filter $tr-dur;

    @include hover {
      filter: hue-rotate(45deg);
    }
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
