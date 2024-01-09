<template>
  <div class="favourites">
    <BgEllipse
      class="favourites-first-ellipse"
      :size="$screen.mdAndDown ? 342 : 1066"
      color="#00C2FF"
    />
    <BgEllipse class="favourites-second-ellipse for-mobile-or-tablet" :size="306" color="#B32FC9" />

    <div class="favourites__head">
      <div class="favourites__title">
        ИЗБРАННОЕ
        <small
          >Ваши сохраненные<br />
          материалы</small
        >
      </div>

      <AppButton primary to="https://az-most.ru" target="_blank"
        >Настроить профиль AZ-MOST</AppButton
      >
    </div>

    <div class="favourites__grid">
      <template v-for="fav in showedFavourites">
        <nuxt-link
          v-if="fav.type === ContentType.Video"
          class="favourites__item"
          :to="`video/${fav.id}`"
        >
          <AppImage
            class="favourites__item-bg"
            :url="fav.video_cover_desktop_1400px"
            :url-full-x2="fav.video_cover_desktop_2800px"
            :url-full="fav.video_cover_desktop_1400px"
            :url-thin-x2="fav.video_cover_mobile_840px"
            :url-thin="fav.video_cover_mobile_420px"
          />
          <p>
            {{ (fav as VideoPlump).video_article }}
          </p>
        </nuxt-link>
        <nuxt-link
          v-else-if="fav.type === ContentType.Article"
          class="favourites__item"
          :to="`article/${fav.id}`"
        >
          <AppImage
            class="favourites__item-bg"
            :url="fav.cover_desktop_1400px"
            :url-full-x2="fav.cover_desktop_2800px"
            :url-full="fav.cover_desktop_1400px"
            :url-thin-x2="fav.cover_mobile_840px"
            :url-thin="fav.cover_mobile_420px"
          />
          <p>
            {{ (fav as ArticlePlump).article_name }}
          </p>
        </nuxt-link>
        <nuxt-link
          v-else-if="fav.type === ContentType.Stories"
          class="favourites__item"
          :to="`histories/?id=${fav.id}`"
        >
          <img :src="`${baseUrl}${(fav as History).cover_image}`" class="favourites__item-bg" />
          <p>
            {{ (fav as History).title }}
          </p>
        </nuxt-link>
      </template>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useScreen } from '~/utils/composables/useScreen';
import { VideoPlump } from '~/utils/composables/store/videos';
import { ArticlePlump } from '~/utils/composables/store/articles';
import { History } from '~/utils/composables/store/histories';
import { useFavourites } from '~/utils/composables/useFavourites';
import BgEllipse from '~/components/common/BgEllipse.vue';
import { ContentType } from '~/utils/types';

const { baseUrl } = useRuntimeConfig().public;
const { $screen } = useScreen();
const { getFavourites, favourites } = useFavourites();

await getFavourites();

const showedFavourites = computed(() => {
  if (!favourites.value) {
    return [];
  }

  const keys = Object.keys(favourites.value.data);

  return keys.reduce((res, k) => {
    res = res.concat(favourites.value.data[k].map((f) => ({ ...f, type: k })));

    return res;
  }, [] as ((VideoPlump | ArticlePlump) & { type: ContentType })[]);
});
</script>

<style scoped lang="scss">
.favourites {
  position: relative;

  min-height: 100vh;
  padding: 56px;

  background: url('~/assets/img/home/bg.png') no-repeat top -340px left 0;

  &-first-ellipse {
    top: 130px;
    left: -740px;
  }

  &__head {
    display: flex;
  }

  &__title {
    margin-right: 70px;

    font-family: $secondary-font-family;
    font-size: 50px;
    line-height: 28px;
    font-weight: 900;
    small {
      display: block;

      margin-top: 20px;

      font-size: 30px;
      line-height: 27px;
      font-weight: 400;
    }
  }

  &__grid {
    display: grid;
    grid-gap: 33px;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;

    max-width: 1437px;
    margin-top: 71px;
  }

  &__item {
    position: relative;
    @include z-index(1);

    display: flex;
    flex-direction: column;

    padding: 30px;
    aspect-ratio: 1;

    overflow: hidden;

    font-size: 21px;
    line-height: 19px;
    letter-spacing: -0.21px;

    border-radius: 40px;

    transition: background $tr-dur;

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
      left: 0;
      z-index: -1;

      display: block;

      width: 100%;
      height: 100%;
      object-position: center;
      object-fit: cover;

      transition: transform $tr-dur;
    }

    @include hover {
      .favourites__item-bg {
        transform: scale(1.1);
      }
    }

    p {
      position: relative;
      z-index: 2;

      margin-top: auto;

      @include ellipsis(4);
    }
  }

  @include lg-and-down {
    &__item {
      padding: 16px;
      p {
        font-size: 16px;
        line-height: 16px;
      }
    }
  }

  @include md-and-down {
    min-height: initial;
    padding: 30px 27px;

    background: none;

    &__head {
      flex-direction: column;

      .app-button {
        width: fit-content;
      }
    }

    &__title {
      margin-bottom: 20px;
    }

    &__grid {
      grid-gap: 20px;
      grid-template-columns: 1fr 1fr 1fr;

      margin-top: 24px;
    }
  }

  @include xs {
    &-first-ellipse {
      top: 280px;
      right: -270px;
      left: auto;
    }
    &-second-ellipse {
      top: -40px;
      left: -220px;
    }

    &__head {
      .app-button {
        width: 100%;
        padding: 0;
      }
    }

    &__title {
      margin-bottom: 25px;

      font-size: 22px;
      line-height: 28px;

      small {
        margin-top: 0;

        font-size: 18px;
        line-height: 22px;
      }
    }

    &__grid {
      grid-gap: 20px;
      grid-template-columns: 1fr 1fr;

      margin-top: 24px;
    }

    &__item {
      padding: 12px 20px;

      border-radius: 20px;

      p {
        font-size: 11px;
        line-height: 13px;
        letter-spacing: -0.11px;
      }
    }
  }
}
</style>
