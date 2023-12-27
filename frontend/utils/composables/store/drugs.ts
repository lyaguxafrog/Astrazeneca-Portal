import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { loadableEmpty } from '~/utils/functions/loadable';

export type Drug = {
  id: number;
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

  return {
    getDrugs,
  };
};
