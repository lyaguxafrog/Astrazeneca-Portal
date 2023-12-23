<template>
  <InsidePageHead hide-favourites-button />
  <div class="articles-page">
    <BgEllipse size="1138" color="#4DDFFF" pale class="articles-page__first-ellipse" />
    <BgEllipse
      :size="!$screen.mdAndDown ? 984 : 306"
      color="#B32FC9"
      :pale="!$screen.mdAndDown"
      class="articles-page__second-ellipse"
    />

    <div class="articles-page__title">
      <span>PRO</span>терапию
      <small>рака легкого</small>
    </div>

    <div v-if="activeSlideContent" class="articles-page__slide-title for-mobile-or-tablet">
      {{ activeSlideContent.title }}
    </div>

    <ItemsSlider :items="articles" :desktop-slides-per-view="1.7" @onSlideChange="onSlideChange">
      <template #default="{ item }">
        <nuxt-link class="articles-page__slide" :to="item.link">
          <div
            class="articles-page__slide-title for-desktop items-slier__visible-on-active"
            v-html="item.title"
          />
          <img class="articles-page__slide-image" :src="item.previewUrl" alt="" />
          <p v-html="item.text" class="for-desktop" />
        </nuxt-link>
      </template>
    </ItemsSlider>

    <p v-if="activeSlideContent" class="for-mobile-or-tablet">
      {{ activeSlideContent.text }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { useScreen } from '~/utils/composables/useScreen';
import InsidePageHead from '~/components/common/InsidePageHead.vue';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();

const articles = ref([
  {
    id: '1',
    previewUrl: '/img/video.png',
    link: '/article/1',
    title: 'Заголовок статьи',
    text: 'Первый абзац статьи, анонс содержания всей статьи, первый абзац статьи, анонс содержания всей статьи, тут первый абзац статьи, анонс содержания всей статьи, здесь первый абзац статьи, анонс содержания всей статьи, далее первый абзац статьи.',
  },
  {
    id: '2',
    previewUrl: '/img/video.png',
    link: '/article/1',
    title: 'Заголовок статьи2',
    text: 'Первый абзац статьи41515, анонс содержания всей статьи, первый абзац статьи, анонс содержания всей статьи, тут первый абзац статьи, анонс содержания всей статьи, здесь первый абзац статьи, анонс содержания всей статьи, далее первый абзац статьи.',
  },
  {
    id: '3',
    previewUrl: '/img/video.png',
    link: '/article/1',
    title: 'Заголовок статьи3',
    text: 'Первый абзац статьи, анонс содержания всей статьи, первый абзац статьи, анонс содержания всей статьи, тут первый абзац статьи, анонс содержания всей статьи, здесь первый абзац статьи, анонс содержания всей статьи, далее первый абзац статьи.',
  },
  {
    id: '4',
    previewUrl: '/img/video.png',
    link: '/article/1',
    title: 'Заголовок статьи',
    text: 'Первый абзац статьи123, анонс содержания всей статьи, первый абзац статьи, анонс содержания всей статьи, тут первый абзац статьи, анонс содержания всей статьи, здесь первый абзац статьи, анонс содержания всей статьи, далее первый абзац статьи.',
  },
  {
    id: '5',
    previewUrl: '/img/video.png',
    link: '/article/1',
    title: 'Заголовок статьи',
    text: 'Первый абзац статьи123, анонс содержания всей статьи, первый абзац статьи, анонс содержания всей статьи, тут первый абзац статьи, анонс содержания всей статьи, здесь первый абзац статьи, анонс содержания всей статьи, далее первый абзац статьи.',
  },
]);

const activeSlide = ref(1);
const activeSlideContent = toRef(() => articles.value[activeSlide.value]);
const onSlideChange = (index: number | undefined) => {
  if (index !== undefined) {
    activeSlide.value = index;
  }
};
</script>

<style scoped lang="scss">
.articles-page {
  position: relative;

  padding-bottom: 40px;

  &__first-ellipse {
    top: -440px;
    left: -840px;
  }

  &__second-ellipse {
    top: 0;
    right: -570px;
    left: auto;
  }

  &__title {
    padding: 9px 92px 35px;

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 28px;
    font-weight: 900;
    color: $primary-color;
    text-transform: uppercase;
    span {
      color: $accent-color;
    }
    small {
      display: block;

      margin-top: 17px;

      font-size: 30px;
      line-height: 44px;
      font-weight: 400;
    }
  }

  &::v-deep {
    .swiper-slide {
      &:not(.swiper-slide-active) {
        p {
          opacity: 0.5;
        }
      }
    }
  }

  &__slide {
    &-title {
      margin-bottom: 28px;

      font-family: $secondary-font-family;
      font-size: 40px;
      line-height: 35px;
    }
    &-image {
      width: 100%;
      height: 530px;
      object-fit: cover;

      border-radius: 40px;
    }

    p {
      margin-top: 43px;

      font-size: 24px;
      line-height: 28px;

      transition: opacity $tr-dur;
    }
  }

  @include md-and-down {
    &__title {
      margin-bottom: 30px;
      padding: 0 27px;

      font-size: 27px;
      line-height: 28px;

      small {
        margin-top: 2px;

        font-size: 18px;
        line-height: 22px;
      }
    }

    &__slide {
      &-title {
        padding: 0 27px;

        font-size: 27px;
        line-height: 20px;
        font-weight: 900;
      }
      &-image {
        height: auto;
      }
    }
    p {
      margin-top: 20px;
      padding: 0 27px;

      font-size: 14px;
      line-height: 16px;
    }
  }
}
</style>
