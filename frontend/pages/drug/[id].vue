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
          v-for="item in content.faq"
          :key="item.order"
          ref="itemsEls"
          class="drug-page__right-item"
          :class="{ expanded: activeItem?.order === item.order }"
          @click="openProps(item)"
        >
          <div class="drug-page__right-item-title">
            {{ item.title }}

            <AppIcon size="15" class="for-mobile-or-tablet" :name="IconName.DropIcon" />
          </div>
          <div class="drug-page__right-item-content for-mobile-or-tablet">
            <p v-html="item.text" />
          </div>
        </div>
        <AppButton
          v-if="content.file_field"
          class="drug-page__right-btn"
          target="_blank"
          :to="`${baseUrl}${content.file_field}`"
          :petite="$screen.mdAndDown"
        >
          Инструкция
        </AppButton>
        <AppButton
          v-else-if="content.url_field"
          class="drug-page__right-btn"
          target="_blank"
          :to="content.url_field"
          :petite="$screen.mdAndDown"
        >
          Инструкция
        </AppButton>
        <div v-if="content.application_practices.length" class="drug-page__slider">
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
                <SwiperSlide v-for="item in content.application_practices" :key="item.id">
                  <nuxt-link
                    class="drug-page__slider-item"
                    :to="item.type === 'video' ? `/video/${item.id}` : `/article/${item.id}`"
                  >
                    <img
                      v-if="item.image"
                      onerror="this.style.display = 'none'"
                      class="drug-page__slider-item-bg"
                      :src="`${baseUrl}${item.image}`"
                    />
                    <p>{{ item.name }}</p>
                  </nuxt-link>
                </SwiperSlide>
              </Swiper>
              <div ref="nextRef" class="swiper-button next">
                <AppIcon :name="IconName.NextSliderBtnBig" :size="51" />
              </div>
              <div ref="prevRef" class="swiper-button prev">
                <AppIcon :name="IconName.PrevSliderBtnBig" :size="51" />
              </div>
            </template>

            <ItemsSlider
              v-else-if="content.application_practices.length"
              :desktop-slides-per-view="2"
              :items="content.application_practices"
              #default="{ item }"
            >
              <nuxt-link
                :to="item.type === 'video' ? `/video/${item.id}` : `/article/${item.id}`"
                class="drug-page__slider-item"
              >
                <img
                  v-if="item.image"
                  onerror="this.style.display = 'none'"
                  class="drug-page__slider-item-bg"
                  :src="`${baseUrl}${item.image}`"
                />
                <p v-html="item.name" />
              </nuxt-link>
            </ItemsSlider>
          </div>
        </div>
      </div>
    </div>

    <AppModal :name="ModalsName.DrugProps" :on-close="onModalClose">
      <div v-if="activeItem" class="drug-page__modal">
        <div class="drug-page__modal-title">
          {{ activeItem.title }}
        </div>
        <div class="drug-page__modal-text" v-html="activeItem.text" />
        <!--        <div class="drug-page__modal-description">
          <p v-html="activeItem.description" />
          <AppButton primary mini @click="openProps(list[1])"> Противопоказания </AppButton>
        </div>-->
      </div>
    </AppModal>
    <Teleport to="#footerAccessInfo">
      <p v-html="content.approvals_and_decodings"></p>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { Navigation } from 'swiper/modules';
import { useRoute } from '#app';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { IconName } from '~/components/app/AppIcon.utils';
import { DrugFaq, DrugPlump, useDrugsStore } from '~/utils/composables/store/drugs';
import { ModalsName, useModal } from '~/utils/composables/useModal';
import { useScreen } from '~/utils/composables/useScreen';
import BgEllipse from '~/components/common/BgEllipse.vue';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import { ArticlePlump } from '~/utils/composables/store/articles';

const nextRef = ref(null);
const prevRef = ref(null);

const $route = useRoute();
const { baseUrl } = useRuntimeConfig().public;
const drugId = toRef(() => +$route.params.id);

const { openModal } = useModal();
const { $screen } = useScreen();

const { getDrug } = useDrugsStore();

const content = await getDrug(drugId.value);

const activeItem = ref<DrugFaq>();
const itemsEls = ref();

const onModalClose = () => {
  activeItem.value = undefined;
};

const openProps = (item: DrugFaq) => {
  if (activeItem.value?.order === item.order) {
    activeItem.value = undefined;
  } else {
    activeItem.value = item;
  }

  if (!$screen.value.mdAndDown) {
    openModal(ModalsName.DrugProps);
  } else {
    itemsEls.value.forEach((el: HTMLElement) => {
      const content = el.querySelector('.drug-page__right-item-content') as HTMLElement;
      if (content) {
        content.style.height = `0`;
      }
    });

    const activeIndex = content?.faq.findIndex((el) => el.order === activeItem.value?.order);

    if ((activeIndex || activeIndex === 0) && activeIndex >= 0 && itemsEls.value[activeIndex]) {
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
      max-height: 500px;
      object-fit: contain;
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

      p {
        position: relative;
        z-index: 2;
      }

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
      position: relative;

      display: block;

      padding: 64px 30px 64px 64px;
      overflow: hidden;
      @include aspect(1, 1);

      font-size: 32px;
      line-height: 30px;
      word-break: break-word;

      background: conic-gradient(
        from 164deg at 50% 50%,
        #e130ff 8.287965506315231deg,
        #002f75 180deg,
        #00d1ff 350.40282011032104deg
      );
      border-radius: 40px;

      &:after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        z-index: 1;

        background-color: rgba(#000, 0.3);
      }

      &-bg {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;

        display: block;

        width: 100%;
        height: 100%;
        object-fit: cover;

        transition: transform $tr-dur;
      }

      p {
        position: relative;
        z-index: 2;
      }

      @include hover {
        .drug-page__slider-item-bg {
          transform: scale(1.05);
        }
      }
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
    padding: 35px 27px 10px;

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

        width: 72%;
        margin: 20px auto 0;
      }

      &-icons {
        max-width: 500px;
        margin: -24px auto 0;
        padding: 0 28px;

        img {
          width: 18%;
        }
      }
    }

    &__right {
      width: 100%;
      margin-top: 16px;

      &-item {
        padding: 12px 0;

        &:first-of-type {
          border-top: 1px solid $primary-color;
        }

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
