<template>
  <InsidePageHead />
  <div class="video-page">
    <BgEllipse size="1138" color="#4DDFFF" pale class="video-page__first-ellipse" />
    <BgEllipse size="984" color="#B32FC9" pale class="video-page__second-ellipse" />

    <div class="video-page__title">Заголовок видео может быть очень длинным</div>
    <div class="video-page__video">
      <video
        src="/videos/A_large_rock_waterfall.mp4"
        :style="{ backgroundImage: `url(${'/img/photo_2023-12-11_19-13-51.jpg'})` }"
      />
      <PlayVideoButton class="video-page__video-play" />
    </div>

    <div class="video-page__subtitle">Конспект видео:</div>

    <div class="video-page__text">
      Расшифровка видео в текстовом виде, скроллится вниз, расшифровка видео в текстовом виде,
      скроллится вниз, расшифровка видео в текстовом виде, скроллится вниз, расшифровка видео в
      текстовом виде, скроллится вниз, расшифровка видео в текстовом виде, скроллится вниз,
      расшифровка видео в текстовом виде, скроллится вниз, расшифровка видео в текстовом виде,
      скроллится вниз, расшифровка видео в текстовом виде, скроллится вниз, расшифровка видео в
      текстовом виде, скроллится вниз, расшифровка видео в текстовом виде, скроллится
      вниз, расшифровка видео в текстовом виде, скроллится вниз, расшифровка видео в текстовом виде,
      скроллится вниз, расшифровка видео в текстовом виде, скроллится вниз, расшифровка видео в
      текстовом виде, скроллится вниз
    </div>

    <div class="video-page__recommended">
      <div class="video-page__recommended-title">
        Рекомендуемые<br />
        видео
      </div>

      <ItemsSlider :desktop-slides-per-view="3" :items="videos" #default="{ item }">
        <nuxt-link class="video-page__recommended-slide" :to="item.link">
          <p v-html="item.title" />
          <img :src="item.previewUrl" alt="" />
          <PlayVideoButton class="video-page__recommended-slide-play" />
        </nuxt-link>
      </ItemsSlider>
    </div>
  </div>
</template>

<script setup lang="ts">
import InsidePageHead from '~/components/common/InsidePageHead.vue';
import PlayVideoButton from '~/components/common/PlayVideoButton.vue';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import { Video } from '~/utils/types/videos';
import BgEllipse from '~/components/common/BgEllipse.vue';

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
    link: '/video/2',
    title: 'Заголовок видео',
  },
  {
    id: '3',
    previewUrl: '/img/video.png',
    link: '/video/3',
    title: 'Заголовок видео',
  },
  {
    id: '4',
    previewUrl: '/img/video.png',
    link: '/video/4',
    title: 'Заголовок видео',
  },
  {
    id: '5',
    previewUrl: '/img/video.png',
    link: '/video/5',
    title: 'Заголовок видео',
  },
]);
</script>

<style scoped lang="scss">
.video-page {
  position: relative;

  padding: 0 92px;

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
    width: 60%;

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 1;
    font-weight: 900;
  }

  &__video {
    position: relative;

    margin-top: 45px;

    video {
      display: block;

      width: 100%;
      object-position: center;

      background-size: cover;
    }
  }

  &__subtitle {
    margin-top: 66px;

    font-size: 36px;
    line-height: 19px;
  }

  &__text {
    margin-top: 48px;

    font-size: 24px;
    line-height: 28px;
  }

  &__recommended {
    margin-top: 150px;

    &-title {
      margin-bottom: 94px;

      font-family: $secondary-font-family;
      font-size: 50px;
      line-height: 1;
      font-weight: 900;
    }

    p {
      margin-bottom: 24px;

      font-size: 30px;
    }

    img {
      display: block;

      width: 100%;

      border-radius: 40px;
    }

    &-slide {
      &-play {
        transform: translate(-50%, -50%) scale(0.7);
      }
    }
  }

  @include md-and-down {
    $mobile-page-pudding: 27px;

    padding: 0;

    &__title {
      width: 80%;
      padding: 0 $mobile-page-pudding;

      font-size: 27px;
      line-height: 20px;
    }

    &__fav {
      margin: 7px 12px;
    }

    &__subtitle {
      margin-top: 22px;
      padding: 0 $mobile-page-pudding;

      font-size: 19px;
      line-height: 19px;
    }

    &__text {
      margin-top: 25px;
      padding: 0 $mobile-page-pudding;

      font-size: 14px;
      line-height: 16px;
    }

    &__recommended {
      margin-top: 110px;

      &-title {
        margin-bottom: 22px;
        padding: 0 $mobile-page-pudding;

        font-size: 22px;
        line-height: 21px;
      }

      p {
        margin-bottom: 16px;

        font-size: 16px;
      }

      img {
        border-radius: 16px;
      }
    }
  }
}
</style>
