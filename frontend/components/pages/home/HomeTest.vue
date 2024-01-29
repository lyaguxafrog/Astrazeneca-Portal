<template>
  <div v-if="content.data?.length" class="home-test">
    <BgEllipse
      class="home-test__first-ellipse"
      color="#00C2FF"
      :pale="!$screen.mdAndDown"
      :size="$screen.mdAndDown ? 330 : 1547"
    />
    <BgEllipse
      class="home-test__second-ellipse"
      color="#B32FC9"
      :size="$screen.mdAndDown ? 306 : 1000"
    />

    <div class="home-test__title h2">практикум</div>

    <ItemsSlider
      :withNavigation="!$screen.mdAndDown"
      :items="content.data"
      :desktop-slides-per-view="1"
      :initial-slide="0"
      :hide-pagination="!$screen.mdAndDown"
      #default="{ item }"
    >
      <nuxt-link class="home-test__item link" :to="`/test/${item.id}`">
        <div
          v-if="!$screen.mdAndDown"
          class="home-test__item-text caption-m"
          v-html="item.question"
        />
        <AppImage
          class="home-test__item-img"
          :url="item.image_desktop_810px"
          :url-full="item.image_desktop_810px"
          :url-full-x2="item.image_desktop_1620px"
          :url-thin-x2="item.image_mobile_400px"
          :url-thin="item.image_mobile_800px"
        />
        <div
          v-if="$screen.mdAndDown"
          class="home-test__item-text caption-m"
          v-html="item.question"
        />
        <AppButton primary class="home-test__item-btn"> Начать </AppButton>
      </nuxt-link>
    </ItemsSlider>
  </div>
</template>

<script setup lang="ts">
import { useScreen } from '~/utils/composables/useScreen';
import { useRequest } from '~/utils/composables/useRequest';
import { TestPracticum } from '~/pages/test/[id].vue';
import BgEllipse from '~/components/common/BgEllipse.vue';
import ItemsSlider from '~/components/common/ItemsSlider.vue';

const { $screen } = useScreen();

const content = await useRequest<TestPracticum[]>('/practicum_tests', {
  method: 'GET',
});
</script>

<style scoped lang="scss">
.home-test {
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
    margin-bottom: 80px;
    padding: 0 95px;
  }

  &__item {
    display: flex;
    flex-direction: column;

    max-width: 625px;
    height: 100%;
    margin: 0 auto;

    &-text {
      margin-bottom: 40px;
    }

    &-btn {
      width: 280px;
      margin: 60px auto 0;
    }

    &-img {
      margin-top: auto;
    }

    :deep(img) {
      @include aspect(1, 1);

      border: 1px solid $primary-color;
      border-radius: 40px;
    }
  }

  :deep(.swiper-button) {
    top: auto;
    bottom: 410px;
  }

  @include lg-and-down {
    &__item {
      max-width: 460px;
    }

    :deep(.swiper-button) {
      top: auto;
      bottom: 320px;
    }
  }

  @include md-and-down {
    margin-bottom: 60px;

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
      margin-bottom: 50px;
      padding: 0 27px;
    }

    &__item {
      &-text {
        margin: 26px 0 0;
      }

      &-btn {
        width: fit-content;
        margin-top: 36px;
      }
    }
  }
}
</style>
