<template>
  <div v-if="drugs?.length" class="home-drugs">
    <BgEllipse
      class="home-drugs__first-ellipse"
      color="#00C2FF"
      pale
      :size="$screen.mdAndDown ? 230 : 684"
    />
    <BgEllipse
      class="home-drugs__second-ellipse"
      color="#B32FC9"
      :size="$screen.mdAndDown ? 306 : 1300"
    />

    <div class="home-drugs__title">Препараты</div>

    <ItemsSlider
      :withNavigation="!$screen.mdAndDown"
      :items="drugs"
      :desktop-slides-per-view="1"
      :mobile-slides-per-view="1"
      :initial-slide="0"
      :hide-pagination="!$screen.mdAndDown"
      #default="{ item }"
    >
      <nuxt-link class="home-drugs__item link" :to="`/drug/${item.id}`">
        <AppImage :url="item.image" :url-full="item.image" :url-full-x2="item.image" />
        <div class="home-drugs__item-link">Узнать подробнее</div>
        <div class="swiper-lazy-preloader" />
      </nuxt-link>
    </ItemsSlider>
  </div>
</template>

<script setup lang="ts">
import { useScreen } from '~/utils/composables/useScreen';
import { useDrugsStore } from '~/utils/composables/store/drugs';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();
const { getDrugs } = useDrugsStore();
const { baseUrl } = useRuntimeConfig().public;

const drugs = await getDrugs();
</script>

<style scoped lang="scss">
.home-drugs {
  position: relative;

  margin-top: 72px;

  &__first-ellipse {
    top: 50px;
    left: 50%;

    transform: translateX(-50%);
  }
  &__second-ellipse {
    top: -150px;
    right: -1100px;
    @include z-index(2);
  }

  &__title {
    margin-bottom: 103px;
    padding-left: 93px;

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 28px;
    font-weight: 900;
    text-transform: uppercase;
  }

  &__item {
    display: block;

    width: 40vw;
    min-width: 500px;
    max-width: 690px;
    margin: 13px auto;

    img {
      width: 100%;
      max-height: 550px;
      object-fit: contain;
    }

    &-link {
      display: block;

      margin-top: 59px;

      font-size: 40px;
      text-align: center;
      letter-spacing: -0.8px;
    }
  }

  @include md-and-down {
    margin-top: 122px;

    &__first-ellipse {
      top: 100px;
    }
    &__second-ellipse {
      top: -180px;
      right: -210px;
    }

    &__title {
      margin-bottom: 43px;
      padding-left: 26px;

      font-size: 27px;
      line-height: 28px;
    }

    &__item {
      width: 62%;
      min-width: initial;
      margin: 13px auto;

      &-link {
        margin-top: 12px;

        font-size: 14px;
        letter-spacing: initial;
      }
    }
  }
}
</style>
