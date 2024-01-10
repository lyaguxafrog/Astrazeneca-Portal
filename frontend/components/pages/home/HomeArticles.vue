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

    <div v-if="activeSlideContent" class="articles__slide-title for-mobile-or-tablet">
      {{ activeSlideContent.article_name }}
    </div>

    <ItemsSlider
      :items="articles.data"
      :desktop-slides-per-view="1.7"
      @onSlideChange="onSlideChange"
    >
      <template #default="{ item }">
        <nuxt-link class="articles__slide" :to="`/article/${item.id}`">
          <div
            class="articles__slide-title for-desktop items-slier__visible-on-active"
            v-html="item.article_name"
          />
          <div class="articles__slide-image-wrapper">
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
      v-if="activeSlideContent"
      class="for-mobile-or-tablet"
      v-html="activeSlideContent.information"
    />
  </div>
</template>

<script lang="ts" setup>
import { useScreen } from '~/utils/composables/useScreen';
import { useArticlesStore } from '~/utils/composables/store/articles';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';

const { $screen } = useScreen();
const { getArticles, articles } = useArticlesStore();
const { baseUrl } = useRuntimeConfig().public;

await getArticles();

const activeSlide = ref(1);
const activeSlideContent = toRef(() => articles.value.data?.[activeSlide.value]);
const onSlideChange = (index: number | undefined) => {
  if (index !== undefined) {
    activeSlide.value = index;
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
      @include ellipsis(2);

      transition: color $tr-dur;
    }
    &-image {
      &:deep(img) {
        width: 100%;
        height: 100%;
        object-fit: cover;

        transition: transform $tr-dur;
      }

      &-wrapper {
        width: 100%;
        height: 530px;
        // margin-top: auto;
        overflow: hidden;

        border-radius: 40px;
      }
    }

    p {
      margin-top: 43px;

      font-size: 24px;
      line-height: 28px;
      word-break: break-word;
      @include ellipsis(5);

      transition: opacity $tr-dur;
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
        min-height: auto;
        padding: 0 27px 2px;

        font-size: 27px;
        line-height: 30px;
        font-weight: 900;
        @include ellipsis(4);
      }
      &-image-wrapper {
        height: auto;

        @include aspect(1,1);
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
