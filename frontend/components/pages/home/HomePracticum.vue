<template>
  <div v-if="content.data?.length" class="home-practicum">
    <BgEllipse
      class="home-practicum__first-ellipse"
      color="#00C2FF"
      :pale="!$screen.mdAndDown"
      :size="$screen.mdAndDown ? 330 : 1547"
    />
    <BgEllipse
      class="home-practicum__second-ellipse"
      color="#B32FC9"
      :size="$screen.mdAndDown ? 306 : 1000"
    />

    <div class="home-practicum__title h2">практикум</div>
    <div class="home-practicum__subtitle">{{ content.data[activeSlideIndex].title }}</div>

    <div class="home-practicum__slider">
      <Swiper
        :modules="[Navigation]"
        :navigation="{
          nextEl: nextRef,
          prevEl: prevRef,
        }"
        @swiper="onSwiper"
        @slide-change="onSlideChange"
      >
        <SwiperSlide
          v-for="practicum in content.data"
          :key="practicum.id"
          class="home-practicum__item"
        >
          <AppImage
            :url="practicum.image"
            :url-full="practicum.image_desktop_810px"
            :url-full-x2="practicum.image_desktop_1620px"
            :url-thin="practicum.image_mobile_400px"
            :url-thin-x2="practicum.image_mobile_800px"
          />
          <p v-html="practicum.desription" />
          <AppButton primary class="home-practicum__item-button" :to="`/practicum/${practicum.id}`">
            Начать
          </AppButton>
          <div class="swiper-lazy-preloader" />
        </SwiperSlide>
      </Swiper>
      <div ref="nextRef" class="swiper-button next">
        <AppIcon v-if="$screen.mdAndDown" :name="IconName.RightArrow" :size="48" />
        <AppIcon v-else :name="IconName.RightArrowBig" :size="185" />
      </div>
      <div ref="prevRef" class="swiper-button prev">
        <AppIcon v-if="$screen.mdAndDown" :name="IconName.LeftArrow" :size="48" />
        <AppIcon v-else :name="IconName.LeftArrowBig" :size="185" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {computed, ref} from 'vue';
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import BgEllipse from '~/components/common/BgEllipse.vue';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { Swiper as SwiperType } from 'swiper/types';

const { $screen } = useScreen();
const { specialityId } = useSpecialityStore();

const nextRef = ref(null);
const prevRef = ref(null);

type Practicum = {
  id: number;
  title: string;
  desription: string;
  image: string;
  image_desktop_810px: string;
  image_desktop_1620px: string;
  image_mobile_400px: string;
  image_mobile_800px: string;
  speciality: number[];
};

const res = await useRequest<Practicum[]>('/practicum', {
  method: 'GET',
});

const content = computed(() => {
  if (res.data) {
    return {
      data: res.data.filter((p) => p.speciality.includes(specialityId.value))
    }
  }

  return {
    data: res.data,
  };
});

const activeSlideIndex = ref(0);
const swiper = ref<SwiperType>();

const onSwiper = (s: SwiperType) => {
  swiper.value = s;
};

const onSlideChange = () => {
  setTimeout(() => {
    if (swiper.value) {
      activeSlideIndex.value = swiper.value.realIndex;
    }
  }, 200);
};
</script>

<style scoped lang="scss">
.home-practicum {
  position: relative;

  margin-top: 30px;

  .swiper-lazy-preloader {
    top: 38%;
  }

  &__first-ellipse {
    top: 10px;
    left: -1130px;
  }
  &__second-ellipse {
    top: -250px;
    right: -700px;
  }

  &__title {
    padding: 0 95px;
  }

  &__subtitle {
    margin-top: 13px;
    padding: 0 95px;

    font-family: $secondary-font-family;
    font-size: 30px;
    line-height: 35px;
  }

  &__slider {
    position: relative;
  }

  &__item {
    :deep(img) {
      display: block;

      width: 818px;
      max-width: 60%;
      margin: 0 auto;
      object-fit: contain;
      @include aspect(818, 754);
    }

    p {
      max-width: 845px;
      margin: -53px auto 0;

      font-size: 36px;
      line-height: 42px;
      font-weight: 300;
    }

    &-button {
      width: 280px;
      margin: 38px auto;
    }
  }

  .swiper-button {
    position: absolute;
    top: 300px;
    left: calc(50% - 586px);
    @include z-index(2);

    cursor: pointer;
    &.next {
      right: calc(50% - 586px);
      left: auto;
    }
  }

  @include lg-and-down {
    .swiper-button {
      left: calc(50% - 500px);

      cursor: pointer;
      &.next {
        right: calc(50% - 500px);
      }
    }
  }

  @include md-and-down {

    .swiper-lazy-preloader {
      top: 30%;
    }

    &__first-ellipse {
      top: -10px;
      right: -270px;
      left: auto;
    }
    &__second-ellipse {
      top: -80px;
      right: auto;
      left: -230px;
    }

    &__title {
      padding: 0 27px;
    }

    &__subtitle {
      margin-top: -2px;
      padding: 0 27px;

      font-size: 18px;
      line-height: 22px;
    }

    &__item {
      img {
        width: 86%;
        margin: 0 auto;
      }

      p {
        margin-top: -20px;
        padding: 0 26px;

        font-size: 14px;
        line-height: 19px;
      }

      &-button {
        width: fit-content;
        margin: 34px auto;
      }
    }

    .swiper-button {
      top: 26%;
      left: 27px;

      cursor: pointer;
      &.next {
        right: 27px;
      }
    }
  }
}
</style>
