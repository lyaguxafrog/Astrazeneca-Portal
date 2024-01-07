import { loadableEmpty } from '~/utils/functions/loadable';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export type History = {
  id: number;
  title: string;
  avatar: string;
  cover_image: string;
  is_active: boolean;
  link_to_page: boolean;
  video: string;
  specialties: number[];
};

export const useHistoriesStore = () => {
  const { specialityId } = useSpecialityStore();

  const state = useState('histories-state', () => ({
    histories: loadableEmpty<History[]>([]),
  }));

  const showedStories = computed(() => {
    const data = state.value.histories.data;

    console.log(data);

    if (!data) {
      return [] as History[];
    }

    if (specialityId.value) {
      return data.filter(
        (s) => !s.specialties.length || s.specialties.includes(specialityId.value)
      );
    }

    return data.filter((s) => !s.specialties.length);
  });

  const getHistories = async (force?: boolean) => {
    let url = '/stories';

    console.log(specialityId.value);

    if (specialityId.value) {
      url += `/${specialityId.value}`;
    }

    if (!state.value.histories.loaded || force) {
      const res = await useRequest<History[]>(url, {
        method: 'GET',
      });

      if (res.data) {
        console.log(res.data);
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
