<template>
  <div class="videos-slider">
    <div class="videos-slider__materials">
      <div class="videos-slider__materials-head">
        <BgEllipse
          class="videos-slider__materials-first-ellipse"
          :size="$screen.mdAndDown ? 386 : 1066"
          color="#00C2FF"
        />
        <div v-if="speciality" class="videos-slider__materials-title">
          <span>PRO</span>{{ speciality.pro }}
          <small>рака легкого</small>
        </div>

        <div v-if="videos?.length" class="videos-slider__materials-buttons">
          <div v-if="!$screen.mdAndDown" class="videos-slider__materials-selected">
            <template v-if="selectedType === 'видеолекция'"> Видеоматериалы </template>
            <template v-else> Клинические случаи </template>
          </div>

          <div class="videos-slider__materials-buttons-wrapper">
            <AppButton
              :primary="selectedType === 'видеолекция'"
              :selected="selectedType === 'видеолекция'"
              :petite="$screen.mdAndDown"
              @click="setType('видеолекция')"
            >
              <template v-if="!$screen.mdAndDown"> Видеолекции </template>
              <template v-else> Видеоматериалы </template>
            </AppButton>
            <AppButton
              :primary="selectedType === 'кейс'"
              :selected="selectedType === 'кейс'"
              :petite="$screen.mdAndDown"
              @click="setType('кейс')"
            >
              Клинические случаи
            </AppButton>
          </div>
        </div>
      </div>

      <ItemsSlider v-if="shownVideos" :items="shownVideos" :desktop-slides-per-view="1.7">
        <template #default="{ item }">
          <nuxt-link class="items-slider__content" :to="`video/${item.id}`">
            <div
              class="videos-slider__title items-slier__visible-on-active"
              v-html="item.video_article_url"
            />
            <img class="videos-slider__image" :src="`${baseUrl}${item.video_cover_url}`" alt="" />
            <PlayVideoButton />
          </nuxt-link>
        </template>
      </ItemsSlider>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useScreen } from '~/utils/composables/useScreen';
import ItemsSlider from '~/components/common/ItemsSlider.vue';
import PlayVideoButton from '~/components/common/PlayVideoButton.vue';
import BgEllipse from '~/components/common/BgEllipse.vue';
import { useVideosStore, VideoContentType } from '~/utils/composables/store/videos';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

const { $screen } = useScreen();
const { getVideos } = useVideosStore();
const { speciality } = useSpecialityStore();
const { baseUrl } = useRuntimeConfig().public;

const videos = await getVideos();

const selectedType = ref<VideoContentType>('видеолекция');

const shownVideos = computed(() => videos?.filter((v) => v.content_type === selectedType.value));

const setType = (type: VideoContentType) => {
  selectedType.value = type;
};
</script>

<style lang="scss" scoped>
.videos-slider {
  &__materials {
    position: relative;

    padding: 77px 0 9px;

    background: url('~/assets/img/home/bg.png') no-repeat bottom 48px left 0;

    &-head {
      padding: 0 56px;
    }

    &-first-ellipse {
      top: 130px;
      left: -740px;
      @include md-and-down {
        top: -60px;
        right: -350px;
        @include z-index(2);
      }
    }

    &-title {
      font-family: $secondary-font-family;
      font-size: 60px;
      font-weight: 900;
      color: $primary-color;
      text-transform: uppercase;
      span {
        color: $accent-color;
      }
      small {
        display: block;

        font-size: 40px;
        line-height: 0.4;
        font-weight: 400;
      }
    }

    &-buttons {
      display: flex;
      justify-content: space-between;

      margin: 78px 46px 43px 40px;

      &-wrapper {
        display: flex;

        margin-top: 22px;
      }

      button {
        width: 320px;
        margin-left: 26px;
        padding: 0;
      }
    }

    &-selected {
      font-family: $secondary-font-family;
      font-size: 50px;
      font-weight: 900;
      text-transform: uppercase;
    }
  }

  &__title {
    margin-bottom: 17px;

    font-family: $secondary-font-family;
    font-size: 40px;
  }

  img {
    display: block;

    width: 100%;
    object-fit: cover;

    border-radius: 34px;
  }

  &__link {
    display: block;
  }

  &__image {
    display: block;

    width: 100%;
    height: 530px;
    object-fit: cover;
  }

  @include xl-and-down {
    &__materials {
      &-head {
        padding: 0 16px;
      }

      &-buttons {
        margin: 78px 0 43px;
      }

      &-selected {
        font-size: 40px;
      }
    }
  }

  @include lg-and-down {
    &__materials {
      &-selected {
        display: none;
      }
    }
  }

  @include md-and-down {
    &__title {
      margin-bottom: 14px;

      font-size: 16px;
    }

    &__image {
      height: auto;
    }
    &__materials {
      padding: 3px 0 5px;

      background: none;

      &-head {
        padding: 0 27px;
      }

      &-title {
        font-size: 27px;

        small {
          font-size: 18px;
          line-height: 0.7;
        }
      }

      &-buttons {
        display: block;

        width: 220px;
        margin: 22px auto 10px;

        &-wrapper {
          display: contents;
        }

        button {
          width: 100%;
          margin-bottom: 14px;
          margin-left: 0;
        }
      }
    }
    .items-slider__content {
      @include aspect(1, 1);

      img {
        height: 100%;
        object-fit: cover;
      }
    }
  }
}
</style>
