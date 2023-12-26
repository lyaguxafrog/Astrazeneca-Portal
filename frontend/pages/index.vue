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

    <div class="home__materials">
      <div class="home__materials-head">
        <BgEllipse
          class="home__materials-first-ellipse"
          :size="$screen.mdAndDown ? 386 : 1066"
          color="#00C2FF"
        />
        <div class="home__materials-title">
          <span>PRO</span>терапию
          <small>рака легкого</small>
        </div>

        <div class="home__materials-buttons">
          <div v-if="!$screen.mdAndDown" class="home__materials-selected">
            <template v-if="selectedType === 1"> Видеоматериалы </template>
            <template v-else> Клинические случаи </template>
          </div>

          <div class="home__materials-buttons-wrapper">
            <AppButton
              :primary="selectedType === 1"
              :selected="selectedType === 1"
              :petite="$screen.mdAndDown"
              @click="setType(1)"
            >
              <template v-if="!$screen.mdAndDown"> Видеолекции </template>
              <template v-else> Видеоматериалы </template>
            </AppButton>
            <AppButton
              :primary="selectedType === 2"
              :selected="selectedType === 2"
              :petite="$screen.mdAndDown"
              @click="setType(2)"
            >
              Клинические случаи
            </AppButton>
          </div>
        </div>
      </div>

      <HomeVideosSlider />
    </div>

    <HomeEvents />

    <HomeDrugs />
  </div>
  <SpecialitySlider v-if="showSpecialitySlider" class="home__specialitySlider" />
</template>

<script lang="ts" setup>
import { isClient } from '@vueuse/core';
import { useScreen } from '~/utils/composables/useScreen';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { useVideosStore } from '~/utils/composables/store/videos';
import { useDrugsStore } from '~/utils/composables/store/drugs';
import BgEllipse from '~/components/common/BgEllipse.vue';
import DefaultHistoriesSlider from '~/components/layout/DefaultHistoriesSlider.vue';
import HomeVideosSlider from '~/components/pages/home/HomeVideosSlider.vue';
import HomePracticum from '~/components/pages/home/HomePracticum.vue';
import HomeDrugs from '~/components/pages/home/HomeDrugs.vue';
import HomeEvents from '~/components/pages/home/HomeEvents.vue';
import SpecialitySlider from '~/components/common/SpecialitySlider.vue';
import { awaitExpression } from '@babel/types';

const { $screen } = useScreen();
const { speciality } = useSpecialityStore();
const { getVideos } = useVideosStore();
const { getDrugs } = useDrugsStore();

const videos = await getVideos();
const drugs = await getDrugs();

const showSpecialitySlider = toRef(() => $screen.value.mdAndDown && !speciality.value);

const selectedType = ref(1);

const setType = (id: number) => {
  selectedType.value = id;
};

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

  &__materials {
    position: relative;

    padding: 77px 0 9px;

    background: url('~/assets/img/home/bg.png') no-repeat bottom 48px left 0;

    &-head {
      padding: 0 56px;
    }

    &-first-ellipse {
      top: 130px;
      left: -740px;
      @include md-and-down {
        top: -60px;
        right: -350px;
        @include z-index(2);
      }
    }

    &-title {
      font-family: $secondary-font-family;
      font-size: 60px;
      font-weight: 900;
      color: $primary-color;
      text-transform: uppercase;
      span {
        color: $accent-color;
      }
      small {
        display: block;

        font-size: 40px;
        line-height: 0.4;
        font-weight: 400;
      }
    }

    &-buttons {
      display: flex;
      justify-content: space-between;

      margin: 78px 46px 43px 40px;

      &-wrapper {
        display: flex;

        margin-top: 22px;
      }

      button {
        width: 320px;
        margin-left: 26px;
        padding: 0;
      }
    }

    &-selected {
      font-family: $secondary-font-family;
      font-size: 50px;
      font-weight: 900;
      text-transform: uppercase;
    }
  }

  @include xl-and-down {
    &__materials {
      &-head {
        padding: 0 16px;
      }

      &-buttons {
        margin: 78px 0 43px;
      }

      &-selected {
        font-size: 40px;
      }
    }
  }

  @include lg-and-down {
    &__materials {
      &-selected {
        display: none;
      }
    }
  }

  @include md-and-down {
    &__materials {
      padding: 3px 0 5px;

      background: none;

      &-head {
        padding: 0 27px;
      }

      &-title {
        font-size: 27px;

        small {
          font-size: 18px;
          line-height: 0.7;
        }
      }

      &-buttons {
        display: block;

        width: 220px;
        margin: 22px auto 10px;

        &-wrapper {
          display: contents;
        }

        button {
          width: 100%;
          margin-bottom: 14px;
          margin-left: 0;
        }
      }
    }

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
