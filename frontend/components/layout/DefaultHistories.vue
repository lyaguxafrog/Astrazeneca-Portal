<template>
  <div :class="{stop: stopSwipe}" class="histories__wrapper">
    <InsidePageHead v-if="!$screen.mdAndDown" class="histories__back" />
    <div v-if="histories.length" class="histories" >
      <Swiper
        ref="historiesEl"
        class="histories__swiper"
        grab-cursor
        centered-slides
        slide-to-clicked-slide
        :slides-per-view="1"
        :space-between="$screen.mdAndDown ? 0 : 0"
        :modules="[Pagination, Navigation]"
        :pagination="{ clickable: true }"
        :navigation="{
        nextEl: nextRef,
        prevEl: prevRef,
      }"
        :initial-slide="activeHistoryIndex"
        :breakpoints="{
        1200: {
          slidesPerView: 3
        },
        992: {
          slidesPerView: 2
        }
      }"
        @swiper="onSwiper"
        @slide-change="onSlideChange"
      >
        <SwiperSlide v-for="history in histories" :key="history.id" class="history" :class="{isMounted}">
          <AppImage
            class="history__bg"
            :url="history.cover_image"
            :url-full-x2="history.cover_900px"
            :url-full="history.cover_450px"
            :url-thin-x2="history.cover_900px"
            :url-thin="history.cover_450px"
          />
          <video
            ref="videosRef"
            playsinline
            :muted="muted"
            :src="`${baseUrl}${history.video}`"
            @touchend="onVideoTouchEnd"
          />
          <AppButton v-if="!$screen.mdAndDown" mode="icon" class="history__volume" petite @click="toggleVolume">
            <AppIcon
              :name="muted ? IconName.VolumeOff : IconName.VolumeOn"
              :size="$screen.mdAndDown ? 30 : 48"
            />
          </AppButton>
        </SwiperSlide>
      </Swiper>
      <div v-if="activeHistory" class="history__controls">
        <AppFavouriteButton
          v-if="userId"
          white
          :content-type="ContentType.Stories"
          :content-id="activeHistory.id"
        />
        <AppButton v-if="$screen.mdAndDown" mode="icon" class="history__volume" petite @click="toggleVolume">
          <AppIcon
            :name="muted ? IconName.VolumeOff : IconName.VolumeOn"
            :size="$screen.mdAndDown ? 30 : 48"
          />
        </AppButton>
        <AppButton
          v-if="activeHistory.link_to_page && userId"
          primary
          :to="activeHistory.link_to_page"
          petite
          class="history__link"
        >
          Перейти
        </AppButton>
      </div>

      <div v-if="!$screen.mdAndDown" ref="nextRef" class="swiper-button next">
        <AppIcon :name="IconName.NextSliderBtnBig" :size="48" />
      </div>
      <div v-if="!$screen.mdAndDown" ref="prevRef" class="swiper-button prev">
        <AppIcon :name="IconName.PrevSliderBtnBig" :size="48" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref, toRef, watch } from 'vue';
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
import InsidePageHead from '~/components/common/InsidePageHead.vue';
import { useAuth } from "~/utils/composables/useAuth";

const { histories, getHistories, viewStory } = useHistoriesStore();
const { baseUrl } = useRuntimeConfig().public;
const $router = useRouter();
const $route = useRoute();
const { $screen } = useScreen();
const swiper = ref<SwiperType>();
const videosRef = ref<HTMLVideoElement[]>([]);
const { userId } = useAuth();

await getHistories();

const activeSlideId = toRef(() => +($route.query.historyId || 0));

const activeHistoryIndex = toRef(() =>
  histories.value.findIndex((h) => h.id === activeSlideId.value)
);
const activeHistory = toRef(() => histories.value[activeHistoryIndex.value]);
const activeVideo = toRef(() => videosRef.value[activeHistoryIndex.value]);
const muted = ref(true);

const nextRef = ref(null);
const prevRef = ref(null);
const historiesEl = ref();

const { back } = useBack();
const stopSwipe = ref(false);

const isMounted = ref(false);

const { direction } = useSwipe(historiesEl, {
  threshold: 150,
  passive: false,
  onSwipeEnd: async () => {
    if (!$screen.value.mdAndDown || stopSwipe.value) {
      return;
    }

    if (direction.value === 'up' || direction.value === 'down') {
      stopSwipe.value = true;
      await back();

      window.setTimeout(async () => {
        stopSwipe.value = false;
      }, 3000);
    }
  },
});

watch(
  () => $route.query.historyId,
  (newValue) => {
    if (newValue) {
      swiper.value?.slideTo(activeHistoryIndex.value);
    }
  }
);

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
  viewStory(activeHistory.value.id);
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

const onSlideChange = async () => {
  if (swiper.value) {
    const id = histories.value[swiper.value?.realIndex].id;
    await $router.replace({ query: { historyId: id, access_token: $route.query.access_token } });

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
    isMounted.value = true;
  }, 600);
});
</script>

<style lang="scss" scoped>
.stop {
  pointer-events: none;
}

.histories {
  position: relative;
  @include z-index(2);

  width: 100%;
  max-width: 1330px;
  margin: 0 auto;

  &__wrapper {
    background: $main-bg-color;
  }

  &__back {
    height: 0;
    min-height: 0;
    margin-bottom: -19px;
    margin-left: 20px;
    padding: 20px 0 0;
  }

  .history {
    position: relative;

    height: 100%;

    @include md-and-up {
      &:not(.swiper-slide-active) {
        transform: scale(0.48);

        .history__volume {
          opacity: 0;
          transition: none;
        }
      }
    }

    &.isMounted {
      @include md-and-up {
        transition: transform $tr-dur;
      }
    }

    &__bg {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
    }

    &__controls {
      display: flex;
      flex-direction: row-reverse;
      justify-content: center;
      align-items: center;

      width: 440px;
      margin: 16px auto 0;
      padding-bottom: 16px;
    }

    &__volume {
      position: absolute;
      right: 20px;
      bottom: 20px;
      @include z-index(2);

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
    position: relative;
    @include z-index(1);

    display: block;

    width: 100%;
    height: 85vh;
    object-fit: cover;

    background-position: center;
    background-size: cover;

    @include lg-and-down {
      @media (orientation: portrait) {
        height: 70vh;
      }
    }
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

    @include lg-and-down {
      left: 16%;
      &.next {
        right: 16%;
      }
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
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    @include z-index(4);

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

        width: 100%;
        margin: 0;
        padding: 0 20px;
      }
      &__link {
        width: 149px;
        margin-right: 0;
        margin-left: 10px;
        padding: 0;
      }

      video {
        height: 100%;
        max-height: initial;
      }

      &__volume {
        position: static;

        margin-left: auto;
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
