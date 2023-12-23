<template>
  <div class="speciality-slider">
    <BgEllipse size="132" color="#FF4DF8" class="speciality-slider__first-ellipse" />
    <BgEllipse size="220" color="#00C2FF" class="speciality-slider__second-ellipse" />
    <BgEllipse size="132" color="#0085FF" class="speciality-slider__third-ellipse" />
    <div class="speciality-slider__title">УКАЖИТЕ ВАШУ СПЕЦИАЛЬНОСТЬ:</div>
    <Swiper
      class="speciality-slider__swiper"
      centered-slides
      :space-between="30"
      :modules="[Navigation]"
      :navigation="{
        nextEl: nextRef,
        prevEl: prevRef,
      }"
    >
      <SwiperSlide v-for="slide in specialities" :key="slide.id" class="speciality-slider__slide">
        <div class="speciality-slider__slide-content">
          <img :src="slide.img" alt="" />
          <p>
            {{ slide.name }}
          </p>
        </div>
      </SwiperSlide>
    </Swiper>
    <div ref="nextRef" class="swiper-button next">
      <AppIcon :name="IconName.NextSliderBtnBig" :size="$screen.mdAndDown ? 20 : 74" />
    </div>
    <div ref="prevRef" class="swiper-button prev">
      <AppIcon :name="IconName.PrevSliderBtnBig" :size="$screen.mdAndDown ? 20 : 74" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();

const nextRef = ref(null);
const prevRef = ref(null);

const specialities = [
  {
    id: '1',
    name: 'Патоморфолог',
    img: '/img/specialities/DNA.png',
  },
  {
    id: '2',
    name: 'Радиотерапевт',
    img: '/img/specialities/MRI.png',
  },
  {
    id: '3',
    name: 'Хирург',
    img: '/img/specialities/SCALPEL.png',
  },
  {
    id: '4',
    name: 'Химиотерапевт',
    img: '/img/specialities/chemytherapy.png',
  },
];
</script>

<style lang="scss" scoped>
.speciality-slider {
  position: relative;

  padding: 36px 0 50px;

  &__first-ellipse {
    top: 250px;
    left: 150px;
  }
  &__second-ellipse {
    top: 160px;
    left: 320px;
  }
  &__third-ellipse {
    top: 240px;
    right: 160px;
  }

  &__title {
    margin-bottom: 38px;

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 55px;
    font-weight: 900;
    text-align: center;
  }

  &__swiper {
    width: 400px;
  }

  &__slide {
    &-content {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;

      width: 288px;
      height: 288px;
      margin: 0 auto;

      border: 2.5px solid $primary-color;
      border-radius: 50%;
    }

    img {
      width: 90%;
      height: 90%;
      margin-top: -75px;
      margin-bottom: -40px;
      object-fit: contain;
    }

    p {
      font-size: 20px;
      letter-spacing: -0.04px;
    }
  }

  .swiper-button {
    position: absolute;
    top: 57%;
    left: calc(50% - 268px);

    cursor: pointer;
    &.next {
      right: calc(50% - 268px);
      left: auto;
    }
  }
}
</style>
