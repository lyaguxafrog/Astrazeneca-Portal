<template>
  <InsidePageHead :content-type="ContentType.Video" :content-id="+videoId" />
  <div v-if="content" class="video-page">
    <BgEllipse size="1138" color="#4DDFFF" pale class="video-page__first-ellipse" />
    <BgEllipse size="984" color="#B32FC9" pale class="video-page__second-ellipse" />

    <div class="video-page__title">{{ content.video_article }}</div>
    <div class="video-page__video" @click="startVideo">
      <video ref="videoEl" :controls="isStarted" :src="`${baseUrl}${content.video_url}`" />
      <template v-if="!isStarted">
        <img :src="`${baseUrl}${content.video_cover_url}`" class="video-page__video-cover" />
        <PlayVideoButton class="video-page__video-play" />
      </template>
    </div>

    <div class="video-page__subtitle">Конспект видео:</div>

    <div class="video-page__text" v-html="content.conspect" />

    <div v-if="content.video_recomendations.length" class="video-page__recommended">
      <div class="video-page__recommended-title">
        Рекомендуемые<br />
        видео
      </div>

      <ItemsSlider
        :desktop-slides-per-view="3"
        :centered-slides="content.video_recomendations.length > 3"
        :items="content.video_recomendations"
        #default="{ item }"
      >
        <nuxt-link class="video-page__recommended-slide" :to="`/video/${item.id}`">
          <p v-html="item.title" />
          <img :src="`${baseUrl}${item.preview}`" alt="" />
          <PlayVideoButton class="video-page__recommended-slide-play" />
        </nuxt-link>
      </ItemsSlider>
    </div>
  </div>

  <Teleport to="#footerAccessInfo">
    <span v-html="content?.access_number"></span>
  </Teleport>
</template>

<script setup lang="ts">
import { useRoute } from '#app';
import { useVideosStore } from '~/utils/composables/store/videos';
import InsidePageHead from '~/components/common/InsidePageHead.vue';
import PlayVideoButton from '~/components/common/PlayVideoButton.vue';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';
import { ContentType } from '~/utils/types';

const $route = useRoute();
const { getVideo } = useVideosStore();
const { baseUrl } = useRuntimeConfig().public;

const videoId = toRef(() => $route.params.id);

const content = await getVideo(+videoId.value);
const isStarted = ref(false);
const videoEl = ref();
const startVideo = () => {
  videoEl.value.play();
  isStarted.value = true;
};
</script>

<style scoped lang="scss">
.video-page {
  position: relative;

  padding: 0 92px;

  &__first-ellipse {
    top: -90px;
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

    &-cover {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1;

      width: 100%;
      height: 100%;
      object-fit: cover;
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

    &::v-deep {
      strong {
        font-weight: 700;
      }
    }
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
      img {
        display: block;

        @include aspect(1, 1);
        object-fit: cover;
      }
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
