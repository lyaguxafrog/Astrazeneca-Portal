import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { loadableEmpty } from '~/utils/functions/loadable';

export type Drug = {
  id: number;
  image: string;
  image_desktop_1400px: string;
  image_desktop_700px: string;
  image_mobile_540px: string;
  image_mobile_270px: string;
};

export type DrugFaq = {
  order: number;
  title: string;
  text: string;
  approvals_and_decodings?: string;
};

export type DrugPlump = {
  id: number;
  name: string;
  brief_info: string;
  url_field: string;
  file_field: string;
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
    practic_desktop_400px?: string;
    practic_desktop_800px?: string;
    practic_mobile_280px?: string;
    practic_mobile_560px?: string;
    name: string;
  }[];
  faq: DrugFaq[];
  image_desktop_1400px: string;
  image_desktop_700px: string;
  image_mobile_540px: string;
  image_mobile_270px: string;
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
