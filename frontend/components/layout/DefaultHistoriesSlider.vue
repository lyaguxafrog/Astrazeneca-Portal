<template>
  <div class="histories-slider" :class="{ min }">
    {{ histories }}
    <template v-if="histories?.length">
      <Swiper
        :slides-per-view="4"
        :modules="[Navigation]"
        :navigation="{
          nextEl: nextRef,
          prevEl: prevRef,
        }"
      >
        <SwiperSlide
          v-for="(history, index) in histories"
          :key="history.id"
          class="histories-slider__item"
        >
          <nuxt-link :to="`/histories?id=${history.id}`">
            <div class="histories-slider__item-content">
              <img :src="`${baseUrl}/${history.avatar}`" alt="" :style="{ borderColor: '#fff' }" />
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
import { ref } from 'vue';
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
const { histories } = useHistoriesStore();

const nextRef = ref(null);
const prevRef = ref(null);
</script>

<style lang="scss" scoped>
$root: histories-slider;

.#{$root} {
  position: relative;

  width: 100%;
  max-width: 606px;

  &.min {
    width: 100%;
    max-width: 440px;

    transition: max-width $tr-dur;

    .#{$root} {
      &__item {
        &-content {
          width: 88px;

          transition: width $tr-dur;
        }

        img {
          height: 88px;
        }

        p {
          margin-top: 14px;
          padding-bottom: 2px;

          font-size: 17px;

          transition: font-size $tr-dur, color $tr-dur;
        }
      }
    }

    .swiper-button {
      transform: scale(0.8) translateY(-5px);
      transition: transform $tr-dur;
    }
  }

  &__item {
    &-content {
      display: flex;
      flex-direction: column;
      align-items: flex-start;

      width: 120px;

      @include hover {
        p {
          color: $accent-color;
        }
      }
    }

    img {
      display: block;

      width: 100%;
      height: 120px;
      object-fit: cover;
      @include aspect(120, 120);

      border: 5px solid;
      border-radius: 50%;
    }

    p {
      width: 100%;
      margin-top: 17px;

      font-size: 20px;
      line-height: 0.9;
      font-weight: 300;
      text-align: center;
      letter-spacing: -0.2px;

      transition: color $tr-dur;
    }
  }

  .swiper-button {
    position: absolute;
    top: 26%;
    left: -43px;
    @include z-index(3);

    &.next {
      right: -17px;
      left: auto;
    }
  }

  @include lg-and-down {
    max-width: 530px;

    &__item {
      &-content {
        width: 100px;

        img {
          height: 100px;
        }
      }
    }
  }

  @include md-and-down {
    max-width: 100%;

    &__item {
      display: flex;
      justify-content: center;

      a {
        display: block;

        width: 80%;
      }

      &-content {
        width: 100%;
      }
      img {
        height: auto;

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

      font-size: 9px;
      letter-spacing: -0.09px;
    }
  }
}
</style>
