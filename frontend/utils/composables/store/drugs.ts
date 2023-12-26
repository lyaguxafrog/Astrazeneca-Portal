import { useState } from '#app';
import {useRequest} from '~/utils/composables/useRequest';

export const useDrugsStore = () => {
  const store = useState('drags-state', () => ({

  }));

  const getDrugs = async () => {
    const res = await useRequest('/drugs', {
      method: 'GET',
    });

    console.log(res);
  };

  return {
    getDrugs,
  };
};
