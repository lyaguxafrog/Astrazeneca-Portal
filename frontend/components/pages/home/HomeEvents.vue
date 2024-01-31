<template>
  <div v-if="shownEvents?.length" class="home-events">
    <div class="home-events__title">Мероприятия</div>

    <ItemsSlider :items="shownEvents" :desktop-slides-per-view="2.75" #default="{ item }">
      <a :href="item.url" target="_blank" class="home-events__item">
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
import {computed} from "vue";
import { useRuntimeConfig } from '#app';
import { DateTime } from 'luxon';
import { useEventsStore } from '~/utils/composables/store/events';
import ItemsSlider from '~/components/common/ItemsSlider.vue';

const { getEvents } = useEventsStore();
const { baseUrl } = useRuntimeConfig().public;
const events = await getEvents();

const shownEvents = computed(() => {
  const sortedEvents = events.data?.sort((e1, e2) => DateTime.fromISO(e1.date) - DateTime.fromISO(e2.date));

  const today = DateTime.fromISO(DateTime.now().toFormat('yyyy-MM-dd'));

  const activeSlideFind = sortedEvents.findIndex((e) => {
    const checkDate = DateTime.fromISO(e.date);

    return checkDate >= today;
  });

  const moveIndex = activeSlideFind >= 0 ? activeSlideFind : sortedEvents?.length - 1;

  if (moveIndex >= 0) {
    const spliced = sortedEvents?.splice(0, moveIndex ? moveIndex - 1 : sortedEvents?.length - 1);

    return [...sortedEvents, ...spliced];
  }

  return [...sortedEvents];
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
    display: block;

    overflow: hidden;

    border-radius: 40px;

    transition: filter $tr-dur;

    @include hover {
      filter: hue-rotate(45deg);
    }
  }

  &__item {
    :deep(img) {
      @include aspect(1,1);
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

    a {
      border-radius: 20px;
    }
  }
}
</style>
