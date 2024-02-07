<template>
  <InsidePageHead />
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
        <AppImage
          responsiveHeight
          :url="content.image_desktop_700px"
          :url-full="content.image_desktop_700px"
          :url-full-x2="content.image_desktop_1400px"
          :url-thin-x2="content.image_mobile_540px"
          :url-thin="content.image_mobile_270px"
        />

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
        <Accordion :items="content.faq" :modalName="ModalsName.DrugProps" />
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
                    <AppImage
                      class="drug-page__slider-item-bg"
                      :url="item.practic_desktop_400px"
                      :url-full-x2="item.practic_desktop_800px"
                      :url-full="item.practic_desktop_400px"
                      :url-thin-x2="item.practic_mobile_560px"
                      :url-thin="item.practic_mobile_280px"
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
                <AppImage
                  class="drug-page__slider-item-bg"
                  :url="item.practic_desktop_400px"
                  :url-full-x2="item.practic_desktop_800px"
                  :url-full="item.practic_desktop_400px"
                  :url-thin-x2="item.practic_mobile_560px"
                  :url-thin="item.practic_mobile_280px"
                />
                <p v-html="item.name" />
              </nuxt-link>
            </ItemsSlider>
          </div>
        </div>
      </div>
    </div>

    <AppModal :name="ModalsName.DrugProps">
      <div v-if="activeItem" class="drug-page__modal">
        <div class="drug-page__modal-title">
          {{ activeItem.title }}
        </div>
        <div class="drug-page__modal-text" v-html="activeItem.text" />
        <div class="drug-page__modal-description">
          <p
            v-if="activeItem.approvals_and_decodings"
            v-html="activeItem.approvals_and_decodings"
          />
          <AppButton
            v-if="nextItem && content.faq.length > 1"
            class="drug-page__modal-description-btn"
            primary
            mini
            @click="openProps(nextItem)"
          >
            {{ nextItem.title }}
          </AppButton>
        </div>
      </div>
    </AppModal>
    <Teleport to="#footerAccessInfo">
      <p v-html="content.approvals_and_decodings"></p>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute } from '#app';
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { IconName } from '~/components/app/AppIcon.utils';
import { DrugFaq, useDrugsStore } from '~/utils/composables/store/drugs';
import { ModalsName, useModal } from '~/utils/composables/useModal';
import { useScreen } from '~/utils/composables/useScreen';
import BgEllipse from '~/components/common/BgEllipse.vue';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import Accordion from '~/components/common/Accordion.vue';
import InsidePageHead from '~/components/common/InsidePageHead.vue';

const nextRef = ref(null);
const prevRef = ref(null);

const $route = useRoute();
const { baseUrl } = useRuntimeConfig().public;
const drugId = toRef(() => +$route.params.id);

const { getModalPayload, setModalPayload } = useModal();
const { $screen } = useScreen();

const { getDrug } = useDrugsStore();

const content = await getDrug(drugId.value);

const activeItem = toRef(() => getModalPayload(ModalsName.DrugProps).item);

const nextItem = toRef(() => {
  if (!content) {
    return 0;
  }

  const index = content?.faq.findIndex((f) => f.order === activeItem.value?.order);

  if (index !== content?.faq.length - 1) {
    return content?.faq[index + 1];
  } else {
    return content?.faq[0];
  }
});

useHead({
  title: content?.name ? content?.name : 'Препараты',
});

const openProps = (item: DrugFaq) => {
  setModalPayload(ModalsName.DrugProps, { item: item, items: content.faq });
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

    :deep(img) {
      width: 100%;
      max-height: 500px;
      object-fit: contain;
      @include aspect(673, 628);
    }

    &-icons {
      display: flex;
      justify-content: space-between;

      margin-top: 10px;
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

        background-color: rgba(#000, 0.4);
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

        @include ellipsis(6);
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
        margin-right: 10px;

        font-size: 14px;
        line-height: 18px;
        color: $primary-color;
      }

      &-btn {
        margin-left: auto;
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

        p {
          line-height: 1.05;
        }
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
