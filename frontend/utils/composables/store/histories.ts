import { loadableEmpty } from '~/utils/functions/loadable';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export type History = {
  id: number;
  title: string;
  avatar: string;
  cover_image: string;
  is_active: boolean;
  link_to_page: string;
  video: string;
  specialties: number[];
};

export const useHistoriesStore = () => {
  const { specialityId } = useSpecialityStore();

  const state = useState('histories-state', () => ({
    histories: loadableEmpty<History[]>([]),
  }));

  const getHistories = async (force?: boolean) => {
    let url = '/stories';

    if (specialityId.value) {
      url += `/${specialityId.value}`;
    }

    if (!state.value.histories.loaded || force) {
      const res = await useRequest<History[]>(url, {
        method: 'GET',
      });

      if (res.data) {
        state.value.histories.data = res.data;
        state.value.histories.loaded = true;
      }
    }
  };

  return {
    histories: toRef(() => state.value.histories.data),

    getHistories,
  };
};
