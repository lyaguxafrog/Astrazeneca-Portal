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
          <nuxt-link :to="link(history.id)" :replace="replaceMode">
            <div class="histories-slider__item-content">
              <div class="histories-slider__item-content-img">
                <AppImage
                  :url="history.avatar"
                  :url-full="history.avatar_desktop_120px"
                  :url-full-x2="history.avatar_desktop_280px"
                  :url-thin="history.avatar_desktop_70px"
                  :url-thin-x2="history.avatar_desktop_140px"
                  :style="{ borderColor: history.color }"
                />
              </div>
              <p>
                {{ history.title }}
              </p>
            </div>
          </nuxt-link>
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
import {ref, toRef} from 'vue';
import { useRoute } from "#app";
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useHistoriesStore } from '~/utils/composables/store/histories';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';

defineProps<{
  min?: boolean;
}>();

const { baseUrl } = useRuntimeConfig().public;
const { $screen } = useScreen();
const { histories, getHistories } = useHistoriesStore();
const $route = useRoute();

const replaceMode = toRef(() => $route.name === 'histories');

const link = (id) => {
  let url = `/histories?id=${id}`;

  if ($route.query.access_token) {
    url += `&access_token=${$route.query.access_token}`;
  }
  return url;
}

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
    max-width: 460px;
    margin-left: 0;

    transition: max-width $tr-dur;

    .#{$root} {
      &__item {
        &-content {
          width: 88px;

          transition: width $tr-dur;
        }

        &:deep(img) {
          height: 88px;
        }

        p {
          width: calc(100% + 28px);
          margin-top: 8px;
          margin-left: -14px;
          padding-bottom: 1px;

          font-size: 17px;
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
    a {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    &-content {
      display: flex;
      flex-direction: column;
      align-items: flex-start;

      width: 120px;

      &-img {
        display: grid;

        width: 100%;

        @include aspect(120, 120);
      }

      @include hover {
        p {
          color: $accent-color;
        }
      }

      :deep(img) {
        display: block;

        width: 100%;
        height: 120px;
        object-fit: cover;

        border: 5px solid;
        border-radius: 50%;
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
          height: 100px;
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

      a {
        display: block;

        width: 80%;
      }

      &-content {
        width: 100%;
        &-img {
          width: 100%;
          height: 100%;
        }
      }

      :deep(img) {
        height: 100%;

        border-width: 2px;
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
