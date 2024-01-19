<template>
  <div class="home">
    <div v-if="$screen.mdAndDown" class="home__intro">
      <BgEllipse class="home__intro-first-ellipse" size="386" color="#00C2FF" />
      <BgEllipse class="home__intro-second-ellipse" size="258" color="#FF4DF8" />
      <div class="home__intro-title"><span>PRO</span>РАК ЛЕГКОГО</div>

      <div class="home__intro-bottom">
        <div class="home__intro-text">
          <img src="~/assets/img/home/arrow.svg" alt="" />
          <p>информационный портал для специалистов здравоохранения</p>
        </div>
        <DefaultHistoriesSlider class="home__intro-histories" />
      </div>
    </div>

    <template v-if="specialityId">
      <HomeVideosSlider @showAll="showAllModal" />

      <HomeArticles @showAll="showAllModal" />

      <HomeEvents />

      <HomeDrugs />
    </template>

    <Teleport v-if="accessInfo?.number" to="#footerAccessInfo">
      <div v-html="accessInfo?.number" />
    </Teleport>
  </div>
  <SpecialitySlider v-if="showSpecialitySlider" class="home__specialitySlider" />
  <HomeAddContentModal @load-all="loadAllContent" />
</template>

<script lang="ts" setup>
import { onMounted, toRef, watch, ref } from 'vue';
import { isClient } from '@vueuse/core';
import { useScreen } from '~/utils/composables/useScreen';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import BgEllipse from '~/components/common/BgEllipse.vue';
import DefaultHistoriesSlider from '~/components/layout/DefaultHistoriesSlider.vue';
import HomeVideosSlider from '~/components/pages/home/HomeVideosSlider.vue';
import HomeDrugs from '~/components/pages/home/HomeDrugs.vue';
import HomeEvents from '~/components/pages/home/HomeEvents.vue';
import SpecialitySlider from '~/components/common/SpecialitySlider.vue';
import HomeArticles from '~/components/pages/home/HomeArticles.vue';
import HomeAddContentModal from '~/components/pages/home/HomeAddContentModal.vue';
import { useRequest } from '~/utils/composables/useRequest';
import { useVideosStore } from '~/utils/composables/store/videos';
import { useArticlesStore } from '~/utils/composables/store/articles';
import {ModalsName, useModal} from "~/utils/composables/useModal";

const { openModal, closeModal } = useModal();

const { $screen } = useScreen();
const { specialityId } = useSpecialityStore();
const { getVideos } = useVideosStore();
const { getArticles } = useArticlesStore();

const accessInfo = ref({
  number: '',
});

onMounted(async () => {
  const res = await useRequest<{
    number: string;
  }>('/main_page', {
    method: 'GET',
  });

  if (res.data) {
    accessInfo.value = res.data;
  }
});

const showSpecialitySlider = toRef(() => $screen.value.mdAndDown && !specialityId.value);

watch(
  specialityId,
  (newValue) => {
    if (!$screen.value.mdAndDown) {
      return;
    }

    if (newValue) {
      enableScroll();
    } else {
      disableScroll();
    }
  },
  {
    immediate: isClient,
  }
);

const showAllModal = () => {
  if (sessionStorage.getItem('showAllContent')) {
    return;
  }

  openModal(ModalsName.VideosAddContent);
}

const loadAllContent = () => {
  if (sessionStorage.getItem('showAllContent')) {
    return;
  }

  sessionStorage.setItem('showAllContent', '1');

  getVideos(true);
  getArticles(true);

  closeModal(ModalsName.VideosAddContent);
};
</script>

<style lang="scss" scoped>
.home {
  min-height: 100vh;

  background: url('~/assets/img/home/bg.png') no-repeat top -340px left 0;

  &__intro {
    position: relative;

    display: flex;
    flex-direction: column;

    min-height: calc(100vh - 60px - 18px);
    padding-bottom: 18px;

    background: url('~/assets/img/home/intro-bg.png') no-repeat bottom 39px left 46% / auto 99%;

    &-title {
      padding: 67px 45px;

      font-family: $text-font-family;
      font-size: 51px;
      line-height: 0.9;
      font-weight: 500;
      color: $primary-color;
      span {
        color: $accent-color;
      }
    }
    &-first-ellipse {
      top: 18vh;
      left: -290px;
    }
    &-second-ellipse {
      top: 44vh;
      right: -220px;
      z-index: 2;
    }

    &-bottom {
      display: flex;
      flex-direction: column;
      justify-content: flex-end;

      height: 390px;
      margin-top: auto;

      background: linear-gradient(180deg, rgba(19, 37, 72, 0) 0%, #132548 56.25%);
    }

    &-text {
      display: flex;
      align-items: center;

      margin-bottom: 16px;

      font-family: $secondary-font-family;
      font-size: 19px;
      line-height: 1.3;
      text-transform: uppercase;

      img {
        margin-right: 14px;
        margin-left: -69px;
      }

      p {
        width: 260px;
      }
    }

    &-histories {
      padding: 0 25px;
    }
  }

  @include md-and-down {
    min-height: 50vh;

    background: none;

    &__specialitySlider {
      position: fixed;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      @include z-index(4);
    }
  }
}
</style>
