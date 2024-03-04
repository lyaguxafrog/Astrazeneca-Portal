<template>
  <div class="histories-slider" :class="{ min }">
    <template v-if="histories?.length">
      <Swiper
        :slides-per-view="4"
        :modules="[Navigation]"
        :navigation="{
          nextEl: nextRef,
          prevEl: prevRef,
        }"
      >
        <SwiperSlide v-for="history in histories" :key="history.id" class="histories-slider__item">
          <div @click="link(history.id)">
            <div class="histories-slider__item-content">
              <div
                class="histories-slider__item-content-img"
                :style="{
                  borderColor: !viewedStories.includes(history.id)
                    ? '#00D1FF'
                    : activeSlideId === history.id
                    ? '#E130FF'
                    : '',
                }"
              >
                <AppImage
                  :url="history.avatar"
                  :url-full="history.avatar_desktop_120px"
                  :url-full-x2="history.avatar_desktop_280px"
                  :url-thin="history.avatar_mobile_70px"
                  :url-thin-x2="history.avatar_mobile_140px"
                />
              </div>
              <p>
                {{ history.title }}
              </p>
            </div>
          </div>
        </SwiperSlide>
      </Swiper>
      <div ref="nextRef" class="swiper-button next">
        <AppIcon :name="IconName.NextSliderBtn" :size="$screen.mdAndDown ? 20 : 34" />
      </div>
      <div ref="prevRef" class="swiper-button prev">
        <AppIcon :name="IconName.PrevSliderBtn" :size="$screen.mdAndDown ? 20 : 34" />
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup>
import { ref, toRef, onMounted } from 'vue';
import { useRoute, useRouter } from '#app';
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useHistoriesStore } from '~/utils/composables/store/histories';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';

defineProps<{
  min?: boolean;
}>();

const activeSlideId = toRef(() => +($route.query.historyId || 0));
const { baseUrl } = useRuntimeConfig().public;
const { $screen } = useScreen();
const { histories, getHistories, viewedStories } = useHistoriesStore();
const $route = useRoute();
const $router = useRouter();

const replaceMode = toRef(() => !!$route.query.historyId);

const link = (id: number) => {
  const query = {
    ...$route.query,
    historyId: id,
  };

  if (replaceMode.value) {
    $router.replace({
      query,
    });
  } else {
    $router.push({
      query,
    });
  }
};

const nextRef = ref(null);
const prevRef = ref(null);

onMounted(async () => {
  await getHistories();
});
</script>

<style lang="scss" scoped>
$root: histories-slider;

.#{$root} {
  position: relative;

  width: 100%;
  max-width: 606px;
  margin-left: -16px;

  &.min {
    width: 100%;
    max-width: 500px;
    margin-left: 0;

    transition: max-width $tr-dur;

    .#{$root} {
      &__item {
        &-content {
          width: 88px;

          transition: width $tr-dur;
        }

        &:deep(img) {
          height: 78px;
          @include aspect(120, 120);
        }

        p {
          width: calc(100% + 40px);
          margin-top: 8px;
          margin-left: -20px;
          padding-bottom: 1px;

          font-size: 15px;
          line-height: 1.1;
          word-break: break-word;

          transition: font-size $tr-dur, color $tr-dur;
        }
      }
    }

    .swiper-button {
      top: 32px;

      transform: scale(0.8) translateY(-5px);
      transition: transform $tr-dur;
    }
  }

  &__item {
    & > div {
      display: flex;
      flex-direction: column;
      align-items: center;

      cursor: pointer;
    }

    &-content {
      display: flex;
      flex-direction: column;
      align-items: flex-start;

      width: 120px;

      &-img {
        display: grid;

        width: 100%;
        overflow: hidden;

        border: 5px solid transparent;
        border-radius: 50%;

        transition: border-color $tr-dur;
      }

      @include hover {
        p {
          color: $accent-color;
        }
      }

      :deep(img) {
        display: block;

        width: 100%;
        height: 110px;
        object-fit: cover;
      }
    }

    p {
      width: 100%;
      margin-top: 17px;

      font-size: 20px;
      line-height: 1;
      font-weight: 300;
      text-align: center;
      letter-spacing: -0.2px;
      @include ellipsis(3);

      transition: color $tr-dur;
    }
  }

  .swiper-button {
    position: absolute;
    top: 46px;
    left: -30px;
    @include z-index(3);

    &.next {
      right: -30px;
      left: auto;
    }
  }

  @include lg-and-down {
    max-width: 530px;

    &__item {
      &-content {
        width: 100px;

        :deep(img) {
          height: 90px;
        }

        p {
          margin-top: 10px;
        }
      }
    }
  }

  @include md-and-down {
    max-width: 100%;
    margin-left: 0;

    &__item {
      display: flex;
      justify-content: center;

      & > div {
        display: block;

        width: 80%;
      }

      &-content {
        width: 100%;
        &-img {
          width: 100%;
          height: 100%;

          border-width: 2px;
        }
      }

      :deep(img) {
        height: 100%;
        @include aspect(1, 1);
      }
    }

    .swiper-button {
      top: 43%;
      left: 8px;

      transform: translateY(-50%);

      &.next {
        right: 8px;
        left: auto;
      }
    }

    p {
      margin-top: 8px;
    }
  }

  @include xs {
    &__item {
      p {
        font-size: 9px;
        letter-spacing: -0.09px;
      }
    }
  }
}
</style>
