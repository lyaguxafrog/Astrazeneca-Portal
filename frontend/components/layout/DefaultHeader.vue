<template>
  <div class="default-header" :class="{ extends: isExtendsHeader || activeSlideId }">
    <div ref="scrollHeaderEl" class="default-header__content">
      <div class="default-header__main" :class="{ min: !isExtendsHeader }">
        <div class="default-header__first-row">
          <transition mode="out-in">
            <nuxt-link v-if="!isExtendsHeader" to="/" class="default-header__title min">
              <span>PRO</span>Рак Легкого
            </nuxt-link>
            <div v-else></div>
          </transition>

          <DefaultMenu @openSearch="openSearch" />
        </div>
        <div class="default-header__title" :class="{ hide: !isExtendsHeader }">
          <div class="default-header__title-content"><span>PRO</span>Рак Легкого</div>
        </div>

        <div class="default-header__second-row">
          <DefaultHistoriesSlider :min="!isExtendsHeader" />

          <div class="default-header__text" :class="{ min: !isExtendsHeader }">
            <img src="~/assets/img/home/arrow-desktop.svg" alt="" />
            <p>
              информационный<br />
              портал для специалистов здравоохранения
            </p>
          </div>
        </div>
      </div>

      <transition mode="out-in">
        <DefaultHistories v-if="activeSlideId" key="2" />

        <div v-else-if="isExtendsHeader" key="1" class="default-header__modal">
          <div class="default-header__specialities">
            <SpecialitySlider />
          </div>
        </div>
      </transition>
    </div>
  </div>
  <DefaultSearch ref="searchEl" />
</template>

<script lang="ts" setup>
import { isClient } from '@vueuse/core';
import { useRoute } from '#app';
import { ref, toRef, watch } from 'vue';
import DefaultMenu from '~/components/layout/DefaultMenu.vue';
import DefaultHistoriesSlider from '~/components/layout/DefaultHistoriesSlider.vue';
import DefaultHistories from '~/components/layout/DefaultHistories.vue';
import SpecialitySlider from '~/components/common/SpecialitySlider.vue';
import DefaultSearch from '~/components/layout/DefaultSearch.vue';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { useScreen } from '~/utils/composables/useScreen';

const $route = useRoute();
const { $screen } = useScreen();
const { specialityId } = useSpecialityStore();

const isExtendsHeader = toRef(() => !specialityId.value && !$route.query.historyId);

const activeSlideId = toRef(() => +($route.query.historyId || 0));

const searchEl = ref();
const scrollHeaderEl = ref();

const openSearch = () => {
  searchEl.value.open();
};

watch(
  [isExtendsHeader, activeSlideId],
  (newValue) => {
    if (newValue.find((v) => !!v)) {
      disableScroll(scrollHeaderEl.value, $screen.value.mdAndDown);
    } else {
      enableScroll(scrollHeaderEl.value, $screen.value.mdAndDown);
    }
  },
  {
    immediate: isClient,
  }
);
</script>

<style lang="scss" scoped>
.default-header {
  position: relative;
  @include z-index(4);

  height: 280px;

  &.extends {
    margin-bottom: 150vh;
  }

  &__content {
    height: 100vh;
    overflow-x: hidden !important;

    // pointer-events: none;
    @include scrollbar($body-scrollbar-width);

    & > * {
      pointer-events: all;
    }
  }

  &__main {
    position: relative;
    @include z-index(3);

    width: 100vw;
    padding-bottom: 50px;
    padding-left: 70px;

    background-color: $main-bg-color;
    box-shadow: 0 4px 94px 0 rgba(0, 0, 0, 0.45);

    &.min {
      padding-bottom: 20px;

      transition: padding $tr-dur;
    }
  }

  &__first-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;

    padding-top: 44px;
    padding-right: 58px;
  }

  &__title {
    max-width: 600px;
    height: 235px;
    overflow: hidden;

    font-family: $text-font-family;
    font-size: 85px;
    line-height: 72px;
    font-weight: 500;
    color: $primary-color;
    text-transform: uppercase;
    letter-spacing: 0.85px;

    transform: translate3d(0, 0, 0);
    will-change: height;

    &-content {
      box-sizing: content-box;

      padding-top: 40px;
    }

    span {
      color: $accent-color;
    }

    &.hide {
      height: 17px;

      opacity: 0;
      transition: height $tr-dur, opacity $tr-dur;
    }

    &.min {
      height: auto;
      margin-top: 1px;
      margin-left: -16px;
      padding-top: 0;

      font-size: 22px;
      line-height: 20px;
      letter-spacing: 0;
    }
  }

  &__second-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;

    min-height: 135px;
  }

  &__text {
    display: flex;
    align-items: center;

    max-width: 646px;
    margin-top: 21px;
    margin-right: 9%;
    margin-left: 20px;

    font-family: $secondary-font-family;
    font-size: 27px;
    line-height: 28px;
    text-transform: uppercase;

    &.min {
      margin-top: 4px;
    }

    p {
      margin-left: 22px;
    }
  }

  &__modal {
    padding: 15px 0;

    background: rgba(19, 37, 72, 0.8);
  }

  &__specialities {
    max-width: 837px;
    margin: 0 auto;

    background: rgba(19, 37, 72, 0.5);
    border: 2px solid $border-radius;
    border-radius: 40px;
    box-shadow: 0 0 70px 0 #00153e;

    backdrop-filter: blur(8px);
  }

  @include xl-and-down {
    &__text {
      max-width: 520px;
      margin-right: 4%;

      font-size: 21px;
      line-height: 22px;
    }
  }

  @include lg-and-down {
    &__main {
      padding-left: 40px;
    }

    &__title {
      &.min {
        margin-left: -20px;
      }
    }

    &__text {
      max-width: 380px;
      margin-right: 10px;

      font-size: 19px;
      line-height: 20px;

      img {
        width: 90px;
      }

      p {
        margin-left: 10px;
      }
    }
  }
}
</style>
