import { loadableEmpty } from '~/utils/functions/loadable';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export type History = {
  id: string;
  title: string;
  avatar: string;
};

export const useHistoriesStore = () => {
  const { speciality } = useSpecialityStore();

  const state = useState('histories-state', () => ({
    histories: loadableEmpty<History[]>(),
  }));

  const getHistories = async (specialityId?: number) => {
    let url = '/stories';

    if (specialityId) {
      url += `/speciality/${specialityId}`;
    }

    if (!state.value.histories.loaded) {
      const res = await useRequest<History[]>(url, {
        method: 'GET',
      });

      if (res.data) {
        state.value.histories.data = res.data;
        state.value.histories.loaded = true;
      }
    }

    return state.value.histories.data;
  };

  watch(
    speciality,
    () => {
      if (speciality.value) {
        state.value.histories.loaded = false;
        getHistories(speciality.value.id);
      }
    },
    {
      deep: true,
    }
  );

  return {
    histories: toRef(() => state.value.histories),

    getHistories,
  };
};
