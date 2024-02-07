<template>
  <div v-if="content.data" ref="wrapperEl" class="practicum">
    <BackBtn class="practicum__back" @click="backHelper" />

    <BgEllipse
      class="practicum__first-ellipse"
      :color="$screen.mdAndDown ? '#906DFF' : '#4DDFFF'"
      :size="$screen.mdAndDown ? 306 : 1138"
    />
    <BgEllipse
      class="practicum__second-ellipse"
      :color="$screen.mdAndDown ? '#4DDFFF' : '#B32FC9'"
      :size="$screen.mdAndDown ? 330 : 984"
    />
    <div class="practicum__container">
      <div class="practicum__left">
        <div class="practicum__title h2">практикум</div>
        <AppIcon
          class="practicum__info-ico"
          :name="IconName.Info"
          @click="openInfoModal"
          :size="$screen.mdAndDown ? 24 : 32"
        />
        <AppImage
          :url="content.data.image"
          :url-full="content.data.image_desktop_810px"
          :url-full-x2="content.data.image_desktop_1620px"
          :url-thin="content.data.image_mobile_400px"
          :url-thin-x2="content.data.image_mobile_800px"
        />
        <template v-if="!$screen.mdAndDown">
          <template v-for="item in leftContent">
            <div v-if="item.type === 'text'" class="practicum__text" v-html="item.text"></div>
            <ConfirmButton
              v-if="item.type === 'button'"
              :active="item.confirmation"
              :primary="item.fill_flag"
              :action="() => onBtnClick(item)"
              :to="item.url"
              :file="item.pdf_file"
            >
              {{ item.button_title }}
            </ConfirmButton>

            <Accordion
              v-if="item.type === 'drop'"
              :items="item.items"
              :modal-name="ModalsName.PracticumDiscoverModal"
            />

            <AppImage
              v-if="item.type === 'img'"
              class="practicum__img"
              :url="item.image"
              :url-full-x2="item.image_desktop_1620px"
              :url-full="item.image_desktop_810px"
              :url-thin-x2="item.image_mobile_800px"
              :url-thin="item.image_mobile_400px"
            />
          </template>
          <div class="practicum__description" v-html="activeScreen.approvals_and_decodings"></div>
        </template>
      </div>

      <div class="practicum__right">
        <div v-if="activeScreenIndex === 0" class="practicum__info" v-html="content.data.pacient_description">
        </div>
        <template v-for="item in rightContent">
          <div v-if="item.type === 'text'" class="practicum__text" v-html="item.text"></div>

          <Accordion
            v-if="item.type === 'drop'"
            :items="item.items"
            :modal-name="ModalsName.PracticumDiscoverModal"
          />

          <ConfirmButton
            v-if="item.type === 'button'"
            class="practicum__btn"
            right
            :active="item.confirmation"
            :primary="item.fill_flag"
            :action="() => onBtnClick(item)"
            :to="item.url"
            :file="item.pdf_file"
          >
            {{ item.button_title }}
          </ConfirmButton>

          <AppImage
            v-if="item.type === 'img'"
            class="practicum__img"
            :url="item.image"
            :url-full-x2="item.image_desktop_1620px"
            :url-full="item.image_desktop_810px"
            :url-thin-x2="item.image_mobile_800px"
            :url-thin="item.image_mobile_400px"
          />
        </template>
      </div>

      <template v-if="$screen.mdAndDown">
        <template v-for="item in leftContent">
          <div v-if="item.type === 'text'" class="practicum__text" v-html="item.text"></div>
          <ConfirmButton
            v-if="item.type === 'button'"
            :active="item.confirmation"
            :primary="item.fill_flag"
            :action="() => onBtnClick(item)"
            :to="item.url"
            :file="item.pdf_file"
          >
            {{ item.button_title }}
          </ConfirmButton>
        </template>
        <div class="practicum__description" v-html="activeScreen.approvals_and_decodings"></div>
      </template>
    </div>
  </div>
  <DiscoverModal />
  <InfoModal :literature="activeScreen.literature" :description="activeScreen.leterature_approvals_and_decodings" />
</template>

<script lang="ts" setup>
import {computed, toRef, ref} from 'vue';
import { useRoute } from '#app';
import { useScreen } from '~/utils/composables/useScreen';
import { IconName } from '~/components/app/AppIcon.utils';
import { ModalsName, useModal } from '~/utils/composables/useModal';
import BgEllipse from '~/components/common/BgEllipse.vue';
import InfoModal from '~/components/pages/practicum/InfoModal.vue';
import Accordion from '~/components/common/Accordion.vue';
import DiscoverModal from '~/components/pages/practicum/DiscoverModal.vue';
import ConfirmButton from '~/components/pages/practicum/ConfirmButton.vue';
import BackBtn from '~/components/common/BackBtn.vue';
import { useRequest } from '~/utils/composables/useRequest';
import { useBack } from '~/utils/composables/useHistory';

const $route = useRoute();
const { $screen } = useScreen();
const { baseUrl } = useRuntimeConfig().public;
const { back } = useBack();

const { openModal } = useModal();

const content = await useRequest<Practicum>(`/practicum/${$route.params.id}`, {
  method: 'GET',
});

const prevScreenIndexes = ref<number[]>([]);
const activeScreenIndex = ref(0);
const activeScreen = toRef(() => {
  const s = {...content.data?.screens[activeScreenIndex.value]} as Screen;

  if (!s) {
    return undefined;
  }

  s.screen_button_block_left = s.screen_button_block_left.map((i) => ({...i, type: 'button'}));
  s.screen_text_block_left = s.screen_text_block_left.map((i) => ({...i, type: 'text'}));
  s.screen_image_block_left = s.screen_image_block_left.map((i) => ({...i, type: 'img'}));
  s.screen_popup_block_left = s.screen_popup_block_left.map((i) => ({...i, type: 'drop', items: [{
      title: i.menu_title,
      text: i.text,
    }]}));

  s.screen_button_block_right = s.screen_button_block_right.map((i) => ({...i, type: 'button'}));
  s.screen_text_block_right = s.screen_text_block_right.map((i) => ({...i, type: 'text'}));
  s.screen_image_block_right = s.screen_image_block_right.map((i) => ({...i, type: 'img'}));
  s.screen_popup_block_right = s.screen_popup_block_right.map((i) => ({...i, type: 'drop', items: [{
    title: i.menu_title,
      text: i.text,
    }]}));

  return s;
});

const leftContent = computed(() => {
  if (!activeScreen.value) {
    return;
  }

  const screen = activeScreen.value;

  const content = [...screen.screen_button_block_left, ...screen.screen_text_block_left, ...screen.screen_popup_block_left, ...screen.screen_image_block_left];

  return content.sort((c1, c2) => c1.order - c2.order);
});

const rightContent = computed(() => {
  if (!activeScreen.value) {
    return;
  }

  const screen = activeScreen.value;

  const content = [...screen.screen_text_block_right, ...screen.screen_popup_block_right, ...screen.screen_button_block_right, ...screen.screen_image_block_right];

  return content.sort((c1, c2) => c1.order - c2.order);
});

const wrapperEl = ref<HTMLElement>();

const backHelper = () => {
  const index = prevScreenIndexes.value.pop();
  if (index || index === 0) {
    activeScreenIndex.value = index;
  } else {
    back();
  }
};

const onBtnClick = (btn: Btn) => {
  if (btn.screen_number) {
    prevScreenIndexes.value.push(activeScreenIndex.value);
    activeScreenIndex.value = btn.screen_number - 1;

    const top = wrapperEl.value?.getBoundingClientRect().top + window.pageYOffset;
    window.scrollTo({
      top: top,
      behavior: 'smooth',
    })
    return;
  }

  if (btn.url) {
    window.location.href = btn.url;
    return;
  }
};

const openInfoModal = () => {
  openModal(ModalsName.PracticumInfoModal);
};
const openDiscoverModal = () => {
  openModal(ModalsName.PracticumDiscoverModal);
};

type Btn = {
  id: number;
  button_title: string;
  order: number;
  pdf_file: string | null;
  screen: number;
  screen_number: number;
  screen_redirect: null;
  url: string | null;
  fill_flag: boolean;
  confirmation: boolean;
};

type TextBlock = {
  id: number;
  order: number;
  screen: number;
  text: string;
};

type ImgBlock = {
  id: number;
  image: string;
  image_desktop_1620px: string;
  image_desktop_810px: string;
  image_mobile_800px: string;
  image_mobile_400px: string;
  order: number;
};

type DropBlock = {
  id: number;
  menu_title: string;
  order: number;
  screen: number;
  text: string;
};

type Screen = {
  id: number,
  approvals_and_decodings: string,
  leterature_approvals_and_decodings: string,
  literature: string,

  screen_button_block_left: Btn[];
  screen_text_block_left: TextBlock[];
  screen_popup_block_left: DropBlock[];
  screen_image_block_left: ImgBlock[];

  screen_text_block_right: TextBlock[];
  screen_popup_block_right: DropBlock[];
  screen_button_block_right: Btn[];
  screen_image_block_right: ImgBlock[];
};

type Practicum = {
  id: number;
  image: string;
  image_desktop_810px: string;
  image_desktop_1620px: string;
  image_mobile_400px: string;
  image_mobile_800px: string;
  pacient_description: string;
  screens: Screen[];
};
</script>

<style lang="scss" scoped>
.practicum {
  position: relative;

  &__back {
    margin: 20px 20px 0;
  }

  &__first-ellipse {
    top: -310px;
    left: -800px;
  }
  &__second-ellipse {
    top: 90px;
    right: -640px;
  }

  &__container {
    display: flex;
    align-items: flex-start;

    padding: 26px 90px;
  }

  &__info-ico {
    position: absolute;
    top: 600px;
    right: 0;
    @include z-index(3);

    color: $primary-color;

    cursor: pointer;
    transition: color $tr-dur;

    @include hover {
      color: $white-color;
    }
  }

  &__left {
    position: relative;

    width: 37%;
    margin-right: 7%;

    :deep(img) {
      width: 100%;
      margin: 33px auto 9px;
      @include aspect(643, 690)
    }
  }

  :deep(img) {
    max-width: 100%;
  }

  &__right {
    width: 50%;
  }

  &__text {
    max-width: 730px;
    margin-top: 43px;
    margin-bottom: 43px;

    font-size: 26px;
    line-height: 32px;
    font-weight: 300;
    letter-spacing: -0.26px;

    &::v-deep {
      h3 {
        font-family: $secondary-font-family;
        font-size: 34px;
        line-height: 1;
        font-weight: 300;
      }

      h4 {
        margin-bottom: 28px;

        font-size: 34px;
        line-height: 1;
        font-weight: 600;
      }
    }
  }

  &__btn {
    width: fit-content;
    margin-top: 43px;
    margin-bottom: 43px;
  }

  &__img {
    display: block;

    margin: 34px 0;
  }

  &__description {
    margin-top: 34px;
    margin-bottom: 46px;

    font-size: 12px;
    color: $primary-color;
  }

  &__info {
    margin-top: 65px;

    font-size: 26px;
    line-height: 34px;
    font-weight: 300;

    :deep(b), :deep(strong){
      font-weight: 700;
    }
  }

  &__discover {
    margin-bottom: 25px;
    padding-bottom: 20px;

    font-size: 24px;
    color: $primary-color;

    border-bottom: 1px solid $primary-color;

    cursor: pointer;
    transition: color $tr-dur;

    @include hover {
      color: $white-color;
    }
  }

  @include lg-and-down {
    &__info-ico {
      top: 400px;
    }

    &__container {
      padding: 0 40px;
    }

    &__left {
      width: 45%;
      margin-right: 4%;
    }

    &__info {
      font-size: 20px;
      line-height: 1.2;
    }
  }

  @include md-and-down {
    &__first-ellipse {
      top: 20px;
      left: -190px;
    }
    &__second-ellipse {
      top: 230px;
      right: -230px;
    }

    &__container {
      display: block;

      padding: 35px 27px 0;
    }

    &__text {
      margin-top: 18px;
      margin-bottom: 18px;

      font-size: 15px;
      line-height: 1;

      &::v-deep {
        h3 {
          font-size: 15px;
          line-height: 20px;
        }

        h4 {
          margin-bottom: 19px;

          font-size: 19px;
          line-height: 17px;
        }
      }
    }

    &__btn {
      min-width: 100px;
      margin-top: 33px;
      margin-bottom: 33px;
    }

    &__info-ico {
      top: 276px;
    }

    &__left {
      width: 100%;

      :deep(img) {
        display: block;

        width: 77%;
        max-height: 270px;
        margin: 26px auto 0;
        object-fit: contain;
      }
    }

    &__right {
      width: 100%;
    }

    &__info {
      margin: 0;

      font-size: 14px;
      line-height: 18px;
    }

    &__subtitle {
      margin-top: 24px;
      margin-bottom: 15px;

      font-family: $secondary-font-family;
      font-size: 15px;
      line-height: 20px;
      font-weight: 300;
    }

    &__description {
      margin-top: 26px;
      margin-bottom: 10px;

      font-size: 9px;
      line-height: 10px;
    }
  }
}
</style>
