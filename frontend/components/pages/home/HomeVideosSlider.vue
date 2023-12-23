<template>
  <div class="videos-slider">
    <ItemsSlider :items="videos" :desktop-slides-per-view="1.7">
      <template #default="{ item }">
        <nuxt-link class="items-slider__content" :to="item.link">
          <div class="videos-slider__title items-slier__visible-on-active" v-html="item.title" />
          <img class="videos-slider__image" :src="item.previewUrl" alt="" />
          <PlayVideoButton />
        </nuxt-link>
      </template>
    </ItemsSlider>
  </div>
</template>

<script lang="ts" setup>
import { Video } from '~/utils/types/videos';
import { useScreen } from '~/utils/composables/useScreen';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import PlayVideoButton from '~/components/common/PlayVideoButton.vue';

const { $screen } = useScreen();

const videos = ref<Video[]>([
  {
    id: '1',
    previewUrl: '/img/video.png',
    link: '/video/1',
    title: 'Заголовок видео',
  },
  {
    id: '2',
    previewUrl: '/img/video.png',
    link: '/video/1',
    title: 'Заголовок видео',
  },
  {
    id: '3',
    previewUrl: '/img/video.png',
    link: '/video/1',
    title: 'Заголовок видео',
  },
  {
    id: '4',
    previewUrl: '/img/video.png',
    link: '/video/1',
    title: 'Заголовок видео',
  },
  {
    id: '5',
    previewUrl: '/img/video.png',
    link: '/video/1',
    title: 'Заголовок видео',
  },
]);
</script>

<style lang="scss" scoped>
.videos-slider {
  &__title {
    margin-bottom: 17px;

    font-family: $secondary-font-family;
    font-size: 40px;
  }

  img {
    display: block;

    width: 100%;
    object-fit: cover;

    border-radius: 34px;
  }

  &__link {
    display: block;
  }

  &__image {
    display: block;

    width: 100%;
    height: 530px;
    object-fit: cover;
  }

  @include md-and-down {
    &__title {
      margin-bottom: 14px;

      font-size: 16px;
    }

    &__image {
      height: auto;
    }
  }
}
</style>
