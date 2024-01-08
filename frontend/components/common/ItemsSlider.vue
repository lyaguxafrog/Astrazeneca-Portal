<template>
  <div class="items-slider" :class="{ hidePagination }">
    <Swiper
      grab-cursor
      :centered-slides="centeredSlides"
      :space-between="$screen.mdAndDown ? 40 : 100"
      :slides-per-view="$screen.mdAndDown ? mobileSlidesPerView : desktopSlidesPerView"
      :initial-slide="items.length < 3 ? 0 : initialSlide"
      :modules="[Pagination, Navigation]"
      :pagination="{ clickable: true }"
      :slides-offset-before="$screen.mdAndDown ? 22 : undefined"
      :slides-offset-after="$screen.mdAndDown ? 22 : undefined"
      :navigation="{
        nextEl: nextRef,
        prevEl: prevRef,
      }"
      @swiper="onSwiper"
      @slide-change="onSlideChange"
    >
      <SwiperSlide v-for="item in items" :key="item.id" class="items-slider__slide">
        <slot name="default" :item="item"></slot>
      </SwiperSlide>
    </Swiper>
    <div v-if="withNavigation" ref="nextRef" class="swiper-button next">
      <AppIcon v-if="$screen.mdAndDown" :name="IconName.NextSliderBtn" :size="48" />
      <AppIcon v-else :name="IconName.NextSliderBtnBig" :size="107" />
    </div>
    <div v-if="withNavigation" ref="prevRef" class="swiper-button prev">
      <AppIcon v-if="$screen.mdAndDown" :name="IconName.PrevSliderBtn" :size="48" />
      <AppIcon v-else :name="IconName.PrevSliderBtnBig" :size="107" />
    </div>
  </div>
</template>

<script setup lang="ts" generic="T extends SliderProps">
import { Pagination, Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import { ref } from 'vue';
import { Swiper as SwiperType } from 'swiper/types';

export type SliderProps = {
  id: number;
};

withDefaults(
  defineProps<{
    items: T[];
    desktopSlidesPerView: number;
    mobileSlidesPerView?: number;
    initialSlide?: number;
    withNavigation?: boolean;
    hidePagination?: boolean;
    centeredSlides?: boolean;
  }>(),
  {
    initialSlide: 1,
    mobileSlidesPerView: 1.5,
    centeredSlides: true,
  }
);

defineSlots<{
  default: (props: { item: T }) => void;
}>();

const emit = defineEmits<{
  (event: 'onSlideChange', value: number | undefined): void;
}>();

const { $screen } = useScreen();

const nextRef = ref(null);
const prevRef = ref(null);

const swiper = ref<SwiperType>();

const onSwiper = (s: SwiperType) => {
  swiper.value = s;
};

const onSlideChange = () => {
  emit('onSlideChange', swiper.value?.realIndex);
};
</script>

<style lang="scss" scoped>
.items-slider {
  position: relative;

  .swiper-button {
    position: absolute;
    top: 220px;
    left: calc(50% - 34vw);

    cursor: pointer;
    @include z-index(2);

    &.next {
      right: calc(50% - 34vw);
      left: auto;
    }
  }

  &__slide {
    position: relative;

    height: auto;
    overflow: hidden;
  }

  :slotted(.items-slider__content) {
    display: block;

    width: 100%;
  }

  &::v-deep {
    &.hidePagination {
      .swiper {
        &-pagination {
          display: none;
        }
      }
    }

    .swiper {
      &-pagination {
        position: static;

        margin-top: 50px;

        &-bullet {
          width: 16px;
          height: 16px;
          margin: 0 40px;

          background-color: $white-color;

          opacity: 1;

          &-active {
            background-color: $primary-color;
          }
        }
      }
    }
  }

  :slotted(img) {
    display: block;

    width: 100%;
    object-fit: cover;

    border-radius: 54px;
  }

  @include md-and-down {
    :slotted(img) {
      border-radius: 20px;
    }

    &::v-deep {
      .swiper {
        display: flex;
        flex-direction: column-reverse;

        &-slide {
          filter: grayscale(0.7);
          transition: filter $tr-dur;

          .items-slier__visible-on-active {
            opacity: 0;
            transition: opacity $tr-dur;
          }

          &-active {
            filter: grayscale(0);

            .items-slier__visible-on-active {
              opacity: 1;
            }
          }
        }

        &-pagination {
          margin-top: 0;
          margin-bottom: 16px;

          &-bullet {
            width: 10px;
            height: 10px;
            margin: 0 10px;
          }
        }
      }
    }
  }
}
</style>
