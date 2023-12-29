import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { loadableEmpty } from '~/utils/functions/loadable';

export type Drug = {
  id: number;
  image: string;
};

export type DrugFaq = {
  order: number;
  title: string;
  text: string;
};

export type DrugPlump = {
  id: number;
  name: string;
  image: string;
  brief_info: string;
  approvals_and_decodings: string;
  icons: {
    id: number;
    image_file: string;
  }[];
  application_practice_articles: number[];
  application_practice_videos: number[];
  application_practices: {
    id: number;
    type: 'article' | 'video';
    image: string;
    name: string;
  }[];
  faq: DrugFaq[];
};

export const useDrugsStore = () => {
  const store = useState('drags-state', () => ({
    drugs: loadableEmpty<Drug[]>([]),
  }));

  const getDrugs = async () => {
    if (!store.value.drugs.loaded) {
      const res = await useRequest<Drug[]>('/drugs', {
        method: 'GET',
      });

      if (res.data) {
        store.value.drugs.data = res.data;
        store.value.drugs.loaded = true;
      }
    }

    return store.value.drugs.data;
  };

  const getDrug = async (id: number) => {
    const res = await useRequest<DrugPlump>(`/drugs/${id}`, {
      method: 'GET',
    });

    return res.data;
  };

  return {
    getDrugs,
    getDrug,
  };
};
