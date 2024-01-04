<template>
  <div ref="historiesEl" class="histories">
    <Swiper
      class="histories__swiper"
      grab-cursor
      centered-slides
      slide-to-clicked-slide
      :slides-per-view="$screen.mdAndDown ? 1 : 3"
      :space-between="$screen.mdAndDown ? 0 : 0"
      :modules="[Pagination, Navigation]"
      :pagination="{ clickable: true }"
      :navigation="{
        nextEl: nextRef,
        prevEl: prevRef,
      }"
      :initial-slide="activeSlide"
      @swiper="onSwiper"
      @slide-change="onSlideChange"
    >
      <SwiperSlide v-for="history in histories" :key="history.id" class="history">
        <video
          ref="videosRef"
          playsinline
          :muted="muted"
          :src="`${baseUrl}${history.video}`"
          :style="{ backgroundImage: `url(${baseUrl}${history.cover_image})` }"
          @touchend="onVideoTouchEnd"
        />
        <AppButton mode="icon" class="history__volume" petite @click="toggleVolume">
          <AppIcon
            :name="muted ? IconName.VolumeOff : IconName.VolumeOn"
            :size="$screen.mdAndDown ? 30 : 48"
          />
        </AppButton>
      </SwiperSlide>
    </Swiper>

    <div v-if="activeHistory" class="history__controls">
      <AppFavouriteButton white :content-type="ContentType.Story" :content-id="activeHistory.id" />
      <AppButton primary :to="activeHistory.link" petite class="history__link"> Перейти </AppButton>
    </div>

    <div v-if="!$screen.mdAndDown" ref="nextRef" class="swiper-button next">
      <AppIcon :name="IconName.NextSliderBtnBig" :size="48" />
    </div>
    <div v-if="!$screen.mdAndDown" ref="prevRef" class="swiper-button prev">
      <AppIcon :name="IconName.PrevSliderBtnBig" :size="48" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref, toRef } from 'vue';
import { useRoute, useRouter } from '#app';
import { onLongPress, useSwipe } from '@vueuse/core';
import { Navigation, Pagination } from 'swiper/modules';
import { Swiper as SwiperType } from 'swiper/types';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useScreen } from '~/utils/composables/useScreen';
import { useHistoriesStore } from '~/utils/composables/store/histories';
import { useBack } from '~/utils/composables/useHistory';
import { IconName } from '~/components/app/AppIcon.utils';
import { ContentType } from '~/utils/types';

definePageMeta({
  hideFooter: true,
});

const { histories } = useHistoriesStore();
const { baseUrl } = useRuntimeConfig().public;
const $router = useRouter();
const $route = useRoute();
const { $screen } = useScreen();
const swiper = ref<SwiperType>();
const videosRef = ref<HTMLVideoElement[]>([]);

const activeSlide = ref(+($route.query.index || 0));
const activeHistory = toRef(() => histories.value[activeSlide.value]);
const activeVideo = toRef(() => videosRef.value[activeSlide.value]);
const muted = ref(true);

const nextRef = ref(null);
const prevRef = ref(null);
const historiesEl = ref();

const { back } = useBack();

const { direction } = useSwipe(historiesEl, {
  passive: false,
  threshold: 150,
  onSwipe: () => {
    if (direction.value === 'up' || direction.value === 'down') {
      back();
    }
  },
});

const toggleVolume = () => {
  muted.value = !muted.value;
  activeVideo.value.muted = muted.value;
};
const stopAll = () => {
  videosRef.value.forEach((v) => {
    v.currentTime = 0;
    v.pause();
  });
};

const start = () => {
  activeVideo.value?.play();
};

const pause = () => {
  activeVideo.value?.pause();
};

const onVideoTouchEnd = () => {
  setTimeout(start, 500);
};

const startActiveVideo = () => {
  stopAll();
  start();
};

const onSlideChange = () => {
  if (swiper.value) {
    activeSlide.value = swiper.value.realIndex;
    $router.replace({ query: { index: activeSlide.value } });

    startActiveVideo();
  }
};

const onSwiper = (s: SwiperType) => {
  swiper.value = s;
};

onLongPress(activeVideo, pause, {
  modifiers: {
    prevent: true,
  },
});

onMounted(() => {
  setTimeout(() => {
    startActiveVideo();
  }, 500);
});
</script>

<style lang="scss" scoped>
.histories {
  position: relative;

  width: 100%;
  max-width: 1330px;
  margin: 0 auto;

  .history {
    position: relative;

    height: 100%;

    @include md-and-up {
      transition: transform $tr-dur;
      &:not(.swiper-slide-active) {
        transform: scale(0.48);

        .history__volume {
          opacity: 0;
          transition: none;
        }
      }
    }

    &__controls {
      display: flex;
      flex-direction: row-reverse;
      justify-content: center;
      align-items: center;

      width: 440px;
      margin: 16px auto;
    }

    &__volume {
      position: absolute;
      right: 20px;
      bottom: 20px;

      margin-left: 20px;

      color: $primary-color;

      transition: opacity $tr-dur $tr-dur;
    }

    &__link {
      width: 220px;
      margin-right: 20px;
      padding: 0;
    }
  }

  video {
    display: block;

    width: 100%;
    height: 754px;
    max-height: 60vw;
    object-fit: cover;

    background-position: center;
    background-size: cover;
  }

  .swiper-button {
    position: absolute;
    top: 354px;
    left: 27%;

    cursor: pointer;
    @include z-index(2);

    &.next {
      right: 27%;
      left: auto;
    }
  }

  &::v-deep {
    .swiper {
      &-pagination {
        top: 24px;
        bottom: auto;
        left: 50%;

        display: flex;
        align-items: center;

        width: 35%;
        padding: 0 17px;

        transform: translateX(-50%);

        &-bullet {
          width: 100%;
          height: 3px;
          margin: 0 3px;

          background-color: $white-color;
          border-radius: 3px;
          box-shadow: 0 0 13px 0 rgba(0, 0, 0, 0.25);

          opacity: 1;

          &-active {
            background-color: $primary-color;
          }
        }
      }
    }
  }

  @include md-and-down {
    position: relative;

    height: 100vh;

    &__swiper {
      width: auto;
      height: 100%;
    }

    .history {
      &__controls {
        position: absolute;
        top: 40px;
        @include z-index(2);

        display: flex;
        flex-direction: row;
        justify-content: space-between;

        width: 100%;
        margin: 0;
        padding: 0 20px;
      }
      &__link {
        width: 149px;
        margin-right: 0;
        padding: 0;
      }

      video {
        height: 100%;
        max-height: initial;
      }
    }

    &::v-deep {
      .swiper {
        &-pagination {
          top: 20px;

          width: 100%;
        }
      }
    }
  }
}
</style>
