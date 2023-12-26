<template>
  <div class="speciality-slider">
    <BgEllipse size="132" color="#FF4DF8" class="speciality-slider__first-ellipse" />
    <BgEllipse size="220" color="#00C2FF" class="speciality-slider__second-ellipse" />
    <BgEllipse size="132" color="#0085FF" class="speciality-slider__third-ellipse" />
    <div class="speciality-slider__title">УКАЖИТЕ ВАШУ СПЕЦИАЛЬНОСТЬ:</div>

    <div class="speciality-slider__wrapper">
      <Swiper
        v-if="specialities"
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
          <div class="speciality-slider__slide-content" @click="setSpeciality(slide.id)">
            <img :src="slide.image" alt="" />
            <p>
              {{ slide.name }}
            </p>
          </div>
        </SwiperSlide>
      </Swiper>
      <div ref="nextRef" class="swiper-button next">
        <AppIcon :name="IconName.NextSliderBtnBig" :size="$screen.mdAndDown ? 51 : 74" />
      </div>
      <div ref="prevRef" class="swiper-button prev">
        <AppIcon :name="IconName.PrevSliderBtnBig" :size="$screen.mdAndDown ? 51 : 74" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();

const { getSpecialities, setSpeciality } = useSpecialityStore();

const specialities = await getSpecialities();

const nextRef = ref(null);
const prevRef = ref(null);
</script>

<style lang="scss" scoped>
.speciality-slider {
  padding: 36px 0 50px;

  &__wrapper {
    position: relative;

    height: fit-content;
  }

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
      box-sizing: content-box;

      width: 288px;
      height: 288px;
      margin: 7px auto;

      border-radius: 50%;
      box-shadow: 0 0 0 2px $primary-color;

      cursor: pointer;
      transition: color $tr-dur, box-shadow $tr-dur;

      @include hover {
        color: $primary-color;

        box-shadow: 0 0 0 6px $primary-color;
      }
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
    top: 39%;
    left: calc(50% - 268px);
    @include z-index(3);

    cursor: pointer;
    &.next {
      right: calc(50% - 268px);
      left: auto;
    }
  }

  @include md-and-down {
    padding-top: 66px;
    overflow: auto;

    background-color: $main-bg-color;

    &__swiper {
      width: 100%;
    }

    &__first-ellipse {
      top: 250px;
      left: -80px;
    }
    &__second-ellipse {
      top: 190px;
      left: 53%;

      transform: translateX(-50%);
    }
    &__third-ellipse {
      top: 249px;
      right: -60px;
    }

    &__title {
      margin-bottom: 64px;

      font-size: 24px;
      line-height: 26px;
    }

    &__slide {
      &-content {
        width: 60vmin;
        height: 60vmin;

        border-width: 1px;

        img {
          width: 110%;
          height: 102%;
        }

        p {
          font-size: 18px;
          letter-spacing: -0.36px;
        }
      }
    }

    .swiper-button {
      top: 41%;
      left: calc(50% - 47vmin);
      &.next {
        right: calc(50% - 47vmin);
      }
    }
  }
}
</style>
