<template>
  <div v-if="events.data?.length" class="home-events">
    <div class="home-events__title">Мероприятия</div>

    <ItemsSlider :items="shownEvents" :initial-slide="initialSlide" :desktop-slides-per-view="2.75" #default="{ item }">
      <a :href="item.url" target="_blank">
        <AppImage
          :url="item.cover"
          :url-full-x2="item.image_desktop_1400px"
          :url-full="item.image_desktop_570px"
          :url-thin-x2="item.image_mobile_540px"
          :url-thin="item.image_mobile_270px"
        />
      </a>
    </ItemsSlider>
  </div>
</template>

<script setup lang="ts">
import { useRuntimeConfig } from '#app';
import { DateTime } from "luxon";
import { useEventsStore } from '~/utils/composables/store/events';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import {computed} from "vue";

const { getEvents } = useEventsStore();
const { baseUrl } = useRuntimeConfig().public;
const events = await getEvents();

const shownEvents = computed(() => {
  return events.data?.sort((e1, e2) => DateTime.fromISO(e1.date) - DateTime.fromISO(e2.date));
});

const initialSlide = computed(() => {
  const today = DateTime.now();

  return shownEvents.value?.findIndex((e) => {
    const checkDate = DateTime.fromISO(e.date);

    return checkDate > today;
  });
});
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
