<template>
  <div class="home-practicum">
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

    <div class="home-practicum__title">практикум</div>
    <div class="home-practicum__subtitle">Интерактивный клинический случай</div>

    <div class="home-practicum__slider">
      <Swiper
        :modules="[Navigation]"
        :navigation="{
          nextEl: nextRef,
          prevEl: prevRef,
        }"
      >
        <SwiperSlide v-for="practicum in content" :key="practicum.id" class="home-practicum__item">
          <img :src="practicum.img" alt="" />
          <p v-html="practicum.text" />
          <AppButton primary class="home-practicum__item-button" :to="`/practicum/${practicum.id}`">
            Начать
          </AppButton>
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
import { ref } from 'vue';
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();

const nextRef = ref(null);
const prevRef = ref(null);

const content = [
  {
    id: '1',
    img: '/img/p1.png',
    text: 'Пациент, 52 года, обратился с жалобой <b>на кашель, одышку, боли в груди и кровохарканье</b>. Ознакомьтесь с данными исследований и определите верный диагноз.',
  },
  {
    id: '2',
    img: '/img/p2.png',
    text: 'Пациент, 52 года, обратился с жалобой <b>на кашель, одышку, боли в груди и кровохарканье</b>. Ознакомьтесь с данными исследований и определите верный диагноз.',
  },
  {
    id: '3',
    img: '/img/p3.png',
    text: 'Пациент, 52 года, обратился с жалобой <b>на кашель, одышку, боли в груди и кровохарканье</b>. Ознакомьтесь с данными исследований и определите верный диагноз.',
  },
];
</script>

<style scoped lang="scss">
.home-practicum {
  position: relative;

  margin-top: 30px;

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

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 28px;
    font-weight: 900;
    text-transform: uppercase;
  }

  &__subtitle {
    width: 70%;
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
    img {
      display: block;

      width: 818px;
      max-width: 60%;
      margin: 0 auto;
      object-fit: contain;
    }

    p {
      max-width: 845px;
      margin: -53px auto 0;

      font-size: 36px;
      line-height: 42px;
      font-weight: 300;

      :deep(b) {
        font-weight: 700;
      }
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

      font-size: 22px;
      line-height: 28px;
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
        width: auto;
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
