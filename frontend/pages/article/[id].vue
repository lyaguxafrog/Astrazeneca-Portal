<template>
  <InsidePageHead />
  <div v-if="content" class="article-page">
    <BgEllipse size="1138" color="#4DDFFF" pale class="article-page__first-ellipse" />
    <BgEllipse
      :size="!$screen.mdAndDown ? 984 : 306"
      color="#B32FC9"
      :pale="!$screen.mdAndDown"
      class="article-page__second-ellipse"
    />

    <div class="article-page__title">
      <span>PRO</span>терапию
      <small>рака легкого</small>
    </div>

    <div class="article-page__intro">{{ content.article_name }}</div>

    <div class="article-page__bold">
      Первый абзац текста, краткое содержание и ключевая идея текста в одно-два предложения. Первый
      абзац текста, краткое содержание и ключевая идея текста в одно-два предложения.
    </div>

    <template v-for="block in content.content_blocks">
      <div
        v-if="block.content_type === 'text'"
        :key="block.id"
        class="article-page__text"
        v-html="block.text"
      />

      <div v-if="block.content_type === 'quote'" :key="block.id" class="article-page__quote">
        <div class="article-page__quote-text" v-html="block.text" />
        <img :src="`${baseUrl}${block.image}`" alt="" />
      </div>

      <div v-if="block.content_type === 'text_with_image'" class="article-page__image-and-text">
        <img :src="`${baseUrl}${block.image}`" />
        <span v-html="block.text" />
      </div>
    </template>
    <div
      v-if="content.final_content"
      class="article-page__description"
      v-html="content.final_content"
    />

    <Teleport to="#footerAccessInfo">
      <div v-html="content.access_number" />
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from '#app';
import { useArticlesStore } from '~/utils/composables/store/articles';
import { useScreen } from '~/utils/composables/useScreen';
import InsidePageHead from '~/components/common/InsidePageHead.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';

const $route = useRoute();
const { $screen } = useScreen();
const { getArticle } = useArticlesStore();
const { baseUrl } = useRuntimeConfig().public;

const articleId = toRef(() => +$route.params.id);

const content = await getArticle(articleId.value);
</script>

<style scoped lang="scss">
.article-page {
  position: relative;

  padding: 9px 92px 100px;

  &__first-ellipse {
    top: -150px;
    left: -840px;
  }

  &__second-ellipse {
    top: 0;
    right: -570px;
    left: auto;
  }

  &__title {
    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 28px;
    font-weight: 900;
    color: $primary-color;
    text-transform: uppercase;
    span {
      color: $accent-color;
    }
    small {
      display: block;

      margin-top: 17px;

      font-size: 30px;
      line-height: 44px;
      font-weight: 400;
    }
  }

  &__intro {
    min-height: 436px;
    margin-top: 31px;
    margin-bottom: 54px;
    padding: 70px 270px 0 89px;

    font-family: $secondary-font-family;
    font-size: 60px;
    line-height: 48px;
    font-weight: 900;

    background: url('~/assets/img/article/bg.png') no-repeat center center / cover;
    border-radius: 40px;
  }

  &__bold {
    font-family: $secondary-font-family;
    font-size: 32px;
    line-height: 36px;
    font-weight: 900;
  }

  &__text {
    margin-top: 29px;

    font-size: 24px;
    line-height: 32px;
    letter-spacing: -0.24px;

    &::v-deep {
      b,
      strong {
        font-weight: 700;
      }
    }
  }

  a {
    color: $primary-color;

    @include hover {
      text-decoration: underline;
    }
  }

  &__quote {
    display: flex;
    justify-content: flex-end;
    align-items: flex-start;

    margin-top: 8px;

    &-text {
      position: relative;

      width: 53.1%;
      margin-top: 76px;
      margin-right: 9.9%;
      margin-bottom: 64px;

      font-size: 30px;
      line-height: 34px;
      color: $primary-color;
      font-style: italic;
      letter-spacing: -0.3px;

      &:before,
      &:after {
        content: '';
        position: absolute;
        top: -39px;
        left: -122px;

        width: 66px;
        height: 66px;

        background: url('~/assets/img/article/quota.svg') no-repeat center center / contain;
      }

      &:after {
        top: auto;
        right: -60px;
        bottom: -62px;
        left: auto;

        background-image: url('~/assets/img/article/quota-2.svg');
      }
    }

    img {
      width: 302px;

      border-radius: 50%;
    }
  }

  &__image-and-text {
    font-size: 24px;
    line-height: 32px;
    letter-spacing: -0.24px;

    img {
      float: left;

      width: 245px;
      margin-top: -17px;
      margin-right: 55px;
    }
  }

  &__description {
    max-width: 1100px;
    margin-top: 79px;

    font-size: 18px;
    line-height: 19px;
    font-weight: 300;
  }

  @include lg-and-down {
    padding: 9px 40px 100px;

    &__quote {
      &-text {
        &:before {
          left: -80px;
        }
      }
    }
  }

  @include md-and-down {
    $mobile-page-pudding: 27px;

    padding: 0 $mobile-page-pudding;

    &__second-ellipse {
      top: auto;
      right: -230px;
      bottom: -60px;
      left: auto;
    }

    &__title {
      font-size: 27px;
      line-height: 28px;

      small {
        margin-top: 2px;

        font-size: 18px;
        line-height: 22px;
      }
    }

    &__intro {
      min-height: 165px;
      margin-top: 26px;
      margin-bottom: 66px;
      padding: 19px;

      font-size: 27px;
      line-height: 23px;

      border-radius: 20px;
    }

    &__bold {
      font-size: 14px;
      line-height: 16px;
    }

    &__text {
      margin-top: 39px;

      font-size: 12px;
      line-height: 14px;
      font-weight: 400;
      letter-spacing: -0.12px;
    }

    &__quote {
      flex-direction: row-reverse;

      img {
        width: 113px;
        margin-top: 20px;
      }

      &-text {
        margin-top: 18px;
        margin-right: 0;
        margin-bottom: 50px;
        margin-left: 10%;

        font-size: 12px;
        line-height: 16px;
        letter-spacing: -0.36px;

        &:before,
        &:after {
          top: -10px;
          left: -32px;

          width: 22px;
          height: 22px;
        }

        &:after {
          top: auto;
          right: 12px;
          bottom: -12px;
          left: auto;
        }
      }
    }

    &__image-and-text {
      font-size: 12px;
      line-height: 14px;
      letter-spacing: -0.12px;

      img {
        float: right;

        width: 100px;
        margin-top: 0;
        margin-right: 0;
      }
    }

    &__description {
      max-width: 60%;
      margin-top: 30px;

      font-size: 10px;
      line-height: 13px;
      letter-spacing: -0.1px;
    }
  }
}
</style>
