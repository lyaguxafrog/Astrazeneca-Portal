<template>
  <div class="home">
    <div v-if="$screen.mdAndDown" class="home__intro">
      <BgEllipse class="home__intro-first-ellipse" size="386" color="#00C2FF" />
      <BgEllipse class="home__intro-second-ellipse" size="258" color="#FF4DF8" />
      <div class="home__intro-title"><span>PRO</span>РАК ЛЕГКОГО</div>

      <div class="home__intro-bottom">
        <div class="home__intro-text">
          <img src="~/assets/img/home/arrow.svg" alt="" />
          <p>информационный портал для специалистов здравоохранения</p>
        </div>
        <DefaultHistoriesSlider class="home__intro-histories" />
      </div>
    </div>

    <template v-if="speciality">
      <HomeVideosSlider />

      <HomeEvents />

      <HomeDrugs />
    </template>
  </div>
  <SpecialitySlider v-if="showSpecialitySlider" class="home__specialitySlider" />
</template>

<script lang="ts" setup>
import { isClient } from '@vueuse/core';
import { useScreen } from '~/utils/composables/useScreen';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { useDrugsStore } from '~/utils/composables/store/drugs';
import BgEllipse from '~/components/common/BgEllipse.vue';
import DefaultHistoriesSlider from '~/components/layout/DefaultHistoriesSlider.vue';
import HomeVideosSlider from '~/components/pages/home/HomeVideosSlider.vue';
import HomeDrugs from '~/components/pages/home/HomeDrugs.vue';
import HomeEvents from '~/components/pages/home/HomeEvents.vue';
import SpecialitySlider from '~/components/common/SpecialitySlider.vue';

const { $screen } = useScreen();
const { speciality } = useSpecialityStore();
const { getDrugs } = useDrugsStore();

const drugs = await getDrugs();

const showSpecialitySlider = toRef(() => $screen.value.mdAndDown && !speciality.value);

watch(
  speciality,
  (newValue) => {
    if (!$screen.value.mdAndDown) {
      return;
    }

    if (newValue) {
      enableScroll();
    } else {
      disableScroll();
    }
  },
  {
    immediate: isClient,
  }
);
</script>

<style lang="scss" scoped>
.home {
  &__intro {
    position: relative;

    display: flex;
    flex-direction: column;

    min-height: 100vh;
    padding-bottom: 18px;

    background: url('~/assets/img/home/intro-bg.png') no-repeat bottom 39px left 46% / auto 99%;

    &-title {
      padding: 67px 45px;

      font-family: $text-font-family;
      font-size: 51px;
      line-height: 0.9;
      font-weight: 500;
      color: $primary-color;
      span {
        color: $accent-color;
      }
    }
    &-first-ellipse {
      top: 18vh;
      left: -290px;
    }
    &-second-ellipse {
      top: 44vh;
      right: -220px;
      z-index: 2;
    }

    &-bottom {
      display: flex;
      flex-direction: column;
      justify-content: flex-end;

      height: 390px;
      margin-top: auto;

      background: linear-gradient(180deg, rgba(19, 37, 72, 0) 0%, #132548 56.25%);
    }

    &-text {
      display: flex;
      align-items: center;

      margin-bottom: 16px;

      font-family: $secondary-font-family;
      font-size: 19px;
      line-height: 1.3;
      text-transform: uppercase;

      img {
        margin-right: 14px;
        margin-left: -69px;
      }

      p {
        width: 260px;
      }
    }

    &-histories {
      padding: 0 25px;
    }
  }

  @include md-and-down {
    &__specialitySlider {
      position: fixed;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      @include z-index(4);
    }
  }
}
</style>
