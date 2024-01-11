<template>
  <div v-if="$screen.mdAndDown || isOpen" class="search" @click.self="close">
    <div class="search__container">
      <div class="search__input">
        <AppIcon :name="IconName.SearchBlack" :size="$screen.mdAndDown ? 20 : 30" />
        <input ref="inputEl" v-model="searchString" type="text" placeholder="Поиск по сайту" />
      </div>

      <div ref="scrollEl" class="search__results">
        <div v-if="isEmpty" class="search__results-empty">
          По Вашему запросу ничего не&nbsp;найдено
        </div>
        <template v-if="result.length" v-for="block in result">
          <div v-if="block.items.length" :key="block.id" class="search__results-block">
            <div class="search__results-block-title">
              {{ block.name }}
            </div>
            <nuxt-link
              v-for="item in block.items"
              :key="item.id"
              class="search__results-block-item"
              :to="item.link"
              :style="{ backgroundColor: $screen.mdAndDown ? block.color : '', order: item.order }"
              @click="close"
            >
              <p>
                {{ item.name }}
              </p>
              <span v-if="!$screen.mdAndDown" :style="{ color: block.color }"
              >| {{ block.postfix }}</span
              >
              <AppIcon
                v-if="$screen.mdAndDown"
                class="search__results-block-icon"
                :name="block.icon"
                :size="$screen.xs ? 21 : 36"
              />
            </nuxt-link>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { nextTick, ref } from 'vue';
import { useRouter, useRoute } from '#app';
import { watchDebounced } from '@vueuse/core';
import { IconName } from '~/components/app/AppIcon.utils';
import { disableScroll, enableScroll } from '~/utils/functions/scroll-lock';
import { useRequest } from '~/utils/composables/useRequest';
import { useScreen } from '~/utils/composables/useScreen';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

type SearchResult = {
  id: number;
  title: string;
  url?: string;
  model?: 'video_lecture' | 'article' | 'event';
  content_type?: 'video_lecture' | 'article' | 'event';
  speciality?: number[];
};

const $route = useRoute();
const $router = useRouter();
const { $screen } = useScreen();
const { specialityId } = useSpecialityStore();

const isOpen = ref();
const inputEl = ref();
const scrollEl = ref();
const isEmpty = ref(false);

const searchString = ref($route.query.s);

const result = ref<
  {
    id: string;
    name: string;
    postfix: string;
    color: string;
    items: {
      id: number;
      name: string;
      link?: string;
      order?: number;
    }[];
    icon: IconName;
  }[]
  >([
  {
    id: '1',
    name: 'Статьи',
    postfix: 'статья',
    color: '#00B0BB',
    items: [],
    icon: IconName.Note,
  },
  {
    id: '2',
    name: 'Видео',
    postfix: 'видео',
    color: '#8300A4',
    items: [],
    icon: IconName.Video,
  },
  {
    id: '3',
    name: 'Кейсы',
    postfix: 'кейс',
    color: '#00B0BB',
    items: [],
    icon: IconName.Note,
  },
  {
    id: '4',
    name: 'Мероприятия',
    postfix: 'мероприятие',
    color: '#f74848',
    items: [],
    icon: IconName.Megaphone,
  },
  {
    id: '5',
    name: 'Препараты',
    postfix: 'препарат',
    color: '#00D1FF',
    items: [],
    icon: IconName.Star,
  },
]);

const open = () => {
  disableScroll(scrollEl.value, $screen.value.mdAndDown);
  isOpen.value = true;
  if (!$screen.value.mdAndDown) {
    nextTick(() => {
      inputEl.value.focus();
    });
  }
};
const close = () => {
  if (!$screen.value.mdAndDown) {
    enableScroll(scrollEl.value, $screen.value.mdAndDown);
    isOpen.value = false;
  }
};

defineExpose({
  open,
});

const processResults = (results?: SearchResult[]) => {
  if (!results) {
    return [];
  }

  results.forEach((r, index) => {
    if (r.speciality && r.speciality.length && !r.speciality.includes(specialityId.value) && !sessionStorage.getItem('showAllContent')) {
      return;
    }

    const model = r.model || r.content_type;

    const data = {
      id: r.id,
      name: r.title,
      order: index,
      link:
        r.model === 'event'
          ? r.url
          : model === 'video_lecture'
            ? `/video/${r.id}`
            : model === 'article' ? `/article/${r.id}` : `/drug/${r.id}`,
    };

    if (model === 'article') {
      result.value[0].items.push(data);
    }

    if (model === 'video_lecture') {
      result.value[1].items.push(data);
    }

    if (model === 'event') {
      result.value[3].items.push(data);
    }
    if (model === 'drug') {
      result.value[4].items.push(data);
    }
  });

  return JSON.parse(JSON.stringify(result.value));
};

const defaultItems = await useRequest<SearchResult[]>('/search/page', {
  method: 'GET',
  ignoreError: true,
});

const defaultResults = processResults(defaultItems.data);
result.value = JSON.parse(JSON.stringify(defaultResults));

const clearResults = () => {
  result.value.forEach((x) => (x.items = []));

  isEmpty.value = false;

  $router.replace({
    query: {
      ...$route.query,
      s: undefined,
    },
  });
};

const search = async () => {
  clearResults();

  if (!searchString.value) {
    result.value = JSON.parse(JSON.stringify(defaultResults));
    return;
  }

  await $router.replace({
    query: {
      ...$route.query,
      s: searchString.value,
    },
  });

  const res = await useRequest<SearchResult[]>(`/search/${searchString.value}`, {
    method: 'GET',
  });

  if (res.data) {
    if (!res.data.length) {
      isEmpty.value = true;
      return;
    }

    processResults(res.data);
  }
};

watchDebounced(
  searchString,
  () => {
    search();
  },
  {
    debounce: 500,
    immediate: true,
  }
);
</script>

<style scoped lang="scss">
.search {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  @include z-index(4);

  background: rgba(19, 37, 72, 0.8);

  &__container {
    max-width: 850px;
    margin: 20vh auto 100px;
    overflow: hidden;

    color: $secondary-text-color;

    background: rgba(255, 255, 255, 0.8);
    border-radius: 20px;

    backdrop-filter: blur(27px);
  }

  &__input {
    display: flex;
    align-items: center;

    width: 100%;
    padding: 14px 28px;

    border-bottom: 1.5px solid $secondary-text-color;

    .app-icon {
      color: $secondary-text-color;
    }

    input {
      width: 100%;
      padding: 0 15px;

      font-size: 24px;
      line-height: 42px;
      letter-spacing: -0.24px;

      &::placeholder {
        color: $dimmed-color;
      }
    }
  }

  &__results {
    min-height: 200px;
    max-height: 50vh;
    @include scrollbar($body-scrollbar-width);

    &-empty {
      padding: 20px;

      font-size: 20px;
    }

    &-block {
      padding: 16px 29px 14px;

      border-bottom: 1px solid #bebebe;

      &-icon {
        display: block;

        margin-top: auto;
        margin-left: auto;
      }

      &-title {
        margin-bottom: 1px;

        font-size: 18px;
        font-weight: 700;
        color: $gray-color;
        letter-spacing: -0.18px;
      }

      &-item {
        display: flex;

        width: fit-content;

        font-size: 18px;
        line-height: 42px;
        letter-spacing: -0.18px;

        span {
          margin-left: 8px;
        }

        @include hover {
          color: $accent-color;
        }
      }
    }
  }

  @include md-and-down {
    position: static;

    padding: 26px 28px;

    background: transparent;

    &__container {
      width: 100%;
      max-width: 100%;
      margin: 0;
      overflow: initial;

      background: transparent;
      border-radius: 0;

      backdrop-filter: initial;
    }

    &__input {
      padding: 6px 7px;

      color: $primary-color;

      border: 1.2px solid $primary-color;
      border-radius: 20px;

      .app-icon {
        color: $primary-color;
      }

      input {
        padding: 0 9px;

        font-size: 11px;
        line-height: 23px;
      }
    }

    &__results {
      display: grid;
      grid-gap: 16px;
      grid-template-columns: repeat(3, calc((100% - 32px) / 3));

      min-height: initial;
      max-height: initial;
      margin-top: 30px;
      overflow: initial;

      &-empty {
        width: calc(100vw - 56px);
        padding: 0;

        font-size: 16px;
        color: $white-color;
      }

      &-block {
        display: contents;

        &-title {
          display: none;
        }

        &-item {
          display: flex;
          flex-direction: column;

          width: 100%;
          height: 100%;
          padding: 17px;
          aspect-ratio: 1;

          font-size: 13px;
          line-height: 16px;
          color: $white-color;

          border-radius: 20px;
          p {
            word-break: break-word;
            @include ellipsis(5);
          }
        }
      }
    }
  }

  @include xs {
    &__results {
      grid-template-columns: repeat(3, calc((100% - 32px) / 3));

      &-block {
        &-item {
          padding: 10px;

          p {
            font-size: 9px;
            line-height: 10px;
          }
        }
      }
    }
  }

  @include extra-xs {
    padding: 26px 10px;

    &__results {
      grid-gap: 8px;
      grid-template-columns: repeat(2, calc((100% - 8px) / 2));

      &-block {
        &-item {
          word-break: break-word;
        }
      }
    }
  }
}
</style>
