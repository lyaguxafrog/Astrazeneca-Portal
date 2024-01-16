<template>
  <div v-if="articles.data?.length" class="articles">
    <div class="articles__title">
      Статьи
    </div>
    <BgEllipse size="1138" color="#4DDFFF" pale class="articles__first-ellipse" />
    <BgEllipse
      :size="!$screen.mdAndDown ? 984 : 306"
      color="#B32FC9"
      :pale="!$screen.mdAndDown"
      class="articles__second-ellipse"
    />

    <div v-for="(slide, index) in articles.data" v-show="activeSlide === index" class="articles__slide-title for-mobile-or-tablet">
      <div v-if="!slide.center_title">
        {{ slide.article_name }}
      </div>
    </div>

    <ItemsSlider
      disable-loop
      :items="articles.data"
      :desktop-slides-per-view="1.7"
      @onSlideChange="onSlideChange"
    >
      <template #default="{ item }">
        <nuxt-link class="articles__slide" :to="`/article/${item.id}`">
          <div
            class="articles__slide-title for-desktop items-slier__visible-on-active"
            v-html="!item.center_title ? item.article_name : ''"
          />
          <div class="articles__slide-image-wrapper" :class="{withBefore: item.center_title}">
            <div
              v-if="item.center_title"
              class="articles__slide-title items-slier__visible-on-active"
              v-html="item.article_name"
            />
            <AppImage
              class="articles__slide-image"
              :url="item.cover_desktop_1400px"
              :url-full-x2="item.cover_desktop_2800px"
              :url-full="item.cover_desktop_1400px"
              :url-thin-x2="item.cover_mobile_840px"
              :url-thin="item.cover_mobile_420px"
            />
          </div>
          <p class="for-desktop" v-html="item.information" />
        </nuxt-link>
      </template>
    </ItemsSlider>

    <p
      v-for="(slide, index) in articles.data" v-show="activeSlide === index"
      class="for-mobile-or-tablet"
      v-html="slide.information"
    />
  </div>
</template>

<script lang="ts" setup>
import { useRuntimeConfig } from '#app';
import { ref, toRef } from 'vue';
import { useScreen } from '~/utils/composables/useScreen';
import { useArticlesStore } from '~/utils/composables/store/articles';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';

const emit = defineEmits<{
  (event: 'showAll'): void;
}>();

const { $screen } = useScreen();
const { getArticles, articles } = useArticlesStore();
const { baseUrl } = useRuntimeConfig().public;

await getArticles();

const activeSlide = ref(1);
const activeSlideContent = toRef(() => articles.value.data?.[activeSlide.value]);
const onSlideChange = (index: number | undefined) => {
  if (index !== undefined) {
    setTimeout(() => {
      activeSlide.value = index;
    });
  }

  if (index === articles.value.data?.length - 1) {
    emit('showAll');
  }
};
</script>

<style lang="scss" scoped>
.articles {
  position: relative;

  margin-top: 100px;
  padding-bottom: 40px;

  &__title {
    margin-bottom: 50px;
    margin-left: 96px;

    font-family: $secondary-font-family;
    font-size: 50px;
    font-weight: 900;
    text-transform: uppercase;
  }

  &__first-ellipse {
    top: -100px;
    left: -840px;
  }

  &__second-ellipse {
    top: 0;
    right: -570px;
    left: auto;
  }

  &::v-deep {
    .swiper-slide {
      &:not(.swiper-slide-active) {
        p {
          opacity: 0.5;
        }
      }
    }
  }

  &__slide {
    display: flex;
    flex-direction: column;

    height: 100%;

    @include hover {
      .articles__slide-image {
        &:deep(img) {
          transform: scale(1.05);
        }
      }
    }

    &-title {
      min-height: 76px;
      margin-bottom: 28px;

      font-family: $secondary-font-family;
      font-size: 40px;
      line-height: 38px;

      transition: color $tr-dur;
      will-change: display;
    }
    &-image {
      &:deep(img) {
        width: 100%;
        height: 100%;
        object-fit: cover;

        transition: transform $tr-dur;
      }

      &-wrapper {
        position: relative;

        width: 100%;
        height: 530px;
        // margin-top: auto;
        overflow: hidden;

        border-radius: 40px;

        .articles__slide-title {
          position: absolute;
          top: 50%;
          @include z-index(2);

          min-height: initial;
          padding-left: 40px;

          transform: translateY(-50%);
        }

        &.withBefore {
          &:before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            z-index: 1;

            background-color: rgba(#000, 0.4);
          }
        }
      }
    }

    p {
      margin-top: 43px;

      font-size: 24px;
      line-height: 28px;
      word-break: break-word;
      @include ellipsis(5);

      transition: opacity $tr-dur;
      will-change: display;
    }
  }

  @include lg-and-down {
    &__slide {
      &-title {
        min-height: 114px;
      }
    }
  }

  @include md-and-down {
    &__title {
      margin-bottom: 30px;
      margin-left: 25px;

      font-size: 36px;
    }
    &__slide {
      &-title {
        min-height: 92px;
        padding: 0 27px 2px;

        font-size: 27px;
        line-height: 30px;
        font-weight: 900;
      }
      &-image-wrapper {
        height: auto;

        border-radius: 20px;

        @include aspect(1,1);

        .articles__slide-title {
          padding: 4px;

          font-size: 22px;
          line-height: 24px;
          font-weight: 400;
          text-align: center;
          word-break: break-word;
        }
      }
    }
    p {
      margin-top: 20px;
      padding: 0 27px;

      font-size: 14px;
      line-height: 16px;
      @include ellipsis(7);
    }
  }
}
</style>
