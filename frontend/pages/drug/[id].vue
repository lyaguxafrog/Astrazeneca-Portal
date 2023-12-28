<template>
  <div v-if="content" class="drug-page">
    <BgEllipse
      :size="$screen.mdAndDown ? 290 : 1138"
      color="#4DDFFF"
      :pale="!$screen.mdAndDown"
      class="drug-page__first-ellipse"
    />
    <BgEllipse size="984" color="#B32FC9" pale class="drug-page__second-ellipse for-desktop" />
    <div class="drug-page__title">
      <b>{{ content.name }}</b> <small>{{ content.brief_info }}</small>
    </div>
    <div class="drug-page__content">
      <div class="drug-page__left">
        <img :src="`${baseUrl}${content.image}`" alt="" />

        <div class="drug-page__left-icons">
          <img
            v-for="icon in content.icons"
            :key="icon.id"
            :src="`${baseUrl}${icon.image_file}`"
            alt=""
          />
        </div>
      </div>

      <div class="drug-page__right">
        <div
          v-for="item in list"
          :key="item.id"
          ref="itemsEls"
          class="drug-page__right-item"
          :class="{ expanded: activeItem?.id === item.id }"
          @click="openProps(item)"
        >
          <div class="drug-page__right-item-title">
            {{ item.name }}

            <AppIcon size="15" class="for-mobile-or-tablet" :name="IconName.DropIcon" />
          </div>
          <div class="drug-page__right-item-content for-mobile-or-tablet">
            <p>
              {{ item.text }}
            </p>
          </div>
        </div>
        <AppButton class="drug-page__right-btn" :petite="$screen.mdAndDown"> Инструкция </AppButton>
        <div class="drug-page__slider">
          <div class="drug-page__slider-title">Практика применения</div>

          <div class="drug-page__slider-wrapper">
            <template v-if="!$screen.mdAndDown">
              <Swiper
                :modules="[Navigation]"
                :navigation="{
                  nextEl: nextRef,
                  prevEl: prevRef,
                }"
                :slides-per-view="2"
                :space-between="40"
              >
                <SwiperSlide v-for="item in slides" :key="item.id">
                  <div class="drug-page__slider-item">
                    <p>{{ item.name }}</p>
                  </div>
                </SwiperSlide>
              </Swiper>
              <div ref="nextRef" class="swiper-button next">
                <AppIcon :name="IconName.NextSliderBtnBig" :size="51" />
              </div>
              <div ref="prevRef" class="swiper-button prev">
                <AppIcon :name="IconName.PrevSliderBtnBig" :size="51" />
              </div>
            </template>

            <ItemsSlider v-else :desktop-slides-per-view="2" :items="slides" #default="{ item }">
              <div class="drug-page__slider-item">
                <p v-html="item.name" />
              </div>
            </ItemsSlider>
          </div>
        </div>
      </div>
    </div>

    <AppModal :name="ModalsName.DrugProps">
      <div class="drug-page__modal">
        <div class="drug-page__modal-title">
          {{ activeItem.name }}
        </div>
        <div class="drug-page__modal-text">
          {{ activeItem.text }}
        </div>
        <div class="drug-page__modal-description">
          <p v-html="activeItem.description" />
          <AppButton primary mini @click="openProps(list[1])"> Противопоказания </AppButton>
        </div>
      </div>
    </AppModal>
  </div>
</template>

<script setup lang="ts">
import { Navigation } from 'swiper/modules';
import { useRoute } from '#app';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { IconName } from '~/components/app/AppIcon.utils';
import { useDrugsStore } from '~/utils/composables/store/drugs';
import { ModalsName, useModal } from '~/utils/composables/useModal';
import { useScreen } from '~/utils/composables/useScreen';
import BgEllipse from '~/components/common/BgEllipse.vue';
import ItemsSlider from '~/components/common/ItemsSlider.vue';

const nextRef = ref(null);
const prevRef = ref(null);

const $route = useRoute();
const { baseUrl } = useRuntimeConfig().public;
const drugId = toRef(() => +$route.params.id);

const { openModal } = useModal();
const { $screen } = useScreen();

const { getDrug } = useDrugsStore();

const content = await getDrug(drugId.value);

const list = [
  {
    id: '1',
    name: 'Показания к применению',
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    description:
      'Место под расшифровки<br>Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ',
  },
  {
    id: '2',
    name: 'Противопоказания',
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    description:
      'Место под расшифровки<br>Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ',
  },
  {
    id: '3',
    name: 'Противопоказания',
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    description:
      'Место под расшифровки<br>Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ',
  },
  {
    id: '4',
    name: 'Противопоказания',
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    description:
      'Место под расшифровки<br>Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ',
  },
  {
    id: '5',
    name: 'Противопоказания',
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    description:
      'Место под расшифровки<br>Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ',
  },
  {
    id: '6',
    name: 'Противопоказания',
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    description:
      'Место под расшифровки<br>Номера одобрения: ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ, ХХХХХХХХ',
  },
];

const activeItem = ref();
const itemsEls = ref();
const openProps = (item) => {
  if (activeItem.value?.id === item.id) {
    activeItem.value = undefined;
  } else {
    activeItem.value = item;
  }

  if (!$screen.value.mdAndDown) {
    openModal(ModalsName.DrugProps);
  } else {
    itemsEls.value.forEach((el) => {
      const content = el.querySelector('.drug-page__right-item-content');

      content.style.height = `0`;
    });

    const activeIndex = list.findIndex((el) => el.id === activeItem.value?.id);

    if (activeIndex >= 0 && itemsEls.value[activeIndex]) {
      const content = itemsEls.value[activeIndex].querySelector('.drug-page__right-item-content');

      const height = content.scrollHeight;

      content.style.height = `${height}px`;
    }
  }
};
</script>

<style scoped lang="scss">
.drug-page {
  position: relative;

  padding: 44px 90px;

  &__first-ellipse {
    top: 10px;
    left: -750px;
  }
  &__second-ellipse {
    top: 270px;
    right: -590px;
  }

  &__title {
    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 28px;
    font-weight: 900;

    b {
      text-transform: uppercase;
    }

    small {
      display: block;

      margin-top: 14px;

      font-size: 30px;
      line-height: 35px;
      font-weight: 400;
    }
  }

  &__content {
    display: flex;
  }

  &__left {
    width: 38.7%;
    margin-top: 79px;

    img {
      width: 100%;
    }

    &-icons {
      display: flex;
      justify-content: space-between;

      margin-top: -3px;
      padding: 0 51px 0 5px;
      img {
        width: 20%;
      }
    }
  }

  &__right {
    width: 46.2%;
    margin-top: 20px;
    margin-left: 4.9%;

    &-item {
      padding: 25px 0;

      font-size: 24px;
      line-height: 24px;
      font-weight: 300;
      color: $primary-color;

      border-bottom: 1px solid $primary-color;

      cursor: pointer;
      transition: color $tr-dur;

      @include hover {
        color: $white-color;
      }
    }

    &-btn {
      width: 315px;
      margin-top: 42px;
    }
  }

  &__slider {
    margin-top: 66px;

    &-wrapper {
      position: relative;
    }

    &-title {
      margin-bottom: 30px;

      font-family: $secondary-font-family;
      font-size: 34px;
      font-weight: 900;
    }

    &-item {
      padding: 64px;
      aspect-ratio: 1;

      font-size: 32px;
      line-height: 30px;

      background: url('~/assets/img/drug/bg.png') no-repeat center center / cover;
      border-radius: 40px;
    }

    .swiper-button {
      position: absolute;
      top: 50%;
      left: -120px;

      transform: translateY(-50%);

      &.next {
        right: -120px;
        left: auto;
      }
    }
  }

  &__modal {
    &-title {
      margin-bottom: 46px;

      font-family: $secondary-font-family;
      font-size: 32px;
      line-height: 21px;
      font-weight: 900;
    }

    &-text {
      font-size: 20px;
      line-height: 24px;
      font-weight: 300;
    }

    &-description {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;

      margin-top: 40px;

      p {
        font-size: 14px;
        line-height: 18px;
        color: $primary-color;
      }
    }
  }

  @include lg-and-down {
    padding: 30px 40px;

    &__right {
      width: 60%;
      margin-left: 0;
    }

    &__slider {
      &-item {
        padding: 40px;
      }

      .swiper-button {
        left: -60px;

        &.next {
          right: -50px;
        }
      }
    }
  }

  @include md-and-down {
    padding: 35px 27px;

    &__first-ellipse {
      top: 70px;
      right: -220px;
      left: auto;
    }

    &__title {
      font-size: 27px;
      small {
        width: 90%;
        margin-top: -1px;

        font-size: 15px;
        line-height: 20px;
      }
    }

    &__content {
      flex-direction: column;
    }

    &__left {
      width: 100%;
      margin-top: 3px;

      img {
        display: block;

        width: 60%;
        margin: 0 auto;
      }

      &-icons {
        margin-top: -7px;
        padding: 0 28px;

        img {
          width: 18%;
        }
      }
    }

    &__right {
      width: 100%;
      margin-top: 16px;

      border-top: 1px solid $primary-color;

      &-item {
        padding: 12px 0;
        &-title {
          display: flex;
          justify-content: space-between;
          align-items: center;

          font-size: 16px;
        }

        .app-icon {
          transition: transform $tr-dur;
        }

        &.expanded {
          font-weight: 700;
          letter-spacing: -0.32px;

          .app-icon {
            transform: rotate(180deg);
          }
        }

        &-content {
          height: 0;
          overflow: hidden;

          font-size: 14px;
          line-height: 18px;
          font-weight: 300;
          color: $white-color;
          letter-spacing: -0.28px;

          transition: height $tr-dur;

          p {
            padding-top: 14px;
            padding-right: 15px;
          }
        }
      }

      &-btn {
        width: 164px;
        margin-top: 72px;
      }
    }

    &__slider {
      margin-top: 46px;
      &-wrapper {
        margin: -4px -27px;
      }

      &-item {
        padding: 46px 33px;

        font-size: 22px;
        line-height: 21px;

        border-radius: 20px;
      }

      &-title {
        width: 50%;

        font-size: 22px;
        line-height: 21px;
      }
    }
  }
}
</style>
