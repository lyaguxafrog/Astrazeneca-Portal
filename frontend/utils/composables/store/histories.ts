import { toRef } from 'vue';
import { loadableEmpty } from '~/utils/functions/loadable';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import {useCookie, useState} from "#app";

export type History = {
  id: number;
  title: string;
  avatar: string;
  avatar_desktop_120px: string;
  avatar_desktop_280px: string;
  avatar_mobile_70px: string;
  avatar_mobile_140px: string;
  cover_image: string;
  cover_450px: string;
  cover_900px: string;
  is_active: boolean;
  link_to_page: string;
  video: string;
  color: string | null;
  specialties: number[];
};

export const useHistoriesStore = () => {
  const { specialityId } = useSpecialityStore();

  const viewedStoriesId = useCookie('viewed-stories', {
    default: () => [],
  });

  const state = useState('histories-state', () => ({
    histories: loadableEmpty<History[]>([]),
    viewedStories: viewedStoriesId.value as number[],
  }));

  const getHistories = async (force?: boolean) => {
    let url = '/stories';

    if (specialityId.value) {
      url += `/${specialityId.value}`;
    }

    const res = await useRequest<History[]>(url, {
      method: 'GET',
    });

    if (res.data) {
      state.value.histories.data = JSON.parse(JSON.stringify(res.data)).reverse();
      state.value.histories.loaded = true;
    }
  };

  const viewStory = (id: number) => {
    const viewedStoriesId = useCookie('viewed-stories');
    if (!state.value.viewedStories.includes(id)) {
      state.value.viewedStories.push(id);

      viewedStoriesId.value = state.value.viewedStories;
    }
  }

  return {
    histories: toRef(() => state.value.histories.data),
    viewedStories: toRef(() => state.value.viewedStories),

    getHistories,
    viewStory,
  };
};
