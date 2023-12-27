import { loadableEmpty } from '~/utils/functions/loadable';
import { useRequest } from '~/utils/composables/useRequest';

export type History = {
  id: string;
  url: string;
  preview: string;
  name: string;
  avatar: string;
  color: string;
  link: string;
};

export const useHistoriesStore = () => {
  const state = useState('histories-state', () => ({
    histories: loadableEmpty<History[]>(),
  }));

  const getHistories = async () => {
    if (!state.value.histories.loaded) {
      const res = await useRequest<History[]>('/stories/Хирург', {
        method: 'GET',
      });

      if (res.data) {
        state.value.histories.data = res.data;
        state.value.histories.loaded = true;
      }
    }

    return state.value.histories.data;
  };

  return {
    histories: toRef(() => state.value.histories),

    getHistories,
  };
};
